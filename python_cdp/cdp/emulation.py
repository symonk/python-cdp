# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Emulation`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Emulation/

from __future__ import annotations

import enum
from dataclasses import dataclass


@dataclass
class ScreenOrientation:
    """Screen orientation."""

    #: Orientation type.
    type: str
    #: Orientation angle.
    angle: str


@dataclass
class DisplayFeature:
    """Description is missing from the devtools protocol document."""

    #: Orientation of a display feature in relation to screen
    orientation: str
    #: The offset from the screen origin in either the x (for verticalorientation) or y (for horizontal orientation) direction.
    offset: str
    #: A display feature may mask content such that it is not physicallydisplayed - this length along with the offset describes this area. A displayfeature that only splits content will have a 0 mask_length.
    maskLength: str


@dataclass
class MediaFeature:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.
    name: str
    #: Description is missing from the devtools protocol document.
    value: str


class VirtualTimePolicy(str, enum.Enum):
    """advance: If the scheduler runs out of immediate work, the virtual timebase may fast forward to allow the next delayed task (if any) to run; pause: Thevirtual time base may not advance; pauseIfNetworkFetchesPending: The virtualtime base may not advance if there are any pending resource fetches."""

    ADVANCE = "advance"
    PAUSE = "pause"
    PAUSEIFNETWORKFETCHESPENDING = "pauseIfNetworkFetchesPending"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class UserAgentBrandVersion:
    """Used to specify User Agent Cient Hints to emulate.

    See https://wicg.github.io/ua-client-hints
    """

    #: Description is missing from the devtools protocol document.
    brand: str
    #: Description is missing from the devtools protocol document.
    version: str


@dataclass
class UserAgentMetadata:
    """Used to specify User Agent Cient Hints to emulate.

    See https://wicg.github.io/ua-client-hints
    Missing optional values will be filled in by the target with what it would normally use.
    """

    #: Brands appearing in Sec-CH-UA.
    brands: str
    #: Brands appearing in Sec-CH-UA-Full-Version-List.
    fullVersionList: str
    #: Description is missing from the devtools protocol document.
    fullVersion: str
    #: Description is missing from the devtools protocol document.
    platform: str
    #: Description is missing from the devtools protocol document.
    platformVersion: str
    #: Description is missing from the devtools protocol document.
    architecture: str
    #: Description is missing from the devtools protocol document.
    model: str
    #: Description is missing from the devtools protocol document.
    mobile: str
    #: Description is missing from the devtools protocol document.
    bitness: str
    #: Description is missing from the devtools protocol document.
    wow64: str


class DisabledImageType(str, enum.Enum):
    """Enum of image types that can be disabled."""

    AVIF = "avif"
    WEBP = "webp"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)
