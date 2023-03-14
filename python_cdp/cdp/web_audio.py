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
import typing
from dataclasses import dataclass


class GraphObjectId(str):
    """An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in
    Web Audio API."""

    def to_json(self) -> GraphObjectId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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

    def to_json(self) -> NodeType:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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

    def to_json(self) -> ParamType:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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

    #: The current context time in second in BaseAudioContext.# noqa
    currentTime: float
    #: The time spent on rendering graph divided by render quantum duration, andmultiplied by 100. 100 means the audio renderer reached the full capacity andglitch may occur.# noqa
    renderCapacity: float
    #: A running mean of callback interval.# noqa
    callbackIntervalMean: float
    #: A running variance of callback interval.# noqa
    callbackIntervalVariance: float


@dataclass
class BaseAudioContext:
    """Protocol object for BaseAudioContext."""

    #: Description is missing from the devtools protocol document.# noqa
    contextId: GraphObjectId
    #: Description is missing from the devtools protocol document.# noqa
    contextType: ContextType
    #: Description is missing from the devtools protocol document.# noqa
    contextState: ContextState
    #: Description is missing from the devtools protocol document.# noqa
    realtimeData: typing.Optional[ContextRealtimeData] = None
    #: Platform-dependent callback buffer size.# noqa
    callbackBufferSize: float
    #: Number of output channels supported by audio hardware in use.# noqa
    maxOutputChannelCount: float
    #: Context sample rate.# noqa
    sampleRate: float


@dataclass
class AudioListener:
    """Protocol object for AudioListener."""

    #: Description is missing from the devtools protocol document.# noqa
    listenerId: GraphObjectId
    #: Description is missing from the devtools protocol document.# noqa
    contextId: GraphObjectId


@dataclass
class AudioNode:
    """Protocol object for AudioNode."""

    #: Description is missing from the devtools protocol document.# noqa
    nodeId: GraphObjectId
    #: Description is missing from the devtools protocol document.# noqa
    contextId: GraphObjectId
    #: Description is missing from the devtools protocol document.# noqa
    nodeType: NodeType
    #: Description is missing from the devtools protocol document.# noqa
    numberOfInputs: float
    #: Description is missing from the devtools protocol document.# noqa
    numberOfOutputs: float
    #: Description is missing from the devtools protocol document.# noqa
    channelCount: float
    #: Description is missing from the devtools protocol document.# noqa
    channelCountMode: ChannelCountMode
    #: Description is missing from the devtools protocol document.# noqa
    channelInterpretation: ChannelInterpretation


@dataclass
class AudioParam:
    """Protocol object for AudioParam."""

    #: Description is missing from the devtools protocol document.# noqa
    paramId: GraphObjectId
    #: Description is missing from the devtools protocol document.# noqa
    nodeId: GraphObjectId
    #: Description is missing from the devtools protocol document.# noqa
    contextId: GraphObjectId
    #: Description is missing from the devtools protocol document.# noqa
    paramType: ParamType
    #: Description is missing from the devtools protocol document.# noqa
    rate: AutomationRate
    #: Description is missing from the devtools protocol document.# noqa
    defaultValue: float
    #: Description is missing from the devtools protocol document.# noqa
    minValue: float
    #: Description is missing from the devtools protocol document.# noqa
    maxValue: float
