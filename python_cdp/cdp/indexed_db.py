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

    #: Database name.
    name: str
    #: Database version (type is not 'integer', as the standard requires theversion number to be 'unsigned long long')
    version: str
    #: Object stores in this database.
    objectStores: str


@dataclass
class ObjectStore:
    """Object store."""

    #: Object store name.
    name: str
    #: Object store key path.
    keyPath: str
    #: If true, object store has auto increment flag set.
    autoIncrement: str
    #: Indexes in this object store.
    indexes: str


@dataclass
class ObjectStoreIndex:
    """Object store index."""

    #: Index name.
    name: str
    #: Index key path.
    keyPath: str
    #: If true, index is unique.
    unique: str
    #: If true, index allows multiple entries for a key.
    multiEntry: str


@dataclass
class Key:
    """Key."""

    #: Key type.
    type: str
    #: Number value.
    number: str
    #: String value.
    string: str
    #: Date value.
    date: str
    #: Array value.
    array: str


@dataclass
class KeyRange:
    """Key range."""

    #: Lower bound.
    lower: str
    #: Upper bound.
    upper: str
    #: If true lower bound is open.
    lowerOpen: str
    #: If true upper bound is open.
    upperOpen: str


@dataclass
class DataEntry:
    """Data entry."""

    #: Key object.
    key: str
    #: Primary key object.
    primaryKey: str
    #: Value object.
    value: str


@dataclass
class KeyPath:
    """Key path."""

    #: Key path type.
    type: str
    #: String value.
    string: str
    #: Array value.
    array: str
