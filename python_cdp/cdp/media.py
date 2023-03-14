# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Media`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Media/

from __future__ import annotations

from dataclasses import dataclass


class PlayerId(str):
    """Players will get an ID that is unique within the agent context."""

    def to_json(self) -> str:
        return self


class Timestamp(float):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> float:
        return self


@dataclass
class PlayerMessage:
    """Have one type per entry in MediaLogRecord::Type Corresponds to
    kMessage."""

    ...


@dataclass
class PlayerProperty:
    """Corresponds to kMediaPropertyChange."""

    ...


@dataclass
class PlayerEvent:
    """Corresponds to kMediaEventTriggered."""

    ...


@dataclass
class PlayerErrorSourceLocation:
    """Represents logged source line numbers reported in an error.

    NOTE: file and line are from chromium c++ implementation code, not js.
    """

    ...


@dataclass
class PlayerError:
    """Corresponds to kMediaError."""

    ...
