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
from dataclasses import dataclass

@dataclass
class TouchPoint:
    """ Description is missing from the devtools protocol document. """

class GestureSourceType(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
class MouseButton(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
class TimeSinceEpoch(float):
    """ UTC time in seconds, counted from January 1, 1970. """

    def to_json(self) -> float:
        return self
    
@dataclass
class DragDataItem:
    """ Description is missing from the devtools protocol document. """

@dataclass
class DragData:
    """ Description is missing from the devtools protocol document. """
