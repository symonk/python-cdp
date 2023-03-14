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

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


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

    #: Request URL.
    requestURL: str
    #: Request method.
    requestMethod: str
    #: Request headers
    requestHeaders: str
    #: Number of seconds since epoch.
    responseTime: str
    #: HTTP response status code.
    responseStatus: str
    #: HTTP response status text.
    responseStatusText: str
    #: HTTP response type
    responseType: str
    #: Response headers
    responseHeaders: str


@dataclass
class Cache:
    """Cache identifier."""

    #: An opaque unique id of the cache.
    cacheId: str
    #: Security origin of the cache.
    securityOrigin: str
    #: Storage key of the cache.
    storageKey: str
    #: The name of the cache.
    cacheName: str


@dataclass
class Header:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.
    name: str
    #: Description is missing from the devtools protocol document.
    value: str


@dataclass
class CachedResponse:
    """Cached response."""

    #: Entry content, base64-encoded. (Encoded as a base64 string when passedover JSON)
    body: str
