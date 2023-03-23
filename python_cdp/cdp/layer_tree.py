# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `LayerTree`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/LayerTree/

from __future__ import annotations

import typing
from dataclasses import dataclass

from . import dom
from .utils import memoize_event


class LayerId(str):
    """Unique Layer identifier."""

    def to_json(self) -> LayerId:
        return self

    @classmethod
    def from_json(cls, value: str) -> LayerId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SnapshotId(str):
    """Unique snapshot identifier."""

    def to_json(self) -> SnapshotId:
        return self

    @classmethod
    def from_json(cls, value: str) -> SnapshotId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class ScrollRect:
    """Rectangle where scrolling happens on the main thread."""

    # Rectangle itself. # noqa
    rect: dom.Rect
    # Reason for rectangle to force scrolling on the main thread # noqa
    type: typing.List[typing.Literal["RepaintsOnScroll", "TouchEventHandler", "WheelEventHandler"]]


@dataclass
class StickyPositionConstraint:
    """Sticky position constraints."""

    # Layout rectangle of the sticky element before being shifted # noqa
    sticky_box_rect: dom.Rect
    # Layout rectangle of the containing block of the sticky element # noqa
    containing_block_rect: dom.Rect
    # The nearest sticky layer that shifts the sticky box # noqa
    nearest_layer_shifting_sticky_box: typing.Optional[LayerId]
    # The nearest sticky layer that shifts the containing block # noqa
    nearest_layer_shifting_containing_block: typing.Optional[LayerId]


@dataclass
class PictureTile:
    """Serialized fragment of layer picture along with its offset within the layer."""

    # Offset from owning layer left boundary # noqa
    x: float
    # Offset from owning layer top boundary # noqa
    y: float
    # Base64-encoded snapshot data. (Encoded as a base64 string when passed overJSON) # noqa
    picture: str


@dataclass
class Layer:
    """Information about a compositing layer."""

    # The unique id for this layer. # noqa
    layer_id: LayerId
    # Offset from parent layer, X coordinate. # noqa
    offset_x: float
    # Offset from parent layer, Y coordinate. # noqa
    offset_y: float
    # Layer width. # noqa
    width: float
    # Layer height. # noqa
    height: float
    # Indicates how many time this layer has painted. # noqa
    paint_count: int
    # Indicates whether this layer hosts any content, rather than being used fortransform/scrolling purposes only. # noqa
    draws_content: bool
    # The id of parent (not present for root). # noqa
    parent_layer_id: typing.Optional[LayerId]
    # The backend id for the node associated with this layer. # noqa
    backend_node_id: typing.Optional[dom.BackendNodeId]
    # Transformation matrix for layer, default is identity matrix # noqa
    transform: typing.Optional[float]
    # Transform anchor point X, absent if no transform specified # noqa
    anchor_x: typing.Optional[float]
    # Transform anchor point Y, absent if no transform specified # noqa
    anchor_y: typing.Optional[float]
    # Transform anchor point Z, absent if no transform specified # noqa
    anchor_z: typing.Optional[float]
    # Set if layer is not visible. # noqa
    invisible: typing.Optional[bool]
    # Rectangles scrolling on main thread only. # noqa
    scroll_rects: typing.Optional[ScrollRect]
    # Sticky position constraint information # noqa
    sticky_position_constraint: typing.Optional[StickyPositionConstraint]


@dataclass
class PaintProfile:
    """Array of timings, one per paint step."""


@dataclass
@memoize_event("LayerTree.layerPainted")
class LayerPainted:
    """Description is missing from the devtools protocol document."""

    layer_id: LayerId
    clip: dom.Rect


@dataclass
@memoize_event("LayerTree.layerTreeDidChange")
class LayerTreeDidChange:
    """Description is missing from the devtools protocol document."""

    layers: typing.Optional[typing.List[Layer]]


async def compositing_reasons() -> None:
    """Provides the reasons why the given layer was composited.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables compositing tree inspection.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables compositing tree inspection.

    # noqa
    """
    ...


async def load_snapshot() -> None:
    """Returns the snapshot identifier.

    # noqa
    """
    ...


async def make_snapshot() -> None:
    """Returns the layer snapshot identifier.

    # noqa
    """
    ...


async def profile_snapshot() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def release_snapshot() -> None:
    """Releases layer snapshot captured by the back-end.

    # noqa
    """
    ...


async def replay_snapshot() -> None:
    """Replays the layer snapshot and returns the resulting bitmap.

    # noqa
    """
    ...


async def snapshot_command_log() -> None:
    """Replays the layer snapshot and returns canvas log.

    # noqa
    """
    ...
