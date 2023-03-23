# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Database`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Database/

from __future__ import annotations

from dataclasses import dataclass

from .utils import memoize_event


class DatabaseId(str):
    """Unique identifier of Database object."""

    def to_json(self) -> DatabaseId:
        return self

    @classmethod
    def from_json(cls, value: str) -> DatabaseId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class Database:
    """Database object."""

    # Database ID. # noqa
    id: DatabaseId
    # Database domain. # noqa
    domain: str
    # Database name. # noqa
    name: str
    # Database version. # noqa
    version: str


@dataclass
class Error:
    """Database error."""

    # Error message. # noqa
    message: str
    # Error code. # noqa
    code: int


@dataclass
@memoize_event("Database.addDatabase")
class AddDatabase:
    """Description is missing from the devtools protocol document."""

    database: Database


async def disable() -> None:
    """Disables database tracking, prevents database events from being sent to the client.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables database tracking, database events will now be delivered to the client.

    # noqa
    """
    ...


async def execute_sql() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def get_database_table_names() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...
