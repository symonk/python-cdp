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
import typing
from dataclasses import dataclass

from . import network


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
    requestId: network.RequestId
    #: Description is missing from the devtools protocol document.# noqa
    url: typing.Optional[str] = None


@dataclass
class AffectedFrame:
    """Information about the frame affected by an inspector issue."""

    #: Description is missing from the devtools protocol document.# noqa
    frameId: page.FrameId


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

    #: Description is missing from the devtools protocol document.# noqa
    cookieWarningReasons: CookieWarningReason
    #: Description is missing from the devtools protocol document.# noqa
    cookieExclusionReasons: CookieExclusionReason
    #: Optionally identifies the site-for-cookies and the cookie url, which maybe used by the front-end as additional context.# noqa
    operation: CookieOperation
    #: If AffectedCookie is not set then rawCookieLine contains the raw Set-Cookie header string. This hints at a problem where the cookie line issyntactically or semantically malformed in a way that no valid cookie could becreated.# noqa
    cookie: typing.Optional[AffectedCookie] = None
    #: Description is missing from the devtools protocol document.# noqa
    rawCookieLine: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    siteForCookies: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    cookieUrl: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    request: typing.Optional[AffectedRequest] = None


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

    #: The way the mixed content issue is being resolved.# noqa
    resolutionStatus: MixedContentResolutionStatus
    #: The unsafe http url causing the mixed content issue.# noqa
    insecureURL: str
    #: The url responsible for the call to an unsafe url.# noqa
    mainResourceURL: str
    #: The type of resource causing the mixed content issue (css, js, iframe,form,...). Marked as optional because it is mapped to fromblink::mojom::RequestContextType, which will be replaced bynetwork::mojom::RequestDestination# noqa
    resourceType: typing.Optional[MixedContentResourceType] = None
    #: The mixed content request. Does not always exist (e.g. for unsafe formsubmission urls).# noqa
    request: typing.Optional[AffectedRequest] = None
    #: Optional because not every mixed content issue is necessarily linked to aframe.# noqa
    frame: typing.Optional[AffectedFrame] = None


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
    request: AffectedRequest
    #: Description is missing from the devtools protocol document.# noqa
    reason: BlockedByResponseReason
    #: Description is missing from the devtools protocol document.# noqa
    parentFrame: typing.Optional[AffectedFrame] = None
    #: Description is missing from the devtools protocol document.# noqa
    blockedFrame: typing.Optional[AffectedFrame] = None


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
    resolution: HeavyAdResolutionStatus
    #: The reason the ad was blocked, total network or cpu or peak cpu.# noqa
    reason: HeavyAdReason
    #: The frame that was blocked.# noqa
    frame: AffectedFrame


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
    url: str
    #: Description is missing from the devtools protocol document.# noqa
    lineNumber: int
    #: Description is missing from the devtools protocol document.# noqa
    columnNumber: int
    #: Description is missing from the devtools protocol document.# noqa
    scriptId: typing.Optional[runtime.ScriptId] = None


@dataclass
class ContentSecurityPolicyIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: Specific directive that is violated, causing the CSP issue.# noqa
    violatedDirective: str
    #: Description is missing from the devtools protocol document.# noqa
    isReportOnly: bool
    #: Description is missing from the devtools protocol document.# noqa
    contentSecurityPolicyViolationType: ContentSecurityPolicyViolationType
    #: The url not included in allowed sources.# noqa
    blockedURL: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    frameAncestor: typing.Optional[AffectedFrame] = None
    #: Description is missing from the devtools protocol document.# noqa
    sourceCodeLocation: typing.Optional[SourceCodeLocation] = None
    #: Description is missing from the devtools protocol document.# noqa
    violatingNodeId: typing.Optional[dom.BackendNodeId] = None


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
    sourceCodeLocation: SourceCodeLocation
    #: Description is missing from the devtools protocol document.# noqa
    isWarning: bool
    #: Description is missing from the devtools protocol document.# noqa
    type: SharedArrayBufferIssueType


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
    violationType: TwaQualityEnforcementViolationType
    #: Description is missing from the devtools protocol document.# noqa
    httpStatusCode: typing.Optional[int] = None
    #: The package name of the Trusted Web Activity client app. This field isonly used when violation type is kDigitalAssetLinks.# noqa
    packageName: typing.Optional[str] = None
    #: The signature of the Trusted Web Activity client app. This field is onlyused when violation type is kDigitalAssetLinks.# noqa
    signature: typing.Optional[str] = None


@dataclass
class LowTextContrastIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    violatingNodeId: dom.BackendNodeId
    #: Description is missing from the devtools protocol document.# noqa
    violatingNodeSelector: str
    #: Description is missing from the devtools protocol document.# noqa
    contrastRatio: float
    #: Description is missing from the devtools protocol document.# noqa
    thresholdAA: float
    #: Description is missing from the devtools protocol document.# noqa
    thresholdAAA: float
    #: Description is missing from the devtools protocol document.# noqa
    fontSize: str
    #: Description is missing from the devtools protocol document.# noqa
    fontWeight: str


