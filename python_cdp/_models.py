from __future__ import annotations  # isort: skip
import pathlib
import typing
from dataclasses import dataclass

from ._headers import CONSTANT_IMPORTS
from ._headers import PREAMBLE
from ._utils import get_generation_rootdir
from ._utils import name_to_snake_case


@dataclass
class DevToolsType:
    id: str
    type: str

    @classmethod
    def from_json(cls, json_object) -> DevToolsType:
        return cls(id=json_object.get("id"), type=json_object.get("type"))

    def generate_code(self) -> str:
        """Generate code!"""
        return ""


@dataclass
class DevToolsEvent:
    ...


@dataclass
class DevToolsCommand:
    ...


@dataclass
class DevtoolsDomain:
    """Encapsulation of an individual devtools domain."""

    domain: str
    description: str
    dependencies: typing.List[str]
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
            description=json_payload.get("description", "Docstring missing from the devtools specification."),
            dependencies=json_payload.get("dependencies", []),
            experimental=json_payload.get("experimental", False),
            events=json_payload.get("events", []),
            types=[DevToolsType.from_json(t) for t in json_payload.get("types", [])],
            commands=json_payload.get("commands", []),
        )

    def generate_code(self) -> str:
        """Generate the full source code for the domain module."""
        source = PREAMBLE.format(domain=self.domain)
        source += "\n" + CONSTANT_IMPORTS
        source += f'''
@dataclass
class {self.domain}:
    """Encapsulation of the CDP `{self.domain}` Domain.
       This domains experimental status is: {str(self.experimental).upper()}"""
'''
        for type in self.types:
            source += type.generate_code()
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

    @classmethod
    def from_json(cls, object) -> Domains:
        """Build and generate the full protocol."""
        return cls(domains=[DevtoolsDomain.from_json(domain) for domain in object["domains"]])

    def create_source_code_on_disk(self) -> None:
        """Automatically generates all the python CDP modules for all of the
        nested children domains."""
        for domain in self.domains:
            domain.create_py_module()
