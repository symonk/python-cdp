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

from dataclasses import dataclass

from . import runtime


class HeapSnapshotObjectId(str):
    """Heap snapshot object id."""

    def to_json(self) -> HeapSnapshotObjectId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class SamplingHeapProfileNode:
    """Sampling Heap Profile node.

    Holds callsite information, allocation statistics and child nodes.
    """

    #: Function location.# noqa
    call_frame: runtime.CallFrame
    #: Allocations size in bytes for the node excluding children.# noqa
    self_size: float
    #: Node id. Ids are unique across all profiles collected betweenstartSampling and stopSampling.# noqa
    id: int
    #: Child nodes.# noqa
    children: SamplingHeapProfileNode


@dataclass
class SamplingHeapProfileSample:
    """A single sample from a sampling profile."""

    #: Allocation size in bytes attributed to the sample.# noqa
    size: float
    #: Id of the corresponding profile tree node.# noqa
    node_id: int
    #: Time-ordered sample ordinal number. It is unique across all profilesretrieved between startSampling and stopSampling.# noqa
    ordinal: float


@dataclass
class SamplingHeapProfile:
    """Sampling profile."""

    #: Description is missing from the devtools protocol document.# noqa
    head: SamplingHeapProfileNode
    #: Description is missing from the devtools protocol document.# noqa
    samples: SamplingHeapProfileSample
