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

from dataclasses import dataclass


@dataclass
class DatabaseWithObjectStores:
    """Database with an array of object stores."""

    #: Database name.# noqa
    name: str
    #: Database version (type is not 'integer', as the standard requires theversion number to be 'unsigned long long')# noqa
    version: str
    #: Object stores in this database.# noqa
    objectStores: str


@dataclass
class ObjectStore:
    """Object store."""

    #: Object store name.# noqa
    name: str
    #: Object store key path.# noqa
    keyPath: str
    #: If true, object store has auto increment flag set.# noqa
    autoIncrement: str
    #: Indexes in this object store.# noqa
    indexes: str


@dataclass
class ObjectStoreIndex:
    """Object store index."""

    #: Index name.# noqa
    name: str
    #: Index key path.# noqa
    keyPath: str
    #: If true, index is unique.# noqa
    unique: str
    #: If true, index allows multiple entries for a key.# noqa
    multiEntry: str


@dataclass
class Key:
    """Key."""

    #: Key type.# noqa
    type: str
    #: Number value.# noqa
    number: str
    #: String value.# noqa
    string: str
    #: Date value.# noqa
    date: str
    #: Array value.# noqa
    array: str


@dataclass
class KeyRange:
    """Key range."""

    #: Lower bound.# noqa
    lower: str
    #: Upper bound.# noqa
    upper: str
    #: If true lower bound is open.# noqa
    lowerOpen: str
    #: If true upper bound is open.# noqa
    upperOpen: str


@dataclass
class DataEntry:
    """Data entry."""

    #: Key object.# noqa
    key: str
    #: Primary key object.# noqa
    primaryKey: str
    #: Value object.# noqa
    value: str


@dataclass
class KeyPath:
    """Key path."""

    #: Key path type.# noqa
    type: str
    #: String value.# noqa
    string: str
    #: Array value.# noqa
    array: str
