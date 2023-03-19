# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `DeviceAccess`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/DeviceAccess/

from __future__ import annotations

import typing
from dataclasses import dataclass

from .utils import memoize_event


class RequestId(str):
    """Device request id."""

    def to_json(self) -> RequestId:
        return self

    @classmethod
    def from_json(cls, value: str) -> RequestId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class DeviceId(str):
    """A device id."""

    def to_json(self) -> DeviceId:
        return self

    @classmethod
    def from_json(cls, value: str) -> DeviceId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class PromptDevice:
    """Device information displayed in a user prompt to select a device."""

    # Description is missing from the devtools protocol document.# noqa
    id: DeviceId
    # Display name as it appears in a device request user prompt.# noqa
    name: str


@dataclass
@memoize_event("DeviceAccess.deviceRequestPrompted")
class DeviceRequestPrompted:
    """A device request opened a user prompt to select a device.

    Respond with the selectPrompt or cancelPrompt command.
    """

    id: typing.Any
    devices: typing.Any


async def enable() -> None:
    """Enable events in this domain.

    # noqa
    """
    ...


async def disable() -> None:
    """Disable events in this domain.

    # noqa
    """
    ...


async def select_prompt() -> None:
    """Select a device in response to a DeviceAccess.deviceRequestPrompted event.

    # noqa
    """
    ...


async def cancel_prompt() -> None:
    """Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event.

    # noqa
    """
    ...
