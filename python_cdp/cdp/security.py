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
from .utils import memoize_event


class CertificateId(int):
    """An internal certificate ID value."""

    def to_json(self) -> CertificateId:
        return self

    @classmethod
    def from_json(cls, value: int) -> CertificateId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class MixedContentType(str, enum.Enum):
    """A description of mixed content (HTTP resources on HTTPS pages), as defined by https://www.w3.org/TR/mixed-
    content/#categories."""

    BLOCKABLE = "blockable"
    OPTIONALLY_BLOCKABLE = "optionally-blockable"
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
    INSECURE_BROKEN = "insecure-broken"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class CertificateSecurityState:
    """Details about the security state of the page certificate."""

    # Protocol name (e.g. "TLS 1.2" or "QUIC").# noqa


str
# Key Exchange used by the connection, or the empty string if notapplicable.# noqa
str
# Cipher name.# noqa
str
# Page certificate.# noqa
typing.List[str]
# Certificate subject name.# noqa
str
# Name of the issuing CA.# noqa
str
# Certificate valid from date.# noqa
network.TimeSinceEpoch
# Certificate valid to (expiration) date# noqa
network.TimeSinceEpoch
# True if the certificate uses a weak signature aglorithm.# noqa
bool
# True if the certificate has a SHA1 signature in the chain.# noqa
bool
# True if modern SSL# noqa
bool
# True if the connection is using an obsolete SSL protocol.# noqa
bool
# True if the connection is using an obsolete SSL key exchange.# noqa
bool
# True if the connection is using an obsolete SSL cipher.# noqa
bool
# True if the connection is using an obsolete SSL signature.# noqa
bool
# (EC)DH group used by the connection, if applicable.# noqa
typing.Optional[str]
# TLS MAC. Note that AEAD ciphers do not have separate MACs.# noqa
typing.Optional[str]
# The highest priority network error code, if the certificate has an error.# noqa
typing.Optional[str]


class SafetyTipStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    BAD_REPUTATION = "bad_reputation"
    LOOKALIKE = "lookalike"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SafetyTipInfo:
    """Description is missing from the devtools protocol document."""

    # Describes whether the page triggers any safety tips or reputationwarnings. Default is unknown.# noqa


SafetyTipStatus
# The URL the safety tip suggested ("Did you mean?"). Only filled in forlookalike matches.# noqa
typing.Optional[str]


@dataclass
class VisibleSecurityState:
    """Security state information about the page."""

    # The security level of the page.# noqa


SecurityState
# Array of security state issues ids.# noqa
typing.List[str]
# Security state details about the page certificate.# noqa
CertificateSecurityState
# The type of Safety Tip triggered on the page. Note that this field will beset even if the Safety Tip UI was not actually shown.# noqa
SafetyTipInfo


@dataclass
class SecurityStateExplanation:
    """An explanation of an factor contributing to the security state."""

    # Security state representing the severity of the factor being explained.# noqa


SecurityState
# Title describing the type of factor.# noqa
str
# Short phrase describing the type of factor.# noqa
str
# Full text explanation of the factor.# noqa
str
# The type of mixed content described by the explanation.# noqa
MixedContentType
# Page certificate.# noqa
typing.List[str]
# Recommendations to fix any issues.# noqa
typing.Optional[typing.List[str]]


@dataclass
class InsecureContentStatus:
    """Information about insecure content on the page."""

    # Always false.# noqa


bool
# Always false.# noqa
bool
# Always false.# noqa
bool
# Always false.# noqa
bool
# Always false.# noqa
bool
# Always set to unknown.# noqa
SecurityState
# Always set to unknown.# noqa
SecurityState


class CertificateErrorAction(str, enum.Enum):
    """The action to take when a certificate error occurs.

    continue will continue processing the request and cancel will cancel the request.
    """

    CONTINUE = "continue"
    CANCEL = "cancel"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
@memoize_event("Security.certificateError")
class CertificateError:
    """There is a certificate error.

    If overriding certificate errors is enabled, then it should be handled with the `handleCertificateError` command.
    Note: this event does not fire if the certificate error has been allowed internally. Only one client per target
    should override certificate errors at the same time.
    """

    event_id: int
    error_type: str
    request_url: str


@dataclass
@memoize_event("Security.visibleSecurityStateChanged")
class VisibleSecurityStateChanged:
    """The security state of the page changed."""

    visible_security_state: VisibleSecurityState


@dataclass
@memoize_event("Security.securityStateChanged")
class SecurityStateChanged:
    """The security state of the page changed.

    No longer being sent.
    """

    security_state: SecurityState
    scheme_is_cryptographic: bool
    explanations: typing.List[SecurityStateExplanation]
    insecure_content_status: InsecureContentStatus
    summary: typing.Optional[str]


async def disable() -> None:
    """Disables tracking security state changes.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables tracking security state changes.

    # noqa
    """
    ...


async def set_ignore_certificate_errors() -> None:
    """Enable/disable whether all certificate errors should be ignored.

    # noqa
    """
    ...


async def handle_certificate_error() -> None:
    """Handles a certificate error that fired a certificateError event.

    # noqa
    """
    ...


async def set_override_certificate_errors() -> None:
    """Enable/disable overriding certificate errors.

    If enabled, all certificate error events need to be handled by the DevTools client and should be answered with
    `handleCertificateError` commands. # noqa
    """
    ...
