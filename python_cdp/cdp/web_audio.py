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

    #: The current context time in second in BaseAudioContext.
    currentTime: str
    #: The time spent on rendering graph divided by render quantum duration, andmultiplied by 100. 100 means the audio renderer reached the full capacity andglitch may occur.
    renderCapacity: str
    #: A running mean of callback interval.
    callbackIntervalMean: str
    #: A running variance of callback interval.
    callbackIntervalVariance: str


@dataclass
class BaseAudioContext:
    """Protocol object for BaseAudioContext."""

    #: Description is missing from the devtools protocol document.
    contextId: str
    #: Description is missing from the devtools protocol document.
    contextType: str
    #: Description is missing from the devtools protocol document.
    contextState: str
    #: Description is missing from the devtools protocol document.
    realtimeData: str
    #: Platform-dependent callback buffer size.
    callbackBufferSize: str
    #: Number of output channels supported by audio hardware in use.
    maxOutputChannelCount: str
    #: Context sample rate.
    sampleRate: str


@dataclass
class AudioListener:
    """Protocol object for AudioListener."""

    #: Description is missing from the devtools protocol document.
    listenerId: str
    #: Description is missing from the devtools protocol document.
    contextId: str


@dataclass
class AudioNode:
    """Protocol object for AudioNode."""

    #: Description is missing from the devtools protocol document.
    nodeId: str
    #: Description is missing from the devtools protocol document.
    contextId: str
    #: Description is missing from the devtools protocol document.
    nodeType: str
    #: Description is missing from the devtools protocol document.
    numberOfInputs: str
    #: Description is missing from the devtools protocol document.
    numberOfOutputs: str
    #: Description is missing from the devtools protocol document.
    channelCount: str
    #: Description is missing from the devtools protocol document.
    channelCountMode: str
    #: Description is missing from the devtools protocol document.
    channelInterpretation: str


@dataclass
class AudioParam:
    """Protocol object for AudioParam."""

    #: Description is missing from the devtools protocol document.
    paramId: str
    #: Description is missing from the devtools protocol document.
    nodeId: str
    #: Description is missing from the devtools protocol document.
    contextId: str
    #: Description is missing from the devtools protocol document.
    paramType: str
    #: Description is missing from the devtools protocol document.
    rate: str
    #: Description is missing from the devtools protocol document.
    defaultValue: str
    #: Description is missing from the devtools protocol document.
    minValue: str
    #: Description is missing from the devtools protocol document.
    maxValue: str
