# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `PerformanceTimeline`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/PerformanceTimeline/

from __future__ import annotations

import typing
from dataclasses import dataclass

from . import dom
from . import network
from . import page
from .utils import memoize_event


@dataclass
class LargestContentfulPaint:
    """See https://github.com/WICG/LargestContentfulPaint and largest_contentful_paint.idl."""

    # Description is missing from the devtools protocol document.# noqa


network.TimeSinceEpoch
# Description is missing from the devtools protocol document.# noqa
network.TimeSinceEpoch
# The number of pixels being painted.# noqa
float
# The id attribute of the element, if available.# noqa
typing.Optional[str]
# The URL of the image (may be trimmed).# noqa
typing.Optional[str]
# Description is missing from the devtools protocol document.# noqa
typing.Optional[dom.BackendNodeId]


@dataclass
class LayoutShiftAttribution:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa


dom.Rect
# Description is missing from the devtools protocol document.# noqa
dom.Rect
# Description is missing from the devtools protocol document.# noqa
typing.Optional[dom.BackendNodeId]


@dataclass
class LayoutShift:
    """See https://wicg.github.io/layout-instability/#sec-layout-shift and layout_shift.idl."""

    # Score increment produced by this event.# noqa


float
# Description is missing from the devtools protocol document.# noqa
bool
# Description is missing from the devtools protocol document.# noqa
network.TimeSinceEpoch
# Description is missing from the devtools protocol document.# noqa
typing.List[LayoutShiftAttribution]


@dataclass
class TimelineEvent:
    """Description is missing from the devtools protocol document."""

    # Identifies the frame that this event is related to. Empty for non-frametargets.# noqa


page.FrameId
# The event type, as specified in https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype This determines which of the optional"details" fiedls is present.# noqa
str
# Name may be empty depending on the type.# noqa
str
# Time in seconds since Epoch, monotonically increasing within documentlifetime.# noqa
network.TimeSinceEpoch
# Event duration, if applicable.# noqa
typing.Optional[float]
# Description is missing from the devtools protocol document.# noqa
LargestContentfulPaint
# Description is missing from the devtools protocol document.# noqa
LayoutShift


@dataclass
@memoize_event("PerformanceTimeline.timelineEventAdded")
class TimelineEventAdded:
    """Sent when a performance timeline event is added.

    See reportPerformanceTimeline method.
    """

    event: TimelineEvent


async def enable() -> None:
    """Previously buffered events would be reported before method returns.

    See also: timelineEventAdded # noqa
    """
    ...
