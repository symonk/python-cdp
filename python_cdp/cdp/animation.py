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
from .utils import memoize_event


@dataclass
class Animation:
    """Animation instance."""

    # `Animation`'s id.# noqa


str
# `Animation`'s name.# noqa
str
# `Animation`'s internal paused state.# noqa
bool
# `Animation`'s play state.# noqa
str
# `Animation`'s playback rate.# noqa
float
# `Animation`'s start time.# noqa
float
# `Animation`'s current time.# noqa
float
# Animation type of `Animation`.# noqa
str
# `Animation`'s source animation node.# noqa
AnimationEffect
# A unique ID for `Animation` representing the sources that triggered thisCSS animation/transition.# noqa
typing.Optional[str]


@dataclass
class AnimationEffect:
    """AnimationEffect instance."""

    # `AnimationEffect`'s delay.# noqa


float
# `AnimationEffect`'s end delay.# noqa
float
# `AnimationEffect`'s iteration start.# noqa
float
# `AnimationEffect`'s iterations.# noqa
float
# `AnimationEffect`'s iteration duration.# noqa
float
# `AnimationEffect`'s playback direction.# noqa
str
# `AnimationEffect`'s fill mode.# noqa
str
# `AnimationEffect`'s timing function.# noqa
str
# `AnimationEffect`'s target node.# noqa
typing.Optional[dom.BackendNodeId]
# `AnimationEffect`'s keyframes.# noqa
KeyframesRule


@dataclass
class KeyframesRule:
    """Keyframes Rule."""

    # List of animation keyframes.# noqa


typing.List[KeyframeStyle]
# CSS keyframed animation's name.# noqa
typing.Optional[str]


@dataclass
class KeyframeStyle:
    """Keyframe Style."""

    # Keyframe's time offset.# noqa


str
# `AnimationEffect`'s timing function.# noqa
str


@dataclass
@memoize_event("Animation.animationCanceled")
class AnimationCanceled:
    """Event for when an animation has been cancelled."""

    id: str


@dataclass
@memoize_event("Animation.animationCreated")
class AnimationCreated:
    """Event for each animation that has been created."""

    id: str


@dataclass
@memoize_event("Animation.animationStarted")
class AnimationStarted:
    """Event for animation that has been started."""

    animation: Animation


async def disable() -> None:
    """Disables animation domain notifications.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables animation domain notifications.

    # noqa
    """
    ...


async def get_current_time() -> None:
    """Returns the current time of the an animation.

    # noqa
    """
    ...


async def get_playback_rate() -> None:
    """Gets the playback rate of the document timeline.

    # noqa
    """
    ...


async def release_animations() -> None:
    """Releases a set of animations to no longer be manipulated.

    # noqa
    """
    ...


async def resolve_animation() -> None:
    """Gets the remote object of the Animation.

    # noqa
    """
    ...


async def seek_animations() -> None:
    """Seek a set of animations to a particular time within each animation.

    # noqa
    """
    ...


async def set_paused() -> None:
    """Sets the paused state of a set of animations.

    # noqa
    """
    ...


async def set_playback_rate() -> None:
    """Sets the playback rate of the document timeline.

    # noqa
    """
    ...


async def set_timing() -> None:
    """Sets the timing of an animation node.

    # noqa
    """
    ...
