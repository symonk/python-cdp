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
from dataclasses import dataclass


class RegistrationID(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class ServiceWorkerRegistration:
    """ServiceWorker registration."""

    #: Description is missing from the devtools protocol document.
    registrationId: str
    #: Description is missing from the devtools protocol document.
    scopeURL: str
    #: Description is missing from the devtools protocol document.
    isDeleted: str


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

    #: Description is missing from the devtools protocol document.
    versionId: str
    #: Description is missing from the devtools protocol document.
    registrationId: str
    #: Description is missing from the devtools protocol document.
    scriptURL: str
    #: Description is missing from the devtools protocol document.
    runningStatus: str
    #: Description is missing from the devtools protocol document.
    status: str
    #: The Last-Modified header value of the main script.
    scriptLastModified: str
    #: The time at which the response headers of the main script were receivedfrom the server. For cached script it is the last time the cache entry wasvalidated.
    scriptResponseTime: str
    #: Description is missing from the devtools protocol document.
    controlledClients: str
    #: Description is missing from the devtools protocol document.
    targetId: str


@dataclass
class ServiceWorkerErrorMessage:
    """ServiceWorker error message."""

    #: Description is missing from the devtools protocol document.
    errorMessage: str
    #: Description is missing from the devtools protocol document.
    registrationId: str
    #: Description is missing from the devtools protocol document.
    versionId: str
    #: Description is missing from the devtools protocol document.
    sourceURL: str
    #: Description is missing from the devtools protocol document.
    lineNumber: str
    #: Description is missing from the devtools protocol document.
    columnNumber: str
