# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `DOMStorage`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage/

from __future__ import annotations

import typing
from dataclasses import dataclass


class SerializedStorageKey(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> SerializedStorageKey:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class StorageId:
    """DOM Storage identifier."""

    #: Whether the storage is local storage (not session storage).# noqa
    is_local_storage: bool
    #: Security origin for the storage.# noqa
    security_origin: typing.Optional[str] = None
    #: Represents a key by which DOM Storage keys its CachedStorageAreas# noqa
    storage_key: typing.Optional[SerializedStorageKey] = None


@dataclass
class Item:
    """DOM Storage item."""
