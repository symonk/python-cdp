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

from . import network
from . import service_worker


class ServiceName(str, enum.Enum):
    """The Background Service that will be associated with the commands/events.

    Every Background Service operates independently, but they share the
    same API.
    """

    BACKGROUNDFETCH = "backgroundFetch"
    BACKGROUNDSYNC = "backgroundSync"
    PUSHMESSAGING = "pushMessaging"
    NOTIFICATIONS = "notifications"
    PAYMENTHANDLER = "paymentHandler"
    PERIODICBACKGROUNDSYNC = "periodicBackgroundSync"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class EventMetadata:
    """A key-value pair for additional event information to pass along."""

    #: Description is missing from the devtools protocol document.# noqa
    key: str
    #: Description is missing from the devtools protocol document.# noqa
    value: str


@dataclass
class BackgroundServiceEvent:
    """Description is missing from the devtools protocol document."""

    #: Timestamp of the event (in seconds).# noqa
    timestamp: network.TimeSinceEpoch
    #: The origin this event belongs to.# noqa
    origin: str
    #: The Service Worker ID that initiated the event.# noqa
    serviceWorkerRegistrationId: service_worker.RegistrationID
    #: The Background Service this event belongs to.# noqa
    service: ServiceName
    #: A description of the event.# noqa
    eventName: str
    #: An identifier that groups related events together.# noqa
    instanceId: str
    #: A list of event-specific information.# noqa
    eventMetadata: EventMetadata
    #: Storage key this event belongs to.# noqa
    storageKey: str
