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
    windowState: typing.Optional[WindowState] = None


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
    userVisibleOnly: typing.Optional[bool] = None
    #: For "clipboard" permission, may specify allowWithoutSanitization.# noqa
    allowWithoutSanitization: typing.Optional[bool] = None
    #: For "camera" permission, may specify panTiltZoom.# noqa
    panTiltZoom: typing.Optional[bool] = None


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
