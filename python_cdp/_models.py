from __future__ import annotations  # isort: skip
import collections
import itertools
import pathlib
import typing
from dataclasses import dataclass

from ._const import MISSING_DESCRIPTION_IN_PROTOCOL_DOC
from ._headers import CONSTANT_IMPORTS
from ._headers import PREAMBLE
from ._protocols import GeneratesSourceCode
from ._utils import get_generation_rootdir
from ._utils import name_to_snake_case


@dataclass
class DevToolsObjectProperty:
    """Encapsulation of a property for objects that are not simple primitive
    types."""

    @classmethod
    def from_json(cls, json_object) -> DevToolsObjectProperty:
        return cls()


TypeStore = collections.namedtuple("TypeStore", "parent, annotation")
PRIMITIVE_TYPE_FACTORY = {
    "string": TypeStore("str", "str"),
    "number": TypeStore("float", "float"),
    "boolean": TypeStore("bool", "bool"),
}


@dataclass
class DevToolsType:
    id: str
    description: str
    type: str
    properties: typing.List[DevToolsObjectProperty]
    enum_options: typing.List[str]

    @classmethod
    def from_json(cls, json_object) -> DevToolsType:
        return cls(
            id=json_object.get("id"),
            description=json_object.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC),
            type=json_object.get("type"),
            properties=[DevToolsObjectProperty.from_json(p) for p in json_object.get("properties", [])],
            enum_options=json_object.get("enum", []),
        )

    def generate_code(self) -> str:
        """Build out python source code for the CDP types."""
        if self.type in PRIMITIVE_TYPE_FACTORY:
            return self._build_for_primitive_type()
        return self._build_for_object_type()

    def _build_for_enum_type(self) -> str:
        """Generate source code for enum types."""
        return f'''
@dataclass
class {self.id}:
    """ {self.description} """
'''

    def _build_for_object_type(self) -> str:
        """Generate source code for object types."""
        return f'''
@dataclass
class {self.id}:
    """ {self.description} """
    ...
'''

    def _build_for_primitive_type(self) -> str:
        """Generate source code for primitive types (simple subclass
        wrappers)."""
        return f'''
class {self.id}({PRIMITIVE_TYPE_FACTORY[self.type].parent}):
    """ {self.description} """

    def to_json(self) -> {PRIMITIVE_TYPE_FACTORY[self.type].annotation}:
        return self
    '''


@dataclass
class DevToolsEvent:
    def __init__(self, *args, **kw):
        ...

    def generate_code(self) -> str:
        return ""

    @classmethod
    def from_json(cls, json_payload):
        return cls(**json_payload)


@dataclass
class DevToolsCommand:
    def __init__(self, *args, **kw):
        ...

    def generate_code(self) -> str:
        return ""

    @classmethod
    def from_json(cls, json_payload):
        return cls(**json_payload)


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
    def from_json(cls, json_payload: typing.Dict[str, typing.Any]) -> DevtoolsDomain:
        """Shovel the json arguments into this model and recursively build out
        nested objects."""
        return cls(
            domain=typing.cast(str, json_payload.get("domain")),
            description=json_payload.get("description", MISSING_DESCRIPTION_IN_PROTOCOL_DOC),
            deprecated=json_payload.get("deprecated", False),
            dependencies=json_payload.get("dependencies", []),
            experimental=json_payload.get("experimental", False),
            events=[DevToolsEvent.from_json(e) for e in json_payload.get("events", [])],
            types=[DevToolsType.from_json(t) for t in json_payload.get("types", [])],
            commands=[DevToolsCommand.from_json(c) for c in json_payload.get("commands", [])],
        )

    def generate_code(self) -> str:
        """Generate the full source code for the domain module."""
        source = PREAMBLE.format(domain=self.domain)
        source += "\n" + CONSTANT_IMPORTS
        iterator: typing.Iterator[GeneratesSourceCode] = itertools.chain(self.types, self.events, self.commands)
        for item in iterator:
            source += item.generate_code()
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
    def from_json(cls, object) -> Domains:
        """Build and generate the full protocol."""
        return cls(domains=[DevtoolsDomain.from_json(domain) for domain in object["domains"]])

    def create_source_code_on_disk(self) -> None:
        """Automatically generates all the python CDP modules for all of the
        nested children domains."""
        for domain in self.domains:
            domain.create_py_module()
