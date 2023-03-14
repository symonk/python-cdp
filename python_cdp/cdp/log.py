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

    #: Log entry source.
    source: str
    #: Log entry severity.
    level: str
    #: Logged text.
    text: str
    #: Description is missing from the devtools protocol document.
    category: str
    #: Timestamp when this entry was added.
    timestamp: str
    #: URL of the resource if known.
    url: str
    #: Line number in the resource.
    lineNumber: str
    #: JavaScript stack trace.
    stackTrace: str
    #: Identifier of the network request associated with this entry.
    networkRequestId: str
    #: Identifier of the worker associated with this entry.
    workerId: str
    #: Call arguments.
    args: str


@dataclass
class ViolationSetting:
    """Violation configuration setting."""

    #: Violation type.
    name: str
    #: Time threshold to trigger upon.
    threshold: str
