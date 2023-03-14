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

import typing
from dataclasses import dataclass

from . import dom


@dataclass
class Animation:
    """Animation instance."""

    #: `Animation`'s id.# noqa
    id: str
    #: `Animation`'s name.# noqa
    name: str
    #: `Animation`'s internal paused state.# noqa
    pausedState: bool
    #: `Animation`'s play state.# noqa
    playState: str
    #: `Animation`'s playback rate.# noqa
    playbackRate: float
    #: `Animation`'s start time.# noqa
    startTime: float
    #: `Animation`'s current time.# noqa
    currentTime: float
    #: Animation type of `Animation`.# noqa
    type: str
    #: `Animation`'s source animation node.# noqa
    source: typing.Optional[AnimationEffect] = None
    #: A unique ID for `Animation` representing the sources that triggered thisCSS animation/transition.# noqa
    cssId: typing.Optional[str] = None


@dataclass
class AnimationEffect:
    """AnimationEffect instance."""

    #: `AnimationEffect`'s delay.# noqa
    delay: float
    #: `AnimationEffect`'s end delay.# noqa
    endDelay: float
    #: `AnimationEffect`'s iteration start.# noqa
    iterationStart: float
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
    backendNodeId: typing.Optional[dom.BackendNodeId] = None
    #: `AnimationEffect`'s keyframes.# noqa
    keyframesRule: typing.Optional[KeyframesRule] = None


@dataclass
class KeyframesRule:
    """Keyframes Rule."""

    #: List of animation keyframes.# noqa
    keyframes: KeyframeStyle
    #: CSS keyframed animation's name.# noqa
    name: typing.Optional[str] = None


@dataclass
class KeyframeStyle:
    """Keyframe Style."""

    #: Keyframe's time offset.# noqa
    offset: str
    #: `AnimationEffect`'s timing function.# noqa
    easing: str
