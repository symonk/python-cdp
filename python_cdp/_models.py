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
from ._templates import PRIMITIVE_TYPE_TO_JSON
from ._templates import SIMPLE_ENUM_FROM_JSON
from ._templates import SIMPLE_PRIMITIVE_REPR
from ._types import AnyDict
from ._utils import api_type_to_python_annotation
from ._utils import get_generation_rootdir
from ._utils import indent
from ._utils import name_to_snake_case
from ._utils import resolve_docstring

TypeStore = collections.namedtuple("TypeStore", "parent, annotation")
PRIMITIVE_TYPE_FACTORY = {
    "string": TypeStore("str", "str"),
    "number": TypeStore("float", "float"),
    "boolean": TypeStore("bool", "bool"),
}


@dataclass
class DevToolsArrayItem:
    """Encapsulation of a property `item` array entry."""

    cdp_domain: str
    type: typing.Optional[str] = None
    ref: typing.Optional[str] = None

    @classmethod
    def from_json(cls, payload: AnyDict, cdp_domain: str) -> DevToolsArrayItem:
        return cls(type=payload.get("type"), ref=payload.get("$ref"), cdp_domain=cdp_domain)

    def generate_code(self) -> str:
        """Generate code."""
        return ""


@dataclass
class DevToolsObjectProperty:
    """Encapsulation of a property for objects that are not simple primitive
    types."""

    cdp_domain: str
    name: str
    description: str
    items: DevToolsArrayItem
    ref: typing.Optional[str] = None
    optional: typing.Optional[bool] = False
    type: typing.Optional[str] = None

    @classmethod
    def from_json(cls, payload: AnyDict, cdp_domain: str) -> DevToolsObjectProperty:
        return cls(
            cdp_domain=cdp_domain,
            name=typing.cast(str, payload.get("name")),
            description=payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC),
            ref=payload.get("$ref", None),
            optional=payload.get("optional", False),
            items=DevToolsArrayItem.from_json(payload.get("items", {}), cdp_domain=cdp_domain),
            type=payload.get("type", None),
        )

    def generate_code(self) -> str:
        """Generate the source code for this particular type property."""
        source = ""
        source += "".join(textwrap.wrap(self.description, width=80, initial_indent="    #: "))
        source += "# noqa"  # Todo: Remove this and wrap appropriately.
        source += "\n"
        source += self.generate_annotation()
        source += "\n"
        return source

    def generate_annotation(self) -> str:
        """Generate the attribute and type hint string."""
        base = f"{name_to_snake_case(self.name)}: "
        annotation = self.ref or self.type
        wrap_array = False
        assert annotation is not None, "no ref or type parsed for a property!"
        if self.type == "array":
            wrap_array = True
            annotation = self.items.type or self.items.ref
            assert annotation is not None, "array item had no type or ref!"
        if "." in annotation:
            dom, sep, anno = annotation.partition(".")
            annotation = "".join((name_to_snake_case(dom), sep, anno))
            if dom.title() == self.cdp_domain.title():
                # Fix shortcomings in the protocol spec where modules are referencing other types
                # with a prefix type that breaks our imports. i.e `network.py` referring to `Network.TYPE`
                # This prevents any issues there, those types live in that particular module and just
                # uses the types that already live in that modules global namespace.
                annotation = anno
        pythonic_type = api_type_to_python_annotation(annotation)
        if self.optional:
            base += f"typing.Optional[{pythonic_type if not wrap_array else f'typing.List[{pythonic_type}]'}] = None"
        else:
            base += pythonic_type
        return indent(base)


