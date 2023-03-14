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

    #: `Animation`'s id.
    id: str
    #: `Animation`'s name.
    name: str
    #: `Animation`'s internal paused state.
    pausedState: str
    #: `Animation`'s play state.
    playState: str
    #: `Animation`'s playback rate.
    playbackRate: str
    #: `Animation`'s start time.
    startTime: str
    #: `Animation`'s current time.
    currentTime: str
    #: Animation type of `Animation`.
    type: str
    #: `Animation`'s source animation node.
    source: str
    #: A unique ID for `Animation` representing the sources that triggered thisCSS animation/transition.
    cssId: str


@dataclass
class AnimationEffect:
    """AnimationEffect instance."""

    #: `AnimationEffect`'s delay.
    delay: str
    #: `AnimationEffect`'s end delay.
    endDelay: str
    #: `AnimationEffect`'s iteration start.
    iterationStart: str
    #: `AnimationEffect`'s iterations.
    iterations: str
    #: `AnimationEffect`'s iteration duration.
    duration: str
    #: `AnimationEffect`'s playback direction.
    direction: str
    #: `AnimationEffect`'s fill mode.
    fill: str
    #: `AnimationEffect`'s target node.
    backendNodeId: str
    #: `AnimationEffect`'s keyframes.
    keyframesRule: str
    #: `AnimationEffect`'s timing function.
    easing: str


@dataclass
class KeyframesRule:
    """Keyframes Rule."""

    #: CSS keyframed animation's name.
    name: str
    #: List of animation keyframes.
    keyframes: str


@dataclass
class KeyframeStyle:
    """Keyframe Style."""

    #: Keyframe's time offset.
    offset: str
    #: `AnimationEffect`'s timing function.
    easing: str
