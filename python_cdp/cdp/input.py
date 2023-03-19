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
import typing
from dataclasses import dataclass

from .utils import memoize_event


@dataclass
class TouchPoint:
    """Description is missing from the devtools protocol document."""

    # X coordinate of the event relative to the main frame's viewport in CSSpixels.# noqa
    x: float
    # Y coordinate of the event relative to the main frame's viewport in CSSpixels. 0 refers to the top of the viewport and Y increases as it proceedstowards the bottom of the viewport.# noqa
    y: float
    # X radius of the touch area (default: 1.0).# noqa
    radius_x: typing.Optional[float] = None
    # Y radius of the touch area (default: 1.0).# noqa
    radius_y: typing.Optional[float] = None
    # Rotation angle (default: 0.0).# noqa
    rotation_angle: typing.Optional[float] = None
    # Force (default: 1.0).# noqa
    force: typing.Optional[float] = None
    # The normalized tangential pressure, which has a range of [-1,1] (default:0).# noqa
    tangential_pressure: typing.Optional[float] = None
    # The plane angle between the Y-Z plane and the plane containing both thestylus axis and the Y axis, in degrees of the range [-90,90], a positive tiltXis to the right (default: 0)# noqa
    tilt_x: typing.Optional[int] = None
    # The plane angle between the X-Z plane and the plane containing both thestylus axis and the X axis, in degrees of the range [-90,90], a positive tiltYis towards the user (default: 0).# noqa
    tilt_y: typing.Optional[int] = None
    # The clockwise rotation of a pen stylus around its own major axis, indegrees in the range [0,359] (default: 0).# noqa
    twist: typing.Optional[int] = None
    # Identifier used to track touch sources between events, must be uniquewithin an event.# noqa
    id: typing.Optional[float] = None


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


@dataclass
class DragDataItem:
    """Description is missing from the devtools protocol document."""

    # Mime type of the dragged data.# noqa
    mime_type: str
    # Depending of the value of `mimeType`, it contains the dragged link, text,HTML markup or any other data.# noqa
    data: str
    # Title associated with a link. Only valid when `mimeType` == "text/uri-list".# noqa
    title: typing.Optional[str] = None
    # Stores the base URL for the contained markup. Only valid when `mimeType`== "text/html".# noqa
    base_url: typing.Optional[str] = None


@dataclass
class DragData:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa
    items: DragDataItem
    # Bit field representing allowed drag operations. Copy = 1, Link = 2, Move =16# noqa
    drag_operations_mask: int
    # List of filenames that should be included when dropping# noqa
    files: typing.Optional[typing.List[str]] = None


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
