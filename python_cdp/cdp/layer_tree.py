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


class ScrollRect(None):
    """Rectangle where scrolling happens on the main thread."""

    def to_json(self) -> ScrollRect:
        return self

    @classmethod
    def from_json(cls, value: None) -> ScrollRect:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class StickyPositionConstraint(None):
    """Sticky position constraints."""

    def to_json(self) -> StickyPositionConstraint:
        return self

    @classmethod
    def from_json(cls, value: None) -> StickyPositionConstraint:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class PictureTile(None):
    """Serialized fragment of layer picture along with its offset within the layer."""

    def to_json(self) -> PictureTile:
        return self

    @classmethod
    def from_json(cls, value: None) -> PictureTile:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Layer(None):
    """Information about a compositing layer."""

    def to_json(self) -> Layer:
        return self

    @classmethod
    def from_json(cls, value: None) -> Layer:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
