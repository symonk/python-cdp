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
from dataclasses import dataclass


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

    #: `EventListener`'s type.
    type: str
    #: `EventListener`'s useCapture.
    useCapture: str
    #: `EventListener`'s passive flag.
    passive: str
    #: `EventListener`'s once flag.
    once: str
    #: Script id of the handler code.
    scriptId: str
    #: Line number in the script (0-based).
    lineNumber: str
    #: Column number in the script (0-based).
    columnNumber: str
    #: Event handler function value.
    handler: str
    #: Event original handler function value.
    originalHandler: str
    #: Node the listener is added to (if any).
    backendNodeId: str
