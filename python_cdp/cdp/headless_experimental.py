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

from dataclasses import dataclass


@dataclass
class ScreenshotParams:
    """Encoding options for a screenshot."""

    #: Image compression format (defaults to png).# noqa
    format: str
    #: Compression quality from range [0..100] (jpeg only).# noqa
    quality: str
    #: Optimize image encoding for speed, not for resulting size (defaults tofalse)# noqa
    optimizeForSpeed: str
