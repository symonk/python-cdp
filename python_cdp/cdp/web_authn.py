# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `WebAuthn`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/WebAuthn/

from __future__ import annotations

import enum
from dataclasses import dataclass


class AuthenticatorId(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class AuthenticatorProtocol(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    U2F = "u2f"
    CTAP2 = "ctap2"


class Ctap2Version(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    CTAP2_0 = "ctap2_0"
    CTAP2_1 = "ctap2_1"


class AuthenticatorTransport(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    USB = "usb"
    NFC = "nfc"
    BLE = "ble"
    CABLE = "cable"
    INTERNAL = "internal"


@dataclass
class VirtualAuthenticatorOptions:
    """Description is missing from the devtools protocol document."""


@dataclass
class Credential:
    """Description is missing from the devtools protocol document."""
