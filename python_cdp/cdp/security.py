# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Security`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Security/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import network


@dataclass
class CertificateId:
    """An internal certificate ID value."""


class MixedContentType(str, enum.Enum):
    """A description of mixed content (HTTP resources on HTTPS pages), as
    defined by https://www.w3.org/TR/mixed-content/#categories."""

    BLOCKABLE = "blockable"
    OPTIONALLY_BLOCKABLE = "optionally_blockable"
    NONE = "none"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class SecurityState(str, enum.Enum):
    """The security level of a page or resource."""

    UNKNOWN = "unknown"
    NEUTRAL = "neutral"
    INSECURE = "insecure"
    SECURE = "secure"
    INFO = "info"
    INSECURE_BROKEN = "insecure_broken"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class CertificateSecurityState:
    """Details about the security state of the page certificate."""

    #: Protocol name (e.g. "TLS 1.2" or "QUIC").# noqa
    protocol: str
    #: Key Exchange used by the connection, or the empty string if notapplicable.# noqa
    key_exchange: str
    #: Cipher name.# noqa
    cipher: str
    #: Page certificate.# noqa
    certificate: str
    #: Certificate subject name.# noqa
    subject_name: str
    #: Name of the issuing CA.# noqa
    issuer: str
    #: Certificate valid from date.# noqa
    valid_from: network.TimeSinceEpoch
    #: Certificate valid to (expiration) date# noqa
    valid_to: network.TimeSinceEpoch
    #: True if the certificate uses a weak signature aglorithm.# noqa
    certificate_has_weak_signature: bool
    #: True if the certificate has a SHA1 signature in the chain.# noqa
    certificate_has_sha1_signature: bool
    #: True if modern SSL# noqa
    modern_ssl: bool
    #: True if the connection is using an obsolete SSL protocol.# noqa
    obsolete_ssl_protocol: bool
    #: True if the connection is using an obsolete SSL key exchange.# noqa
    obsolete_ssl_key_exchange: bool
    #: True if the connection is using an obsolete SSL cipher.# noqa
    obsolete_ssl_cipher: bool
    #: True if the connection is using an obsolete SSL signature.# noqa
    obsolete_ssl_signature: bool
    #: (EC)DH group used by the connection, if applicable.# noqa
    key_exchange_group: typing.Optional[str] = None
    #: TLS MAC. Note that AEAD ciphers do not have separate MACs.# noqa
    mac: typing.Optional[str] = None
    #: The highest priority network error code, if the certificate has an error.# noqa
    certificate_network_error: typing.Optional[str] = None


class SafetyTipStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    BADREPUTATION = "badReputation"
    LOOKALIKE = "lookalike"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SafetyTipInfo:
    """Description is missing from the devtools protocol document."""

    #: Describes whether the page triggers any safety tips or reputationwarnings. Default is unknown.# noqa
    safety_tip_status: SafetyTipStatus
    #: The URL the safety tip suggested ("Did you mean?"). Only filled in forlookalike matches.# noqa
    safe_url: typing.Optional[str] = None


@dataclass
class VisibleSecurityState:
    """Security state information about the page."""

    #: The security level of the page.# noqa
    security_state: SecurityState
    #: Array of security state issues ids.# noqa
    security_state_issue_ids: str
    #: Security state details about the page certificate.# noqa
    certificate_security_state: typing.Optional[CertificateSecurityState] = None
    #: The type of Safety Tip triggered on the page. Note that this field willbe set even if the Safety Tip UI was not actually shown.# noqa
    safety_tip_info: typing.Optional[SafetyTipInfo] = None


@dataclass
class SecurityStateExplanation:
    """An explanation of an factor contributing to the security state."""

    #: Security state representing the severity of the factor being explained.# noqa
    security_state: SecurityState
    #: Title describing the type of factor.# noqa
    title: str
    #: Short phrase describing the type of factor.# noqa
    summary: str
    #: Full text explanation of the factor.# noqa
    description: str
    #: The type of mixed content described by the explanation.# noqa
    mixed_content_type: MixedContentType
    #: Page certificate.# noqa
    certificate: str
    #: Recommendations to fix any issues.# noqa
    recommendations: typing.Optional[typing.List[str]] = None


@dataclass
class InsecureContentStatus:
    """Information about insecure content on the page."""

    #: Always false.# noqa
    ran_mixed_content: bool
    #: Always false.# noqa
    displayed_mixed_content: bool
    #: Always false.# noqa
    contained_mixed_form: bool
    #: Always false.# noqa
    ran_content_with_cert_errors: bool
    #: Always false.# noqa
    displayed_content_with_cert_errors: bool
    #: Always set to unknown.# noqa
    ran_insecure_content_style: SecurityState
    #: Always set to unknown.# noqa
    displayed_insecure_content_style: SecurityState


class CertificateErrorAction(str, enum.Enum):
    """The action to take when a certificate error occurs.

    continue will continue processing the request and cancel will cancel
    the request.
    """

    CONTINUE = "continue"
    CANCEL = "cancel"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


def disable() -> None:
    """Disables tracking security state changes.

    # noqa
    """
    ...


def enable() -> None:
    """Enables tracking security state changes.

    # noqa
    """
    ...


def set_ignore_certificate_errors() -> None:
    """Enable/disable whether all certificate errors should be ignored.

    # noqa
    """
    ...


def handle_certificate_error() -> None:
    """Handles a certificate error that fired a certificateError event.

    # noqa
    """
    ...


def set_override_certificate_errors() -> None:
    """Enable/disable overriding certificate errors.

    If enabled, all certificate error events need to be handled by the
    DevTools client and should be answered with `handleCertificateError`
    commands. # noqa
    """
    ...
