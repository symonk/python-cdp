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

from . import dom
from . import network
from . import page
from . import runtime


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
    request_id: network.RequestId
    #: Description is missing from the devtools protocol document.# noqa
    url: typing.Optional[str] = None


@dataclass
class AffectedFrame:
    """Information about the frame affected by an inspector issue."""

    #: Description is missing from the devtools protocol document.# noqa
    frame_id: page.FrameId


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
    cookie_warning_reasons: CookieWarningReason
    #: Description is missing from the devtools protocol document.# noqa
    cookie_exclusion_reasons: CookieExclusionReason
    #: Optionally identifies the site-for-cookies and the cookie url, which maybe used by the front-end as additional context.# noqa
    operation: CookieOperation
    #: If AffectedCookie is not set then rawCookieLine contains the raw Set-Cookie header string. This hints at a problem where the cookie line issyntactically or semantically malformed in a way that no valid cookie could becreated.# noqa
    cookie: typing.Optional[AffectedCookie] = None
    #: Description is missing from the devtools protocol document.# noqa
    raw_cookie_line: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    site_for_cookies: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    cookie_url: typing.Optional[str] = None
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
    resolution_status: MixedContentResolutionStatus
    #: The unsafe http url causing the mixed content issue.# noqa
    insecure_url: str
    #: The url responsible for the call to an unsafe url.# noqa
    main_resource_url: str
    #: The type of resource causing the mixed content issue (css, js, iframe,form,...). Marked as optional because it is mapped to fromblink::mojom::RequestContextType, which will be replaced bynetwork::mojom::RequestDestination# noqa
    resource_type: typing.Optional[MixedContentResourceType] = None
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
    parent_frame: typing.Optional[AffectedFrame] = None
    #: Description is missing from the devtools protocol document.# noqa
    blocked_frame: typing.Optional[AffectedFrame] = None


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
    line_number: int
    #: Description is missing from the devtools protocol document.# noqa
    column_number: int
    #: Description is missing from the devtools protocol document.# noqa
    script_id: typing.Optional[runtime.ScriptId] = None


@dataclass
class ContentSecurityPolicyIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: Specific directive that is violated, causing the CSP issue.# noqa
    violated_directive: str
    #: Description is missing from the devtools protocol document.# noqa
    is_report_only: bool
    #: Description is missing from the devtools protocol document.# noqa
    content_security_policy_violation_type: ContentSecurityPolicyViolationType
    #: The url not included in allowed sources.# noqa
    blocked_url: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    frame_ancestor: typing.Optional[AffectedFrame] = None
    #: Description is missing from the devtools protocol document.# noqa
    source_code_location: typing.Optional[SourceCodeLocation] = None
    #: Description is missing from the devtools protocol document.# noqa
    violating_node_id: typing.Optional[dom.BackendNodeId] = None


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
    source_code_location: SourceCodeLocation
    #: Description is missing from the devtools protocol document.# noqa
    is_warning: bool
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
    violation_type: TwaQualityEnforcementViolationType
    #: Description is missing from the devtools protocol document.# noqa
    http_status_code: typing.Optional[int] = None
    #: The package name of the Trusted Web Activity client app. This field isonly used when violation type is kDigitalAssetLinks.# noqa
    package_name: typing.Optional[str] = None
    #: The signature of the Trusted Web Activity client app. This field is onlyused when violation type is kDigitalAssetLinks.# noqa
    signature: typing.Optional[str] = None


@dataclass
class LowTextContrastIssueDetails:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    violating_node_id: dom.BackendNodeId
    #: Description is missing from the devtools protocol document.# noqa
    violating_node_selector: str
    #: Description is missing from the devtools protocol document.# noqa
    contrast_ratio: float
    #: Description is missing from the devtools protocol document.# noqa
    threshold_aa: float
    #: Description is missing from the devtools protocol document.# noqa
    threshold_aaa: float
    #: Description is missing from the devtools protocol document.# noqa
    font_size: str
    #: Description is missing from the devtools protocol document.# noqa
    font_weight: str


