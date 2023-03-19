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
import typing
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


@dataclass
class VirtualAuthenticatorOptions:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa
    protocol: AuthenticatorProtocol
    # Description is missing from the devtools protocol document.# noqa
    transport: AuthenticatorTransport
    # Defaults to ctap2_0. Ignored if |protocol| == u2f.# noqa
    ctap2_version: typing.Optional[Ctap2Version]
    # Defaults to false.# noqa
    has_resident_key: typing.Optional[bool]
    # Defaults to false.# noqa
    has_user_verification: typing.Optional[bool]
    # If set to true, the authenticator will support the largeBlob extension.https://w3c.github.io/webauthn#largeBlob Defaults to false.# noqa
    has_large_blob: typing.Optional[bool]
    # If set to true, the authenticator will support the credBlob extension.https://fidoalliance.org/specs/fido-v2.1-rd-20201208/fido-client-to-authenticator-protocol-v2.1-rd-20201208.html#sctn-credBlob-extension Defaults tofalse.# noqa
    has_cred_blob: typing.Optional[bool]
    # If set to true, the authenticator will support the minPinLength extension.https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-20210615.html#sctn-minpinlength-extensionDefaults to false.# noqa
    has_min_pin_length: typing.Optional[bool]
    # If set to true, the authenticator will support the prf extension.https://w3c.github.io/webauthn/#prf-extension Defaults to false.# noqa
    has_prf: typing.Optional[bool]
    # If set to true, tests of user presence will succeed immediately.Otherwise, they will not be resolved. Defaults to true.# noqa
    automatic_presence_simulation: typing.Optional[bool]
    # Sets whether User Verification succeeds or fails for an authenticator.Defaults to false.# noqa
    is_user_verified: typing.Optional[bool]


@dataclass
class Credential:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa
    credential_id: str
    # Description is missing from the devtools protocol document.# noqa
    is_resident_credential: bool
    # The ECDSA P-256 private key in PKCS#8 format. (Encoded as a base64 stringwhen passed over JSON)# noqa
    private_key: str
    # Signature counter. This is incremented by one for each successfulassertion. See https://w3c.github.io/webauthn/#signature-counter# noqa
    sign_count: int
    # Relying Party ID the credential is scoped to. Must be set when adding acredential.# noqa
    rp_id: typing.Optional[str]
    # An opaque byte sequence with a maximum size of 64 bytes mapping thecredential to a specific user. (Encoded as a base64 string when passed overJSON)# noqa
    user_handle: typing.Optional[str]
    # The large blob associated with the credential. Seehttps://w3c.github.io/webauthn/#sctn-large-blob-extension (Encoded as a base64string when passed over JSON)# noqa
    large_blob: typing.Optional[str]


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
