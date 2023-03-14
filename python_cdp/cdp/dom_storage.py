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
    """Description is missing from the devtools protocol document.."""

    def to_json(self) -> str:
        return self


@dataclass
class StorageId:
    """DOM Storage identifier."""

    ...


@dataclass
class Item:
    """DOM Storage item."""

    ...
