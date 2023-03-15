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


class AuthenticatorId(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> AuthenticatorId:
        return self

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

    #: Description is missing from the devtools protocol document.# noqa
    protocol: AuthenticatorProtocol
    #: Description is missing from the devtools protocol document.# noqa
    transport: AuthenticatorTransport
    #: Defaults to ctap2_0. Ignored if |protocol| == u2f.# noqa
    ctap2_version: typing.Optional[Ctap2Version] = None
    #: Defaults to false.# noqa
    has_resident_key: typing.Optional[bool] = None
    #: Defaults to false.# noqa
    has_user_verification: typing.Optional[bool] = None
    #: If set to true, the authenticator will support the largeBlob extension.https://w3c.github.io/webauthn#largeBlob Defaults to false.# noqa
    has_large_blob: typing.Optional[bool] = None
    #: If set to true, the authenticator will support the credBlob extension.https://fidoalliance.org/specs/fido-v2.1-rd-20201208/fido-client-to-authenticator-protocol-v2.1-rd-20201208.html#sctn-credBlob-extension Defaults tofalse.# noqa
    has_cred_blob: typing.Optional[bool] = None
    #: If set to true, the authenticator will support the minPinLengthextension. https://fidoalliance.org/specs/fido-v2.1-ps-20210615/fido-client-to-authenticator-protocol-v2.1-ps-20210615.html#sctn-minpinlength-extensionDefaults to false.# noqa
    has_min_pin_length: typing.Optional[bool] = None
    #: If set to true, the authenticator will support the prf extension.https://w3c.github.io/webauthn/#prf-extension Defaults to false.# noqa
    has_prf: typing.Optional[bool] = None
    #: If set to true, tests of user presence will succeed immediately.Otherwise, they will not be resolved. Defaults to true.# noqa
    automatic_presence_simulation: typing.Optional[bool] = None
    #: Sets whether User Verification succeeds or fails for an authenticator.Defaults to false.# noqa
    is_user_verified: typing.Optional[bool] = None


@dataclass
class Credential:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    credential_id: str
    #: Description is missing from the devtools protocol document.# noqa
    is_resident_credential: bool
    #: The ECDSA P-256 private key in PKCS#8 format. (Encoded as a base64 stringwhen passed over JSON)# noqa
    private_key: str
    #: Signature counter. This is incremented by one for each successfulassertion. See https://w3c.github.io/webauthn/#signature-counter# noqa
    sign_count: int
    #: Relying Party ID the credential is scoped to. Must be set when adding acredential.# noqa
    rp_id: typing.Optional[str] = None
    #: An opaque byte sequence with a maximum size of 64 bytes mapping thecredential to a specific user. (Encoded as a base64 string when passed overJSON)# noqa
    user_handle: typing.Optional[str] = None
    #: The large blob associated with the credential. Seehttps://w3c.github.io/webauthn/#sctn-large-blob-extension (Encoded as a base64string when passed over JSON)# noqa
    large_blob: typing.Optional[str] = None
