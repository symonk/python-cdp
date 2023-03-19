# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `HeadlessExperimental`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/HeadlessExperimental/

from __future__ import annotations


class ScreenshotParams(None):
    """Encoding options for a screenshot."""

    def to_json(self) -> ScreenshotParams:
        return self

    @classmethod
    def from_json(cls, value: None) -> ScreenshotParams:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


async def begin_frame() -> None:
    """Sends a BeginFrame to the target and returns when the frame was completed.

    Optionally captures a screenshot from the resulting frame. Requires that the target was created with enabled
    BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also
    https://goo.gle/chrome-headless-rendering
    for more background. # noqa
    """
    ...


async def disable() -> None:
    """Disables headless events for the target.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables headless events for the target.

    # noqa
    """
    ...
