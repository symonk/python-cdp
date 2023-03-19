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


class CertificateSecurityState(None):
    """Details about the security state of the page certificate."""

    def to_json(self) -> CertificateSecurityState:
        return self

    @classmethod
    def from_json(cls, value: None) -> CertificateSecurityState:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SafetyTipStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    BAD_REPUTATION = "bad_reputation"
    LOOKALIKE = "lookalike"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class SafetyTipInfo(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> SafetyTipInfo:
        return self

    @classmethod
    def from_json(cls, value: None) -> SafetyTipInfo:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class VisibleSecurityState(None):
    """Security state information about the page."""

    def to_json(self) -> VisibleSecurityState:
        return self

    @classmethod
    def from_json(cls, value: None) -> VisibleSecurityState:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SecurityStateExplanation(None):
    """An explanation of an factor contributing to the security state."""

    def to_json(self) -> SecurityStateExplanation:
        return self

    @classmethod
    def from_json(cls, value: None) -> SecurityStateExplanation:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class InsecureContentStatus(None):
    """Information about insecure content on the page."""

    def to_json(self) -> InsecureContentStatus:
        return self

    @classmethod
    def from_json(cls, value: None) -> InsecureContentStatus:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
