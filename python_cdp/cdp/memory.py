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


@dataclass
class SamplingProfileNode:
    """Heap profile sample."""


@dataclass
class SamplingProfile:
    """Array of heap profile samples."""


@dataclass
class Module:
    """Executable module information."""
