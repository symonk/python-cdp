# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Browser`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Browser/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass


class BrowserContextID(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> BrowserContextID:
        return self

    @classmethod
    def from_json(cls, value: str) -> BrowserContextID:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class WindowID:
    """Description is missing from the devtools protocol document."""


class WindowState(str, enum.Enum):
    """The state of the browser window."""

    NORMAL = "normal"
    MINIMIZED = "minimized"
    MAXIMIZED = "maximized"
    FULLSCREEN = "fullscreen"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class Bounds:
    """Browser window bounds information."""

    #: The offset from the left edge of the screen to the window in pixels.# noqa
    left: typing.Optional[int] = None
    #: The offset from the top edge of the screen to the window in pixels.# noqa
    top: typing.Optional[int] = None
    #: The window width in pixels.# noqa
    width: typing.Optional[int] = None
    #: The window height in pixels.# noqa
    height: typing.Optional[int] = None
    #: The window state. Default to normal.# noqa
    window_state: typing.Optional[WindowState] = None


class PermissionType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    ACCESSIBILITYEVENTS = "accessibilityEvents"
    AUDIOCAPTURE = "audioCapture"
    BACKGROUNDSYNC = "backgroundSync"
    BACKGROUNDFETCH = "backgroundFetch"
    CLIPBOARDREADWRITE = "clipboardReadWrite"
    CLIPBOARDSANITIZEDWRITE = "clipboardSanitizedWrite"
    DISPLAYCAPTURE = "displayCapture"
    DURABLESTORAGE = "durableStorage"
    FLASH = "flash"
    GEOLOCATION = "geolocation"
    IDLEDETECTION = "idleDetection"
    LOCALFONTS = "localFonts"
    MIDI = "midi"
    MIDISYSEX = "midiSysex"
    NFC = "nfc"
    NOTIFICATIONS = "notifications"
    PAYMENTHANDLER = "paymentHandler"
    PERIODICBACKGROUNDSYNC = "periodicBackgroundSync"
    PROTECTEDMEDIAIDENTIFIER = "protectedMediaIdentifier"
    SENSORS = "sensors"
    STORAGEACCESS = "storageAccess"
    TOPLEVELSTORAGEACCESS = "topLevelStorageAccess"
    VIDEOCAPTURE = "videoCapture"
    VIDEOCAPTUREPANTILTZOOM = "videoCapturePanTiltZoom"
    WAKELOCKSCREEN = "wakeLockScreen"
    WAKELOCKSYSTEM = "wakeLockSystem"
    WINDOWMANAGEMENT = "windowManagement"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PermissionSetting(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    GRANTED = "granted"
    DENIED = "denied"
    PROMPT = "prompt"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class PermissionDescriptor:
    """Definition of PermissionDescriptor defined in the Permissions API:

    https://w3c.github.io/permissions/#dictdef-permissiondescriptor.
    """

    #: Name of permission. See https://cs.chromium.org/chromium/src/third_party/blink/renderer/modules/permissions/permission_descriptor.idl for validpermission names.# noqa
    name: str
    #: For "midi" permission, may also specify sysex control.# noqa
    sysex: typing.Optional[bool] = None
    #: For "push" permission, may specify userVisibleOnly. Note thatuserVisibleOnly = true is the only currently supported type.# noqa
    user_visible_only: typing.Optional[bool] = None
    #: For "clipboard" permission, may specify allowWithoutSanitization.# noqa
    allow_without_sanitization: typing.Optional[bool] = None
    #: For "camera" permission, may specify panTiltZoom.# noqa
    pan_tilt_zoom: typing.Optional[bool] = None


class BrowserCommandId(str, enum.Enum):
    """Browser command ids used by executeBrowserCommand."""

    OPENTABSEARCH = "openTabSearch"
    CLOSETABSEARCH = "closeTabSearch"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class Bucket:
    """Chrome histogram bucket."""

    #: Minimum value (inclusive).# noqa
    low: int
    #: Maximum value (exclusive).# noqa
    high: int
    #: Number of samples.# noqa
    count: int


@dataclass
class Histogram:
    """Chrome histogram."""

    #: Name.# noqa
    name: str
    #: Sum of sample values.# noqa
    sum: int
    #: Total number of samples.# noqa
    count: int
    #: Buckets.# noqa
    buckets: Bucket


async def set_permission() -> None:
    """Set permission settings for given origin.

    # noqa
    """
    ...


async def grant_permissions() -> None:
    """Grant specific permissions to the given origin and reject all others.

    # noqa
    """
    ...


async def reset_permissions() -> None:
    """Reset all permission management for all origins.

    # noqa
    """
    ...


async def set_download_behavior() -> None:
    """Set the behavior when downloading a file.

    # noqa
    """
    ...


async def cancel_download() -> None:
    """Cancel a download if in progress # noqa."""
    ...


async def close() -> None:
    """Close browser gracefully.

    # noqa
    """
    ...


async def crash() -> None:
    """Crashes browser on the main thread.

    # noqa
    """
    ...


async def crash_gpu_process() -> None:
    """Crashes GPU process.

    # noqa
    """
    ...


async def get_version() -> None:
    """Returns version information.

    # noqa
    """
    ...


async def get_browser_command_line() -> None:
    """Returns the command line switches for the browser process if, and only
    if.

    --enable-automation is on the commandline. # noqa
    """
    ...


async def get_histograms() -> None:
    """Get Chrome histograms.

    # noqa
    """
    ...


async def get_histogram() -> None:
    """Get a Chrome histogram by name.

    # noqa
    """
    ...


async def get_window_bounds() -> None:
    """Get position and size of the browser window.

    # noqa
    """
    ...


async def get_window_for_target() -> None:
    """Get the browser window that contains the devtools target.

    # noqa
    """
    ...


async def set_window_bounds() -> None:
    """Set position and/or size of the browser window.

    # noqa
    """
    ...


async def set_dock_tile() -> None:
    """Set dock tile details, platform-specific.

    # noqa
    """
    ...


async def execute_browser_command() -> None:
    """Invoke custom browser commands used by telemetry.

    # noqa
    """
    ...
