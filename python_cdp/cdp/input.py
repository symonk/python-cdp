# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Input`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Input/

from __future__ import annotations

import enum
from dataclasses import dataclass

from .utils import memoize_event


class TouchPoint(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> TouchPoint:
        return self

    @classmethod
    def from_json(cls, value: None) -> TouchPoint:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class GestureSourceType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    DEFAULT = "default"
    TOUCH = "touch"
    MOUSE = "mouse"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class MouseButton(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    NONE = "none"
    LEFT = "left"
    MIDDLE = "middle"
    RIGHT = "right"
    BACK = "back"
    FORWARD = "forward"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class TimeSinceEpoch(float):
    """UTC time in seconds, counted from January 1, 1970."""

    def to_json(self) -> TimeSinceEpoch:
        return self

    @classmethod
    def from_json(cls, value: float) -> TimeSinceEpoch:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class DragDataItem(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> DragDataItem:
        return self

    @classmethod
    def from_json(cls, value: None) -> DragDataItem:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class DragData(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> DragData:
        return self

    @classmethod
    def from_json(cls, value: None) -> DragData:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("Input.dragIntercepted")
class DragIntercepted:
    """Emitted only when `Input.setInterceptDrags` is enabled.

    Use this data with `Input.dispatchDragEvent` to restore normal drag and drop behavior.
    """

    data: DragData


async def dispatch_drag_event() -> None:
    """Dispatches a drag event into the page.

    # noqa
    """
    ...


async def dispatch_key_event() -> None:
    """Dispatches a key event to the page.

    # noqa
    """
    ...


async def insert_text() -> None:
    """This method emulates inserting text that doesn't come from a key press, for example an emoji keyboard or an IME.

    # noqa
    """
    ...


async def ime_set_composition() -> None:
    """This method sets the current candidate text for ime.

    Use imeCommitComposition to commit the final text. Use imeSetComposition with empty string as text to cancel
    composition. # noqa
    """
    ...


async def dispatch_mouse_event() -> None:
    """Dispatches a mouse event to the page.

    # noqa
    """
    ...


async def dispatch_touch_event() -> None:
    """Dispatches a touch event to the page.

    # noqa
    """
    ...


async def emulate_touch_from_mouse_event() -> None:
    """Emulates touch event from the mouse event parameters.

    # noqa
    """
    ...


async def set_ignore_input_events() -> None:
    """Ignores input events (useful while auditing page).

    # noqa
    """
    ...


async def set_intercept_drags() -> None:
    """Prevents default drag and drop behavior and instead emits `Input.dragIntercepted` events.

    Drag and drop behavior can be directly controlled via `Input.dispatchDragEvent`. # noqa
    """
    ...


async def synthesize_pinch_gesture() -> None:
    """Synthesizes a pinch gesture over a time period by issuing appropriate touch events.

    # noqa
    """
    ...


async def synthesize_scroll_gesture() -> None:
    """Synthesizes a scroll gesture over a time period by issuing appropriate touch events.

    # noqa
    """
    ...


async def synthesize_tap_gesture() -> None:
    """Synthesizes a tap gesture over a time period by issuing appropriate touch events.

    # noqa
    """
    ...
