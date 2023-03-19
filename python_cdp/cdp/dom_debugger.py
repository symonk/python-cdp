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


class EventListener(None):
    """Object event listener."""

    def to_json(self) -> EventListener:
        return self

    @classmethod
    def from_json(cls, value: None) -> EventListener:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
