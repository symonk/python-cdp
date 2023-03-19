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

from .utils import memoize_event


class GraphObjectId(str):
    """An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in Web Audio API."""

    def to_json(self) -> GraphObjectId:
        return self

    @classmethod
    def from_json(cls, value: str) -> GraphObjectId:
        return cls(value)

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

    @classmethod
    def from_json(cls, value: str) -> NodeType:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ChannelCountMode(str, enum.Enum):
    """Enum of AudioNode::ChannelCountMode from the spec."""

    CLAMPED_MAX = "clamped-max"
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

    @classmethod
    def from_json(cls, value: str) -> ParamType:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class AutomationRate(str, enum.Enum):
    """Enum of AudioParam::AutomationRate from the spec."""

    A_RATE = "a-rate"
    K_RATE = "k-rate"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class ContextRealtimeData:
    """Fields in AudioContext that change in real-time."""

    # The current context time in second in BaseAudioContext.# noqa
    current_time: float
    # The time spent on rendering graph divided by render quantum duration, andmultiplied by 100. 100 means the audio renderer reached the full capacity andglitch may occur.# noqa
    render_capacity: float
    # A running mean of callback interval.# noqa
    callback_interval_mean: float
    # A running variance of callback interval.# noqa
    callback_interval_variance: float


@dataclass
class BaseAudioContext:
    """Protocol object for BaseAudioContext."""

    # Description is missing from the devtools protocol document.# noqa
    context_id: GraphObjectId
    # Description is missing from the devtools protocol document.# noqa
    context_type: ContextType
    # Description is missing from the devtools protocol document.# noqa
    context_state: ContextState
    # Platform-dependent callback buffer size.# noqa
    callback_buffer_size: float
    # Number of output channels supported by audio hardware in use.# noqa
    max_output_channel_count: float
    # Context sample rate.# noqa
    sample_rate: float
    # Description is missing from the devtools protocol document.# noqa
    realtime_data: typing.Optional[ContextRealtimeData]


@dataclass
class AudioListener:
    """Protocol object for AudioListener."""

    # Description is missing from the devtools protocol document.# noqa
    listener_id: GraphObjectId
    # Description is missing from the devtools protocol document.# noqa
    context_id: GraphObjectId


@dataclass
class AudioNode:
    """Protocol object for AudioNode."""

    # Description is missing from the devtools protocol document.# noqa
    node_id: GraphObjectId
    # Description is missing from the devtools protocol document.# noqa
    context_id: GraphObjectId
    # Description is missing from the devtools protocol document.# noqa
    node_type: NodeType
    # Description is missing from the devtools protocol document.# noqa
    number_of_inputs: float
    # Description is missing from the devtools protocol document.# noqa
    number_of_outputs: float
    # Description is missing from the devtools protocol document.# noqa
    channel_count: float
    # Description is missing from the devtools protocol document.# noqa
    channel_count_mode: ChannelCountMode
    # Description is missing from the devtools protocol document.# noqa
    channel_interpretation: ChannelInterpretation


@dataclass
class AudioParam:
    """Protocol object for AudioParam."""

    # Description is missing from the devtools protocol document.# noqa
    param_id: GraphObjectId
    # Description is missing from the devtools protocol document.# noqa
    node_id: GraphObjectId
    # Description is missing from the devtools protocol document.# noqa
    context_id: GraphObjectId
    # Description is missing from the devtools protocol document.# noqa
    param_type: ParamType
    # Description is missing from the devtools protocol document.# noqa
    rate: AutomationRate
    # Description is missing from the devtools protocol document.# noqa
    default_value: float
    # Description is missing from the devtools protocol document.# noqa
    min_value: float
    # Description is missing from the devtools protocol document.# noqa
    max_value: float


@dataclass
@memoize_event("WebAudio.contextCreated")
class ContextCreated:
    """Notifies that a new BaseAudioContext has been created."""

    context: BaseAudioContext


@dataclass
@memoize_event("WebAudio.contextWillBeDestroyed")
class ContextWillBeDestroyed:
    """Notifies that an existing BaseAudioContext will be destroyed."""

    context_id: GraphObjectId


@dataclass
@memoize_event("WebAudio.contextChanged")
class ContextChanged:
    """Notifies that existing BaseAudioContext has changed some properties (id stays the same).."""

    context: BaseAudioContext


@dataclass
@memoize_event("WebAudio.audioListenerCreated")
class AudioListenerCreated:
    """Notifies that the construction of an AudioListener has finished."""

    listener: AudioListener


@dataclass
@memoize_event("WebAudio.audioListenerWillBeDestroyed")
class AudioListenerWillBeDestroyed:
    """Notifies that a new AudioListener has been created."""

    context_id: GraphObjectId
    listener_id: GraphObjectId


@dataclass
@memoize_event("WebAudio.audioNodeCreated")
class AudioNodeCreated:
    """Notifies that a new AudioNode has been created."""

    node: AudioNode


@dataclass
@memoize_event("WebAudio.audioNodeWillBeDestroyed")
class AudioNodeWillBeDestroyed:
    """Notifies that an existing AudioNode has been destroyed."""

    context_id: GraphObjectId
    node_id: GraphObjectId


@dataclass
@memoize_event("WebAudio.audioParamCreated")
class AudioParamCreated:
    """Notifies that a new AudioParam has been created."""

    param: AudioParam


@dataclass
@memoize_event("WebAudio.audioParamWillBeDestroyed")
class AudioParamWillBeDestroyed:
    """Notifies that an existing AudioParam has been destroyed."""

    context_id: GraphObjectId
    node_id: GraphObjectId
    param_id: GraphObjectId


@dataclass
@memoize_event("WebAudio.nodesConnected")
class NodesConnected:
    """Notifies that two AudioNodes are connected."""

    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: typing.Optional[float]
    destination_input_index: typing.Optional[float]


@dataclass
@memoize_event("WebAudio.nodesDisconnected")
class NodesDisconnected:
    """Notifies that AudioNodes are disconnected.

    The destination can be null, and it means all the outgoing connections from the source are disconnected.
    """

    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: typing.Optional[float]
    destination_input_index: typing.Optional[float]


@dataclass
@memoize_event("WebAudio.nodeParamConnected")
class NodeParamConnected:
    """Notifies that an AudioNode is connected to an AudioParam."""

    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: typing.Optional[float]


@dataclass
@memoize_event("WebAudio.nodeParamDisconnected")
class NodeParamDisconnected:
    """Notifies that an AudioNode is disconnected to an AudioParam."""

    context_id: GraphObjectId
    source_id: GraphObjectId
    destination_id: GraphObjectId
    source_output_index: typing.Optional[float]


async def enable() -> None:
    """Enables the WebAudio domain and starts sending context lifetime events.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables the WebAudio domain.

    # noqa
    """
    ...


async def get_realtime_data() -> None:
    """Fetch the realtime data from the registered contexts.

    # noqa
    """
    ...
