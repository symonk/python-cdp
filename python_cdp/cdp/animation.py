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

from .utils import memoize_event


class Animation(None):
    """Animation instance."""

    def to_json(self) -> Animation:
        return self

    @classmethod
    def from_json(cls, value: None) -> Animation:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class AnimationEffect(None):
    """AnimationEffect instance."""

    def to_json(self) -> AnimationEffect:
        return self

    @classmethod
    def from_json(cls, value: None) -> AnimationEffect:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class KeyframesRule(None):
    """Keyframes Rule."""

    def to_json(self) -> KeyframesRule:
        return self

    @classmethod
    def from_json(cls, value: None) -> KeyframesRule:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class KeyframeStyle(None):
    """Keyframe Style."""

    def to_json(self) -> KeyframeStyle:
        return self

    @classmethod
    def from_json(cls, value: None) -> KeyframeStyle:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
