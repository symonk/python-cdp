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


class PlayerMessage(None):
    """Have one type per entry in MediaLogRecord::Type Corresponds to kMessage."""

    def to_json(self) -> PlayerMessage:
        return self

    @classmethod
    def from_json(cls, value: None) -> PlayerMessage:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class PlayerProperty(None):
    """Corresponds to kMediaPropertyChange."""

    def to_json(self) -> PlayerProperty:
        return self

    @classmethod
    def from_json(cls, value: None) -> PlayerProperty:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class PlayerEvent(None):
    """Corresponds to kMediaEventTriggered."""

    def to_json(self) -> PlayerEvent:
        return self

    @classmethod
    def from_json(cls, value: None) -> PlayerEvent:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class PlayerErrorSourceLocation(None):
    """Represents logged source line numbers reported in an error.

    NOTE: file and line are from chromium c++ implementation code, not js.
    """

    def to_json(self) -> PlayerErrorSourceLocation:
        return self

    @classmethod
    def from_json(cls, value: None) -> PlayerErrorSourceLocation:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class PlayerError(None):
    """Corresponds to kMediaError."""

    def to_json(self) -> PlayerError:
        return self

    @classmethod
    def from_json(cls, value: None) -> PlayerError:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
