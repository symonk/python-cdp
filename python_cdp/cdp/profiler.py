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

    #: Unique id of the node.
    id: str
    #: Function location.
    callFrame: str
    #: Number of samples where this node was on top of the call stack.
    hitCount: str
    #: Child node ids.
    children: str
    #: The reason of being not optimized. The function may be deoptimized ormarked as don't optimize.
    deoptReason: str
    #: An array of source position ticks.
    positionTicks: str


@dataclass
class Profile:
    """Profile."""

    #: The list of profile nodes. First item is the root node.
    nodes: str
    #: Profiling start timestamp in microseconds.
    startTime: str
    #: Profiling end timestamp in microseconds.
    endTime: str
    #: Ids of samples top nodes.
    samples: str
    #: Time intervals between adjacent samples in microseconds. The first deltais relative to the profile startTime.
    timeDeltas: str


@dataclass
class PositionTickInfo:
    """Specifies a number of samples attributed to a certain source
    position."""

    #: Source line number (1-based).
    line: str
    #: Number of samples attributed to the source line.
    ticks: str


@dataclass
class CoverageRange:
    """Coverage data for a source range."""

    #: JavaScript script source offset for the range start.
    startOffset: str
    #: JavaScript script source offset for the range end.
    endOffset: str
    #: Collected execution count of the source range.
    count: str


@dataclass
class FunctionCoverage:
    """Coverage data for a JavaScript function."""

    #: JavaScript function name.
    functionName: str
    #: Source ranges inside the function with coverage data.
    ranges: str
    #: Whether coverage data for this function has block granularity.
    isBlockCoverage: str


@dataclass
class ScriptCoverage:
    """Coverage data for a JavaScript script."""

    #: JavaScript script id.
    scriptId: str
    #: JavaScript script name or url.
    url: str
    #: Functions contained in the script that has coverage data.
    functions: str
