# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Audits`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Audits/

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AffectedCookie:
    """Information about a cookie that is affected by an inspector issue."""

    ...


@dataclass
class AffectedRequest:
    """Information about a request that is affected by an inspector issue."""

    ...


@dataclass
class AffectedFrame:
    """Information about the frame affected by an inspector issue."""

    ...


@dataclass
class CookieExclusionReason:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class CookieWarningReason:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class CookieOperation:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class CookieIssueDetails:
    """This information is currently necessary, as the front-end has a
    difficult time finding a specific cookie.

    With this, we can convey specific error information without the
    cookie.
    """

    ...


@dataclass
class MixedContentResolutionStatus:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class MixedContentResourceType:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class MixedContentIssueDetails:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class BlockedByResponseReason:
    """Enum indicating the reason a response has been blocked.

    These reasons are refinements of the net error BLOCKED_BY_RESPONSE.
    """

    ...


@dataclass
class BlockedByResponseIssueDetails:
    """Details for a request that has been blocked with the BLOCKED_BY_RESPONSE
    code.

    Currently only used for COEP/COOP, but may be extended to include
    some CSP errors in the future.
    """

    ...


@dataclass
class HeavyAdResolutionStatus:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class HeavyAdReason:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class HeavyAdIssueDetails:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ContentSecurityPolicyViolationType:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class SourceCodeLocation:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ContentSecurityPolicyIssueDetails:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class SharedArrayBufferIssueType:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class SharedArrayBufferIssueDetails:
    """Details for a issue arising from an SAB being instantiated in, or
    transferred to a context that is not cross-origin isolated."""

    ...


@dataclass
class TwaQualityEnforcementViolationType:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class TrustedWebActivityIssueDetails:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class LowTextContrastIssueDetails:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class CorsIssueDetails:
    """Details for a CORS related issue, e.g. a warning or error related to
    CORS RFC1918 enforcement."""

    ...


@dataclass
class AttributionReportingIssueType:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class AttributionReportingIssueDetails:
    """Details for issues around "Attribution Reporting API" usage.

    Explainer: https://github.com/WICG/attribution-reporting-api
    """

    ...


@dataclass
class QuirksModeIssueDetails:
    """Details for issues about documents in Quirks Mode or Limited Quirks Mode
    that affects page layouting."""

    ...


@dataclass
class NavigatorUserAgentIssueDetails:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class GenericIssueErrorType:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class GenericIssueDetails:
    """Depending on the concrete errorType, different properties are set."""

    ...


@dataclass
class DeprecationIssueDetails:
    """This issue tracks information needed to print a deprecation message.

    https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md
    """

    ...


@dataclass
class ClientHintIssueReason:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class FederatedAuthRequestIssueDetails:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class FederatedAuthRequestIssueReason:
    """Represents the failure reason when a federated authentication reason
    fails.

    Should be updated alongside RequestIdTokenStatus in
    third_party/blink/public/mojom/devtools/inspector_issue.mojom to include
    all cases except for success.
    """

    ...


@dataclass
class ClientHintIssueDetails:
    """This issue tracks client hints related issues.

    It's used to deprecate old features, encourage the use of new ones,
    and provide general guidance.
    """

    ...


@dataclass
class InspectorIssueCode:
    """A unique identifier for the type of issue.

    Each type may use one of the optional fields in
    InspectorIssueDetails to convey more specific information about the
    kind of issue.
    """

    ...


@dataclass
class InspectorIssueDetails:
    """This struct holds a list of optional fields with additional information
    specific to the kind of issue.

    When adding a new issue code, please also add a new optional field
    to this type.
    """

    ...


@dataclass
class IssueId:
    """A unique id for a DevTools inspector issue.

    Allows other entities (e.g. exceptions, CDP message, console
    messages, etc.) to reference an issue.
    """

    ...


@dataclass
class InspectorIssue:
    """An inspector issue reported from the back-end."""

    ...
