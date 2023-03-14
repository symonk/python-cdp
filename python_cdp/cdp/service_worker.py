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


class ServiceWorkerVersionRunningStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"


class ServiceWorkerVersionStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    NEW = "new"
    INSTALLING = "installing"
    INSTALLED = "installed"
    ACTIVATING = "activating"
    ACTIVATED = "activated"
    REDUNDANT = "redundant"


@dataclass
class ServiceWorkerVersion:
    """ServiceWorker version."""


@dataclass
class ServiceWorkerErrorMessage:
    """ServiceWorker error message."""
