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

from dataclasses import dataclass


@dataclass
class GraphObjectId:
    """An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in
    Web Audio API."""

    ...


@dataclass
class ContextType:
    """Enum of BaseAudioContext types."""

    ...


@dataclass
class ContextState:
    """Enum of AudioContextState from the spec."""

    ...


@dataclass
class NodeType:
    """Enum of AudioNode types."""

    ...


@dataclass
class ChannelCountMode:
    """Enum of AudioNode::ChannelCountMode from the spec."""

    ...


@dataclass
class ChannelInterpretation:
    """Enum of AudioNode::ChannelInterpretation from the spec."""

    ...


@dataclass
class ParamType:
    """Enum of AudioParam types."""

    ...


@dataclass
class AutomationRate:
    """Enum of AudioParam::AutomationRate from the spec."""

    ...


@dataclass
class ContextRealtimeData:
    """Fields in AudioContext that change in real-time."""

    ...


@dataclass
class BaseAudioContext:
    """Protocol object for BaseAudioContext."""

    ...


@dataclass
class AudioListener:
    """Protocol object for AudioListener."""

    ...


@dataclass
class AudioNode:
    """Protocol object for AudioNode."""

    ...


@dataclass
class AudioParam:
    """Protocol object for AudioParam."""

    ...
