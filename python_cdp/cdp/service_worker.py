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

from dataclasses import dataclass


class RegistrationID(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


@dataclass
class ServiceWorkerRegistration:
    """ServiceWorker registration."""


class ServiceWorkerVersionRunningStatus(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


class ServiceWorkerVersionStatus(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


@dataclass
class ServiceWorkerVersion:
    """ServiceWorker version."""


@dataclass
class ServiceWorkerErrorMessage:
    """ServiceWorker error message."""
