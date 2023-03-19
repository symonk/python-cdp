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
from dataclasses import dataclass
import typing
import enum

from .utils import memoize_event
from . import service_worker
from . import network



class ServiceName(str, enum.Enum):
    """ The Background Service that will be associated with the commands/events.
    Every Background Service operates independently, but they share the same
    API. """

    BACKGROUND_FETCH = "background_fetch"
    BACKGROUND_SYNC = "background_sync"
    PUSH_MESSAGING = "push_messaging"
    NOTIFICATIONS = "notifications"
    PAYMENT_HANDLER = "payment_handler"
    PERIODIC_BACKGROUND_SYNC = "periodic_background_sync"


    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)




@dataclass
class EventMetadata:
    """ A key-value pair for additional event information to pass along. """
    # Description is missing from the devtools protocol document. # noqa
    key: str
    # Description is missing from the devtools protocol document. # noqa
    value: str




@dataclass
class BackgroundServiceEvent:
    """ Description is missing from the devtools protocol document. """
    # Timestamp of the event (in seconds). # noqa
    timestamp: network.TimeSinceEpoch
    # The origin this event belongs to. # noqa
    origin: str
    # The Service Worker ID that initiated the event. # noqa
    service_worker_registration_id: service_worker.RegistrationID
    # The Background Service this event belongs to. # noqa
    service: ServiceName
    # A description of the event. # noqa
    event_name: str
    # An identifier that groups related events together. # noqa
    instance_id: str
    # A list of event-specific information. # noqa
    event_metadata: EventMetadata
    # Storage key this event belongs to. # noqa
    storage_key: str


@dataclass
@memoize_event('BackgroundService.recordingStateChanged')
class RecordingStateChanged:
    """ Called when the recording state for the service has been updated. """
    is_recording: bool
    service: ServiceName


@dataclass
@memoize_event('BackgroundService.backgroundServiceEventReceived')
class BackgroundServiceEventReceived:
    """ Called with all existing backgroundServiceEvents when enabled, and all new
    events afterwards if enabled and recording. """
    background_service_event: BackgroundServiceEvent



async def start_observing() -> None:
    """ Enables event updates for the service. # noqa """
    ...



async def stop_observing() -> None:
    """ Disables event updates for the service. # noqa """
    ...



async def set_recording() -> None:
    """ Set the recording state for the service. # noqa """
    ...



async def clear_events() -> None:
    """ Clears all stored data for the service. # noqa """
    ...
