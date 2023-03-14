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

    def to_json(self) -> PlayerId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Timestamp(float):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> Timestamp:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class PlayerMessage:
    """Have one type per entry in MediaLogRecord::Type Corresponds to
    kMessage."""

    #: Keep in sync with MediaLogMessageLevel We are currently keeping themessage level 'error' separate from the PlayerError type because right now theyrepresent different things, this one being a DVLOG(ERROR) style log message thatgets printed based on what log level is selected in the UI, and the other is arepresentation of a media::PipelineStatus object. Soon however we're going to bemoving away from using PipelineStatus for errors and introducing a new errortype which should hopefully let us integrate the error log level into thePlayerError type.# noqa
    level: str
    #: Description is missing from the devtools protocol document.# noqa
    message: str


@dataclass
class PlayerProperty:
    """Corresponds to kMediaPropertyChange."""

    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    value: str


@dataclass
class PlayerEvent:
    """Corresponds to kMediaEventTriggered."""

    #: Description is missing from the devtools protocol document.# noqa
    timestamp: str
    #: Description is missing from the devtools protocol document.# noqa
    value: str


@dataclass
class PlayerErrorSourceLocation:
    """Represents logged source line numbers reported in an error.

    NOTE: file and line are from chromium c++ implementation code, not js.
    """

    #: Description is missing from the devtools protocol document.# noqa
    file: str
    #: Description is missing from the devtools protocol document.# noqa
    line: str


@dataclass
class PlayerError:
    """Corresponds to kMediaError."""

    #: Description is missing from the devtools protocol document.# noqa
    errorType: str
    #: Code is the numeric enum entry for a specific set of error codes, such asPipelineStatusCodes in media/base/pipeline_status.h# noqa
    code: str
    #: A trace of where this error was caused / where it passed through.# noqa
    stack: str
    #: Errors potentially have a root cause error, ie, a DecoderError might becaused by an WindowsError# noqa
    cause: str
    #: Extra data attached to an error, such as an HRESULT, Video Codec, etc.# noqa
    data: str
