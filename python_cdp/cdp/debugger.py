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
from dataclasses import dataclass


class BreakpointId(str):
    """Breakpoint identifier."""

    def to_json(self) -> BreakpointId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CallFrameId(str):
    """Call frame identifier."""

    def to_json(self) -> CallFrameId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class Location:
    """Location in the source code."""

    #: Script identifier as reported in the `Debugger.scriptParsed`.# noqa
    scriptId: str
    #: Line number in the script (0-based).# noqa
    lineNumber: str
    #: Column number in the script (0-based).# noqa
    columnNumber: str


@dataclass
class ScriptPosition:
    """Location in the source code."""

    #: Description is missing from the devtools protocol document.# noqa
    lineNumber: str
    #: Description is missing from the devtools protocol document.# noqa
    columnNumber: str


@dataclass
class LocationRange:
    """Location range within one script."""

    #: Description is missing from the devtools protocol document.# noqa
    scriptId: str
    #: Description is missing from the devtools protocol document.# noqa
    start: str
    #: Description is missing from the devtools protocol document.# noqa
    end: str


@dataclass
class CallFrame:
    """JavaScript call frame.

    Array of call frames form the call stack.
    """

    #: Call frame identifier. This identifier is only valid while the virtualmachine is paused.# noqa
    callFrameId: str
    #: Name of the JavaScript function called on this call frame.# noqa
    functionName: str
    #: Location in the source code.# noqa
    functionLocation: str
    #: Location in the source code.# noqa
    location: str
    #: JavaScript script name or url. Deprecated in favor of using the`location.scriptId` to resolve the URL via a previously sent`Debugger.scriptParsed` event.# noqa
    url: str
    #: Scope chain for this call frame.# noqa
    scopeChain: str
    #: `this` object for this call frame.# noqa
    this: str
    #: The value being returned, if the function is at return point.# noqa
    returnValue: str
    #: Valid only while the VM is paused and indicates whether this frame can berestarted or not. Note that a `true` value here does not guarantee thatDebugger#restartFrame with this CallFrameId will be successful, but it is verylikely.# noqa
    canBeRestarted: str


@dataclass
class Scope:
    """Scope description."""

    #: Scope type.# noqa
    type: str
    #: Object representing the scope. For `global` and `with` scopes itrepresents the actual object; for the rest of the scopes, it is artificialtransient object enumerating scope variables as its properties.# noqa
    object: str
    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Location in the source code where scope starts# noqa
    startLocation: str
    #: Location in the source code where scope ends# noqa
    endLocation: str


@dataclass
class SearchMatch:
    """Search match for resource."""

    #: Line number in resource content.# noqa
    lineNumber: str
    #: Line with match content.# noqa
    lineContent: str


@dataclass
class BreakLocation:
    """Description is missing from the devtools protocol document."""

    #: Script identifier as reported in the `Debugger.scriptParsed`.# noqa
    scriptId: str
    #: Line number in the script (0-based).# noqa
    lineNumber: str
    #: Column number in the script (0-based).# noqa
    columnNumber: str
    #: Description is missing from the devtools protocol document.# noqa
    type: str


@dataclass
class WasmDisassemblyChunk:
    """Description is missing from the devtools protocol document."""

    #: The next chunk of disassembled lines.# noqa
    lines: str
    #: The bytecode offsets describing the start of each line.# noqa
    bytecodeOffsets: str


class ScriptLanguage(str, enum.Enum):
    """Enum of possible script languages."""

    JAVASCRIPT = "JavaScript"
    WEBASSEMBLY = "WebAssembly"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class DebugSymbols:
    """Debug symbols available for a wasm script."""

    #: Type of the debug symbols.# noqa
    type: str
    #: URL of the external symbol source.# noqa
    externalURL: str
