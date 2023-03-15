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
from dataclasses import dataclass
import typing
import enum

from . import dom
from . import page
from . import runtime


@dataclass
class ScreenOrientation:
    """ Screen orientation. """
    #: Orientation type.# noqa
    type: str
    #: Orientation angle.# noqa
    angle: int


@dataclass
class DisplayFeature:
    """ Description is missing from the devtools protocol document. """
    #: Orientation of a display feature in relation to screen# noqa
    orientation: str
    #: The offset from the screen origin in either the x (for verticalorientation) or y (for horizontal orientation) direction.# noqa
    offset: int
    #: A display feature may mask content such that it is not physicallydisplayed - this length along with the offset describes this area. A displayfeature that only splits content will have a 0 mask_length.# noqa
    mask_length: int


@dataclass
class MediaFeature:
    """ Description is missing from the devtools protocol document. """
    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    value: str


class VirtualTimePolicy(str, enum.Enum):
    """ advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to
    allow the next delayed task (if any) to run; pause: The virtual time base may not advance;
    pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending
    resource fetches. """

    ADVANCE = "advance"
    PAUSE = "pause"
    PAUSEIFNETWORKFETCHESPENDING = "pauseIfNetworkFetchesPending"


    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class UserAgentBrandVersion:
    """ Used to specify User Agent Cient Hints to emulate. See https://wicg.github.io/ua-client-hints """
    #: Description is missing from the devtools protocol document.# noqa
    brand: str
    #: Description is missing from the devtools protocol document.# noqa
    version: str


@dataclass
class UserAgentMetadata:
    """ Used to specify User Agent Cient Hints to emulate. See https://wicg.github.io/ua-client-hints
Missing optional values will be filled in by the target with what it would normally use. """
    #: Description is missing from the devtools protocol document.# noqa
    platform: str
    #: Description is missing from the devtools protocol document.# noqa
    platform_version: str
    #: Description is missing from the devtools protocol document.# noqa
    architecture: str
    #: Description is missing from the devtools protocol document.# noqa
    model: str
    #: Description is missing from the devtools protocol document.# noqa
    mobile: bool
    #: Brands appearing in Sec-CH-UA.# noqa
    brands: typing.Optional[typing.List[UserAgentBrandVersion]] = None
    #: Brands appearing in Sec-CH-UA-Full-Version-List.# noqa
    full_version_list: typing.Optional[typing.List[UserAgentBrandVersion]] = None
    #: Description is missing from the devtools protocol document.# noqa
    full_version: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    bitness: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    wow64: typing.Optional[bool] = None


class DisabledImageType(str, enum.Enum):
    """ Enum of image types that can be disabled. """

    AVIF = "avif"
    WEBP = "webp"


    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)
