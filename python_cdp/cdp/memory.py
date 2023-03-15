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
from dataclasses import dataclass
import typing
import enum



class PressureLevel(str, enum.Enum):
    """ Memory pressure level. """

    MODERATE = "moderate"
    CRITICAL = "critical"


    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SamplingProfileNode:
    """ Heap profile sample. """
    #: Size of the sampled allocation.# noqa
    size: float
    #: Total bytes attributed to this sample.# noqa
    total: float
    #: Execution stack at the point of allocation.# noqa
    stack: str


@dataclass
class SamplingProfile:
    """ Array of heap profile samples. """
    #: Description is missing from the devtools protocol document.# noqa
    samples: SamplingProfileNode
    #: Description is missing from the devtools protocol document.# noqa
    modules: Module


@dataclass
class Module:
    """ Executable module information """
    #: Name of the module.# noqa
    name: str
    #: UUID of the module.# noqa
    uuid: str
    #: Base address where the module is loaded into memory. Encoded as a decimalor hexadecimal (0x prefixed) string.# noqa
    base_address: str
    #: Size of the module in bytes.# noqa
    size: float
