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


class GraphObjectId(str):
    """An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in
    Web Audio API."""

    def to_json(self) -> str:
        return self


class ContextType(str):
    """Enum of BaseAudioContext types."""

    def to_json(self) -> str:
        return self


class ContextState(str):
    """Enum of AudioContextState from the spec."""

    def to_json(self) -> str:
        return self


class NodeType(str):
    """Enum of AudioNode types."""

    def to_json(self) -> str:
        return self


class ChannelCountMode(str):
    """Enum of AudioNode::ChannelCountMode from the spec."""

    def to_json(self) -> str:
        return self


class ChannelInterpretation(str):
    """Enum of AudioNode::ChannelInterpretation from the spec."""

    def to_json(self) -> str:
        return self


class ParamType(str):
    """Enum of AudioParam types."""

    def to_json(self) -> str:
        return self


class AutomationRate(str):
    """Enum of AudioParam::AutomationRate from the spec."""

    def to_json(self) -> str:
        return self


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
