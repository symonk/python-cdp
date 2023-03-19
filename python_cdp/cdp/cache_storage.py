# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `CacheStorage`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/CacheStorage/

from __future__ import annotations

import enum


class CacheId(str):
    """Unique identifier of the Cache object."""

    def to_json(self) -> CacheId:
        return self

    @classmethod
    def from_json(cls, value: str) -> CacheId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CachedResponseType(str, enum.Enum):
    """Type of HTTP response cached."""

    BASIC = "basic"
    CORS = "cors"
    DEFAULT = "default"
    ERROR = "error"
    OPAQUE_RESPONSE = "opaque_response"
    OPAQUE_REDIRECT = "opaque_redirect"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class DataEntry(None):
    """Data entry."""

    def to_json(self) -> DataEntry:
        return self

    @classmethod
    def from_json(cls, value: None) -> DataEntry:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Cache(None):
    """Cache identifier."""

    def to_json(self) -> Cache:
        return self

    @classmethod
    def from_json(cls, value: None) -> Cache:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Header(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> Header:
        return self

    @classmethod
    def from_json(cls, value: None) -> Header:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CachedResponse(None):
    """Cached response."""

    def to_json(self) -> CachedResponse:
        return self

    @classmethod
    def from_json(cls, value: None) -> CachedResponse:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


async def delete_cache() -> None:
    """Deletes a cache.

    # noqa
    """
    ...


async def delete_entry() -> None:
    """Deletes a cache entry.

    # noqa
    """
    ...


async def request_cache_names() -> None:
    """Requests cache names.

    # noqa
    """
    ...


async def request_cached_response() -> None:
    """Fetches cache entry.

    # noqa
    """
    ...


async def request_entries() -> None:
    """Requests data from cache.

    # noqa
    """
    ...
