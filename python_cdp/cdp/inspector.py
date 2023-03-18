# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Inspector`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Inspector/

from __future__ import annotations

import typing
from dataclasses import dataclass

from .utils import memoize_event


@dataclass
@memoize_event("Inspector.detached")
class Detached:
    """Fired when remote debugging connection is about to be terminated.

    Contains detach reason.
    """

    reason: typing.Any


@dataclass
@memoize_event("Inspector.targetCrashed")
class TargetCrashed:
    """Fired when debugging target has crashed."""


@dataclass
@memoize_event("Inspector.targetReloadedAfterCrash")
class TargetReloadedAfterCrash:
    """Fired when debugging target has reloaded after crash."""


async def disable() -> None:
    """Disables inspector domain notifications.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables inspector domain notifications.

    # noqa
    """
    ...
