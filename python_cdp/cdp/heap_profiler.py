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


class HeapSnapshotObjectId(str):
    """Heap snapshot object id."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class SamplingHeapProfileNode:
    """Sampling Heap Profile node.

    Holds callsite information, allocation statistics and child nodes.
    """


@dataclass
class SamplingHeapProfileSample:
    """A single sample from a sampling profile."""


@dataclass
class SamplingHeapProfile:
    """Sampling profile."""
