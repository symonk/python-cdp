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


class LayerId(str):
    """Unique Layer identifier."""

    def to_json(self) -> LayerId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SnapshotId(str):
    """Unique snapshot identifier."""

    def to_json(self) -> SnapshotId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class ScrollRect:
    """Rectangle where scrolling happens on the main thread."""

    #: Rectangle itself.# noqa
    rect: dom.Rect
    #: Reason for rectangle to force scrolling on the main thread# noqa
    type: str


@dataclass
class StickyPositionConstraint:
    """Sticky position constraints."""

    #: Layout rectangle of the sticky element before being shifted# noqa
    stickyBoxRect: dom.Rect
    #: Layout rectangle of the containing block of the sticky element# noqa
    containingBlockRect: dom.Rect
    #: The nearest sticky layer that shifts the sticky box# noqa
    nearestLayerShiftingStickyBox: typing.Optional[LayerId] = None
    #: The nearest sticky layer that shifts the containing block# noqa
    nearestLayerShiftingContainingBlock: typing.Optional[LayerId] = None


@dataclass
class PictureTile:
    """Serialized fragment of layer picture along with its offset within the
    layer."""

    #: Offset from owning layer left boundary# noqa
    x: float
    #: Offset from owning layer top boundary# noqa
    y: float
    #: Base64-encoded snapshot data. (Encoded as a base64 string when passedover JSON)# noqa
    picture: str


@dataclass
class Layer:
    """Information about a compositing layer."""

    #: The unique id for this layer.# noqa
    layerId: LayerId
    #: The id of parent (not present for root).# noqa
    parentLayerId: typing.Optional[LayerId] = None
    #: The backend id for the node associated with this layer.# noqa
    backendNodeId: typing.Optional[dom.BackendNodeId] = None
    #: Offset from parent layer, X coordinate.# noqa
    offsetX: float
    #: Offset from parent layer, Y coordinate.# noqa
    offsetY: float
    #: Layer width.# noqa
    width: float
    #: Layer height.# noqa
    height: float
    #: Transformation matrix for layer, default is identity matrix# noqa
    transform: typing.Optional[float] = None
    #: Transform anchor point X, absent if no transform specified# noqa
    anchorX: typing.Optional[float] = None
    #: Transform anchor point Y, absent if no transform specified# noqa
    anchorY: typing.Optional[float] = None
    #: Transform anchor point Z, absent if no transform specified# noqa
    anchorZ: typing.Optional[float] = None
    #: Indicates how many time this layer has painted.# noqa
    paintCount: int
    #: Indicates whether this layer hosts any content, rather than being usedfor transform/scrolling purposes only.# noqa
    drawsContent: bool
    #: Set if layer is not visible.# noqa
    invisible: typing.Optional[bool] = None
    #: Rectangles scrolling on main thread only.# noqa
    scrollRects: typing.Optional[ScrollRect] = None
    #: Sticky position constraint information# noqa
    stickyPositionConstraint: typing.Optional[StickyPositionConstraint] = None


@dataclass
class PaintProfile:
    """Array of timings, one per paint step."""
