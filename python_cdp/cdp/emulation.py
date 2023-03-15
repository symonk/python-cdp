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
import typing
from dataclasses import dataclass


@dataclass
class ScreenOrientation:
    """Screen orientation."""

    #: Orientation type.# noqa
    type: str
    #: Orientation angle.# noqa
    angle: int


@dataclass
class DisplayFeature:
    """Description is missing from the devtools protocol document."""

    #: Orientation of a display feature in relation to screen# noqa
    orientation: str
    #: The offset from the screen origin in either the x (for verticalorientation) or y (for horizontal orientation) direction.# noqa
    offset: int
    #: A display feature may mask content such that it is not physicallydisplayed - this length along with the offset describes this area. A displayfeature that only splits content will have a 0 mask_length.# noqa
    mask_length: int


@dataclass
class MediaFeature:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    value: str


class VirtualTimePolicy(str, enum.Enum):
    """advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to
    allow the next delayed task (if any) to run; pause: The virtual time base may not advance;
    pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending
    resource fetches."""

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

    #: Description is missing from the devtools protocol document.# noqa
    brand: str
    #: Description is missing from the devtools protocol document.# noqa
    version: str


@dataclass
class UserAgentMetadata:
    """Used to specify User Agent Cient Hints to emulate.

    See https://wicg.github.io/ua-client-hints
    Missing optional values will be filled in by the target with what it would normally use.
    """

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
    """Enum of image types that can be disabled."""

    AVIF = "avif"
    WEBP = "webp"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


def can_emulate() -> None:
    """Tells whether emulation is supported.

    # noqa
    """
    ...


def clear_device_metrics_override() -> None:
    """Clears the overridden device metrics.

    # noqa
    """
    ...


def clear_geolocation_override() -> None:
    """Clears the overridden Geolocation Position and Error.

    # noqa
    """
    ...


def reset_page_scale_factor() -> None:
    """Requests that page scale factor is reset to initial values.

    # noqa
    """
    ...


def set_focus_emulation_enabled() -> None:
    """Enables or disables simulating a focused and active page.

    # noqa
    """
    ...


def set_auto_dark_mode_override() -> None:
    """Automatically render all web contents using a dark theme.

    # noqa
    """
    ...


def set_cpu_throttling_rate() -> None:
    """Enables CPU throttling to emulate slow CPUs.

    # noqa
    """
    ...


def set_default_background_color_override() -> None:
    """Sets or clears an override of the default background color of the frame.

    This override is used if the content does not specify one. # noqa
    """
    ...


def set_device_metrics_override() -> None:
    """Overrides the values of device screen dimensions (window.screen.width,
    window.screen.height, window.innerWidth, window.innerHeight, and "device-
    width"/"device-height"-related CSS media query results).

    # noqa
    """
    ...


def set_scrollbars_hidden() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


def set_document_cookie_disabled() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


def set_emit_touch_events_for_mouse() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


def set_emulated_media() -> None:
    """Emulates the given media type or media feature for CSS media queries.

    # noqa
    """
    ...


def set_emulated_vision_deficiency() -> None:
    """Emulates the given vision deficiency.

    # noqa
    """
    ...


def set_geolocation_override() -> None:
    """Overrides the Geolocation Position or Error.

    Omitting any of the parameters emulates position unavailable. # noqa
    """
    ...


def set_idle_override() -> None:
    """Overrides the Idle state.

    # noqa
    """
    ...


def clear_idle_override() -> None:
    """Clears Idle state overrides.

    # noqa
    """
    ...


def set_navigator_overrides() -> None:
    """Overrides value returned by the javascript navigator object.

    # noqa
    """
    ...


def set_page_scale_factor() -> None:
    """Sets a specified page scale factor.

    # noqa
    """
    ...


def set_script_execution_disabled() -> None:
    """Switches script execution in the page.

    # noqa
    """
    ...


def set_touch_emulation_enabled() -> None:
    """Enables touch on platforms which do not support them.

    # noqa
    """
    ...


def set_virtual_time_policy() -> None:
    """Turns on virtual time for all frames (replacing real-time with a
    synthetic time source) and sets the current virtual time policy.

    Note this supersedes any previous time budget. # noqa
    """
    ...


def set_locale_override() -> None:
    """Overrides default host system locale with the specified one.

    # noqa
    """
    ...


def set_timezone_override() -> None:
    """Overrides default host system timezone with the specified one.

    # noqa
    """
    ...


def set_visible_size() -> None:
    """Resizes the frame/viewport of the page.

    Note that this does not affect the frame's container (e.g. browser
    window). Can be used to produce screenshots of the specified size.
    Not supported on Android. # noqa
    """
    ...


def set_disabled_image_types() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


def set_hardware_concurrency_override() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


def set_user_agent_override() -> None:
    """Allows overriding user agent with the given string.

    # noqa
    """
    ...


def set_automation_override() -> None:
    """Allows overriding the automation flag.

    # noqa
    """
    ...
