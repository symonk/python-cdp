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

    SUBTREE_MODIFIED = "subtree-modified"
    ATTRIBUTE_MODIFIED = "attribute-modified"
    NODE_REMOVED = "node-removed"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CSPViolationType(str, enum.Enum):
    """CSP Violation type."""

    TRUSTEDTYPE_SINK_VIOLATION = "trustedtype-sink-violation"
    TRUSTEDTYPE_POLICY_VIOLATION = "trustedtype-policy-violation"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class EventListener:
    """Object event listener."""

    # `EventListener`'s type.# noqa
    type: str
    # `EventListener`'s useCapture.# noqa
    use_capture: bool
    # `EventListener`'s passive flag.# noqa
    passive: bool
    # `EventListener`'s once flag.# noqa
    once: bool
    # Script id of the handler code.# noqa
    script_id: runtime.ScriptId
    # Line number in the script (0-based).# noqa
    line_number: int
    # Column number in the script (0-based).# noqa
    column_number: int
    # Event handler function value.# noqa
    handler: typing.Optional[runtime.RemoteObject] = None
    # Event original handler function value.# noqa
    original_handler: typing.Optional[runtime.RemoteObject] = None
    # Node the listener is added to (if any).# noqa
    backend_node_id: typing.Optional[dom.BackendNodeId] = None


async def get_event_listeners() -> None:
    """Returns event listeners of the given object.

    # noqa
    """
    ...


async def remove_dom_breakpoint() -> None:
    """Removes DOM breakpoint that was set using `setDOMBreakpoint`.

    # noqa
    """
    ...


async def remove_event_listener_breakpoint() -> None:
    """Removes breakpoint on particular DOM event.

    # noqa
    """
    ...


async def remove_instrumentation_breakpoint() -> None:
    """Removes breakpoint on particular native event.

    # noqa
    """
    ...


async def remove_xhr_breakpoint() -> None:
    """Removes breakpoint from XMLHttpRequest.

    # noqa
    """
    ...


async def set_break_on_csp_violation() -> None:
    """Sets breakpoint on particular CSP violations.

    # noqa
    """
    ...


async def set_dom_breakpoint() -> None:
    """Sets breakpoint on particular operation with DOM.

    # noqa
    """
    ...


async def set_event_listener_breakpoint() -> None:
    """Sets breakpoint on particular DOM event.

    # noqa
    """
    ...


async def set_instrumentation_breakpoint() -> None:
    """Sets breakpoint on particular native event.

    # noqa
    """
    ...


async def set_xhr_breakpoint() -> None:
    """Sets breakpoint on XMLHttpRequest.

    # noqa
    """
    ...
