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

from dataclasses import dataclass

from .utils import memoize_event


class TargetID(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> TargetID:
        return self

    @classmethod
    def from_json(cls, value: str) -> TargetID:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SessionID(str):
    """Unique identifier of attached debugging session."""

    def to_json(self) -> SessionID:
        return self

    @classmethod
    def from_json(cls, value: str) -> SessionID:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class TargetInfo(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> TargetInfo:
        return self

    @classmethod
    def from_json(cls, value: None) -> TargetInfo:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class FilterEntry(None):
    """A filter used by target query/discovery/auto-attach operations."""

    def to_json(self) -> FilterEntry:
        return self

    @classmethod
    def from_json(cls, value: None) -> FilterEntry:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class TargetFilter:
    """The entries in TargetFilter are matched sequentially against targets and the first entry that matches determines
    if the target is included or not, depending on the value of `exclude` field in the entry. If filter is not
    specified, the one assumed is.

    [{type: "browser", exclude: true}, {type: "tab", exclude: true}, {}]
    (i.e. include everything but `browser` and `tab`).
    """


class RemoteLocation(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> RemoteLocation:
        return self

    @classmethod
    def from_json(cls, value: None) -> RemoteLocation:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("Target.attachedToTarget")
class AttachedToTarget:
    """Issued when attached to target because of auto-attach or `attachToTarget` command."""

    session_id: SessionID
    target_info: TargetInfo
    waiting_for_debugger: bool


@dataclass
@memoize_event("Target.detachedFromTarget")
class DetachedFromTarget:
    """Issued when detached from target for any reason (including `detachFromTarget` command).

    Can be issued multiple times per target if multiple sessions have been attached to it.
    """

    session_id: SessionID
    target_id: TargetID


@dataclass
@memoize_event("Target.receivedMessageFromTarget")
class ReceivedMessageFromTarget:
    """Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event)."""

    session_id: SessionID
    message: str
    target_id: TargetID


@dataclass
@memoize_event("Target.targetCreated")
class TargetCreated:
    """Issued when a possible inspection target is created."""

    target_info: TargetInfo


@dataclass
@memoize_event("Target.targetDestroyed")
class TargetDestroyed:
    """Issued when a target is destroyed."""

    target_id: TargetID


@dataclass
@memoize_event("Target.targetCrashed")
class TargetCrashed:
    """Issued when a target has crashed."""

    target_id: TargetID
    status: str
    error_code: int


@dataclass
@memoize_event("Target.targetInfoChanged")
class TargetInfoChanged:
    """Issued when some information about a target has changed.

    This only happens between `targetCreated` and `targetDestroyed`.
    """

    target_info: TargetInfo


async def activate_target() -> None:
    """Activates (focuses) the target.

    # noqa
    """
    ...


async def attach_to_target() -> None:
    """Attaches to the target with given id.

    # noqa
    """
    ...


async def attach_to_browser_target() -> None:
    """Attaches to the browser target, only uses flat sessionId mode.

    # noqa
    """
    ...


async def close_target() -> None:
    """Closes the target.

    If the target is a page that gets closed too. # noqa
    """
    ...


async def expose_dev_tools_protocol() -> None:
    """Inject object to the target's main frame that provides a communication channel with browser target.

    Injected object will be available as `window[bindingName]`.

    The object has the follwing API:
    - `binding.send(json)` - a method to send messages over the remote debugging protocol
    - `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses. # noqa
    """
    ...


async def create_browser_context() -> None:
    """Creates a new empty BrowserContext.

    Similar to an incognito profile but you can have more than one. # noqa
    """
    ...


async def get_browser_contexts() -> None:
    """Returns all browser contexts created with `Target.createBrowserContext` method.

    # noqa
    """
    ...


async def create_target() -> None:
    """Creates a new page.

    # noqa
    """
    ...


async def detach_from_target() -> None:
    """Detaches session with given id.

    # noqa
    """
    ...


async def dispose_browser_context() -> None:
    """Deletes a BrowserContext.

    All the belonging pages will be closed without calling their beforeunload hooks. # noqa
    """
    ...


async def get_target_info() -> None:
    """Returns information about a target.

    # noqa
    """
    ...


async def get_targets() -> None:
    """Retrieves a list of available targets.

    # noqa
    """
    ...


async def send_message_to_target() -> None:
    """Sends protocol message over session with given id.

    Consider using flat mode instead; see commands attachToTarget, setAutoAttach, and crbug.com/991325. # noqa
    """
    ...


async def set_auto_attach() -> None:
    """Controls whether to automatically attach to new targets which are considered to be related to this one.

    When turned on, attaches to all existing related targets as well. When turned off, automatically detaches from all
    currently attached targets. This also clears all targets added by `autoAttachRelated` from the list of targets to
    watch for creation of related targets. # noqa
    """
    ...


async def auto_attach_related() -> None:
    """Adds the specified target to the list of targets that will be monitored for any related target creation (such as
    child frames, child workers and new versions of service worker) and reported through `attachedToTarget`.

    The specified target is also auto-attached. This cancels the effect of any previous `setAutoAttach` and is also
    cancelled by subsequent `setAutoAttach`. Only available at the Browser target. # noqa
    """
    ...


async def set_discover_targets() -> None:
    """Controls whether to discover available targets and notify via `targetCreated/targetInfoChanged/targetDestroyed`
    events.

    # noqa
    """
    ...


async def set_remote_locations() -> None:
    """Enables target discovery for the specified locations, when `setDiscoverTargets` was set to `true`.

    # noqa
    """
    ...
