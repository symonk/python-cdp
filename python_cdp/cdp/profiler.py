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
import typing


from . import debugger
from . import runtime


@dataclass
class ProfileNode:
    """ Profile node. Holds callsite information, execution statistics and child nodes. """
    #: Unique id of the node.# noqa
    id: int
    #: Function location.# noqa
    call_frame: runtime.CallFrame
    #: Number of samples where this node was on top of the call stack.# noqa
    hit_count: typing.Optional[int] = None
    #: Child node ids.# noqa
    children: typing.Optional[typing.List[int]] = None
    #: The reason of being not optimized. The function may be deoptimized ormarked as don't optimize.# noqa
    deopt_reason: typing.Optional[str] = None
    #: An array of source position ticks.# noqa
    position_ticks: typing.Optional[typing.List[PositionTickInfo]] = None


@dataclass
class Profile:
    """ Profile. """
    #: The list of profile nodes. First item is the root node.# noqa
    nodes: ProfileNode
    #: Profiling start timestamp in microseconds.# noqa
    start_time: float
    #: Profiling end timestamp in microseconds.# noqa
    end_time: float
    #: Ids of samples top nodes.# noqa
    samples: typing.Optional[typing.List[int]] = None
    #: Time intervals between adjacent samples in microseconds. The first deltais relative to the profile startTime.# noqa
    time_deltas: typing.Optional[typing.List[int]] = None


@dataclass
class PositionTickInfo:
    """ Specifies a number of samples attributed to a certain source position. """
    #: Source line number (1-based).# noqa
    line: int
    #: Number of samples attributed to the source line.# noqa
    ticks: int


@dataclass
class CoverageRange:
    """ Coverage data for a source range. """
    #: JavaScript script source offset for the range start.# noqa
    start_offset: int
    #: JavaScript script source offset for the range end.# noqa
    end_offset: int
    #: Collected execution count of the source range.# noqa
    count: int


@dataclass
class FunctionCoverage:
    """ Coverage data for a JavaScript function. """
    #: JavaScript function name.# noqa
    function_name: str
    #: Source ranges inside the function with coverage data.# noqa
    ranges: CoverageRange
    #: Whether coverage data for this function has block granularity.# noqa
    is_block_coverage: bool


@dataclass
class ScriptCoverage:
    """ Coverage data for a JavaScript script. """
    #: JavaScript script id.# noqa
    script_id: runtime.ScriptId
    #: JavaScript script name or url.# noqa
    url: str
    #: Functions contained in the script that has coverage data.# noqa
    functions: FunctionCoverage
