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

from .utils import memoize_event


class AuthenticatorId(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> AuthenticatorId:
        return self

    @classmethod
    def from_json(cls, value: str) -> AuthenticatorId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class AuthenticatorProtocol(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    U2F = "u2f"
    CTAP2 = "ctap2"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class Ctap2Version(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    CTAP2_0 = "ctap2_0"
    CTAP2_1 = "ctap2_1"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class AuthenticatorTransport(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    USB = "usb"
    NFC = "nfc"
    BLE = "ble"
    CABLE = "cable"
    INTERNAL = "internal"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class VirtualAuthenticatorOptions(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> VirtualAuthenticatorOptions:
        return self

    @classmethod
    def from_json(cls, value: None) -> VirtualAuthenticatorOptions:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Credential(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> Credential:
        return self

    @classmethod
    def from_json(cls, value: None) -> Credential:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("WebAuthn.credentialAdded")
class CredentialAdded:
    """Triggered when a credential is added to an authenticator."""

    authenticator_id: AuthenticatorId
    credential: Credential


@dataclass
@memoize_event("WebAuthn.credentialAsserted")
class CredentialAsserted:
    """Triggered when a credential is used in a webauthn assertion."""

    authenticator_id: AuthenticatorId
    credential: Credential


async def enable() -> None:
    """Enable the WebAuthn domain and start intercepting credential storage and retrieval with a virtual authenticator.

    # noqa
    """
    ...


async def disable() -> None:
    """Disable the WebAuthn domain.

    # noqa
    """
    ...


async def add_virtual_authenticator() -> None:
    """Creates and adds a virtual authenticator.

    # noqa
    """
    ...


async def set_response_override_bits() -> None:
    """Resets parameters isBogusSignature, isBadUV, isBadUP to false if they are not present.

    # noqa
    """
    ...


async def remove_virtual_authenticator() -> None:
    """Removes the given authenticator.

    # noqa
    """
    ...


async def add_credential() -> None:
    """Adds the credential to the specified authenticator.

    # noqa
    """
    ...


async def get_credential() -> None:
    """Returns a single credential stored in the given virtual authenticator that matches the credential ID.

    # noqa
    """
    ...


async def get_credentials() -> None:
    """Returns all the credentials stored in the given virtual authenticator.

    # noqa
    """
    ...


async def remove_credential() -> None:
    """Removes a credential from the authenticator.

    # noqa
    """
    ...


async def clear_credentials() -> None:
    """Clears all the credentials from the specified device.

    # noqa
    """
    ...


async def set_user_verified() -> None:
    """Sets whether User Verification succeeds or fails for an authenticator.

    The default is true. # noqa
    """
    ...


async def set_automatic_presence_simulation() -> None:
    """Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an
    authenticator.

    The default is true. # noqa
    """
    ...
