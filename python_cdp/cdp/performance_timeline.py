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

    #: Description is missing from the devtools protocol document.
    renderTime: str
    #: Description is missing from the devtools protocol document.
    loadTime: str
    #: The number of pixels being painted.
    size: str
    #: The id attribute of the element, if available.
    elementId: str
    #: The URL of the image (may be trimmed).
    url: str
    #: Description is missing from the devtools protocol document.
    nodeId: str


@dataclass
class LayoutShiftAttribution:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.
    previousRect: str
    #: Description is missing from the devtools protocol document.
    currentRect: str
    #: Description is missing from the devtools protocol document.
    nodeId: str


@dataclass
class LayoutShift:
    """See https://wicg.github.io/layout-instability/#sec-layout-shift and
    layout_shift.idl."""

    #: Score increment produced by this event.
    value: str
    #: Description is missing from the devtools protocol document.
    hadRecentInput: str
    #: Description is missing from the devtools protocol document.
    lastInputTime: str
    #: Description is missing from the devtools protocol document.
    sources: str


@dataclass
class TimelineEvent:
    """Description is missing from the devtools protocol document."""

    #: Identifies the frame that this event is related to. Empty for non-frametargets.
    frameId: str
    #: The event type, as specified in https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype This determines which of the optional"details" fiedls is present.
    type: str
    #: Name may be empty depending on the type.
    name: str
    #: Time in seconds since Epoch, monotonically increasing within documentlifetime.
    time: str
    #: Event duration, if applicable.
    duration: str
    #: Description is missing from the devtools protocol document.
    lcpDetails: str
    #: Description is missing from the devtools protocol document.
    layoutShiftDetails: str
