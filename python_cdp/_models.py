from __future__ import annotations  # isort: skip
import collections
import itertools
import pathlib
import textwrap
import typing
from dataclasses import dataclass

from ._const import MISSING_DESCRIPTION_IN_PROTOCOL_DOC
from ._headers import CONSTANT_IMPORTS
from ._headers import PREAMBLE
from ._protocols import GeneratesSourceCode
from ._protocols import Requirable
from ._templates import PRIMITIVE_TYPE_FROM_JSON
from ._templates import PRIMITIVE_TYPE_TO_JSON
from ._templates import SIMPLE_ENUM_FROM_JSON
from ._templates import SIMPLE_PRIMITIVE_REPR
from ._types import AnyDict
from ._utils import api_type_to_python_annotation
from ._utils import camel_to_enum_member
from ._utils import get_generation_rootdir
from ._utils import indent
from ._utils import name_to_pascal_case
from ._utils import name_to_snake_case
from ._utils import resolve_docstring

TypeStore = collections.namedtuple("TypeStore", "parent, annotation")
PRIMITIVE_TYPE_FACTORY = {
    "string": TypeStore("str", "str"),
    "number": TypeStore("float", "float"),
    "boolean": TypeStore("bool", "bool"),
    "integer": TypeStore("int", "int"),
}


def fix_reference_type_circular(domain: str, reference: str) -> str:
    """Patches a small bug in the protocol where certain properties or parameters are advertised as reliant on a type
    that lives in the same module once we have split files by top level `domains`.  The bug is outlined below:

    Occassionally some files i.e `dom.py` have a reference to a type defined within
    that module but the devtools protocol returns data such as `dom.Type`.  Due to
    how we handle imports using `from .domain import X` this is not valid and so
    we manage this internally.  I have opened a defect on the CDP tracker but it was
    marked P3 and unlikely to be resolved soon.

    :param domain: The domain name to check for a circle reference defect.
    :param reference: The reference returned by CDP.
    """
    if reference == "any":
        return "typing.Any"
    if "." in reference:
        split_domain, period, annotation = reference.partition(".")
        if domain.lower() == split_domain.lower():
            return annotation  # Defect, referring to a type in the same module.
        return f"{name_to_snake_case(split_domain)}{period}{annotation}"
    return reference


@dataclass
class DevtoolsArrayItem:
    """Encapsulation of a property `item` array entry."""

    type: typing.Optional[str] = None
    ref: typing.Optional[str] = None

    @classmethod
    def from_json(cls, payload: AnyDict) -> DevtoolsArrayItem:
        return cls(type=payload.get("type"), ref=payload.get("$ref"))


@dataclass
class DevtoolsParam:
    """Encapsulation of a parameter passed to a method call or event type."""

    cdp_domain: str
    name: str
    description: str
    optional: bool
    ref: typing.Optional[str] = None
    type: typing.Optional[str] = None
    items: typing.Optional[DevtoolsArrayItem] = None
    enum_options: typing.Optional[typing.List[str]] = None

    @classmethod
    def from_json(cls, payload: AnyDict, cdp_domain: str) -> DevtoolsParam:
        return cls(
            cdp_domain=cdp_domain,
            name=typing.cast(str, payload.get("name")),
            description=payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC),
            optional=payload.get("optional", False),
            ref=payload.get("$ref"),
            type=payload.get("type"),
            items=DevtoolsArrayItem.from_json(payload["items"]) if "items" in payload else None,
            enum_options=payload.get("enum"),
        )

    def generate_code(self) -> str:
        source = ""
        source += indent(f"{name_to_snake_case(self.name)}: {self.generate_type_hint()}")
        source += "\n"
        return source

    def generate_type_hint(self) -> str:
        """Generates the type hint for this parameter."""
        optional = "typing.Optional[{}]" if self.optional else "{}"
        if self.items is not None:
            if self.items.ref:
                return optional.format(f"typing.List[{self.items.ref}]")
            return optional.format(f"typing.List[{api_type_to_python_annotation(self.items.type)}]")
        if self.enum_options:
            # An array of primitive or reference types let's pythonise the options tho.
            wrapped = ", ".join(f"'{name_to_snake_case(word)}'" for word in self.enum_options)
            return optional.format(f"typing.Literal[{wrapped}]")
        if self.type:
            # various types, could even be an object, read from mapping
            return optional.format(api_type_to_python_annotation(self.type))
        if self.ref:
            # object reference type, return it literally
            return optional.format(fix_reference_type_circular(self.cdp_domain, self.ref))
        return "typing.Any"

    @property
    def requires(self) -> typing.Set[str]:
        """Return the required imports for this particular parameter."""
        imports = set()
        reference = (self.items.ref or self.items.type) if self.items else self.ref
        if reference:
            fixed = fix_reference_type_circular(self.cdp_domain, reference)
            if "." in fixed:
                fixed = fixed.split(".")[0]
                imports.add(f"from . import {fixed}")
        return imports


