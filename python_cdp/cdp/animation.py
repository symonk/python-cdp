# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Animation`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Animation/

from __future__ import annotations
from dataclasses import dataclass
import typing


from . import dom
from . import runtime


@dataclass
class Animation:
    """ Animation instance. """
    #: `Animation`'s id.# noqa
    id: str
    #: `Animation`'s name.# noqa
    name: str
    #: `Animation`'s internal paused state.# noqa
    paused_state: bool
    #: `Animation`'s play state.# noqa
    play_state: str
    #: `Animation`'s playback rate.# noqa
    playback_rate: float
    #: `Animation`'s start time.# noqa
    start_time: float
    #: `Animation`'s current time.# noqa
    current_time: float
    #: Animation type of `Animation`.# noqa
    type: str
    #: `Animation`'s source animation node.# noqa
    source: typing.Optional[AnimationEffect] = None
    #: A unique ID for `Animation` representing the sources that triggered thisCSS animation/transition.# noqa
    css_id: typing.Optional[str] = None


@dataclass
class AnimationEffect:
    """ AnimationEffect instance """
    #: `AnimationEffect`'s delay.# noqa
    delay: float
    #: `AnimationEffect`'s end delay.# noqa
    end_delay: float
    #: `AnimationEffect`'s iteration start.# noqa
    iteration_start: float
    #: `AnimationEffect`'s iterations.# noqa
    iterations: float
    #: `AnimationEffect`'s iteration duration.# noqa
    duration: float
    #: `AnimationEffect`'s playback direction.# noqa
    direction: str
    #: `AnimationEffect`'s fill mode.# noqa
    fill: str
    #: `AnimationEffect`'s timing function.# noqa
    easing: str
    #: `AnimationEffect`'s target node.# noqa
    backend_node_id: typing.Optional[dom.BackendNodeId] = None
    #: `AnimationEffect`'s keyframes.# noqa
    keyframes_rule: typing.Optional[KeyframesRule] = None


@dataclass
class KeyframesRule:
    """ Keyframes Rule """
    #: List of animation keyframes.# noqa
    keyframes: KeyframeStyle
    #: CSS keyframed animation's name.# noqa
    name: typing.Optional[str] = None


@dataclass
class KeyframeStyle:
    """ Keyframe Style """
    #: Keyframe's time offset.# noqa
    offset: str
    #: `AnimationEffect`'s timing function.# noqa
    easing: str
