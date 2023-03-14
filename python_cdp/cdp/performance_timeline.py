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

from dataclasses import dataclass


@dataclass
class LargestContentfulPaint:
    """See https://github.com/WICG/LargestContentfulPaint and
    largest_contentful_paint.idl."""

    #: Description is missing from the devtools protocol document.# noqa
    renderTime: str
    #: Description is missing from the devtools protocol document.# noqa
    loadTime: str
    #: The number of pixels being painted.# noqa
    size: str
    #: The id attribute of the element, if available.# noqa
    elementId: str
    #: The URL of the image (may be trimmed).# noqa
    url: str
    #: Description is missing from the devtools protocol document.# noqa
    nodeId: str


@dataclass
class LayoutShiftAttribution:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    previousRect: str
    #: Description is missing from the devtools protocol document.# noqa
    currentRect: str
    #: Description is missing from the devtools protocol document.# noqa
    nodeId: str


@dataclass
class LayoutShift:
    """See https://wicg.github.io/layout-instability/#sec-layout-shift and
    layout_shift.idl."""

    #: Score increment produced by this event.# noqa
    value: str
    #: Description is missing from the devtools protocol document.# noqa
    hadRecentInput: str
    #: Description is missing from the devtools protocol document.# noqa
    lastInputTime: str
    #: Description is missing from the devtools protocol document.# noqa
    sources: str


@dataclass
class TimelineEvent:
    """Description is missing from the devtools protocol document."""

    #: Identifies the frame that this event is related to. Empty for non-frametargets.# noqa
    frameId: str
    #: The event type, as specified in https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype This determines which of the optional"details" fiedls is present.# noqa
    type: str
    #: Name may be empty depending on the type.# noqa
    name: str
    #: Time in seconds since Epoch, monotonically increasing within documentlifetime.# noqa
    time: str
    #: Event duration, if applicable.# noqa
    duration: str
    #: Description is missing from the devtools protocol document.# noqa
    lcpDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    layoutShiftDetails: str
