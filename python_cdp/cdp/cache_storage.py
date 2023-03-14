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


@dataclass
class Cache:
    """Cache identifier."""


@dataclass
class Header:
    """Description is missing from the devtools protocol document."""


@dataclass
class CachedResponse:
    """Cached response."""
