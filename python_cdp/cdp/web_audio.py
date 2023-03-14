# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `WebAudio`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/WebAudio/

from __future__ import annotations

import enum
from dataclasses import dataclass


class GraphObjectId(str):
    """An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in
    Web Audio API."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class ContextType(str, enum.Enum):
    """Enum of BaseAudioContext types."""

    REALTIME = "realtime"
    OFFLINE = "offline"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ContextState(str, enum.Enum):
    """Enum of AudioContextState from the spec."""

    SUSPENDED = "suspended"
    RUNNING = "running"
    CLOSED = "closed"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class NodeType(str):
    """Enum of AudioNode types."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class ChannelCountMode(str, enum.Enum):
    """Enum of AudioNode::ChannelCountMode from the spec."""

    CLAMPED_MAX = "clamped_max"
    EXPLICIT = "explicit"
    MAX = "max"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ChannelInterpretation(str, enum.Enum):
    """Enum of AudioNode::ChannelInterpretation from the spec."""

    DISCRETE = "discrete"
    SPEAKERS = "speakers"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ParamType(str):
    """Enum of AudioParam types."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class AutomationRate(str, enum.Enum):
    """Enum of AudioParam::AutomationRate from the spec."""

    A_RATE = "a_rate"
    K_RATE = "k_rate"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class ContextRealtimeData:
    """Fields in AudioContext that change in real-time."""


@dataclass
class BaseAudioContext:
    """Protocol object for BaseAudioContext."""


@dataclass
class AudioListener:
    """Protocol object for AudioListener."""


@dataclass
class AudioNode:
    """Protocol object for AudioNode."""


@dataclass
class AudioParam:
    """Protocol object for AudioParam."""
