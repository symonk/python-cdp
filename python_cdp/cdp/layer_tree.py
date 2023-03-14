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
    """ Unique Layer identifier. """

    def to_json(self) -> str:
        return self
    
class SnapshotId(str):
    """ Unique snapshot identifier. """

    def to_json(self) -> str:
        return self
    
@dataclass
class ScrollRect:
    """ Rectangle where scrolling happens on the main thread. """
    ...

@dataclass
class StickyPositionConstraint:
    """ Sticky position constraints. """
    ...

@dataclass
class PictureTile:
    """ Serialized fragment of layer picture along with its offset within the layer. """
    ...

@dataclass
class Layer:
    """ Information about a compositing layer. """
    ...

@dataclass
class PaintProfile:
    """ Array of timings, one per paint step. """
    ...
