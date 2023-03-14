# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `BackgroundService`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/BackgroundService/

from __future__ import annotations

from dataclasses import dataclass


class ServiceName(str):
    """The Background Service that will be associated with the commands/events.

    Every Background Service operates independently, but they share the
    same API..
    """

    def to_json(self) -> str:
        return self


@dataclass
class EventMetadata:
    """A key-value pair for additional event information to pass along."""

    ...


@dataclass
class BackgroundServiceEvent:
    """Description is missing from the devtools protocol document."""

    ...
