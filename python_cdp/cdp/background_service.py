# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `BackgroundService`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/BackgroundService/

from __future__ import annotations

import enum
from dataclasses import dataclass

from .utils import memoize_event


class ServiceName(str, enum.Enum):
    """The Background Service that will be associated with the commands/events.

    Every Background Service operates independently, but they share the same API.
    """

    BACKGROUND_FETCH = "background_fetch"
    BACKGROUND_SYNC = "background_sync"
    PUSH_MESSAGING = "push_messaging"
    NOTIFICATIONS = "notifications"
    PAYMENT_HANDLER = "payment_handler"
    PERIODIC_BACKGROUND_SYNC = "periodic_background_sync"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class EventMetadata(None):
    """A key-value pair for additional event information to pass along."""

    def to_json(self) -> EventMetadata:
        return self

    @classmethod
    def from_json(cls, value: None) -> EventMetadata:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class BackgroundServiceEvent(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> BackgroundServiceEvent:
        return self

    @classmethod
    def from_json(cls, value: None) -> BackgroundServiceEvent:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("BackgroundService.recordingStateChanged")
class RecordingStateChanged:
    """Called when the recording state for the service has been updated."""

    is_recording: bool
    service: ServiceName


@dataclass
@memoize_event("BackgroundService.backgroundServiceEventReceived")
class BackgroundServiceEventReceived:
    """Called with all existing backgroundServiceEvents when enabled, and all new events afterwards if enabled and
    recording."""

    background_service_event: BackgroundServiceEvent


async def start_observing() -> None:
    """Enables event updates for the service.

    # noqa
    """
    ...


async def stop_observing() -> None:
    """Disables event updates for the service.

    # noqa
    """
    ...


async def set_recording() -> None:
    """Set the recording state for the service.

    # noqa
    """
    ...


async def clear_events() -> None:
    """Clears all stored data for the service.

    # noqa
    """
    ...
