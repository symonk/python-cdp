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
import typing


from . import runtime


@dataclass
class DatabaseWithObjectStores:
    """ Database with an array of object stores. """
    #: Database name.# noqa
    name: str
    #: Database version (type is not 'integer', as the standard requires theversion number to be 'unsigned long long')# noqa
    version: float
    #: Object stores in this database.# noqa
    object_stores: ObjectStore


@dataclass
class ObjectStore:
    """ Object store. """
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
    """ Object store index. """
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
    """ Key. """
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
    """ Key range. """
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
    """ Data entry. """
    #: Key object.# noqa
    key: runtime.RemoteObject
    #: Primary key object.# noqa
    primary_key: runtime.RemoteObject
    #: Value object.# noqa
    value: runtime.RemoteObject


@dataclass
class KeyPath:
    """ Key path. """
    #: Key path type.# noqa
    type: str
    #: String value.# noqa
    string: typing.Optional[str] = None
    #: Array value.# noqa
    array: typing.Optional[typing.List[str]] = None
