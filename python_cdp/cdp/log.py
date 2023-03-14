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


@dataclass
class LogEntry:
    """Log entry."""

    #: Log entry source.# noqa
    source: str
    #: Log entry severity.# noqa
    level: str
    #: Logged text.# noqa
    text: str
    #: Description is missing from the devtools protocol document.# noqa
    category: str
    #: Timestamp when this entry was added.# noqa
    timestamp: str
    #: URL of the resource if known.# noqa
    url: str
    #: Line number in the resource.# noqa
    lineNumber: str
    #: JavaScript stack trace.# noqa
    stackTrace: str
    #: Identifier of the network request associated with this entry.# noqa
    networkRequestId: str
    #: Identifier of the worker associated with this entry.# noqa
    workerId: str
    #: Call arguments.# noqa
    args: str


@dataclass
class ViolationSetting:
    """Violation configuration setting."""

    #: Violation type.# noqa
    name: str
    #: Time threshold to trigger upon.# noqa
    threshold: str
