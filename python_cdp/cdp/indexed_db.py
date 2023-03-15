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

    #: Database name.# noqa
    name: str
    #: Database version (type is not 'integer', as the standard requires theversion number to be 'unsigned long long')# noqa
    version: float
    #: Object stores in this database.# noqa
    object_stores: ObjectStore


@dataclass
class ObjectStore:
    """Object store."""

    #: Object store name.# noqa
    name: str
    #: Object store key path.# noqa
    key_path: KeyPath
    #: If true, object store has auto increment flag set.# noqa
    auto_increment: bool
    #: Indexes in this object store.# noqa
    indexes: ObjectStoreIndex


@dataclass
class ObjectStoreIndex:
    """Object store index."""

    #: Index name.# noqa
    name: str
    #: Index key path.# noqa
    key_path: KeyPath
    #: If true, index is unique.# noqa
    unique: bool
    #: If true, index allows multiple entries for a key.# noqa
    multi_entry: bool


@dataclass
class Key:
    """Key."""

    #: Key type.# noqa
    type: str
    #: Number value.# noqa
    number: typing.Optional[float] = None
    #: String value.# noqa
    string: typing.Optional[str] = None
    #: Date value.# noqa
    date: typing.Optional[float] = None
    #: Array value.# noqa
    array: typing.Optional[typing.List[Key]] = None


@dataclass
class KeyRange:
    """Key range."""

    #: If true lower bound is open.# noqa
    lower_open: bool
    #: If true upper bound is open.# noqa
    upper_open: bool
    #: Lower bound.# noqa
    lower: typing.Optional[Key] = None
    #: Upper bound.# noqa
    upper: typing.Optional[Key] = None


@dataclass
class DataEntry:
    """Data entry."""

    #: Key object.# noqa
    key: runtime.RemoteObject
    #: Primary key object.# noqa
    primary_key: runtime.RemoteObject
    #: Value object.# noqa
    value: runtime.RemoteObject


@dataclass
class KeyPath:
    """Key path."""

    #: Key path type.# noqa
    type: str
    #: String value.# noqa
    string: typing.Optional[str] = None
    #: Array value.# noqa
    array: typing.Optional[typing.List[str]] = None


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
