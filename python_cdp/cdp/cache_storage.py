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
    requestURL: str
    #: Request method.# noqa
    requestMethod: str
    #: Request headers# noqa
    requestHeaders: str
    #: Number of seconds since epoch.# noqa
    responseTime: str
    #: HTTP response status code.# noqa
    responseStatus: str
    #: HTTP response status text.# noqa
    responseStatusText: str
    #: HTTP response type# noqa
    responseType: str
    #: Response headers# noqa
    responseHeaders: str


@dataclass
class Cache:
    """Cache identifier."""

    #: An opaque unique id of the cache.# noqa
    cacheId: str
    #: Security origin of the cache.# noqa
    securityOrigin: str
    #: Storage key of the cache.# noqa
    storageKey: str
    #: The name of the cache.# noqa
    cacheName: str


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
