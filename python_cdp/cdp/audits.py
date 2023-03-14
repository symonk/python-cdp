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


@dataclass
class AffectedRequest:
    """Information about a request that is affected by an inspector issue."""


@dataclass
class AffectedFrame:
    """Information about the frame affected by an inspector issue."""


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


class CookieOperation(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    SETCOOKIE = "SetCookie"
    READCOOKIE = "ReadCookie"


@dataclass
class CookieIssueDetails:
    """This information is currently necessary, as the front-end has a
    difficult time finding a specific cookie.

    With this, we can convey specific error information without the
    cookie.
    """


class MixedContentResolutionStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    MIXEDCONTENTBLOCKED = "MixedContentBlocked"
    MIXEDCONTENTAUTOMATICALLYUPGRADED = "MixedContentAutomaticallyUpgraded"
    MIXEDCONTENTWARNING = "MixedContentWarning"


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


@dataclass
class MixedContentIssueDetails:
    """Description is missing from the devtools protocol document."""


class BlockedByResponseReason(str, enum.Enum):
    """Enum indicating the reason a response has been blocked.

    These reasons are refinements of the net error BLOCKED_BY_RESPONSE.
    """

    COEPFRAMERESOURCENEEDSCOEPHEADER = "CoepFrameResourceNeedsCoepHeader"
    COOPSANDBOXEDIFRAMECANNOTNAVIGATETOCOOPPAGE = "CoopSandboxedIFrameCannotNavigateToCoopPage"
    CORPNOTSAMEORIGIN = "CorpNotSameOrigin"
    CORPNOTSAMEORIGINAFTERDEFAULTEDTOSAMEORIGINBYCOEP = "CorpNotSameOriginAfterDefaultedToSameOriginByCoep"
    CORPNOTSAMESITE = "CorpNotSameSite"


@dataclass
class BlockedByResponseIssueDetails:
    """Details for a request that has been blocked with the BLOCKED_BY_RESPONSE
    code.

    Currently only used for COEP/COOP, but may be extended to include
    some CSP errors in the future.
    """


class HeavyAdResolutionStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    HEAVYADBLOCKED = "HeavyAdBlocked"
    HEAVYADWARNING = "HeavyAdWarning"


class HeavyAdReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    NETWORKTOTALLIMIT = "NetworkTotalLimit"
    CPUTOTALLIMIT = "CpuTotalLimit"
    CPUPEAKLIMIT = "CpuPeakLimit"


@dataclass
class HeavyAdIssueDetails:
    """Description is missing from the devtools protocol document."""


class ContentSecurityPolicyViolationType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    KINLINEVIOLATION = "kInlineViolation"
    KEVALVIOLATION = "kEvalViolation"
    KURLVIOLATION = "kURLViolation"
    KTRUSTEDTYPESSINKVIOLATION = "kTrustedTypesSinkViolation"
    KTRUSTEDTYPESPOLICYVIOLATION = "kTrustedTypesPolicyViolation"
    KWASMEVALVIOLATION = "kWasmEvalViolation"


@dataclass
class SourceCodeLocation:
    """Description is missing from the devtools protocol document."""


@dataclass
class ContentSecurityPolicyIssueDetails:
    """Description is missing from the devtools protocol document."""


class SharedArrayBufferIssueType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    TRANSFERISSUE = "TransferIssue"
    CREATIONISSUE = "CreationIssue"


@dataclass
class SharedArrayBufferIssueDetails:
    """Details for a issue arising from an SAB being instantiated in, or
    transferred to a context that is not cross-origin isolated."""


class TwaQualityEnforcementViolationType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    KHTTPERROR = "kHttpError"
    KUNAVAILABLEOFFLINE = "kUnavailableOffline"
    KDIGITALASSETLINKS = "kDigitalAssetLinks"


@dataclass
class TrustedWebActivityIssueDetails:
    """Description is missing from the devtools protocol document."""


@dataclass
class LowTextContrastIssueDetails:
    """Description is missing from the devtools protocol document."""


@dataclass
class CorsIssueDetails:
    """Details for a CORS related issue, e.g. a warning or error related to
    CORS RFC1918 enforcement."""


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


@dataclass
class AttributionReportingIssueDetails:
    """Details for issues around "Attribution Reporting API" usage.

    Explainer: https://github.com/WICG/attribution-reporting-api
    """


@dataclass
class QuirksModeIssueDetails:
    """Details for issues about documents in Quirks Mode or Limited Quirks Mode
    that affects page layouting."""


@dataclass
class NavigatorUserAgentIssueDetails:
    """Description is missing from the devtools protocol document."""


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


@dataclass
class GenericIssueDetails:
    """Depending on the concrete errorType, different properties are set."""


@dataclass
class DeprecationIssueDetails:
    """This issue tracks information needed to print a deprecation message.

    https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md
    """


class ClientHintIssueReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    METATAGALLOWLISTINVALIDORIGIN = "MetaTagAllowListInvalidOrigin"
    METATAGMODIFIEDHTML = "MetaTagModifiedHTML"


@dataclass
class FederatedAuthRequestIssueDetails:
    """Description is missing from the devtools protocol document."""


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


@dataclass
class ClientHintIssueDetails:
    """This issue tracks client hints related issues.

    It's used to deprecate old features, encourage the use of new ones,
    and provide general guidance.
    """


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


@dataclass
class InspectorIssueDetails:
    """This struct holds a list of optional fields with additional information
    specific to the kind of issue.

    When adding a new issue code, please also add a new optional field
    to this type.
    """


class IssueId(str):
    """A unique id for a DevTools inspector issue.

    Allows other entities (e.g. exceptions, CDP message, console
    messages, etc.) to reference an issue.
    """

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class InspectorIssue:
    """An inspector issue reported from the back-end."""
