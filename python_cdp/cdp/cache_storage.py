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
from dataclasses import dataclass


class CacheId(str):
    """Unique identifier of the Cache object."""

    def to_json(self) -> CacheId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CachedResponseType(str, enum.Enum):
    """Type of HTTP response cached."""

    BASIC = "basic"
    CORS = "cors"
    DEFAULT = "default"
    ERROR = "error"
    OPAQUERESPONSE = "opaqueResponse"
    OPAQUEREDIRECT = "opaqueRedirect"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class DataEntry:
    """Data entry."""

    #: Request URL.# noqa
    request_url: str
    #: Request method.# noqa
    request_method: str
    #: Request headers# noqa
    request_headers: Header
    #: Number of seconds since epoch.# noqa
    response_time: float
    #: HTTP response status code.# noqa
    response_status: int
    #: HTTP response status text.# noqa
    response_status_text: str
    #: HTTP response type# noqa
    response_type: CachedResponseType
    #: Response headers# noqa
    response_headers: Header


@dataclass
class Cache:
    """Cache identifier."""

    #: An opaque unique id of the cache.# noqa
    cache_id: CacheId
    #: Security origin of the cache.# noqa
    security_origin: str
    #: Storage key of the cache.# noqa
    storage_key: str
    #: The name of the cache.# noqa
    cache_name: str


@dataclass
class Header:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    value: str


@dataclass
class CachedResponse:
    """Cached response."""

    #: Entry content, base64-encoded. (Encoded as a base64 string when passedover JSON)# noqa
    body: str


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
