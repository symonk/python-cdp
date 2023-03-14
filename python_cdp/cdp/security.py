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

from dataclasses import dataclass


@dataclass
class CertificateId:
    """An internal certificate ID value."""

    ...


class MixedContentType(str):
    """A description of mixed content (HTTP resources on HTTPS pages), as
    defined by https://www.w3.org/TR/mixed-content/#categories."""

    def to_json(self) -> str:
        return self


class SecurityState(str):
    """The security level of a page or resource."""

    def to_json(self) -> str:
        return self


@dataclass
class CertificateSecurityState:
    """Details about the security state of the page certificate."""

    ...


class SafetyTipStatus(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


@dataclass
class SafetyTipInfo:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class VisibleSecurityState:
    """Security state information about the page."""

    ...


@dataclass
class SecurityStateExplanation:
    """An explanation of an factor contributing to the security state."""

    ...


@dataclass
class InsecureContentStatus:
    """Information about insecure content on the page."""

    ...


class CertificateErrorAction(str):
    """The action to take when a certificate error occurs.

    continue will continue processing the request and cancel will cancel
    the request.
    """

    def to_json(self) -> str:
        return self
