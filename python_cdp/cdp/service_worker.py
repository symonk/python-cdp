# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `ServiceWorker`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import target


class RegistrationID(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> RegistrationID:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class ServiceWorkerRegistration:
    """ServiceWorker registration."""

    #: Description is missing from the devtools protocol document.# noqa
    registrationId: RegistrationID
    #: Description is missing from the devtools protocol document.# noqa
    scopeURL: str
    #: Description is missing from the devtools protocol document.# noqa
    isDeleted: bool


class ServiceWorkerVersionRunningStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ServiceWorkerVersionStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    NEW = "new"
    INSTALLING = "installing"
    INSTALLED = "installed"
    ACTIVATING = "activating"
    ACTIVATED = "activated"
    REDUNDANT = "redundant"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class ServiceWorkerVersion:
    """ServiceWorker version."""

    #: Description is missing from the devtools protocol document.# noqa
    versionId: str
    #: Description is missing from the devtools protocol document.# noqa
    registrationId: RegistrationID
    #: Description is missing from the devtools protocol document.# noqa
    scriptURL: str
    #: Description is missing from the devtools protocol document.# noqa
    runningStatus: ServiceWorkerVersionRunningStatus
    #: Description is missing from the devtools protocol document.# noqa
    status: ServiceWorkerVersionStatus
    #: The Last-Modified header value of the main script.# noqa
    scriptLastModified: typing.Optional[float] = None
    #: The time at which the response headers of the main script were receivedfrom the server. For cached script it is the last time the cache entry wasvalidated.# noqa
    scriptResponseTime: typing.Optional[float] = None
    #: Description is missing from the devtools protocol document.# noqa
    controlledClients: typing.Optional[target.TargetID] = None
    #: Description is missing from the devtools protocol document.# noqa
    targetId: typing.Optional[target.TargetID] = None


@dataclass
class ServiceWorkerErrorMessage:
    """ServiceWorker error message."""

    #: Description is missing from the devtools protocol document.# noqa
    errorMessage: str
    #: Description is missing from the devtools protocol document.# noqa
    registrationId: RegistrationID
    #: Description is missing from the devtools protocol document.# noqa
    versionId: str
    #: Description is missing from the devtools protocol document.# noqa
    sourceURL: str
    #: Description is missing from the devtools protocol document.# noqa
    lineNumber: int
    #: Description is missing from the devtools protocol document.# noqa
    columnNumber: int
