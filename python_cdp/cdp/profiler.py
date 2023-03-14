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

from dataclasses import dataclass


@dataclass
class ProfileNode:
    """Profile node.

    Holds callsite information, execution statistics and child nodes.
    """

    #: Unique id of the node.# noqa
    id: str
    #: Function location.# noqa
    callFrame: str
    #: Number of samples where this node was on top of the call stack.# noqa
    hitCount: str
    #: Child node ids.# noqa
    children: str
    #: The reason of being not optimized. The function may be deoptimized ormarked as don't optimize.# noqa
    deoptReason: str
    #: An array of source position ticks.# noqa
    positionTicks: str


@dataclass
class Profile:
    """Profile."""

    #: The list of profile nodes. First item is the root node.# noqa
    nodes: str
    #: Profiling start timestamp in microseconds.# noqa
    startTime: str
    #: Profiling end timestamp in microseconds.# noqa
    endTime: str
    #: Ids of samples top nodes.# noqa
    samples: str
    #: Time intervals between adjacent samples in microseconds. The first deltais relative to the profile startTime.# noqa
    timeDeltas: str


@dataclass
class PositionTickInfo:
    """Specifies a number of samples attributed to a certain source
    position."""

    #: Source line number (1-based).# noqa
    line: str
    #: Number of samples attributed to the source line.# noqa
    ticks: str


@dataclass
class CoverageRange:
    """Coverage data for a source range."""

    #: JavaScript script source offset for the range start.# noqa
    startOffset: str
    #: JavaScript script source offset for the range end.# noqa
    endOffset: str
    #: Collected execution count of the source range.# noqa
    count: str


@dataclass
class FunctionCoverage:
    """Coverage data for a JavaScript function."""

    #: JavaScript function name.# noqa
    functionName: str
    #: Source ranges inside the function with coverage data.# noqa
    ranges: str
    #: Whether coverage data for this function has block granularity.# noqa
    isBlockCoverage: str


@dataclass
class ScriptCoverage:
    """Coverage data for a JavaScript script."""

    #: JavaScript script id.# noqa
    scriptId: str
    #: JavaScript script name or url.# noqa
    url: str
    #: Functions contained in the script that has coverage data.# noqa
    functions: str
