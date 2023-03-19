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
    id: str
    # `Animation`'s name.# noqa
    name: str
    # `Animation`'s internal paused state.# noqa
    paused_state: bool
    # `Animation`'s play state.# noqa
    play_state: str
    # `Animation`'s playback rate.# noqa
    playback_rate: float
    # `Animation`'s start time.# noqa
    start_time: float
    # `Animation`'s current time.# noqa
    current_time: float
    # Animation type of `Animation`.# noqa
    type: typing.List[typing.Literal["CSSTransition", "CSSAnimation", "WebAnimation"]]
    # `Animation`'s source animation node.# noqa
    source: typing.Optional[AnimationEffect]
    # A unique ID for `Animation` representing the sources that triggered thisCSS animation/transition.# noqa
    css_id: typing.Optional[str]


@dataclass
class AnimationEffect:
    """AnimationEffect instance."""

    # `AnimationEffect`'s delay.# noqa
    delay: float
    # `AnimationEffect`'s end delay.# noqa
    end_delay: float
    # `AnimationEffect`'s iteration start.# noqa
    iteration_start: float
    # `AnimationEffect`'s iterations.# noqa
    iterations: float
    # `AnimationEffect`'s iteration duration.# noqa
    duration: float
    # `AnimationEffect`'s playback direction.# noqa
    direction: str
    # `AnimationEffect`'s fill mode.# noqa
    fill: str
    # `AnimationEffect`'s timing function.# noqa
    easing: str
    # `AnimationEffect`'s target node.# noqa
    backend_node_id: typing.Optional[dom.BackendNodeId]
    # `AnimationEffect`'s keyframes.# noqa
    keyframes_rule: typing.Optional[KeyframesRule]


@dataclass
class KeyframesRule:
    """Keyframes Rule."""

    # List of animation keyframes.# noqa
    keyframes: KeyframeStyle
    # CSS keyframed animation's name.# noqa
    name: typing.Optional[str]


@dataclass
class KeyframeStyle:
    """Keyframe Style."""

    # Keyframe's time offset.# noqa
    offset: str
    # `AnimationEffect`'s timing function.# noqa
    easing: str


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
