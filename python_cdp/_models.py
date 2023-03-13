from __future__ import annotations  # isort: skip
import pathlib
import typing
from dataclasses import dataclass
from dataclasses import field

from ._headers import CONSTANT_IMPORTS
from ._headers import PREAMBLE
from ._utils import get_generation_rootdir
from ._utils import name_to_snake_case


@dataclass
class DevToolsType:
    ...


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
    description: str = "Docstring missing from the devtools specification."
    dependencies: typing.List[str] = field(default_factory=list)
    experimental: bool = False
    events: typing.List[DevToolsEvent] = field(default_factory=list)
    types: typing.List[DevToolsType] = field(default_factory=list)
    commands: typing.List[DevToolsCommand] = field(default_factory=list)

    @property
    def py_mod_name(self) -> str:
        """Returns the python module name for this instance."""
        return f"{name_to_snake_case(self.domain)}.py"

    @classmethod
    def from_json(cls, json_payload: typing.Dict[str, typing.Any]) -> DevtoolsDomain:
        """Shovel the json arguments into this model and recursively build out
        nested objects."""
        return cls(
            domain=json_payload["domain"],
            description=json_payload["description"],
            dependencies=json_payload["dependencies"],
            experimental=json_payload["experimental"],
            events=json_payload["events"],
            types=json_payload["types"],
            commands=json_payload["commands"],
        )

    def generate_code(self) -> str:
        """Generate the full source code for the domain module."""
        source = PREAMBLE
        source += "\n" + CONSTANT_IMPORTS
        source += f'''
@dataclass
class {self.__class__.__name__}:
    """Encapsulation of the CDP `{self.__class__.__name__}` Domain.
       This domains experimental status is: {str(self.experimental).upper()}"""
'''
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
