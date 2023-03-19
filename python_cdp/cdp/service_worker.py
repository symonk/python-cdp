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

from .utils import memoize_event


class RegistrationID(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> RegistrationID:
        return self

    @classmethod
    def from_json(cls, value: str) -> RegistrationID:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ServiceWorkerRegistration(None):
    """ServiceWorker registration."""

    def to_json(self) -> ServiceWorkerRegistration:
        return self

    @classmethod
    def from_json(cls, value: None) -> ServiceWorkerRegistration:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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


class ServiceWorkerVersion(None):
    """ServiceWorker version."""

    def to_json(self) -> ServiceWorkerVersion:
        return self

    @classmethod
    def from_json(cls, value: None) -> ServiceWorkerVersion:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ServiceWorkerErrorMessage(None):
    """ServiceWorker error message."""

    def to_json(self) -> ServiceWorkerErrorMessage:
        return self

    @classmethod
    def from_json(cls, value: None) -> ServiceWorkerErrorMessage:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("ServiceWorker.workerErrorReported")
class WorkerErrorReported:
    """Description is missing from the devtools protocol document."""

    error_message: ServiceWorkerErrorMessage


@dataclass
@memoize_event("ServiceWorker.workerRegistrationUpdated")
class WorkerRegistrationUpdated:
    """Description is missing from the devtools protocol document."""

    registrations: typing.List[ServiceWorkerRegistration]


@dataclass
@memoize_event("ServiceWorker.workerVersionUpdated")
class WorkerVersionUpdated:
    """Description is missing from the devtools protocol document."""

    versions: typing.List[ServiceWorkerVersion]


async def deliver_push_message() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def disable() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def dispatch_sync_event() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def dispatch_periodic_sync_event() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def enable() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def inspect_worker() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def set_force_update_on_page_load() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def skip_waiting() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def start_worker() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def stop_all_workers() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def stop_worker() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def unregister() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def update_registration() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...
