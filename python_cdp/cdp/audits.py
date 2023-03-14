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

import enum
from dataclasses import dataclass


@dataclass
class AffectedCookie:
    """Information about a cookie that is affected by an inspector issue."""

    #: The following three properties uniquely identify a cookie# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    path: str
    #: Description is missing from the devtools protocol document.# noqa
    domain: str


@dataclass
class AffectedRequest:
    """Information about a request that is affected by an inspector issue."""

    #: The unique request id.# noqa
    requestId: str
    #: Description is missing from the devtools protocol document.# noqa
    url: str


@dataclass
class AffectedFrame:
    """Information about the frame affected by an inspector issue."""

    #: Description is missing from the devtools protocol document.# noqa
    frameId: str


class CookieExclusionReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    EXCLUDESAMESITEUNSPECIFIEDTREATEDASLAX = "ExcludeSameSiteUnspecifiedTreatedAsLax"
    EXCLUDESAMESITENONEINSECURE = "ExcludeSameSiteNoneInsecure"
    EXCLUDESAMESITELAX = "ExcludeSameSiteLax"
    EXCLUDESAMESITESTRICT = "ExcludeSameSiteStrict"
    EXCLUDEINVALIDSAMEPARTY = "ExcludeInvalidSameParty"
    EXCLUDESAMEPARTYCROSSPARTYCONTEXT = "ExcludeSamePartyCrossPartyContext"
    EXCLUDEDOMAINNONASCII = "ExcludeDomainNonASCII"
    EXCLUDETHIRDPARTYCOOKIEBLOCKEDINFIRSTPARTYSET = "ExcludeThirdPartyCookieBlockedInFirstPartySet"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookieWarningReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    WARNSAMESITEUNSPECIFIEDCROSSSITECONTEXT = "WarnSameSiteUnspecifiedCrossSiteContext"
    WARNSAMESITENONEINSECURE = "WarnSameSiteNoneInsecure"
    WARNSAMESITEUNSPECIFIEDLAXALLOWUNSAFE = "WarnSameSiteUnspecifiedLaxAllowUnsafe"
    WARNSAMESITESTRICTLAXDOWNGRADESTRICT = "WarnSameSiteStrictLaxDowngradeStrict"
    WARNSAMESITESTRICTCROSSDOWNGRADESTRICT = "WarnSameSiteStrictCrossDowngradeStrict"
    WARNSAMESITESTRICTCROSSDOWNGRADELAX = "WarnSameSiteStrictCrossDowngradeLax"
    WARNSAMESITELAXCROSSDOWNGRADESTRICT = "WarnSameSiteLaxCrossDowngradeStrict"
    WARNSAMESITELAXCROSSDOWNGRADELAX = "WarnSameSiteLaxCrossDowngradeLax"
    WARNATTRIBUTEVALUEEXCEEDSMAXSIZE = "WarnAttributeValueExceedsMaxSize"
    WARNDOMAINNONASCII = "WarnDomainNonASCII"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookieOperation(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    SETCOOKIE = "SetCookie"
    READCOOKIE = "ReadCookie"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class CookieIssueDetails:
    """This information is currently necessary, as the front-end has a
    difficult time finding a specific cookie.

    With this, we can convey specific error information without the
    cookie.
    """

    #: If AffectedCookie is not set then rawCookieLine contains the raw Set-Cookie header string. This hints at a problem where the cookie line issyntactically or semantically malformed in a way that no valid cookie could becreated.# noqa
    cookie: str
    #: Description is missing from the devtools protocol document.# noqa
    rawCookieLine: str
    #: Description is missing from the devtools protocol document.# noqa
    cookieWarningReasons: str
    #: Description is missing from the devtools protocol document.# noqa
    cookieExclusionReasons: str
    #: Optionally identifies the site-for-cookies and the cookie url, which maybe used by the front-end as additional context.# noqa
    operation: str
    #: Description is missing from the devtools protocol document.# noqa
    siteForCookies: str
    #: Description is missing from the devtools protocol document.# noqa
    cookieUrl: str
    #: Description is missing from the devtools protocol document.# noqa
    request: str


class MixedContentResolutionStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    MIXEDCONTENTBLOCKED = "MixedContentBlocked"
    MIXEDCONTENTAUTOMATICALLYUPGRADED = "MixedContentAutomaticallyUpgraded"
    MIXEDCONTENTWARNING = "MixedContentWarning"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class MixedContentResourceType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    ATTRIBUTIONSRC = "AttributionSrc"
    AUDIO = "Audio"
    BEACON = "Beacon"
    CSPREPORT = "CSPReport"
    DOWNLOAD = "Download"
    EVENTSOURCE = "EventSource"
    FAVICON = "Favicon"
    FONT = "Font"
    FORM = "Form"
    FRAME = "Frame"
    IMAGE = "Image"
    IMPORT = "Import"
    MANIFEST = "Manifest"
    PING = "Ping"
    PLUGINDATA = "PluginData"
    PLUGINRESOURCE = "PluginResource"
    PREFETCH = "Prefetch"
    RESOURCE = "Resource"
    SCRIPT = "Script"
    SERVICEWORKER = "ServiceWorker"
    SHAREDWORKER = "SharedWorker"
    STYLESHEET = "Stylesheet"
    TRACK = "Track"
    VIDEO = "Video"
    WORKER = "Worker"
    XMLHTTPREQUEST = "XMLHttpRequest"
    XSLT = "XSLT"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class MixedContentIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: The type of resource causing the mixed content issue (css, js, iframe,form,...). Marked as optional because it is mapped to fromblink::mojom::RequestContextType, which will be replaced bynetwork::mojom::RequestDestination# noqa
    resourceType: str
    #: The way the mixed content issue is being resolved.# noqa
    resolutionStatus: str
    #: The unsafe http url causing the mixed content issue.# noqa
    insecureURL: str
    #: The url responsible for the call to an unsafe url.# noqa
    mainResourceURL: str
    #: The mixed content request. Does not always exist (e.g. for unsafe formsubmission urls).# noqa
    request: str
    #: Optional because not every mixed content issue is necessarily linked to aframe.# noqa
    frame: str


class BlockedByResponseReason(str, enum.Enum):
    """Enum indicating the reason a response has been blocked.

    These reasons are refinements of the net error BLOCKED_BY_RESPONSE.
    """

    COEPFRAMERESOURCENEEDSCOEPHEADER = "CoepFrameResourceNeedsCoepHeader"
    COOPSANDBOXEDIFRAMECANNOTNAVIGATETOCOOPPAGE = "CoopSandboxedIFrameCannotNavigateToCoopPage"
    CORPNOTSAMEORIGIN = "CorpNotSameOrigin"
    CORPNOTSAMEORIGINAFTERDEFAULTEDTOSAMEORIGINBYCOEP = "CorpNotSameOriginAfterDefaultedToSameOriginByCoep"
    CORPNOTSAMESITE = "CorpNotSameSite"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class BlockedByResponseIssueDetails:
    """Details for a request that has been blocked with the BLOCKED_BY_RESPONSE
    code.

    Currently only used for COEP/COOP, but may be extended to include
    some CSP errors in the future.
    """

    #: Description is missing from the devtools protocol document.# noqa
    request: str
    #: Description is missing from the devtools protocol document.# noqa
    parentFrame: str
    #: Description is missing from the devtools protocol document.# noqa
    blockedFrame: str
    #: Description is missing from the devtools protocol document.# noqa
    reason: str


class HeavyAdResolutionStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    HEAVYADBLOCKED = "HeavyAdBlocked"
    HEAVYADWARNING = "HeavyAdWarning"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class HeavyAdReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    NETWORKTOTALLIMIT = "NetworkTotalLimit"
    CPUTOTALLIMIT = "CpuTotalLimit"
    CPUPEAKLIMIT = "CpuPeakLimit"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class HeavyAdIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: The resolution status, either blocking the content or warning.# noqa
    resolution: str
    #: The reason the ad was blocked, total network or cpu or peak cpu.# noqa
    reason: str
    #: The frame that was blocked.# noqa
    frame: str


class ContentSecurityPolicyViolationType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    KINLINEVIOLATION = "kInlineViolation"
    KEVALVIOLATION = "kEvalViolation"
    KURLVIOLATION = "kURLViolation"
    KTRUSTEDTYPESSINKVIOLATION = "kTrustedTypesSinkViolation"
    KTRUSTEDTYPESPOLICYVIOLATION = "kTrustedTypesPolicyViolation"
    KWASMEVALVIOLATION = "kWasmEvalViolation"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SourceCodeLocation:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    scriptId: str
    #: Description is missing from the devtools protocol document.# noqa
    url: str
    #: Description is missing from the devtools protocol document.# noqa
    lineNumber: str
    #: Description is missing from the devtools protocol document.# noqa
    columnNumber: str


@dataclass
class ContentSecurityPolicyIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: The url not included in allowed sources.# noqa
    blockedURL: str
    #: Specific directive that is violated, causing the CSP issue.# noqa
    violatedDirective: str
    #: Description is missing from the devtools protocol document.# noqa
    isReportOnly: str
    #: Description is missing from the devtools protocol document.# noqa
    contentSecurityPolicyViolationType: str
    #: Description is missing from the devtools protocol document.# noqa
    frameAncestor: str
    #: Description is missing from the devtools protocol document.# noqa
    sourceCodeLocation: str
    #: Description is missing from the devtools protocol document.# noqa
    violatingNodeId: str


class SharedArrayBufferIssueType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    TRANSFERISSUE = "TransferIssue"
    CREATIONISSUE = "CreationIssue"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SharedArrayBufferIssueDetails:
    """Details for a issue arising from an SAB being instantiated in, or
    transferred to a context that is not cross-origin isolated."""

    #: Description is missing from the devtools protocol document.# noqa
    sourceCodeLocation: str
    #: Description is missing from the devtools protocol document.# noqa
    isWarning: str
    #: Description is missing from the devtools protocol document.# noqa
    type: str


class TwaQualityEnforcementViolationType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    KHTTPERROR = "kHttpError"
    KUNAVAILABLEOFFLINE = "kUnavailableOffline"
    KDIGITALASSETLINKS = "kDigitalAssetLinks"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class TrustedWebActivityIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: The url that triggers the violation.# noqa
    url: str
    #: Description is missing from the devtools protocol document.# noqa
    violationType: str
    #: Description is missing from the devtools protocol document.# noqa
    httpStatusCode: str
    #: The package name of the Trusted Web Activity client app. This field isonly used when violation type is kDigitalAssetLinks.# noqa
    packageName: str
    #: The signature of the Trusted Web Activity client app. This field is onlyused when violation type is kDigitalAssetLinks.# noqa
    signature: str


@dataclass
class LowTextContrastIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    violatingNodeId: str
    #: Description is missing from the devtools protocol document.# noqa
    violatingNodeSelector: str
    #: Description is missing from the devtools protocol document.# noqa
    contrastRatio: str
    #: Description is missing from the devtools protocol document.# noqa
    thresholdAA: str
    #: Description is missing from the devtools protocol document.# noqa
    thresholdAAA: str
    #: Description is missing from the devtools protocol document.# noqa
    fontSize: str
    #: Description is missing from the devtools protocol document.# noqa
    fontWeight: str


@dataclass
class CorsIssueDetails:
    """Details for a CORS related issue, e.g. a warning or error related to
    CORS RFC1918 enforcement."""

    #: Description is missing from the devtools protocol document.# noqa
    corsErrorStatus: str
    #: Description is missing from the devtools protocol document.# noqa
    isWarning: str
    #: Description is missing from the devtools protocol document.# noqa
    request: str
    #: Description is missing from the devtools protocol document.# noqa
    location: str
    #: Description is missing from the devtools protocol document.# noqa
    initiatorOrigin: str
    #: Description is missing from the devtools protocol document.# noqa
    resourceIPAddressSpace: str
    #: Description is missing from the devtools protocol document.# noqa
    clientSecurityState: str


class AttributionReportingIssueType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    PERMISSIONPOLICYDISABLED = "PermissionPolicyDisabled"
    UNTRUSTWORTHYREPORTINGORIGIN = "UntrustworthyReportingOrigin"
    INSECURECONTEXT = "InsecureContext"
    INVALIDHEADER = "InvalidHeader"
    INVALIDREGISTERTRIGGERHEADER = "InvalidRegisterTriggerHeader"
    INVALIDELIGIBLEHEADER = "InvalidEligibleHeader"
    TOOMANYCONCURRENTREQUESTS = "TooManyConcurrentRequests"
    SOURCEANDTRIGGERHEADERS = "SourceAndTriggerHeaders"
    SOURCEIGNORED = "SourceIgnored"
    TRIGGERIGNORED = "TriggerIgnored"
    OSSOURCEIGNORED = "OsSourceIgnored"
    OSTRIGGERIGNORED = "OsTriggerIgnored"
    INVALIDREGISTEROSSOURCEHEADER = "InvalidRegisterOsSourceHeader"
    INVALIDREGISTEROSTRIGGERHEADER = "InvalidRegisterOsTriggerHeader"
    WEBANDOSHEADERS = "WebAndOsHeaders"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class AttributionReportingIssueDetails:
    """Details for issues around "Attribution Reporting API" usage.

    Explainer: https://github.com/WICG/attribution-reporting-api
    """

    #: Description is missing from the devtools protocol document.# noqa
    violationType: str
    #: Description is missing from the devtools protocol document.# noqa
    request: str
    #: Description is missing from the devtools protocol document.# noqa
    violatingNodeId: str
    #: Description is missing from the devtools protocol document.# noqa
    invalidParameter: str


@dataclass
class QuirksModeIssueDetails:
    """Details for issues about documents in Quirks Mode or Limited Quirks Mode
    that affects page layouting."""

    #: If false, it means the document's mode is "quirks" instead of "limited-quirks".# noqa
    isLimitedQuirksMode: str
    #: Description is missing from the devtools protocol document.# noqa
    documentNodeId: str
    #: Description is missing from the devtools protocol document.# noqa
    url: str
    #: Description is missing from the devtools protocol document.# noqa
    frameId: str
    #: Description is missing from the devtools protocol document.# noqa
    loaderId: str


@dataclass
class NavigatorUserAgentIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    url: str
    #: Description is missing from the devtools protocol document.# noqa
    location: str


class GenericIssueErrorType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    CROSSORIGINPORTALPOSTMESSAGEERROR = "CrossOriginPortalPostMessageError"
    FORMLABELFORNAMEERROR = "FormLabelForNameError"
    FORMDUPLICATEIDFORINPUTERROR = "FormDuplicateIdForInputError"
    FORMINPUTWITHNOLABELERROR = "FormInputWithNoLabelError"
    FORMAUTOCOMPLETEATTRIBUTEEMPTYERROR = "FormAutocompleteAttributeEmptyError"
    FORMEMPTYIDANDNAMEATTRIBUTESFORINPUTERROR = "FormEmptyIdAndNameAttributesForInputError"
    FORMARIALABELLEDBYTONONEXISTINGID = "FormAriaLabelledByToNonExistingId"
    FORMINPUTASSIGNEDAUTOCOMPLETEVALUETOIDORNAMEATTRIBUTEERROR = (
        "FormInputAssignedAutocompleteValueToIdOrNameAttributeError"
    )
    FORMLABELHASNEITHERFORNORNESTEDINPUT = "FormLabelHasNeitherForNorNestedInput"
    FORMLABELFORMATCHESNONEXISTINGIDERROR = "FormLabelForMatchesNonExistingIdError"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class GenericIssueDetails:
    """Depending on the concrete errorType, different properties are set."""

    #: Issues with the same errorType are aggregated in the frontend.# noqa
    errorType: str
    #: Description is missing from the devtools protocol document.# noqa
    frameId: str
    #: Description is missing from the devtools protocol document.# noqa
    violatingNodeId: str


@dataclass
class DeprecationIssueDetails:
    """This issue tracks information needed to print a deprecation message.

    https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md
    """

    #: Description is missing from the devtools protocol document.# noqa
    affectedFrame: str
    #: Description is missing from the devtools protocol document.# noqa
    sourceCodeLocation: str
    #: One of the deprecation names fromthird_party/blink/renderer/core/frame/deprecation/deprecation.json5# noqa
    type: str


class ClientHintIssueReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    METATAGALLOWLISTINVALIDORIGIN = "MetaTagAllowListInvalidOrigin"
    METATAGMODIFIEDHTML = "MetaTagModifiedHTML"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class FederatedAuthRequestIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    federatedAuthRequestIssueReason: str


class FederatedAuthRequestIssueReason(str, enum.Enum):
    """Represents the failure reason when a federated authentication reason
    fails.

    Should be updated alongside RequestIdTokenStatus in
    third_party/blink/public/mojom/devtools/inspector_issue.mojom to include
    all cases except for success.
    """

    SHOULDEMBARGO = "ShouldEmbargo"
    TOOMANYREQUESTS = "TooManyRequests"
    WELLKNOWNHTTPNOTFOUND = "WellKnownHttpNotFound"
    WELLKNOWNNORESPONSE = "WellKnownNoResponse"
    WELLKNOWNINVALIDRESPONSE = "WellKnownInvalidResponse"
    WELLKNOWNLISTEMPTY = "WellKnownListEmpty"
    CONFIGNOTINWELLKNOWN = "ConfigNotInWellKnown"
    WELLKNOWNTOOBIG = "WellKnownTooBig"
    CONFIGHTTPNOTFOUND = "ConfigHttpNotFound"
    CONFIGNORESPONSE = "ConfigNoResponse"
    CONFIGINVALIDRESPONSE = "ConfigInvalidResponse"
    CLIENTMETADATAHTTPNOTFOUND = "ClientMetadataHttpNotFound"
    CLIENTMETADATANORESPONSE = "ClientMetadataNoResponse"
    CLIENTMETADATAINVALIDRESPONSE = "ClientMetadataInvalidResponse"
    DISABLEDINSETTINGS = "DisabledInSettings"
    ERRORFETCHINGSIGNIN = "ErrorFetchingSignin"
    INVALIDSIGNINRESPONSE = "InvalidSigninResponse"
    ACCOUNTSHTTPNOTFOUND = "AccountsHttpNotFound"
    ACCOUNTSNORESPONSE = "AccountsNoResponse"
    ACCOUNTSINVALIDRESPONSE = "AccountsInvalidResponse"
    ACCOUNTSLISTEMPTY = "AccountsListEmpty"
    IDTOKENHTTPNOTFOUND = "IdTokenHttpNotFound"
    IDTOKENNORESPONSE = "IdTokenNoResponse"
    IDTOKENINVALIDRESPONSE = "IdTokenInvalidResponse"
    IDTOKENINVALIDREQUEST = "IdTokenInvalidRequest"
    ERRORIDTOKEN = "ErrorIdToken"
    CANCELED = "Canceled"
    RPPAGENOTVISIBLE = "RpPageNotVisible"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class ClientHintIssueDetails:
    """This issue tracks client hints related issues.

    It's used to deprecate old features, encourage the use of new ones,
    and provide general guidance.
    """

    #: Description is missing from the devtools protocol document.# noqa
    sourceCodeLocation: str
    #: Description is missing from the devtools protocol document.# noqa
    clientHintIssueReason: str


class InspectorIssueCode(str, enum.Enum):
    """A unique identifier for the type of issue.

    Each type may use one of the optional fields in
    InspectorIssueDetails to convey more specific information about the
    kind of issue.
    """

    COOKIEISSUE = "CookieIssue"
    MIXEDCONTENTISSUE = "MixedContentIssue"
    BLOCKEDBYRESPONSEISSUE = "BlockedByResponseIssue"
    HEAVYADISSUE = "HeavyAdIssue"
    CONTENTSECURITYPOLICYISSUE = "ContentSecurityPolicyIssue"
    SHAREDARRAYBUFFERISSUE = "SharedArrayBufferIssue"
    TRUSTEDWEBACTIVITYISSUE = "TrustedWebActivityIssue"
    LOWTEXTCONTRASTISSUE = "LowTextContrastIssue"
    CORSISSUE = "CorsIssue"
    ATTRIBUTIONREPORTINGISSUE = "AttributionReportingIssue"
    QUIRKSMODEISSUE = "QuirksModeIssue"
    NAVIGATORUSERAGENTISSUE = "NavigatorUserAgentIssue"
    GENERICISSUE = "GenericIssue"
    DEPRECATIONISSUE = "DeprecationIssue"
    CLIENTHINTISSUE = "ClientHintIssue"
    FEDERATEDAUTHREQUESTISSUE = "FederatedAuthRequestIssue"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class InspectorIssueDetails:
    """This struct holds a list of optional fields with additional information
    specific to the kind of issue.

    When adding a new issue code, please also add a new optional field
    to this type.
    """

    #: Description is missing from the devtools protocol document.# noqa
    cookieIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    mixedContentIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    blockedByResponseIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    heavyAdIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    contentSecurityPolicyIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    sharedArrayBufferIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    twaQualityEnforcementDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    lowTextContrastIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    corsIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    attributionReportingIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    quirksModeIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    navigatorUserAgentIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    genericIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    deprecationIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    clientHintIssueDetails: str
    #: Description is missing from the devtools protocol document.# noqa
    federatedAuthRequestIssueDetails: str


class IssueId(str):
    """A unique id for a DevTools inspector issue.

    Allows other entities (e.g. exceptions, CDP message, console
    messages, etc.) to reference an issue.
    """

    def to_json(self) -> IssueId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class InspectorIssue:
    """An inspector issue reported from the back-end."""

    #: Description is missing from the devtools protocol document.# noqa
    code: str
    #: Description is missing from the devtools protocol document.# noqa
    details: str
    #: A unique id for this issue. May be omitted if no other entity (e.g.exception, CDP message, etc.) is referencing this issue.# noqa
    issueId: str
