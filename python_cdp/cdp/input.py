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


@dataclass
class TouchPoint:
    """Description is missing from the devtools protocol document."""

    #: X coordinate of the event relative to the main frame's viewport in CSSpixels.
    x: str
    #: Y coordinate of the event relative to the main frame's viewport in CSSpixels. 0 refers to the top of the viewport and Y increases as it proceedstowards the bottom of the viewport.
    y: str
    #: X radius of the touch area (default: 1.0).
    radiusX: str
    #: Y radius of the touch area (default: 1.0).
    radiusY: str
    #: Rotation angle (default: 0.0).
    rotationAngle: str
    #: Force (default: 1.0).
    force: str
    #: The normalized tangential pressure, which has a range of [-1,1] (default:0).
    tangentialPressure: str
    #: The plane angle between the Y-Z plane and the plane containing both thestylus axis and the Y axis, in degrees of the range [-90,90], a positive tiltXis to the right (default: 0)
    tiltX: str
    #: The plane angle between the X-Z plane and the plane containing both thestylus axis and the X axis, in degrees of the range [-90,90], a positive tiltYis towards the user (default: 0).
    tiltY: str
    #: The clockwise rotation of a pen stylus around its own major axis, indegrees in the range [0,359] (default: 0).
    twist: str
    #: Identifier used to track touch sources between events, must be uniquewithin an event.
    id: str


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

    def to_json(self) -> float:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class DragDataItem:
    """Description is missing from the devtools protocol document."""

    #: Mime type of the dragged data.
    mimeType: str
    #: Depending of the value of `mimeType`, it contains the dragged link, text,HTML markup or any other data.
    data: str
    #: Title associated with a link. Only valid when `mimeType` == "text/uri-list".
    title: str
    #: Stores the base URL for the contained markup. Only valid when `mimeType`== "text/html".
    baseURL: str


@dataclass
class DragData:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.
    items: str
    #: List of filenames that should be included when dropping
    files: str
    #: Bit field representing allowed drag operations. Copy = 1, Link = 2, Move= 16
    dragOperationsMask: str
