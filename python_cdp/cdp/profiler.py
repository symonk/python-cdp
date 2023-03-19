# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Profiler`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Profiler/

from __future__ import annotations

import typing
from dataclasses import dataclass

from . import debugger
from .utils import memoize_event


class ProfileNode(None):
    """Profile node.

    Holds callsite information, execution statistics and child nodes.
    """

    def to_json(self) -> ProfileNode:
        return self

    @classmethod
    def from_json(cls, value: None) -> ProfileNode:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Profile(None):
    """Profile."""

    def to_json(self) -> Profile:
        return self

    @classmethod
    def from_json(cls, value: None) -> Profile:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class PositionTickInfo(None):
    """Specifies a number of samples attributed to a certain source position."""

    def to_json(self) -> PositionTickInfo:
        return self

    @classmethod
    def from_json(cls, value: None) -> PositionTickInfo:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CoverageRange(None):
    """Coverage data for a source range."""

    def to_json(self) -> CoverageRange:
        return self

    @classmethod
    def from_json(cls, value: None) -> CoverageRange:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class FunctionCoverage(None):
    """Coverage data for a JavaScript function."""

    def to_json(self) -> FunctionCoverage:
        return self

    @classmethod
    def from_json(cls, value: None) -> FunctionCoverage:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ScriptCoverage(None):
    """Coverage data for a JavaScript script."""

    def to_json(self) -> ScriptCoverage:
        return self

    @classmethod
    def from_json(cls, value: None) -> ScriptCoverage:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("Profiler.consoleProfileFinished")
class ConsoleProfileFinished:
    """Description is missing from the devtools protocol document."""

    id: str
    location: debugger.Location
    profile: Profile
    title: typing.Optional[str]


@dataclass
@memoize_event("Profiler.consoleProfileStarted")
class ConsoleProfileStarted:
    """Sent when new profile recording is started using console.profile() call."""

    id: str
    location: debugger.Location
    title: typing.Optional[str]


@dataclass
@memoize_event("Profiler.preciseCoverageDeltaUpdate")
class PreciseCoverageDeltaUpdate:
    """Reports coverage delta since the last poll (either from an event like this, or from `takePreciseCoverage` for the
    current isolate.

    May only be sent if precise code coverage has been started. This event can be trigged by the embedder to, for
    example, trigger collection of coverage data immediately at a certain point in time.
    """

    timestamp: float
    occasion: str
    result: typing.List[ScriptCoverage]


async def disable() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def enable() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def get_best_effort_coverage() -> None:
    """Collect coverage data for the current isolate.

    The coverage data may be incomplete due to garbage collection. # noqa
    """
    ...


async def set_sampling_interval() -> None:
    """Changes CPU profiler sampling interval.

    Must be called before CPU profiles recording started. # noqa
    """
    ...


async def start() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def start_precise_coverage() -> None:
    """Enable precise code coverage.

    Coverage data for JavaScript executed before enabling precise code coverage may be incomplete. Enabling prevents
    running optimized code and resets execution counters. # noqa
    """
    ...


async def stop() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def stop_precise_coverage() -> None:
    """Disable precise code coverage.

    Disabling releases unnecessary execution count records and allows executing optimized code. # noqa
    """
    ...


async def take_precise_coverage() -> None:
    """Collect coverage data for the current isolate, and resets execution counters.

    Precise code coverage needs to have started. # noqa
    """
    ...
