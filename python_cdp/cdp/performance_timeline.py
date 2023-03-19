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

from .utils import memoize_event


class LargestContentfulPaint(None):
    """See https://github.com/WICG/LargestContentfulPaint and largest_contentful_paint.idl."""

    def to_json(self) -> LargestContentfulPaint:
        return self

    @classmethod
    def from_json(cls, value: None) -> LargestContentfulPaint:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class LayoutShiftAttribution(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> LayoutShiftAttribution:
        return self

    @classmethod
    def from_json(cls, value: None) -> LayoutShiftAttribution:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class LayoutShift(None):
    """See https://wicg.github.io/layout-instability/#sec-layout-shift and layout_shift.idl."""

    def to_json(self) -> LayoutShift:
        return self

    @classmethod
    def from_json(cls, value: None) -> LayoutShift:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class TimelineEvent(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> TimelineEvent:
        return self

    @classmethod
    def from_json(cls, value: None) -> TimelineEvent:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
