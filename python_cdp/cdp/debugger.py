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


class BreakpointId(str):
    """Breakpoint identifier."""

    def to_json(self) -> str:
        return self


class CallFrameId(str):
    """Call frame identifier."""

    def to_json(self) -> str:
        return self


@dataclass
class Location:
    """Location in the source code."""

    ...


@dataclass
class ScriptPosition:
    """Location in the source code."""

    ...


@dataclass
class LocationRange:
    """Location range within one script."""

    ...


@dataclass
class CallFrame:
    """JavaScript call frame.

    Array of call frames form the call stack.
    """

    ...


@dataclass
class Scope:
    """Scope description."""

    ...


@dataclass
class SearchMatch:
    """Search match for resource."""

    ...


@dataclass
class BreakLocation:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class WasmDisassemblyChunk:
    """Description is missing from the devtools protocol document."""

    ...


class ScriptLanguage(str):
    """Enum of possible script languages."""

    def to_json(self) -> str:
        return self


@dataclass
class DebugSymbols:
    """Debug symbols available for a wasm script."""

    ...
