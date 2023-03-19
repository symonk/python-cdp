# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Log`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Log/

from __future__ import annotations

import typing
from dataclasses import dataclass

from . import network
from . import runtime
from .utils import memoize_event


@dataclass
class LogEntry:
    """Log entry."""

    # Log entry source.# noqa


str
# Log entry severity.# noqa
str
# Logged text.# noqa
str
# Timestamp when this entry was added.# noqa
runtime.Timestamp
# Description is missing from the devtools protocol document.# noqa
typing.Optional[str]
# URL of the resource if known.# noqa
typing.Optional[str]
# Line number in the resource.# noqa
typing.Optional[int]
# JavaScript stack trace.# noqa
typing.Optional[runtime.StackTrace]
# Identifier of the network request associated with this entry.# noqa
typing.Optional[network.RequestId]
# Identifier of the worker associated with this entry.# noqa
typing.Optional[str]
# Call arguments.# noqa
typing.Optional[typing.List[Runtime.RemoteObject]]


@dataclass
class ViolationSetting:
    """Violation configuration setting."""

    # Violation type.# noqa


str
# Time threshold to trigger upon.# noqa
float


@dataclass
@memoize_event("Log.entryAdded")
class EntryAdded:
    """Issued when new message was logged."""

    entry: LogEntry


async def clear() -> None:
    """Clears the log.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables log domain, prevents further log entries from being reported to the client.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables log domain, sends the entries collected so far to the client by means of the `entryAdded` notification.

    # noqa
    """
    ...


async def start_violations_report() -> None:
    """start violation reporting.

    # noqa
    """
    ...


async def stop_violations_report() -> None:
    """Stop violation reporting.

    # noqa
    """
    ...
