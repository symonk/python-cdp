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


class DatabaseWithObjectStores(None):
    """Database with an array of object stores."""

    def to_json(self) -> DatabaseWithObjectStores:
        return self

    @classmethod
    def from_json(cls, value: None) -> DatabaseWithObjectStores:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ObjectStore(None):
    """Object store."""

    def to_json(self) -> ObjectStore:
        return self

    @classmethod
    def from_json(cls, value: None) -> ObjectStore:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ObjectStoreIndex(None):
    """Object store index."""

    def to_json(self) -> ObjectStoreIndex:
        return self

    @classmethod
    def from_json(cls, value: None) -> ObjectStoreIndex:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Key(None):
    """Key."""

    def to_json(self) -> Key:
        return self

    @classmethod
    def from_json(cls, value: None) -> Key:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class KeyRange(None):
    """Key range."""

    def to_json(self) -> KeyRange:
        return self

    @classmethod
    def from_json(cls, value: None) -> KeyRange:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class DataEntry(None):
    """Data entry."""

    def to_json(self) -> DataEntry:
        return self

    @classmethod
    def from_json(cls, value: None) -> DataEntry:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class KeyPath(None):
    """Key path."""

    def to_json(self) -> KeyPath:
        return self

    @classmethod
    def from_json(cls, value: None) -> KeyPath:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