@dataclass
class CorsIssueDetails:
    """Details for a CORS related issue, e.g. a warning or error related to
    CORS RFC1918 enforcement."""

    #: Description is missing from the devtools protocol document.# noqa
    cors_error_status: network.CorsErrorStatus
    #: Description is missing from the devtools protocol document.# noqa
    is_warning: bool
    #: Description is missing from the devtools protocol document.# noqa
    request: AffectedRequest
    #: Description is missing from the devtools protocol document.# noqa
    location: typing.Optional[SourceCodeLocation] = None
    #: Description is missing from the devtools protocol document.# noqa
    initiator_origin: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    resource_ip_address_space: typing.Optional[network.IPAddressSpace] = None
    #: Description is missing from the devtools protocol document.# noqa
    client_security_state: typing.Optional[network.ClientSecurityState] = None


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
    violation_type: AttributionReportingIssueType
    #: Description is missing from the devtools protocol document.# noqa
    request: typing.Optional[AffectedRequest] = None
    #: Description is missing from the devtools protocol document.# noqa
    violating_node_id: typing.Optional[dom.BackendNodeId] = None
    #: Description is missing from the devtools protocol document.# noqa
    invalid_parameter: typing.Optional[str] = None


@dataclass
class QuirksModeIssueDetails:
    """Details for issues about documents in Quirks Mode or Limited Quirks Mode
    that affects page layouting."""

    #: If false, it means the document's mode is "quirks" instead of "limited-quirks".# noqa
    is_limited_quirks_mode: bool
    #: Description is missing from the devtools protocol document.# noqa
    document_node_id: dom.BackendNodeId
    #: Description is missing from the devtools protocol document.# noqa
    url: str
    #: Description is missing from the devtools protocol document.# noqa
    frame_id: page.FrameId
    #: Description is missing from the devtools protocol document.# noqa
    loader_id: network.LoaderId


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
    error_type: GenericIssueErrorType
    #: Description is missing from the devtools protocol document.# noqa
    frame_id: typing.Optional[page.FrameId] = None
    #: Description is missing from the devtools protocol document.# noqa
    violating_node_id: typing.Optional[dom.BackendNodeId] = None


@dataclass
class DeprecationIssueDetails:
    """This issue tracks information needed to print a deprecation message.

    https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md
    """

    #: Description is missing from the devtools protocol document.# noqa
    source_code_location: SourceCodeLocation
    #: One of the deprecation names fromthird_party/blink/renderer/core/frame/deprecation/deprecation.json5# noqa
    type: str
    #: Description is missing from the devtools protocol document.# noqa
    affected_frame: typing.Optional[AffectedFrame] = None


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
    federated_auth_request_issue_reason: FederatedAuthRequestIssueReason


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
    source_code_location: SourceCodeLocation
    #: Description is missing from the devtools protocol document.# noqa
    client_hint_issue_reason: ClientHintIssueReason


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
    cookie_issue_details: typing.Optional[CookieIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    mixed_content_issue_details: typing.Optional[MixedContentIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    blocked_by_response_issue_details: typing.Optional[BlockedByResponseIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    heavy_ad_issue_details: typing.Optional[HeavyAdIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    content_security_policy_issue_details: typing.Optional[ContentSecurityPolicyIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    shared_array_buffer_issue_details: typing.Optional[SharedArrayBufferIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    twa_quality_enforcement_details: typing.Optional[TrustedWebActivityIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    low_text_contrast_issue_details: typing.Optional[LowTextContrastIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    cors_issue_details: typing.Optional[CorsIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    attribution_reporting_issue_details: typing.Optional[AttributionReportingIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    quirks_mode_issue_details: typing.Optional[QuirksModeIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    navigator_user_agent_issue_details: typing.Optional[NavigatorUserAgentIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    generic_issue_details: typing.Optional[GenericIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    deprecation_issue_details: typing.Optional[DeprecationIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    client_hint_issue_details: typing.Optional[ClientHintIssueDetails] = None
    #: Description is missing from the devtools protocol document.# noqa
    federated_auth_request_issue_details: typing.Optional[FederatedAuthRequestIssueDetails] = None


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
    issue_id: typing.Optional[IssueId] = None