@dataclass
class DevtoolsReturn:
    """Encapsulation of a method return value."""

    name: str
    description: str
    optional: typing.Optional[bool] = None
    type: typing.Optional[str] = None
    items: typing.Optional[DevtoolsArrayItem] = None
    ref: typing.Optional[str] = None

    @classmethod
    def from_json(cls, payload: AnyDict) -> DevtoolsReturn:
        return cls(
            name=typing.cast(str, payload.get("name")),
            description=payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC),
            optional=payload.get("optional", False),
            type=payload.get("type"),
            items=DevtoolsArrayItem.from_json(payload["items"]) if "items" in payload else None,
            ref=payload.get("ref"),
        )


@dataclass
class DevtoolsProperty:
    """Encapsulation of a property for objects that are not simple primitive types."""

    cdp_domain: str
    name: str
    description: str
    items: typing.Optional[DevtoolsArrayItem] = None
    ref: typing.Optional[str] = None
    optional: typing.Optional[bool] = False
    type: typing.Optional[str] = None
    enum_options: typing.Optional[typing.List[str]] = None

    @classmethod
    def from_json(cls, payload: AnyDict, cdp_domain: str) -> DevtoolsProperty:
        return cls(
            cdp_domain=cdp_domain,
            name=typing.cast(str, payload.get("name")),
            description=payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC),
            ref=payload.get("$ref", None),
            optional=payload.get("optional", False),
            items=DevtoolsArrayItem.from_json(payload["items"]) if "items" in payload else None,
            type=payload.get("type", None),
            enum_options=payload.get("enum"),
        )

    def generate_code(self) -> str:
        """Generate the source code for this particular type property."""
        source = ""
        source += "".join(textwrap.wrap(self.description, width=80, initial_indent="    # "))
        source += " # noqa"  # Todo: Remove this and wrap appropriately.
        source += "\n"
        source += self.generate_definition()
        source += "\n"
        return source

    def generate_definition(self) -> str:
        optional = "typing.Optional[{}]" if self.optional else "{}"
        literal = "typing.Literal[{}]" or "{}"
        seq = "typing.List[{}]" if (self.enum_options or self.type == "array") else "{}"
        source = indent(f"{name_to_snake_case(self.name)}: ")
        if self.enum_options:
            return source + optional.format(
                seq.format(literal.format(", ".join(f"'{word}'" for word in self.enum_options))),
            )
        if self.type == "array" and self.items:
            reference = self.items.ref or self.items.type
            assert reference is not None, "item array for property but both are none!"
            if reference in PRIMITIVE_TYPE_FACTORY:
                return source + optional.format(api_type_to_python_annotation(reference))
            return source + optional.format(fix_reference_type_circular(self.cdp_domain, reference))
        if self.type in PRIMITIVE_TYPE_FACTORY:
            return source + optional.format(api_type_to_python_annotation(self.type))
        if self.ref:
            return source + optional.format(fix_reference_type_circular(self.cdp_domain, self.ref))
        return source + "typing.Any"

    @property
    def requires(self) -> typing.Set[str]:
        imports = set()
        reference = (self.items.ref or self.items.type) if self.items else self.ref
        if reference and "." in reference:
            domain, _, _ = reference.partition(".")
            imports.add(f"from . import {name_to_snake_case(domain)}")
        return imports


