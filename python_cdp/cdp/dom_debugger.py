# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `DOMDebugger`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import dom
from . import runtime


class DOMBreakpointType(str, enum.Enum):
    """DOM breakpoint type."""

    SUBTREE_MODIFIED = "subtree_modified"
    ATTRIBUTE_MODIFIED = "attribute_modified"
    NODE_REMOVED = "node_removed"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CSPViolationType(str, enum.Enum):
    """CSP Violation type."""

    TRUSTEDTYPE_SINK_VIOLATION = "trustedtype_sink_violation"
    TRUSTEDTYPE_POLICY_VIOLATION = "trustedtype_policy_violation"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class EventListener:
    """Object event listener."""

    #: `EventListener`'s type.# noqa
    type: str
    #: `EventListener`'s useCapture.# noqa
    useCapture: bool
    #: `EventListener`'s passive flag.# noqa
    passive: bool
    #: `EventListener`'s once flag.# noqa
    once: bool
    #: Script id of the handler code.# noqa
    scriptId: runtime.ScriptId
    #: Line number in the script (0-based).# noqa
    lineNumber: int
    #: Column number in the script (0-based).# noqa
    columnNumber: int
    #: Event handler function value.# noqa
    handler: typing.Optional[runtime.RemoteObject] = None
    #: Event original handler function value.# noqa
    originalHandler: typing.Optional[runtime.RemoteObject] = None
    #: Node the listener is added to (if any).# noqa
    backendNodeId: typing.Optional[dom.BackendNodeId] = None
