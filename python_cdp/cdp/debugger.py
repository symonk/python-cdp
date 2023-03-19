# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Debugger`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Debugger/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import runtime
from .utils import memoize_event


class BreakpointId(str):
    """Breakpoint identifier."""

    def to_json(self) -> BreakpointId:
        return self

    @classmethod
    def from_json(cls, value: str) -> BreakpointId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CallFrameId(str):
    """Call frame identifier."""

    def to_json(self) -> CallFrameId:
        return self

    @classmethod
    def from_json(cls, value: str) -> CallFrameId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Location(None):
    """Location in the source code."""

    def to_json(self) -> Location:
        return self

    @classmethod
    def from_json(cls, value: None) -> Location:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ScriptPosition(None):
    """Location in the source code."""

    def to_json(self) -> ScriptPosition:
        return self

    @classmethod
    def from_json(cls, value: None) -> ScriptPosition:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class LocationRange(None):
    """Location range within one script."""

    def to_json(self) -> LocationRange:
        return self

    @classmethod
    def from_json(cls, value: None) -> LocationRange:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CallFrame(None):
    """JavaScript call frame.

    Array of call frames form the call stack.
    """

    def to_json(self) -> CallFrame:
        return self

    @classmethod
    def from_json(cls, value: None) -> CallFrame:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Scope(None):
    """Scope description."""

    def to_json(self) -> Scope:
        return self

    @classmethod
    def from_json(cls, value: None) -> Scope:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SearchMatch(None):
    """Search match for resource."""

    def to_json(self) -> SearchMatch:
        return self

    @classmethod
    def from_json(cls, value: None) -> SearchMatch:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class BreakLocation(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> BreakLocation:
        return self

    @classmethod
    def from_json(cls, value: None) -> BreakLocation:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class WasmDisassemblyChunk(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> WasmDisassemblyChunk:
        return self

    @classmethod
    def from_json(cls, value: None) -> WasmDisassemblyChunk:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ScriptLanguage(str, enum.Enum):
    """Enum of possible script languages."""

    _JAVA_SCRIPT = "java_script"
    _WEB_ASSEMBLY = "web_assembly"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class DebugSymbols(None):
    """Debug symbols available for a wasm script."""

    def to_json(self) -> DebugSymbols:
        return self

    @classmethod
    def from_json(cls, value: None) -> DebugSymbols:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("Debugger.breakpointResolved")
class BreakpointResolved:
    """Fired when breakpoint is resolved to an actual script and location."""

    breakpoint_id: BreakpointId
    location: Location


@dataclass
@memoize_event("Debugger.paused")
class Paused:
    """Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria."""

    call_frames: typing.List[CallFrame]
    reason: typing.Literal[
        "ambiguous",
        "assert",
        "csp_violation",
        "debug_command",
        "dom",
        "event_listener",
        "exception",
        "instrumentation",
        "oom",
        "other",
        "promise_rejection",
        "xhr",
    ]
    data: typing.Optional[typing.Any]
    hit_breakpoints: typing.Optional[typing.List[str]]
    async_stack_trace: typing.Optional[runtime.StackTrace]
    async_stack_trace_id: typing.Optional[runtime.StackTraceId]
    async_call_stack_trace_id: typing.Optional[runtime.StackTraceId]


@dataclass
@memoize_event("Debugger.resumed")
class Resumed:
    """Fired when the virtual machine resumed execution."""


@dataclass
@memoize_event("Debugger.scriptFailedToParse")
class ScriptFailedToParse:
    """Fired when virtual machine fails to parse the script."""

    script_id: runtime.ScriptId
    url: str
    start_line: int
    start_column: int
    end_line: int
    end_column: int
    execution_context_id: runtime.ExecutionContextId
    hash: str
    execution_context_aux_data: typing.Optional[typing.Any]
    source_map_url: typing.Optional[str]
    has_source_url: typing.Optional[bool]
    is_module: typing.Optional[bool]
    length: typing.Optional[int]
    stack_trace: typing.Optional[runtime.StackTrace]
    code_offset: typing.Optional[int]
    script_language: typing.Optional[ScriptLanguage]
    embedder_name: typing.Optional[str]


@dataclass
@memoize_event("Debugger.scriptParsed")
class ScriptParsed:
    """Fired when virtual machine parses script.

    This event is also fired for all known and uncollected scripts upon enabling debugger.
    """

    script_id: runtime.ScriptId
    url: str
    start_line: int
    start_column: int
    end_line: int
    end_column: int
    execution_context_id: runtime.ExecutionContextId
    hash: str
    execution_context_aux_data: typing.Optional[typing.Any]
    is_live_edit: typing.Optional[bool]
    source_map_url: typing.Optional[str]
    has_source_url: typing.Optional[bool]
    is_module: typing.Optional[bool]
    length: typing.Optional[int]
    stack_trace: typing.Optional[runtime.StackTrace]
    code_offset: typing.Optional[int]
    script_language: typing.Optional[ScriptLanguage]
    debug_symbols: typing.Optional[DebugSymbols]
    embedder_name: typing.Optional[str]


async def continue_to_location() -> None:
    """Continues execution until specific location is reached.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables debugger for given page.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables debugger for the given page.

    Clients should not assume that the debugging has been enabled until the result for this command is received. # noqa
    """
    ...


async def evaluate_on_call_frame() -> None:
    """Evaluates expression on a given call frame.

    # noqa
    """
    ...


async def get_possible_breakpoints() -> None:
    """Returns possible locations for breakpoint.

    scriptId in start and end range locations should be the same. # noqa
    """
    ...


async def get_script_source() -> None:
    """Returns source for the script with given id.

    # noqa
    """
    ...


async def disassemble_wasm_module() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def next_wasm_disassembly_chunk() -> None:
    """Disassemble the next chunk of lines for the module corresponding to the stream.

    If disassembly is complete, this API will invalidate the streamId and return an empty chunk. Any subsequent calls
    for the now invalid stream will return errors. # noqa
    """
    ...


async def get_wasm_bytecode() -> None:
    """This command is deprecated.

    Use getScriptSource instead. # noqa
    """
    ...


async def get_stack_trace() -> None:
    """Returns stack trace with given `stackTraceId`.

    # noqa
    """
    ...


async def pause() -> None:
    """Stops on the next JavaScript statement.

    # noqa
    """
    ...


async def pause_on_async_call() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def remove_breakpoint() -> None:
    """Removes JavaScript breakpoint.

    # noqa
    """
    ...


async def restart_frame() -> None:
    """Restarts particular call frame from the beginning. The old, deprecated behavior of `restartFrame` is to stay
    paused and allow further CDP commands after a restart was scheduled. This can cause problems with restarting, so we
    now continue execution immediatly after it has been scheduled until we reach the beginning of the restarted frame.

    To stay back-wards compatible, `restartFrame` now expects a `mode`
    parameter to be present. If the `mode` parameter is missing, `restartFrame`
    errors out.

    The various return values are deprecated and `callFrames` is always empty.
    Use the call frames from the `Debugger#paused` events instead, that fires
    once V8 pauses at the beginning of the restarted function. # noqa
    """
    ...


async def resume() -> None:
    """Resumes JavaScript execution.

    # noqa
    """
    ...


async def search_in_content() -> None:
    """Searches for given string in script content.

    # noqa
    """
    ...


async def set_async_call_stack_depth() -> None:
    """Enables or disables async call stacks tracking.

    # noqa
    """
    ...


async def set_blackbox_patterns() -> None:
    """Replace previous blackbox patterns with passed ones.

    Forces backend to skip stepping/pausing in scripts with url matching one of the patterns. VM will try to leave
    blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful. # noqa
    """
    ...


async def set_blackboxed_ranges() -> None:
    """Makes backend skip steps in the script in blackboxed ranges.

    VM will try leave blacklisted scripts by performing 'step in' several times, finally resorting to 'step out' if
    unsuccessful. Positions array contains positions where blackbox state is changed. First interval isn't blackboxed.
    Array should be sorted. # noqa
    """
    ...


async def set_breakpoint() -> None:
    """Sets JavaScript breakpoint at a given location.

    # noqa
    """
    ...


async def set_instrumentation_breakpoint() -> None:
    """Sets instrumentation breakpoint.

    # noqa
    """
    ...


async def set_breakpoint_by_url() -> None:
    """Sets JavaScript breakpoint at given location specified either by URL or URL regex.

    Once this command is issued, all existing parsed scripts will have breakpoints resolved and returned in `locations`
    property. Further matching script parsing will result in subsequent `breakpointResolved` events issued. This logical
    breakpoint will survive page reloads. # noqa
    """
    ...


async def set_breakpoint_on_function_call() -> None:
    """Sets JavaScript breakpoint before each call to the given function.

    If another function was created from the same source as a given one, calling it will also trigger the breakpoint. #
    noqa
    """
    ...


async def set_breakpoints_active() -> None:
    """Activates / deactivates all breakpoints on the page.

    # noqa
    """
    ...


async def set_pause_on_exceptions() -> None:
    """Defines pause on exceptions state.

    Can be set to stop on all exceptions, uncaught exceptions, or caught exceptions, no exceptions. Initial pause on
    exceptions state is `none`. # noqa
    """
    ...


async def set_return_value() -> None:
    """Changes return value in top frame.

    Available only at return break position. # noqa
    """
    ...


async def set_script_source() -> None:
    """Edits JavaScript source live.

    In general, functions that are currently on the stack can not be edited with a single exception: If the edited
    function is the top-most stack frame and that is the only activation of that function on the stack. In this case the
    live edit will be successful and a `Debugger.restartFrame` for the top-most function is automatically triggered. #
    noqa
    """
    ...


async def set_skip_all_pauses() -> None:
    """Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).

    # noqa
    """
    ...


async def set_variable_value() -> None:
    """Changes value of variable in a callframe.

    Object-based scopes are not supported and must be mutated manually. # noqa
    """
    ...


async def step_into() -> None:
    """Steps into the function call.

    # noqa
    """
    ...


async def step_out() -> None:
    """Steps out of the function call.

    # noqa
    """
    ...


async def step_over() -> None:
    """Steps over the statement.

    # noqa
    """
    ...
