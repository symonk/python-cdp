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
from . import runtime
from .utils import memoize_event


@dataclass
class ProfileNode:
    """Profile node.

    Holds callsite information, execution statistics and child nodes.
    """

    # Unique id of the node. # noqa
    id: int
    # Function location. # noqa
    call_frame: runtime.CallFrame
    # Number of samples where this node was on top of the call stack. # noqa
    hit_count: typing.Optional[int]
    # Child node ids. # noqa
    children: typing.Optional[int]
    # The reason of being not optimized. The function may be deoptimized ormarked as don't optimize. # noqa
    deopt_reason: typing.Optional[str]
    # An array of source position ticks. # noqa
    position_ticks: typing.Optional[PositionTickInfo]


@dataclass
class Profile:
    """Profile."""

    # The list of profile nodes. First item is the root node. # noqa
    nodes: ProfileNode
    # Profiling start timestamp in microseconds. # noqa
    start_time: float
    # Profiling end timestamp in microseconds. # noqa
    end_time: float
    # Ids of samples top nodes. # noqa
    samples: typing.Optional[int]
    # Time intervals between adjacent samples in microseconds. The first deltais relative to the profile startTime. # noqa
    time_deltas: typing.Optional[int]


@dataclass
class PositionTickInfo:
    """Specifies a number of samples attributed to a certain source position."""

    # Source line number (1-based). # noqa
    line: int
    # Number of samples attributed to the source line. # noqa
    ticks: int


@dataclass
class CoverageRange:
    """Coverage data for a source range."""

    # JavaScript script source offset for the range start. # noqa
    start_offset: int
    # JavaScript script source offset for the range end. # noqa
    end_offset: int
    # Collected execution count of the source range. # noqa
    count: int


@dataclass
class FunctionCoverage:
    """Coverage data for a JavaScript function."""

    # JavaScript function name. # noqa
    function_name: str
    # Source ranges inside the function with coverage data. # noqa
    ranges: CoverageRange
    # Whether coverage data for this function has block granularity. # noqa
    is_block_coverage: bool


@dataclass
class ScriptCoverage:
    """Coverage data for a JavaScript script."""

    # JavaScript script id. # noqa
    script_id: runtime.ScriptId
    # JavaScript script name or url. # noqa
    url: str
    # Functions contained in the script that has coverage data. # noqa
    functions: FunctionCoverage


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
