from __future__ import annotations  # isort: skip
import typing
from dataclasses import dataclass


@dataclass
class DevToolsType:
    ...


@dataclass
class DevToolsEvent:
    ...


@dataclass
class DevToolsCommand:
    ...


class DevtoolsDomain:
    """Encapsulation of an individual devtools domain."""

    domain: str
    experimental: bool
    dependencies: typing.List[str]
    types: typing.List[DevToolsType]
    commands: typing.List[DevToolsCommand]
    events: typing.List[DevToolsEvent]


class Domains:
    """Encapsulation of the top level domains array.  This is composed of an
    array of DevtoolDomain objects.

    For now, only domains in the protocol that are not marked
    `deprecated` are built and accessible, but this is likely subject to
    change in future.
    """

    domains: typing.List[DevtoolsDomain]

    @classmethod
    def from_json(object):
        """Build and generate the full protocol."""
        ...
