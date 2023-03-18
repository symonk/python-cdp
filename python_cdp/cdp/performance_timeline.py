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
    """See https://github.com/WICG/LargestContentfulPaint and
    largest_contentful_paint.idl."""

    #: Description is missing from the devtools protocol document.# noqa
    render_time: network.TimeSinceEpoch
    #: Description is missing from the devtools protocol document.# noqa
    load_time: network.TimeSinceEpoch
    #: The number of pixels being painted.# noqa
    size: float
    #: The id attribute of the element, if available.# noqa
    element_id: typing.Optional[str] = None
    #: The URL of the image (may be trimmed).# noqa
    url: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    node_id: typing.Optional[dom.BackendNodeId] = None


@dataclass
class LayoutShiftAttribution:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    previous_rect: dom.Rect
    #: Description is missing from the devtools protocol document.# noqa
    current_rect: dom.Rect
    #: Description is missing from the devtools protocol document.# noqa
    node_id: typing.Optional[dom.BackendNodeId] = None


@dataclass
class LayoutShift:
    """See https://wicg.github.io/layout-instability/#sec-layout-shift and
    layout_shift.idl."""

    #: Score increment produced by this event.# noqa
    value: float
    #: Description is missing from the devtools protocol document.# noqa
    had_recent_input: bool
    #: Description is missing from the devtools protocol document.# noqa
    last_input_time: network.TimeSinceEpoch
    #: Description is missing from the devtools protocol document.# noqa
    sources: LayoutShiftAttribution


@dataclass
class TimelineEvent:
    """Description is missing from the devtools protocol document."""

    #: Identifies the frame that this event is related to. Empty for non-frametargets.# noqa
    frame_id: page.FrameId
    #: The event type, as specified in https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype This determines which of the optional"details" fiedls is present.# noqa
    type: str
    #: Name may be empty depending on the type.# noqa
    name: str
    #: Time in seconds since Epoch, monotonically increasing within documentlifetime.# noqa
    time: network.TimeSinceEpoch
    #: Event duration, if applicable.# noqa
    duration: typing.Optional[float] = None
    #: Description is missing from the devtools protocol document.# noqa
    lcp_details: typing.Optional[LargestContentfulPaint] = None
    #: Description is missing from the devtools protocol document.# noqa
    layout_shift_details: typing.Optional[LayoutShift] = None


@memoize_event("PerformanceTimeline.timelineEventAdded")
class TimelineEventAdded:
    """Sent when a performance timeline event is added.

    See reportPerformanceTimeline method.
    """

    ...


async def enable() -> None:
    """Previously buffered events would be reported before method returns.

    See also: timelineEventAdded # noqa
    """
    ...
