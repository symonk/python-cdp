# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `IndexedDB`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB/

from __future__ import annotations

import typing
from dataclasses import dataclass

from . import runtime


@dataclass
class DatabaseWithObjectStores:
    """Database with an array of object stores."""

    # Database name.# noqa


str
# Database version (type is not 'integer', as the standard requires theversion number to be 'unsigned long long')# noqa
float
# Object stores in this database.# noqa
typing.List[ObjectStore]


@dataclass
class ObjectStore:
    """Object store."""

    # Object store name.# noqa


str
# Object store key path.# noqa
KeyPath
# If true, object store has auto increment flag set.# noqa
bool
# Indexes in this object store.# noqa
typing.List[ObjectStoreIndex]


@dataclass
class ObjectStoreIndex:
    """Object store index."""

    # Index name.# noqa


str
# Index key path.# noqa
KeyPath
# If true, index is unique.# noqa
bool
# If true, index allows multiple entries for a key.# noqa
bool


@dataclass
class Key:
    """Key."""

    # Key type.# noqa


str
# Number value.# noqa
typing.Optional[float]
# String value.# noqa
typing.Optional[str]
# Date value.# noqa
typing.Optional[float]
# Array value.# noqa
typing.Optional[typing.List[Key]]


@dataclass
class KeyRange:
    """Key range."""

    # If true lower bound is open.# noqa


bool
# If true upper bound is open.# noqa
bool
# Lower bound.# noqa
Key
# Upper bound.# noqa
Key


@dataclass
class DataEntry:
    """Data entry."""

    # Key object.# noqa


runtime.RemoteObject
# Primary key object.# noqa
runtime.RemoteObject
# Value object.# noqa
runtime.RemoteObject


@dataclass
class KeyPath:
    """Key path."""

    # Key path type.# noqa


str
# String value.# noqa
typing.Optional[str]
# Array value.# noqa
typing.Optional[typing.List[str]]


async def clear_object_store() -> None:
    """Clears all entries from an object store.

    # noqa
    """
    ...


async def delete_database() -> None:
    """Deletes a database.

    # noqa
    """
    ...


async def delete_object_store_entries() -> None:
    """Delete a range of entries from an object store # noqa."""
    ...


async def disable() -> None:
    """Disables events from backend.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables events from backend.

    # noqa
    """
    ...


async def request_data() -> None:
    """Requests data from object store or index.

    # noqa
    """
    ...


async def get_metadata() -> None:
    """Gets metadata of an object store.

    # noqa
    """
    ...


async def request_database() -> None:
    """Requests database with given name in given frame.

    # noqa
    """
    ...


async def request_database_names() -> None:
    """Requests database names for given security origin.

    # noqa
    """
    ...
