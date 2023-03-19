# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `HeapProfiler`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler/

from __future__ import annotations

import typing
from dataclasses import dataclass

from .utils import memoize_event


class HeapSnapshotObjectId(str):
    """Heap snapshot object id."""

    def to_json(self) -> HeapSnapshotObjectId:
        return self

    @classmethod
    def from_json(cls, value: str) -> HeapSnapshotObjectId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SamplingHeapProfileNode(None):
    """Sampling Heap Profile node.

    Holds callsite information, allocation statistics and child nodes.
    """

    def to_json(self) -> SamplingHeapProfileNode:
        return self

    @classmethod
    def from_json(cls, value: None) -> SamplingHeapProfileNode:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SamplingHeapProfileSample(None):
    """A single sample from a sampling profile."""

    def to_json(self) -> SamplingHeapProfileSample:
        return self

    @classmethod
    def from_json(cls, value: None) -> SamplingHeapProfileSample:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SamplingHeapProfile(None):
    """Sampling profile."""

    def to_json(self) -> SamplingHeapProfile:
        return self

    @classmethod
    def from_json(cls, value: None) -> SamplingHeapProfile:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("HeapProfiler.addHeapSnapshotChunk")
class AddHeapSnapshotChunk:
    """Description is missing from the devtools protocol document."""

    chunk: str


@dataclass
@memoize_event("HeapProfiler.heapStatsUpdate")
class HeapStatsUpdate:
    """If heap objects tracking has been started then backend may send update for one or more fragments."""

    stats_update: typing.List[int]


@dataclass
@memoize_event("HeapProfiler.lastSeenObjectId")
class LastSeenObjectId:
    """If heap objects tracking has been started then backend regularly sends a current value for last seen object id
    and corresponding timestamp.

    If the were changes in the heap since last event then one or more heapStatsUpdate events will be sent before a new
    lastSeenObjectId event.
    """

    last_seen_object_id: int
    timestamp: float


@dataclass
@memoize_event("HeapProfiler.reportHeapSnapshotProgress")
class ReportHeapSnapshotProgress:
    """Description is missing from the devtools protocol document."""

    done: int
    total: int
    finished: typing.Optional[bool]


@dataclass
@memoize_event("HeapProfiler.resetProfiles")
class ResetProfiles:
    """Description is missing from the devtools protocol document."""


async def add_inspected_heap_object() -> None:
    """Enables console to refer to the node with given id via $x (see Command Line API for more details.

    $x functions). # noqa
    """
    ...


async def collect_garbage() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def disable() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def enable() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def get_heap_object_id() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def get_object_by_heap_object_id() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def get_sampling_profile() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def start_sampling() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def start_tracking_heap_objects() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def stop_sampling() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def stop_tracking_heap_objects() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def take_heap_snapshot() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...
