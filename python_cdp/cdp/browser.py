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

from dataclasses import dataclass


class BrowserContextID(str):
    """Description is missing from the devtools protocol document.."""

    def to_json(self) -> str:
        return self


@dataclass
class WindowID:
    """Description is missing from the devtools protocol document."""

    ...


class WindowState(str):
    """The state of the browser window.."""

    def to_json(self) -> str:
        return self


@dataclass
class Bounds:
    """Browser window bounds information."""

    ...


class PermissionType(str):
    """Description is missing from the devtools protocol document.."""

    def to_json(self) -> str:
        return self


class PermissionSetting(str):
    """Description is missing from the devtools protocol document.."""

    def to_json(self) -> str:
        return self


@dataclass
class PermissionDescriptor:
    """Definition of PermissionDescriptor defined in the Permissions API:

    https://w3c.github.io/permissions/#dictdef-permissiondescriptor.
    """

    ...


class BrowserCommandId(str):
    """Browser command ids used by executeBrowserCommand.."""

    def to_json(self) -> str:
        return self


@dataclass
class Bucket:
    """Chrome histogram bucket."""

    ...


@dataclass
class Histogram:
    """Chrome histogram."""

    ...
