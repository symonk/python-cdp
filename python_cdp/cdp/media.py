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

import typing
from dataclasses import dataclass

from .utils import memoize_event


class PlayerId(str):
    """Players will get an ID that is unique within the agent context."""

    def to_json(self) -> PlayerId:
        return self

    @classmethod
    def from_json(cls, value: str) -> PlayerId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Timestamp(float):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> Timestamp:
        return self

    @classmethod
    def from_json(cls, value: float) -> Timestamp:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class PlayerMessage:
    """Have one type per entry in MediaLogRecord::Type Corresponds to kMessage."""

    # Keep in sync with MediaLogMessageLevel We are currently keeping themessage level 'error' separate from the PlayerError type because right now theyrepresent different things, this one being a DVLOG(ERROR) style log message thatgets printed based on what log level is selected in the UI, and the other is arepresentation of a media::PipelineStatus object. Soon however we're going to bemoving away from using PipelineStatus for errors and introducing a new errortype which should hopefully let us integrate the error log level into thePlayerError type.# noqa


str
# Description is missing from the devtools protocol document.# noqa
str


@dataclass
class PlayerProperty:
    """Corresponds to kMediaPropertyChange."""

    # Description is missing from the devtools protocol document.# noqa


str
# Description is missing from the devtools protocol document.# noqa
str


@dataclass
class PlayerEvent:
    """Corresponds to kMediaEventTriggered."""

    # Description is missing from the devtools protocol document.# noqa


Timestamp
# Description is missing from the devtools protocol document.# noqa
str


@dataclass
class PlayerErrorSourceLocation:
    """Represents logged source line numbers reported in an error.

    NOTE: file and line are from chromium c++ implementation code, not js.
    """

    # Description is missing from the devtools protocol document.# noqa


str
# Description is missing from the devtools protocol document.# noqa
int


@dataclass
class PlayerError:
    """Corresponds to kMediaError."""

    # Description is missing from the devtools protocol document.# noqa


str
# Code is the numeric enum entry for a specific set of error codes, such asPipelineStatusCodes in media/base/pipeline_status.h# noqa
int
# A trace of where this error was caused / where it passed through.# noqa
typing.List[PlayerErrorSourceLocation]
# Errors potentially have a root cause error, ie, a DecoderError might becaused by an WindowsError# noqa
typing.List[PlayerError]
# Extra data attached to an error, such as an HRESULT, Video Codec, etc.# noqa
object


@dataclass
@memoize_event("Media.playerPropertiesChanged")
class PlayerPropertiesChanged:
    """This can be called multiple times, and can be used to set / override / remove player properties.

    A null propValue indicates removal.
    """

    player_id: PlayerId
    properties: typing.List[PlayerProperty]


@dataclass
@memoize_event("Media.playerEventsAdded")
class PlayerEventsAdded:
    """Send events as a list, allowing them to be batched on the browser for less congestion.

    If batched, events must ALWAYS be in chronological order.
    """

    player_id: PlayerId
    events: typing.List[PlayerEvent]


@dataclass
@memoize_event("Media.playerMessagesLogged")
class PlayerMessagesLogged:
    """Send a list of any messages that need to be delivered."""

    player_id: PlayerId
    messages: typing.List[PlayerMessage]


@dataclass
@memoize_event("Media.playerErrorsRaised")
class PlayerErrorsRaised:
    """Send a list of any errors that need to be delivered."""

    player_id: PlayerId
    errors: typing.List[PlayerError]


@dataclass
@memoize_event("Media.playersCreated")
class PlayersCreated:
    """Called whenever a player is created, or when a new agent joins and receives a list of active players.

    If an agent is restored, it will receive the full list of player ids and all events again.
    """

    players: typing.List[PlayerId]


async def enable() -> None:
    """Enables the Media domain # noqa."""
    ...


async def disable() -> None:
    """Disables the Media domain.

    # noqa
    """
    ...
