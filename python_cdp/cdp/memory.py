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


class PressureLevel(str, enum.Enum):
    """Memory pressure level."""

    MODERATE = "moderate"
    CRITICAL = "critical"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class SamplingProfileNode(None):
    """Heap profile sample."""

    def to_json(self) -> SamplingProfileNode:
        return self

    @classmethod
    def from_json(cls, value: None) -> SamplingProfileNode:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SamplingProfile(None):
    """Array of heap profile samples."""

    def to_json(self) -> SamplingProfile:
        return self

    @classmethod
    def from_json(cls, value: None) -> SamplingProfile:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Module(None):
    """Executable module information."""

    def to_json(self) -> Module:
        return self

    @classmethod
    def from_json(cls, value: None) -> Module:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
    """Enable/disable suppressing memory pressure notifications in all processes.

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
    """Retrieve native memory allocations profile collected since renderer process startup.

    # noqa
    """
    ...


async def get_browser_sampling_profile() -> None:
    """Retrieve native memory allocations profile collected since browser process startup.

    # noqa
    """
    ...


async def get_sampling_profile() -> None:
    """Retrieve native memory allocations profile collected since last `startSampling` call.

    # noqa
    """
    ...
