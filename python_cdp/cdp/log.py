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

from dataclasses import dataclass

from .utils import memoize_event


class LogEntry(None):
    """Log entry."""

    def to_json(self) -> LogEntry:
        return self

    @classmethod
    def from_json(cls, value: None) -> LogEntry:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ViolationSetting(None):
    """Violation configuration setting."""

    def to_json(self) -> ViolationSetting:
        return self

    @classmethod
    def from_json(cls, value: None) -> ViolationSetting:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
