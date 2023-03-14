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

from dataclasses import dataclass


class SerializedStorageKey(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class StorageId:
    """DOM Storage identifier."""

    #: Security origin for the storage.
    securityOrigin: str
    #: Represents a key by which DOM Storage keys its CachedStorageAreas
    storageKey: str
    #: Whether the storage is local storage (not session storage).
    isLocalStorage: str


@dataclass
class Item:
    """DOM Storage item."""
