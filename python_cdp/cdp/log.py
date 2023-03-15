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


@dataclass
class LogEntry:
    """Log entry."""

    #: Log entry source.# noqa
    source: str
    #: Log entry severity.# noqa
    level: str
    #: Logged text.# noqa
    text: str
    #: Timestamp when this entry was added.# noqa
    timestamp: runtime.Timestamp
    #: Description is missing from the devtools protocol document.# noqa
    category: typing.Optional[str] = None
    #: URL of the resource if known.# noqa
    url: typing.Optional[str] = None
    #: Line number in the resource.# noqa
    line_number: typing.Optional[int] = None
    #: JavaScript stack trace.# noqa
    stack_trace: typing.Optional[runtime.StackTrace] = None
    #: Identifier of the network request associated with this entry.# noqa
    network_request_id: typing.Optional[network.RequestId] = None
    #: Identifier of the worker associated with this entry.# noqa
    worker_id: typing.Optional[str] = None
    #: Call arguments.# noqa
    args: typing.Optional[typing.List[runtime.RemoteObject]] = None


@dataclass
class ViolationSetting:
    """Violation configuration setting."""

    #: Violation type.# noqa
    name: str
    #: Time threshold to trigger upon.# noqa
    threshold: float


async def clear() -> None:
    """Clears the log.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables log domain, prevents further log entries from being reported to
    the client.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables log domain, sends the entries collected so far to the client by
    means of the `entryAdded` notification.

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