@dataclass
class DevtoolsType:
    cdp_domain: str
    id: str
    description: str
    type: str
    properties: typing.List[DevtoolsProperty]
    enum_options: typing.List[str]

    @classmethod
    def from_json(cls, payload: AnyDict, cdp_domain: str) -> DevtoolsType:
        return cls(
            cdp_domain=cdp_domain,
            id=typing.cast(str, payload.get("id")),
            description=payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC),
            type=typing.cast(str, payload.get("type")),
            # These need kept in order with non optional fields first to avoid pain with the generated dataclasses.
            properties=list(
                sorted(
                    [DevtoolsProperty.from_json(p, cdp_domain=cdp_domain) for p in payload.get("properties", [])],
                    key=lambda i: i.optional,  # type: ignore [arg-type, return-value]
                ),
            ),
            enum_options=payload.get("enum", []),
        )

    def generate_code(self) -> str:
        """Build out python source code for the CDP types."""
        if self.type in PRIMITIVE_TYPE_FACTORY and not self.enum_options:
            # A simple primitive type wrapper will suffice for this class
            return self._build_for_primitive_type()
        elif self.enum_options:
            # A string enum type wrapper is necessary
            return self._build_for_enum_type()
        return self._build_for_object_type()

    def _build_for_enum_type(self) -> str:
        """Generate source code for enum types."""
        source = textwrap.dedent(f"\n\nclass {self.id}(str, enum.Enum):")
        source += "\n"
        source += resolve_docstring(self.description)
        source += "\n"
        for option in self.enum_options:
            source += indent(f'{camel_to_enum_member(option)} = "{name_to_snake_case(option)}"')
            source += "\n"
        source += "\n"
        source += indent(SIMPLE_ENUM_FROM_JSON)
        return source

    def _build_for_object_type(self) -> str:
        """Generate source code for object types."""
        source = "\n"
        source += f'''
@dataclass
class {self.id}:
    """ {self.description} """
'''
        for property in self.properties:
            source += property.generate_code()
        return source

    def _build_for_primitive_type(self) -> str:
        """Generate source code for primitive types (simple subclass wrappers)."""
        source = "\n\n"
        source += textwrap.dedent(f"class {self.id}({PRIMITIVE_TYPE_FACTORY[self.type].parent}):")
        source += "\n"
        source += resolve_docstring(self.description)
        source += indent(PRIMITIVE_TYPE_TO_JSON.format(self.id))
        source += "\n"
        source += indent(PRIMITIVE_TYPE_FROM_JSON.format(PRIMITIVE_TYPE_FACTORY[self.type].parent, self.id))
        source += "\n"
        source += indent(SIMPLE_PRIMITIVE_REPR.format("{self.__class__.__name__}", "({super().__repr__()})"))
        return source

    @property
    def requires(self) -> typing.Set[str]:
        imports = set()
        for property in self.properties:
            imports |= property.requires
        return imports


@dataclass
class DevtoolsEvent:
    """Encapsulation of a CDP Event that can be sent and received across the websocket/connection."""

    cdp_domain: str
    name: str
    description: str
    parameters: typing.Optional[typing.List[DevtoolsParam]]
    experimental: typing.Optional[bool]
    deprecated: typing.Optional[bool]

    def generate_code(self) -> str:
        """Generate the source for every event object advertised in the protocol."""
        source = textwrap.dedent("@dataclass")
        source += "\n"
        source += textwrap.dedent(f"@memoize_event('{self.cdp_domain}.{self.name}')")
        source += "\n"
        source += f"class {self.class_name}:"
        source += "\n"
        source += resolve_docstring(self.description)
        if self.parameters:
            for param in self.parameters:
                source += param.generate_code()
        return source

    @property
    def class_name(self) -> str:
        """Generates the pythonic class name for this event."""
        return name_to_pascal_case(self.name)

    @property
    def requires(self) -> typing.Set[str]:
        """Returns a distinct set of the imports required based on the parameters."""
        imports: typing.Set[str] = set()
        if self.parameters is None:
            return imports
        imports.add("from .utils import memoize_event")
        for parameter in self.parameters:
            imports |= parameter.requires
        return imports

    @classmethod
    def from_json(cls, payload: AnyDict, cdp_domain: str) -> DevtoolsEvent:
        """Generate the event object, including building its nested parameters."""
        return cls(
            cdp_domain=cdp_domain,
            name=typing.cast(str, payload["name"]),
            description=typing.cast(str, payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC)),
            parameters=[DevtoolsParam.from_json(p, cdp_domain=cdp_domain) for p in payload.get("parameters", [])],
            experimental=typing.cast(bool, payload.get("experimental", False)),
            deprecated=typing.cast(bool, payload.get("deprecated", False)),
        )


@dataclass
class DevtoolsCommand:
    """Encapsulation of a devtools command."""

    cdp_domain: str
    name: str
    description: str
    experimental: typing.Optional[bool]
    parameters: typing.Optional[typing.List[DevtoolsParam]]
    returns: typing.Optional[typing.List[DevtoolsReturn]]

    def generate_code(self) -> str:
        source = textwrap.dedent(
            f'''
async def {name_to_snake_case(self.name)}() -> None:
    """ {self.description} # noqa """
    ...
''',
        )
        return source

    @classmethod
    def from_json(cls, payload: AnyDict, cdp_domain: str) -> DevtoolsCommand:
        return cls(
            cdp_domain=cdp_domain,
            name=typing.cast(str, payload.get("name")),
            description=typing.cast(str, payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC)),
            experimental=payload.get("experimental", False),
            parameters=[DevtoolsParam.from_json(p, cdp_domain) for p in payload.get("parameters", [])],
            returns=[DevtoolsReturn.from_json(r) for r in payload.get("returns", [])],
        )


