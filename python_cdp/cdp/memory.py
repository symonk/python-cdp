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

    #: Size of the sampled allocation.# noqa
    size: float
    #: Total bytes attributed to this sample.# noqa
    total: float
    #: Execution stack at the point of allocation.# noqa
    stack: str


@dataclass
class SamplingProfile:
    """Array of heap profile samples."""

    #: Description is missing from the devtools protocol document.# noqa
    samples: SamplingProfileNode
    #: Description is missing from the devtools protocol document.# noqa
    modules: Module


@dataclass
class Module:
    """Executable module information."""

    #: Name of the module.# noqa
    name: str
    #: UUID of the module.# noqa
    uuid: str
    #: Base address where the module is loaded into memory. Encoded as a decimalor hexadecimal (0x prefixed) string.# noqa
    base_address: str
    #: Size of the module in bytes.# noqa
    size: float


async def get_dom_counters() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def prepare_for_leak_detection() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def forcibly_purge_java_script_memory() -> None:
    """Simulate OomIntervention by purging V8 memory.

    # noqa
    """
    ...


async def set_pressure_notifications_suppressed() -> None:
    """Enable/disable suppressing memory pressure notifications in all
    processes.

    # noqa
    """
    ...


async def simulate_pressure_notification() -> None:
    """Simulate a memory pressure notification in all processes.

    # noqa
    """
    ...


async def start_sampling() -> None:
    """Start collecting native memory profile.

    # noqa
    """
    ...


async def stop_sampling() -> None:
    """Stop collecting native memory profile.

    # noqa
    """
    ...


async def get_all_time_sampling_profile() -> None:
    """Retrieve native memory allocations profile collected since renderer
    process startup.

    # noqa
    """
    ...


async def get_browser_sampling_profile() -> None:
    """Retrieve native memory allocations profile collected since browser
    process startup.

    # noqa
    """
    ...


async def get_sampling_profile() -> None:
    """Retrieve native memory allocations profile collected since last
    `startSampling` call.

    # noqa
    """
    ...
