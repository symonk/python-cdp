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

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class CallFrameId(str):
    """Call frame identifier."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class Location:
    """Location in the source code."""

    #: Script identifier as reported in the `Debugger.scriptParsed`.
    scriptId: str
    #: Line number in the script (0-based).
    lineNumber: str
    #: Column number in the script (0-based).
    columnNumber: str


@dataclass
class ScriptPosition:
    """Location in the source code."""

    #: Description is missing from the devtools protocol document.
    lineNumber: str
    #: Description is missing from the devtools protocol document.
    columnNumber: str


@dataclass
class LocationRange:
    """Location range within one script."""

    #: Description is missing from the devtools protocol document.
    scriptId: str
    #: Description is missing from the devtools protocol document.
    start: str
    #: Description is missing from the devtools protocol document.
    end: str


@dataclass
class CallFrame:
    """JavaScript call frame.

    Array of call frames form the call stack.
    """

    #: Call frame identifier. This identifier is only valid while the virtualmachine is paused.
    callFrameId: str
    #: Name of the JavaScript function called on this call frame.
    functionName: str
    #: Location in the source code.
    functionLocation: str
    #: Location in the source code.
    location: str
    #: JavaScript script name or url. Deprecated in favor of using the`location.scriptId` to resolve the URL via a previously sent`Debugger.scriptParsed` event.
    url: str
    #: Scope chain for this call frame.
    scopeChain: str
    #: `this` object for this call frame.
    this: str
    #: The value being returned, if the function is at return point.
    returnValue: str
    #: Valid only while the VM is paused and indicates whether this frame can berestarted or not. Note that a `true` value here does not guarantee thatDebugger#restartFrame with this CallFrameId will be successful, but it is verylikely.
    canBeRestarted: str


@dataclass
class Scope:
    """Scope description."""

    #: Scope type.
    type: str
    #: Object representing the scope. For `global` and `with` scopes itrepresents the actual object; for the rest of the scopes, it is artificialtransient object enumerating scope variables as its properties.
    object: str
    #: Description is missing from the devtools protocol document.
    name: str
    #: Location in the source code where scope starts
    startLocation: str
    #: Location in the source code where scope ends
    endLocation: str


@dataclass
class SearchMatch:
    """Search match for resource."""

    #: Line number in resource content.
    lineNumber: str
    #: Line with match content.
    lineContent: str


@dataclass
class BreakLocation:
    """Description is missing from the devtools protocol document."""

    #: Script identifier as reported in the `Debugger.scriptParsed`.
    scriptId: str
    #: Line number in the script (0-based).
    lineNumber: str
    #: Column number in the script (0-based).
    columnNumber: str
    #: Description is missing from the devtools protocol document.
    type: str


@dataclass
class WasmDisassemblyChunk:
    """Description is missing from the devtools protocol document."""

    #: The next chunk of disassembled lines.
    lines: str
    #: The bytecode offsets describing the start of each line.
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

    #: Type of the debug symbols.
    type: str
    #: URL of the external symbol source.
    externalURL: str
