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

from dataclasses import dataclass


class RequestId(str):
    """Device request id."""

    def to_json(self) -> RequestId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class DeviceId(str):
    """A device id."""

    def to_json(self) -> DeviceId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class PromptDevice:
    """Device information displayed in a user prompt to select a device."""

    #: Description is missing from the devtools protocol document.# noqa
    id: str
    #: Display name as it appears in a device request user prompt.# noqa
    name: str