@dataclass
class DevtoolsDomain:
    """Encapsulation of an individual devtools domain."""

    domain: str
    description: str
    dependencies: typing.List[str]
    deprecated: bool
    experimental: bool
    events: typing.List[DevtoolsEvent]
    types: typing.List[DevtoolsType]
    commands: typing.List[DevtoolsCommand]

    @property
    def py_mod_name(self) -> str:
        """Returns the python module name for this instance."""
        return f"{name_to_snake_case(self.domain)}.py"

    @classmethod
    def from_json(cls, payload: AnyDict) -> DevtoolsDomain:
        """Shovel the json arguments into this model and recursively build out nested objects."""
        return cls(
            domain=typing.cast(str, payload.get("domain")),
            description=payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC),
            deprecated=payload.get("deprecated", False),
            dependencies=payload.get("dependencies", []),
            experimental=payload.get("experimental", False),
            events=[DevtoolsEvent.from_json(e, cdp_domain=payload["domain"]) for e in payload.get("events", [])],
            types=[DevtoolsType.from_json(t, cdp_domain=payload["domain"]) for t in payload.get("types", [])],
            commands=[
                DevtoolsCommand.from_json(c, typing.cast(str, payload.get("domain")))
                for c in payload.get("commands", [])
            ],
        )

    def generate_code(self) -> str:
        """Generate the full source code for the domain module."""
        requires_enum = bool([x for x in self.types if x.enum_options])  # Todo: investigate logic.
        source = PREAMBLE.format(domain=self.domain)
        source += "\n"
        source += CONSTANT_IMPORTS
        if requires_enum:
            source += textwrap.dedent("import enum")
        source += "\n\n"
        source += self.calculate_imports()
        iterator: typing.Iterator[GeneratesSourceCode] = itertools.chain(self.types, self.events, self.commands)
        for item in iterator:
            source += "\n\n"
            source += item.generate_code()
        return source

    def calculate_imports(self) -> str:
        """Calculate the correct imports for this module based on builtins and other domains created in the cdp/*
        directory.

        There might be some shortcomings here in the protocol itself,
        raise bugs/fixes for those respectively.

        Referencing the `dependencies` array is likely not sufficient
        here.  We need
        to calculate them dynamically (better) and sort potential edge
        cases and
        race conditions with order etc.

        This has a heap of bugs already
            ** Audit has no dependency on `Runtime` in the protocol.
            ** Audit has no dependency on `DOM` in the protocol.
            ** Audit has no dependency on `Page` in the protocol.

            ** BackgroundService has no dependency on `Network` in the protocol.
            ** BackgroundService has no dependency on `ServiceWorker` in the protocol.

            ** Dom has no dependency on `Page` in the protocol.
            ** Network depends on itself in error
        """
        # self.commands add later, using raw `dependencies` on the `domain` is also not the best solution for now.
        elements: typing.Iterable[Requirable] = itertools.chain(self.events, self.types)
        imports = set()
        for element in elements:
            imports |= element.requires

        # Todo: Format inline with linter, or leave that up to the linter?
        source = ""
        source += "\n".join(imports)
        # Todo: Handle joining them
        # Todo: Rewrite the docstring here.
        return source

    def create_py_module(self) -> pathlib.Path:
        """Writes the python module for this domain to disk, recursively generating all the python source code."""
        path = get_generation_rootdir() / self.py_mod_name
        with open(str(path), mode="w") as f:
            f.write(self.generate_code())
        return path


@dataclass
class TopLevelDomains:
    """Encapsulation of the top level domains array.  This is composed of an array of DevtoolDomain objects.

    For now, only domains in the protocol that are not marked `deprecated` are built and accessible, but this is likely
    subject to change in future.
    """

    domains: typing.List[DevtoolsDomain]

    def __iter__(self) -> typing.Iterator[DevtoolsDomain]:
        return iter(self.domains)

    @classmethod
    def from_json(cls, payload: AnyDict) -> TopLevelDomains:
        """Build and generate the full protocol."""
        return cls(domains=[DevtoolsDomain.from_json(domain) for domain in payload["domains"]])

    def create_source_code_on_disk(self) -> None:
        """Automatically generates all the python CDP modules for all of the nested children domains."""
        for domain in self.domains:
            domain.create_py_module()
