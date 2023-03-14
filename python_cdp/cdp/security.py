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
from dataclasses import dataclass


@dataclass
class CertificateId:
    """An internal certificate ID value."""


class MixedContentType(str, enum.Enum):
    """A description of mixed content (HTTP resources on HTTPS pages),
    asdefined by https://www.w3.org/TR/mixed-content/#categories."""

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

    #: Protocol name (e.g. "TLS 1.2" or "QUIC").
    protocol: str
    #: Key Exchange used by the connection, or the empty string if notapplicable.
    keyExchange: str
    #: (EC)DH group used by the connection, if applicable.
    keyExchangeGroup: str
    #: Cipher name.
    cipher: str
    #: TLS MAC. Note that AEAD ciphers do not have separate MACs.
    mac: str
    #: Page certificate.
    certificate: str
    #: Certificate subject name.
    subjectName: str
    #: Name of the issuing CA.
    issuer: str
    #: Certificate valid from date.
    validFrom: str
    #: Certificate valid to (expiration) date
    validTo: str
    #: The highest priority network error code, if the certificate has an error.
    certificateNetworkError: str
    #: True if the certificate uses a weak signature aglorithm.
    certificateHasWeakSignature: str
    #: True if the certificate has a SHA1 signature in the chain.
    certificateHasSha1Signature: str
    #: True if modern SSL
    modernSSL: str
    #: True if the connection is using an obsolete SSL protocol.
    obsoleteSslProtocol: str
    #: True if the connection is using an obsolete SSL key exchange.
    obsoleteSslKeyExchange: str
    #: True if the connection is using an obsolete SSL cipher.
    obsoleteSslCipher: str
    #: True if the connection is using an obsolete SSL signature.
    obsoleteSslSignature: str


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

    #: Describes whether the page triggers any safety tips or reputationwarnings. Default is unknown.
    safetyTipStatus: str
    #: The URL the safety tip suggested ("Did you mean?"). Only filled in forlookalike matches.
    safeUrl: str


@dataclass
class VisibleSecurityState:
    """Security state information about the page."""

    #: The security level of the page.
    securityState: str
    #: Security state details about the page certificate.
    certificateSecurityState: str
    #: The type of Safety Tip triggered on the page. Note that this field willbe set even if the Safety Tip UI was not actually shown.
    safetyTipInfo: str
    #: Array of security state issues ids.
    securityStateIssueIds: str


@dataclass
class SecurityStateExplanation:
    """An explanation of an factor contributing to the security state."""

    #: Security state representing the severity of the factor being explained.
    securityState: str
    #: Title describing the type of factor.
    title: str
    #: Short phrase describing the type of factor.
    summary: str
    #: Full text explanation of the factor.
    description: str
    #: The type of mixed content described by the explanation.
    mixedContentType: str
    #: Page certificate.
    certificate: str
    #: Recommendations to fix any issues.
    recommendations: str


@dataclass
class InsecureContentStatus:
    """Information about insecure content on the page."""

    #: Always false.
    ranMixedContent: str
    #: Always false.
    displayedMixedContent: str
    #: Always false.
    containedMixedForm: str
    #: Always false.
    ranContentWithCertErrors: str
    #: Always false.
    displayedContentWithCertErrors: str
    #: Always set to unknown.
    ranInsecureContentStyle: str
    #: Always set to unknown.
    displayedInsecureContentStyle: str


class CertificateErrorAction(str, enum.Enum):
    """The action to take when a certificate error occurs.

    continue willcontinue processing the request and cancel will cancel
    the request.
    """

    CONTINUE = "continue"
    CANCEL = "cancel"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)
