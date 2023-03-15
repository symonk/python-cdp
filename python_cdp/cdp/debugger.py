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
from dataclasses import dataclass
import typing
import enum

from . import runtime


class BreakpointId(str):
    """ Breakpoint identifier. """

    def to_json(self) -> BreakpointId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CallFrameId(str):
    """ Call frame identifier. """

    def to_json(self) -> CallFrameId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class Location:
    """ Location in the source code. """
    #: Script identifier as reported in the `Debugger.scriptParsed`.# noqa
    script_id: runtime.ScriptId
    #: Line number in the script (0-based).# noqa
    line_number: int
    #: Column number in the script (0-based).# noqa
    column_number: typing.Optional[int] = None


@dataclass
class ScriptPosition:
    """ Location in the source code. """
    #: Description is missing from the devtools protocol document.# noqa
    line_number: int
    #: Description is missing from the devtools protocol document.# noqa
    column_number: int


@dataclass
class LocationRange:
    """ Location range within one script. """
    #: Description is missing from the devtools protocol document.# noqa
    script_id: runtime.ScriptId
    #: Description is missing from the devtools protocol document.# noqa
    start: ScriptPosition
    #: Description is missing from the devtools protocol document.# noqa
    end: ScriptPosition


@dataclass
class CallFrame:
    """ JavaScript call frame. Array of call frames form the call stack. """
    #: Call frame identifier. This identifier is only valid while the virtualmachine is paused.# noqa
    call_frame_id: CallFrameId
    #: Name of the JavaScript function called on this call frame.# noqa
    function_name: str
    #: Location in the source code.# noqa
    location: Location
    #: JavaScript script name or url. Deprecated in favor of using the`location.scriptId` to resolve the URL via a previously sent`Debugger.scriptParsed` event.# noqa
    url: str
    #: Scope chain for this call frame.# noqa
    scope_chain: Scope
    #: `this` object for this call frame.# noqa
    this: runtime.RemoteObject
    #: Location in the source code.# noqa
    function_location: typing.Optional[Location] = None
    #: The value being returned, if the function is at return point.# noqa
    return_value: typing.Optional[runtime.RemoteObject] = None
    #: Valid only while the VM is paused and indicates whether this frame can berestarted or not. Note that a `true` value here does not guarantee thatDebugger#restartFrame with this CallFrameId will be successful, but it is verylikely.# noqa
    can_be_restarted: typing.Optional[bool] = None


@dataclass
class Scope:
    """ Scope description. """
    #: Scope type.# noqa
    type: str
    #: Object representing the scope. For `global` and `with` scopes itrepresents the actual object; for the rest of the scopes, it is artificialtransient object enumerating scope variables as its properties.# noqa
    object: runtime.RemoteObject
    #: Description is missing from the devtools protocol document.# noqa
    name: typing.Optional[str] = None
    #: Location in the source code where scope starts# noqa
    start_location: typing.Optional[Location] = None
    #: Location in the source code where scope ends# noqa
    end_location: typing.Optional[Location] = None


@dataclass
class SearchMatch:
    """ Search match for resource. """
    #: Line number in resource content.# noqa
    line_number: float
    #: Line with match content.# noqa
    line_content: str


@dataclass
class BreakLocation:
    """ Description is missing from the devtools protocol document. """
    #: Script identifier as reported in the `Debugger.scriptParsed`.# noqa
    script_id: runtime.ScriptId
    #: Line number in the script (0-based).# noqa
    line_number: int
    #: Column number in the script (0-based).# noqa
    column_number: typing.Optional[int] = None
    #: Description is missing from the devtools protocol document.# noqa
    type: typing.Optional[str] = None


@dataclass
class WasmDisassemblyChunk:
    """ Description is missing from the devtools protocol document. """
    #: The next chunk of disassembled lines.# noqa
    lines: str
    #: The bytecode offsets describing the start of each line.# noqa
    bytecode_offsets: int


class ScriptLanguage(str, enum.Enum):
    """ Enum of possible script languages. """

    JAVASCRIPT = "JavaScript"
    WEBASSEMBLY = "WebAssembly"


    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class DebugSymbols:
    """ Debug symbols available for a wasm script. """
    #: Type of the debug symbols.# noqa
    type: str
    #: URL of the external symbol source.# noqa
    external_url: typing.Optional[str] = None