@dataclass
class DevToolsType:
    cdp_domain: str
    id: str
    description: str
    type: str
    properties: typing.List[DevToolsObjectProperty]
    enum_options: typing.List[str]

    @classmethod
    def from_json(cls, payload: AnyDict, cdp_domain: str) -> DevToolsType:
        return cls(
            cdp_domain=cdp_domain,
            id=typing.cast(str, payload.get("id")),
            description=payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC),
            type=typing.cast(str, payload.get("type")),
            # These need kept in order with non optional fields first to avoid pain with the generated dataclasses.
            properties=list(
                sorted(
                    [DevToolsObjectProperty.from_json(p, cdp_domain=cdp_domain) for p in payload.get("properties", [])],
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
            # Todo: need to consider pythonic naming in these enums.
            option = option.replace("-", "_")
            source += indent(f'{option.upper()} = "{option}"')
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
        """Generate source code for primitive types (simple subclass
        wrappers)."""
        source = "\n\n"
        source += textwrap.dedent(f"class {self.id}({PRIMITIVE_TYPE_FACTORY[self.type].parent}):")
        source += "\n"
        source += resolve_docstring(self.description)
        source += indent(PRIMITIVE_TYPE_TO_JSON.format(self.id))
        source += indent(SIMPLE_PRIMITIVE_REPR.format("{self.__class__.__name__}", "({super().__repr__()})"))
        return source


@dataclass
class DevToolsEvent:
    def __init__(self, *args, **kw):
        ...

    def generate_code(self) -> str:
        return ""

    @classmethod
    def from_json(cls, payload: AnyDict):
        return cls(**payload)


@dataclass
class DevToolsCommand:
    def __init__(self, *args, **kw):
        ...

    def generate_code(self) -> str:
        return ""

    @classmethod
    def from_json(cls, payload: AnyDict):
        return cls(**payload)


@dataclass
class DevtoolsDomain:
    """Encapsulation of an individual devtools domain."""

    domain: str
    description: str
    dependencies: typing.List[str]
    deprecated: bool
    experimental: bool
    events: typing.List[DevToolsEvent]
    types: typing.List[DevToolsType]
    commands: typing.List[DevToolsCommand]

    @property
    def py_mod_name(self) -> str:
        """Returns the python module name for this instance."""
        return f"{name_to_snake_case(self.domain)}.py"

    @classmethod
    def from_json(cls, payload: AnyDict) -> DevtoolsDomain:
        """Shovel the json arguments into this model and recursively build out
        nested objects."""
        return cls(
            domain=typing.cast(str, payload.get("domain")),
            description=payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC),
            deprecated=payload.get("deprecated", False),
            dependencies=payload.get("dependencies", []),
            experimental=payload.get("experimental", False),
            events=[DevToolsEvent.from_json(e) for e in payload.get("events", [])],
            types=[DevToolsType.from_json(t, cdp_domain=payload["domain"]) for t in payload.get("types", [])],
            commands=[DevToolsCommand.from_json(c) for c in payload.get("commands", [])],
        )

    def generate_code(self) -> str:
        """Generate the full source code for the domain module."""
        requires_enum = bool([x for x in self.types if x.enum_options])
        source = PREAMBLE.format(domain=self.domain)
        source += "\n"
        source += CONSTANT_IMPORTS
        if requires_enum:
            source += textwrap.dedent("import enum")
        source += "\n\n"
        source += self.calculate_imports()
        iterator: typing.Iterator[GeneratesSourceCode] = itertools.chain(self.types, self.events, self.commands)
        for item in iterator:
            source += item.generate_code()
        return source

    def calculate_imports(self) -> str:
        """Calculate the correct imports for this module based on builtins and
        other domains created in the cdp/* directory.

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
        if not self.dependencies:
            return ""
        source = ""
        base = "from . import {}"
        necessary_imports = []
        for dependency in self.dependencies:
            if "." not in dependency:
                module = dependency
            else:
                module = dependency.split(".")[0]
            necessary_imports.append(base.format(name_to_snake_case(module)))
        necessary_imports.sort()  # Keep things lexicographical
        for import_statement in necessary_imports:
            source += textwrap.dedent(import_statement)
            source += "\n"
        return source

    def create_py_module(self) -> pathlib.Path:
        """Writes the python module for this domain to disk, recursively
        generating all the python source code."""
        path = get_generation_rootdir() / self.py_mod_name
        with open(str(path), mode="w") as f:
            f.write(self.generate_code())
        return path


@dataclass
class Domains:
    """Encapsulation of the top level domains array.  This is composed of an
    array of DevtoolDomain objects.

    For now, only domains in the protocol that are not marked
    `deprecated` are built and accessible, but this is likely subject to
    change in future.
    """

    domains: typing.List[DevtoolsDomain]

    def __iter__(self) -> typing.Iterator[DevtoolsDomain]:
        return iter(self.domains)

    @classmethod
    def from_json(cls, payload: AnyDict) -> Domains:
        """Build and generate the full protocol."""
        return cls(domains=[DevtoolsDomain.from_json(domain) for domain in payload["domains"]])

    def create_source_code_on_disk(self) -> None:
        """Automatically generates all the python CDP modules for all of the
        nested children domains."""
        for domain in self.domains:
            domain.create_py_module()
