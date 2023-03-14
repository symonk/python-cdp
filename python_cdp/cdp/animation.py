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


@dataclass
class Animation:
    """Animation instance."""

    #: `Animation`'s id.# noqa
    id: str
    #: `Animation`'s name.# noqa
    name: str
    #: `Animation`'s internal paused state.# noqa
    pausedState: str
    #: `Animation`'s play state.# noqa
    playState: str
    #: `Animation`'s playback rate.# noqa
    playbackRate: str
    #: `Animation`'s start time.# noqa
    startTime: str
    #: `Animation`'s current time.# noqa
    currentTime: str
    #: Animation type of `Animation`.# noqa
    type: str
    #: `Animation`'s source animation node.# noqa
    source: str
    #: A unique ID for `Animation` representing the sources that triggered thisCSS animation/transition.# noqa
    cssId: str


@dataclass
class AnimationEffect:
    """AnimationEffect instance."""

    #: `AnimationEffect`'s delay.# noqa
    delay: str
    #: `AnimationEffect`'s end delay.# noqa
    endDelay: str
    #: `AnimationEffect`'s iteration start.# noqa
    iterationStart: str
    #: `AnimationEffect`'s iterations.# noqa
    iterations: str
    #: `AnimationEffect`'s iteration duration.# noqa
    duration: str
    #: `AnimationEffect`'s playback direction.# noqa
    direction: str
    #: `AnimationEffect`'s fill mode.# noqa
    fill: str
    #: `AnimationEffect`'s target node.# noqa
    backendNodeId: str
    #: `AnimationEffect`'s keyframes.# noqa
    keyframesRule: str
    #: `AnimationEffect`'s timing function.# noqa
    easing: str


@dataclass
class KeyframesRule:
    """Keyframes Rule."""

    #: CSS keyframed animation's name.# noqa
    name: str
    #: List of animation keyframes.# noqa
    keyframes: str


@dataclass
class KeyframeStyle:
    """Keyframe Style."""

    #: Keyframe's time offset.# noqa
    offset: str
    #: `AnimationEffect`'s timing function.# noqa
    easing: str
