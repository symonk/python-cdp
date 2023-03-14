# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Memory`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Memory/

from __future__ import annotations

import enum
from dataclasses import dataclass


class PressureLevel(str, enum.Enum):
    """Memory pressure level."""

    MODERATE = "moderate"
    CRITICAL = "critical"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SamplingProfileNode:
    """Heap profile sample."""

    #: Size of the sampled allocation.
    size: str
    #: Total bytes attributed to this sample.
    total: str
    #: Execution stack at the point of allocation.
    stack: str


@dataclass
class SamplingProfile:
    """Array of heap profile samples."""

    #: Description is missing from the devtools protocol document.
    samples: str
    #: Description is missing from the devtools protocol document.
    modules: str


@dataclass
class Module:
    """Executable module information."""

    #: Name of the module.
    name: str
    #: UUID of the module.
    uuid: str
    #: Base address where the module is loaded into memory. Encoded as a decimalor hexadecimal (0x prefixed) string.
    baseAddress: str
    #: Size of the module in bytes.
    size: str
