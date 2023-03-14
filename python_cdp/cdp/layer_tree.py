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

from dataclasses import dataclass


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
    rect: str
    #: Reason for rectangle to force scrolling on the main thread# noqa
    type: str


@dataclass
class StickyPositionConstraint:
    """Sticky position constraints."""

    #: Layout rectangle of the sticky element before being shifted# noqa
    stickyBoxRect: str
    #: Layout rectangle of the containing block of the sticky element# noqa
    containingBlockRect: str
    #: The nearest sticky layer that shifts the sticky box# noqa
    nearestLayerShiftingStickyBox: str
    #: The nearest sticky layer that shifts the containing block# noqa
    nearestLayerShiftingContainingBlock: str


@dataclass
class PictureTile:
    """Serialized fragment of layer picture along with its offset within the
    layer."""

    #: Offset from owning layer left boundary# noqa
    x: str
    #: Offset from owning layer top boundary# noqa
    y: str
    #: Base64-encoded snapshot data. (Encoded as a base64 string when passedover JSON)# noqa
    picture: str


@dataclass
class Layer:
    """Information about a compositing layer."""

    #: The unique id for this layer.# noqa
    layerId: str
    #: The id of parent (not present for root).# noqa
    parentLayerId: str
    #: The backend id for the node associated with this layer.# noqa
    backendNodeId: str
    #: Offset from parent layer, X coordinate.# noqa
    offsetX: str
    #: Offset from parent layer, Y coordinate.# noqa
    offsetY: str
    #: Layer width.# noqa
    width: str
    #: Layer height.# noqa
    height: str
    #: Transformation matrix for layer, default is identity matrix# noqa
    transform: str
    #: Transform anchor point X, absent if no transform specified# noqa
    anchorX: str
    #: Transform anchor point Y, absent if no transform specified# noqa
    anchorY: str
    #: Transform anchor point Z, absent if no transform specified# noqa
    anchorZ: str
    #: Indicates how many time this layer has painted.# noqa
    paintCount: str
    #: Indicates whether this layer hosts any content, rather than being usedfor transform/scrolling purposes only.# noqa
    drawsContent: str
    #: Set if layer is not visible.# noqa
    invisible: str
    #: Rectangles scrolling on main thread only.# noqa
    scrollRects: str
    #: Sticky position constraint information# noqa
    stickyPositionConstraint: str


@dataclass
class PaintProfile:
    """Array of timings, one per paint step."""
