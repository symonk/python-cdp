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


class CSPViolationType(str, enum.Enum):
    """CSP Violation type."""

    TRUSTEDTYPE_SINK_VIOLATION = "trustedtype_sink_violation"
    TRUSTEDTYPE_POLICY_VIOLATION = "trustedtype_policy_violation"


@dataclass
class EventListener:
    """Object event listener."""
