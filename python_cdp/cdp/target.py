# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Target`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Target/

from __future__ import annotations

import typing
from dataclasses import dataclass


class TargetID(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> TargetID:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SessionID(str):
    """Unique identifier of attached debugging session."""

    def to_json(self) -> SessionID:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class TargetInfo:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    targetId: TargetID
    #: Description is missing from the devtools protocol document.# noqa
    type: str
    #: Description is missing from the devtools protocol document.# noqa
    title: str
    #: Description is missing from the devtools protocol document.# noqa
    url: str
    #: Whether the target has an attached client.# noqa
    attached: bool
    #: Opener target Id# noqa
    openerId: typing.Optional[TargetID] = None
    #: Whether the target has access to the originating window.# noqa
    canAccessOpener: bool
    #: Frame id of originating window (is only set if target has an opener).# noqa
    openerFrameId: typing.Optional[page.FrameId] = None
    #: Description is missing from the devtools protocol document.# noqa
    browserContextId: typing.Optional[browser.BrowserContextID] = None
    #: Provides additional details for specific target types. For example, forthe type of "page", this may be set to "portal" or "prerender".# noqa
    subtype: typing.Optional[str] = None


@dataclass
class FilterEntry:
    """A filter used by target query/discovery/auto-attach operations."""

    #: If set, causes exclusion of mathcing targets from the list.# noqa
    exclude: typing.Optional[bool] = None
    #: If not present, matches any type.# noqa
    type: typing.Optional[str] = None


@dataclass
class TargetFilter:
    """The entries in TargetFilter are matched sequentially against targets and
    the first entry that matches determines if the target is included or not,
    depending on the value of `exclude` field in the entry. If filter is not
    specified, the one assumed is.

    [{type: "browser", exclude: true}, {type: "tab", exclude: true}, {}]
    (i.e. include everything but `browser` and `tab`).
    """


@dataclass
class RemoteLocation:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    host: str
    #: Description is missing from the devtools protocol document.# noqa
    port: int
