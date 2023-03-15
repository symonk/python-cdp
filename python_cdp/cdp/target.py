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

from . import browser
from . import page


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
    target_id: TargetID
    #: Description is missing from the devtools protocol document.# noqa
    type: str
    #: Description is missing from the devtools protocol document.# noqa
    title: str
    #: Description is missing from the devtools protocol document.# noqa
    url: str
    #: Whether the target has an attached client.# noqa
    attached: bool
    #: Whether the target has access to the originating window.# noqa
    can_access_opener: bool
    #: Opener target Id# noqa
    opener_id: typing.Optional[TargetID] = None
    #: Frame id of originating window (is only set if target has an opener).# noqa
    opener_frame_id: typing.Optional[page.FrameId] = None
    #: Description is missing from the devtools protocol document.# noqa
    browser_context_id: typing.Optional[browser.BrowserContextID] = None
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


def activate_target() -> None:
    """Activates (focuses) the target.

    # noqa
    """
    ...


def attach_to_target() -> None:
    """Attaches to the target with given id.

    # noqa
    """
    ...


def attach_to_browser_target() -> None:
    """Attaches to the browser target, only uses flat sessionId mode.

    # noqa
    """
    ...


def close_target() -> None:
    """Closes the target.

    If the target is a page that gets closed too. # noqa
    """
    ...


def expose_dev_tools_protocol() -> None:
    """Inject object to the target's main frame that provides a communication
    channel with browser target.

    Injected object will be available as `window[bindingName]`.

    The object has the follwing API:
    - `binding.send(json)` - a method to send messages over the remote debugging protocol
    - `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses. # noqa
    """
    ...


def create_browser_context() -> None:
    """Creates a new empty BrowserContext.

    Similar to an incognito profile but you can have more than one. #
    noqa
    """
    ...


def get_browser_contexts() -> None:
    """Returns all browser contexts created with `Target.createBrowserContext`
    method.

    # noqa
    """
    ...


def create_target() -> None:
    """Creates a new page.

    # noqa
    """
    ...


def detach_from_target() -> None:
    """Detaches session with given id.

    # noqa
    """
    ...


def dispose_browser_context() -> None:
    """Deletes a BrowserContext.

    All the belonging pages will be closed without calling their
    beforeunload hooks. # noqa
    """
    ...


def get_target_info() -> None:
    """Returns information about a target.

    # noqa
    """
    ...


def get_targets() -> None:
    """Retrieves a list of available targets.

    # noqa
    """
    ...


def send_message_to_target() -> None:
    """Sends protocol message over session with given id.

    Consider using flat mode instead; see commands attachToTarget,
    setAutoAttach, and crbug.com/991325. # noqa
    """
    ...


def set_auto_attach() -> None:
    """Controls whether to automatically attach to new targets which are
    considered to be related to this one.

    When turned on, attaches to all existing related targets as well.
    When turned off, automatically detaches from all currently attached
    targets. This also clears all targets added by `autoAttachRelated`
    from the list of targets to watch for creation of related targets. #
    noqa
    """
    ...


def auto_attach_related() -> None:
    """Adds the specified target to the list of targets that will be monitored
    for any related target creation (such as child frames, child workers and
    new versions of service worker) and reported through `attachedToTarget`.

    The specified target is also auto-attached. This cancels the effect
    of any previous `setAutoAttach` and is also cancelled by subsequent
    `setAutoAttach`. Only available at the Browser target. # noqa
    """
    ...


def set_discover_targets() -> None:
    """Controls whether to discover available targets and notify via
    `targetCreated/targetInfoChanged/targetDestroyed` events.

    # noqa
    """
    ...


def set_remote_locations() -> None:
    """Enables target discovery for the specified locations, when
    `setDiscoverTargets` was set to `true`.

    # noqa
    """
    ...
