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
    """ Information about a cookie that is affected by an inspector issue. """
    ...

@dataclass
class AffectedRequest:
    """ Information about a request that is affected by an inspector issue. """
    ...

@dataclass
class AffectedFrame:
    """ Information about the frame affected by an inspector issue. """
    ...

class CookieExclusionReason(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
class CookieWarningReason(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
class CookieOperation(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
@dataclass
class CookieIssueDetails:
    """ This information is currently necessary, as the front-end has a difficult
time finding a specific cookie. With this, we can convey specific error
information without the cookie. """
    ...

class MixedContentResolutionStatus(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
class MixedContentResourceType(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
@dataclass
class MixedContentIssueDetails:
    """ Description is missing from the devtools protocol document. """
    ...

class BlockedByResponseReason(str):
    """ Enum indicating the reason a response has been blocked. These reasons are
refinements of the net error BLOCKED_BY_RESPONSE. """

    def to_json(self) -> str:
        return self
    
@dataclass
class BlockedByResponseIssueDetails:
    """ Details for a request that has been blocked with the BLOCKED_BY_RESPONSE
code. Currently only used for COEP/COOP, but may be extended to include
some CSP errors in the future. """
    ...

class HeavyAdResolutionStatus(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
class HeavyAdReason(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
@dataclass
class HeavyAdIssueDetails:
    """ Description is missing from the devtools protocol document. """
    ...

class ContentSecurityPolicyViolationType(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
@dataclass
class SourceCodeLocation:
    """ Description is missing from the devtools protocol document. """
    ...

@dataclass
class ContentSecurityPolicyIssueDetails:
    """ Description is missing from the devtools protocol document. """
    ...

class SharedArrayBufferIssueType(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
@dataclass
class SharedArrayBufferIssueDetails:
    """ Details for a issue arising from an SAB being instantiated in, or
transferred to a context that is not cross-origin isolated. """
    ...

class TwaQualityEnforcementViolationType(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
@dataclass
class TrustedWebActivityIssueDetails:
    """ Description is missing from the devtools protocol document. """
    ...

@dataclass
class LowTextContrastIssueDetails:
    """ Description is missing from the devtools protocol document. """
    ...

@dataclass
class CorsIssueDetails:
    """ Details for a CORS related issue, e.g. a warning or error related to
CORS RFC1918 enforcement. """
    ...

class AttributionReportingIssueType(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
@dataclass
class AttributionReportingIssueDetails:
    """ Details for issues around "Attribution Reporting API" usage.
Explainer: https://github.com/WICG/attribution-reporting-api """
    ...

@dataclass
class QuirksModeIssueDetails:
    """ Details for issues about documents in Quirks Mode
or Limited Quirks Mode that affects page layouting. """
    ...

@dataclass
class NavigatorUserAgentIssueDetails:
    """ Description is missing from the devtools protocol document. """
    ...

class GenericIssueErrorType(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
@dataclass
class GenericIssueDetails:
    """ Depending on the concrete errorType, different properties are set. """
    ...

@dataclass
class DeprecationIssueDetails:
    """ This issue tracks information needed to print a deprecation message.
https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md """
    ...

class ClientHintIssueReason(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
@dataclass
class FederatedAuthRequestIssueDetails:
    """ Description is missing from the devtools protocol document. """
    ...

class FederatedAuthRequestIssueReason(str):
    """ Represents the failure reason when a federated authentication reason fails.
Should be updated alongside RequestIdTokenStatus in
third_party/blink/public/mojom/devtools/inspector_issue.mojom to include
all cases except for success. """

    def to_json(self) -> str:
        return self
    
@dataclass
class ClientHintIssueDetails:
    """ This issue tracks client hints related issues. It's used to deprecate old
features, encourage the use of new ones, and provide general guidance. """
    ...

class InspectorIssueCode(str):
    """ A unique identifier for the type of issue. Each type may use one of the
optional fields in InspectorIssueDetails to convey more specific
information about the kind of issue. """

    def to_json(self) -> str:
        return self
    
@dataclass
class InspectorIssueDetails:
    """ This struct holds a list of optional fields with additional information
specific to the kind of issue. When adding a new issue code, please also
add a new optional field to this type. """
    ...

class IssueId(str):
    """ A unique id for a DevTools inspector issue. Allows other entities (e.g.
exceptions, CDP message, console messages, etc.) to reference an issue. """

    def to_json(self) -> str:
        return self
    
@dataclass
class InspectorIssue:
    """ An inspector issue reported from the back-end. """
    ...
