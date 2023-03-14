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
from dataclasses import dataclass


class BrowserContextID(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


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


@dataclass
class Histogram:
    """Chrome histogram."""