@dataclass
class CorsIssueDetails:
    """Details for a CORS related issue, e.g. a warning or error related to
    CORS RFC1918 enforcement."""

    #: Description is missing from the devtools protocol document.# noqa
    corsErrorStatus: network.CorsErrorStatus
    #: Description is missing from the devtools protocol document.# noqa
    isWarning: bool
    #: Description is missing from the devtools protocol document.# noqa
    request: AffectedRequest
    #: Description is missing from the devtools protocol document.# noqa
    location: typing.Optional[SourceCodeLocation] = None
    #: Description is missing from the devtools protocol document.# noqa
    initiatorOrigin: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    resourceIPAddressSpace: typing.Optional[network.IPAddressSpace] = None
    #: Description is missing from the devtools protocol document.# noqa
    clientSecurityState: typing.Optional[network.ClientSecurityState] = None


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
    violationType: AttributionReportingIssueType
    #: Description is missing from the devtools protocol document.# noqa
    request: typing.Optional[AffectedRequest] = None
    #: Description is missing from the devtools protocol document.# noqa
    violatingNodeId: typing.Optional[dom.BackendNodeId] = None
    #: Description is missing from the devtools protocol document.# noqa
    invalidParameter: typing.Optional[str] = None


@dataclass
class QuirksModeIssueDetails:
    """Details for issues about documents in Quirks Mode or Limited Quirks Mode
    that affects page layouting."""

    #: If false, it means the document's mode is "quirks" instead of "limited-quirks".# noqa
    isLimitedQuirksMode: bool
    #: Description is missing from the devtools protocol document.# noqa
    documentNodeId: dom.BackendNodeId
    #: Description is missing from the devtools protocol document.# noqa
    url: str
    #: Description is missing from the devtools protocol document.# noqa
    frameId: page.FrameId
    #: Description is missing from the devtools protocol document.# noqa
    loaderId: network.LoaderId


@dataclass
class NavigatorUserAgentIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    url: str
    #: Description is missing from the devtools protocol document.# noqa
    location: typing.Optional[SourceCodeLocation] = None


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
    errorType: GenericIssueErrorType
    #: Description is missing from the devtools protocol document.# noqa
    frameId: typing.Optional[page.FrameId] = None
    #: Description is missing from the devtools protocol document.# noqa
    violatingNodeId: typing.Optional[dom.BackendNodeId] = None


@dataclass
class DeprecationIssueDetails:
    """This issue tracks information needed to print a deprecation message.

    https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md
    """

    #: Description is missing from the devtools protocol document.# noqa
    sourceCodeLocation: SourceCodeLocation
    #: One of the deprecation names fromthird_party/blink/renderer/core/frame/deprecation/deprecation.json5# noqa
    type: str
    #: Description is missing from the devtools protocol document.# noqa
    affectedFrame: typing.Optional[AffectedFrame] = None


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
    federatedAuthRequestIssueReason: FederatedAuthRequestIssueReason


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
    sourceCodeLocation: SourceCodeLocation
    #: Description is missing from the devtools protocol document.# noqa
    clientHintIssueReason: ClientHintIssueReason


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
    cookieIssueDetails: typing.Optional[CookieIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    mixedContentIssueDetails: typing.Optional[MixedContentIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    blockedByResponseIssueDetails: typing.Optional[BlockedByResponseIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    heavyAdIssueDetails: typing.Optional[HeavyAdIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    contentSecurityPolicyIssueDetails: typing.Optional[ContentSecurityPolicyIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    sharedArrayBufferIssueDetails: typing.Optional[SharedArrayBufferIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    twaQualityEnforcementDetails: typing.Optional[TrustedWebActivityIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    lowTextContrastIssueDetails: typing.Optional[LowTextContrastIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    corsIssueDetails: typing.Optional[CorsIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    attributionReportingIssueDetails: typing.Optional[AttributionReportingIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    quirksModeIssueDetails: typing.Optional[QuirksModeIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    navigatorUserAgentIssueDetails: typing.Optional[NavigatorUserAgentIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    genericIssueDetails: typing.Optional[GenericIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    deprecationIssueDetails: typing.Optional[DeprecationIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    clientHintIssueDetails: typing.Optional[ClientHintIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    federatedAuthRequestIssueDetails: typing.Optional[FederatedAuthRequestIssueDetails] = None


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
    code: InspectorIssueCode
    #: Description is missing from the devtools protocol document.# noqa
    details: InspectorIssueDetails
    #: A unique id for this issue. May be omitted if no other entity (e.g.exception, CDP message, etc.) is referencing this issue.# noqa
    issueId: typing.Optional[IssueId] = None
