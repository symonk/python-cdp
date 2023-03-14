# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Network`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Network/

from __future__ import annotations

import enum
from dataclasses import dataclass


class ResourceType(str, enum.Enum):
    """Resource type as it was perceived by the rendering engine."""

    DOCUMENT = "Document"
    STYLESHEET = "Stylesheet"
    IMAGE = "Image"
    MEDIA = "Media"
    FONT = "Font"
    SCRIPT = "Script"
    TEXTTRACK = "TextTrack"
    XHR = "XHR"
    FETCH = "Fetch"
    PREFETCH = "Prefetch"
    EVENTSOURCE = "EventSource"
    WEBSOCKET = "WebSocket"
    MANIFEST = "Manifest"
    SIGNEDEXCHANGE = "SignedExchange"
    PING = "Ping"
    CSPVIOLATIONREPORT = "CSPViolationReport"
    PREFLIGHT = "Preflight"
    OTHER = "Other"


class LoaderId(str):
    """Unique loader identifier."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class RequestId(str):
    """Unique request identifier."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class InterceptionId(str):
    """Unique intercepted request identifier."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class ErrorReason(str, enum.Enum):
    """Network level fetch failure reason."""

    FAILED = "Failed"
    ABORTED = "Aborted"
    TIMEDOUT = "TimedOut"
    ACCESSDENIED = "AccessDenied"
    CONNECTIONCLOSED = "ConnectionClosed"
    CONNECTIONRESET = "ConnectionReset"
    CONNECTIONREFUSED = "ConnectionRefused"
    CONNECTIONABORTED = "ConnectionAborted"
    CONNECTIONFAILED = "ConnectionFailed"
    NAMENOTRESOLVED = "NameNotResolved"
    INTERNETDISCONNECTED = "InternetDisconnected"
    ADDRESSUNREACHABLE = "AddressUnreachable"
    BLOCKEDBYCLIENT = "BlockedByClient"
    BLOCKEDBYRESPONSE = "BlockedByResponse"


class TimeSinceEpoch(float):
    """UTC time in seconds, counted from January 1, 1970."""

    def to_json(self) -> float:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class MonotonicTime(float):
    """Monotonically increasing time in seconds since an arbitrary point in the
    past."""

    def to_json(self) -> float:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class Headers:
    """Request / response headers as keys / values of JSON object."""


class ConnectionType(str, enum.Enum):
    """The underlying connection technology that the browser is supposedly
    using."""

    NONE = "none"
    CELLULAR2G = "cellular2g"
    CELLULAR3G = "cellular3g"
    CELLULAR4G = "cellular4g"
    BLUETOOTH = "bluetooth"
    ETHERNET = "ethernet"
    WIFI = "wifi"
    WIMAX = "wimax"
    OTHER = "other"


class CookieSameSite(str, enum.Enum):
    """Represents the cookie's 'SameSite' status:

    https://tools.ietf.org/html/draft-west-first-party-cookies
    """

    STRICT = "Strict"
    LAX = "Lax"
    NONE = "None"


class CookiePriority(str, enum.Enum):
    """Represents the cookie's 'Priority' status:

    https://tools.ietf.org/html/draft-west-cookie-priority-00
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class CookieSourceScheme(str, enum.Enum):
    """Represents the source scheme of the origin that originally set the
    cookie.

    A value of "Unset" allows protocol clients to emulate legacy cookie
    scope for the scheme. This is a temporary ability and it will be
    removed in the future.
    """

    UNSET = "Unset"
    NONSECURE = "NonSecure"
    SECURE = "Secure"


@dataclass
class ResourceTiming:
    """Timing information for the request."""


class ResourcePriority(str, enum.Enum):
    """Loading priority of a resource request."""

    VERYLOW = "VeryLow"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    VERYHIGH = "VeryHigh"


@dataclass
class PostDataEntry:
    """Post data entry for HTTP request."""


@dataclass
class Request:
    """HTTP request data."""


@dataclass
class SignedCertificateTimestamp:
    """Details of a signed certificate timestamp (SCT)."""


@dataclass
class SecurityDetails:
    """Security details about a request."""


class CertificateTransparencyCompliance(str, enum.Enum):
    """Whether the request complied with Certificate Transparency policy."""

    UNKNOWN = "unknown"
    NOT_COMPLIANT = "not_compliant"
    COMPLIANT = "compliant"


class BlockedReason(str, enum.Enum):
    """The reason why request was blocked."""

    OTHER = "other"
    CSP = "csp"
    MIXED_CONTENT = "mixed_content"
    ORIGIN = "origin"
    INSPECTOR = "inspector"
    SUBRESOURCE_FILTER = "subresource_filter"
    CONTENT_TYPE = "content_type"
    COEP_FRAME_RESOURCE_NEEDS_COEP_HEADER = "coep_frame_resource_needs_coep_header"
    COOP_SANDBOXED_IFRAME_CANNOT_NAVIGATE_TO_COOP_PAGE = "coop_sandboxed_iframe_cannot_navigate_to_coop_page"
    CORP_NOT_SAME_ORIGIN = "corp_not_same_origin"
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP = (
        "corp_not_same_origin_after_defaulted_to_same_origin_by_coep"
    )
    CORP_NOT_SAME_SITE = "corp_not_same_site"


class CorsError(str, enum.Enum):
    """The reason why request was blocked."""

    DISALLOWEDBYMODE = "DisallowedByMode"
    INVALIDRESPONSE = "InvalidResponse"
    WILDCARDORIGINNOTALLOWED = "WildcardOriginNotAllowed"
    MISSINGALLOWORIGINHEADER = "MissingAllowOriginHeader"
    MULTIPLEALLOWORIGINVALUES = "MultipleAllowOriginValues"
    INVALIDALLOWORIGINVALUE = "InvalidAllowOriginValue"
    ALLOWORIGINMISMATCH = "AllowOriginMismatch"
    INVALIDALLOWCREDENTIALS = "InvalidAllowCredentials"
    CORSDISABLEDSCHEME = "CorsDisabledScheme"
    PREFLIGHTINVALIDSTATUS = "PreflightInvalidStatus"
    PREFLIGHTDISALLOWEDREDIRECT = "PreflightDisallowedRedirect"
    PREFLIGHTWILDCARDORIGINNOTALLOWED = "PreflightWildcardOriginNotAllowed"
    PREFLIGHTMISSINGALLOWORIGINHEADER = "PreflightMissingAllowOriginHeader"
    PREFLIGHTMULTIPLEALLOWORIGINVALUES = "PreflightMultipleAllowOriginValues"
    PREFLIGHTINVALIDALLOWORIGINVALUE = "PreflightInvalidAllowOriginValue"
    PREFLIGHTALLOWORIGINMISMATCH = "PreflightAllowOriginMismatch"
    PREFLIGHTINVALIDALLOWCREDENTIALS = "PreflightInvalidAllowCredentials"
    PREFLIGHTMISSINGALLOWEXTERNAL = "PreflightMissingAllowExternal"
    PREFLIGHTINVALIDALLOWEXTERNAL = "PreflightInvalidAllowExternal"
    PREFLIGHTMISSINGALLOWPRIVATENETWORK = "PreflightMissingAllowPrivateNetwork"
    PREFLIGHTINVALIDALLOWPRIVATENETWORK = "PreflightInvalidAllowPrivateNetwork"
    INVALIDALLOWMETHODSPREFLIGHTRESPONSE = "InvalidAllowMethodsPreflightResponse"
    INVALIDALLOWHEADERSPREFLIGHTRESPONSE = "InvalidAllowHeadersPreflightResponse"
    METHODDISALLOWEDBYPREFLIGHTRESPONSE = "MethodDisallowedByPreflightResponse"
    HEADERDISALLOWEDBYPREFLIGHTRESPONSE = "HeaderDisallowedByPreflightResponse"
    REDIRECTCONTAINSCREDENTIALS = "RedirectContainsCredentials"
    INSECUREPRIVATENETWORK = "InsecurePrivateNetwork"
    INVALIDPRIVATENETWORKACCESS = "InvalidPrivateNetworkAccess"
    UNEXPECTEDPRIVATENETWORKACCESS = "UnexpectedPrivateNetworkAccess"
    NOCORSREDIRECTMODENOTFOLLOW = "NoCorsRedirectModeNotFollow"


@dataclass
class CorsErrorStatus:
    """Description is missing from the devtools protocol document."""


class ServiceWorkerResponseSource(str, enum.Enum):
    """Source of serviceworker response."""

    CACHE_STORAGE = "cache_storage"
    HTTP_CACHE = "http_cache"
    FALLBACK_CODE = "fallback_code"
    NETWORK = "network"


@dataclass
class TrustTokenParams:
    """Determines what type of Trust Token operation is executed and depending
    on the type, some additional parameters.

    The values
    are specified in third_party/blink/renderer/core/fetch/trust_token.idl.
    """


class TrustTokenOperationType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    ISSUANCE = "Issuance"
    REDEMPTION = "Redemption"
    SIGNING = "Signing"


class AlternateProtocolUsage(str, enum.Enum):
    """The reason why Chrome uses a specific transport protocol for HTTP
    semantics."""

    ALTERNATIVEJOBWONWITHOUTRACE = "alternativeJobWonWithoutRace"
    ALTERNATIVEJOBWONRACE = "alternativeJobWonRace"
    MAINJOBWONRACE = "mainJobWonRace"
    MAPPINGMISSING = "mappingMissing"
    BROKEN = "broken"
    DNSALPNH3JOBWONWITHOUTRACE = "dnsAlpnH3JobWonWithoutRace"
    DNSALPNH3JOBWONRACE = "dnsAlpnH3JobWonRace"
    UNSPECIFIEDREASON = "unspecifiedReason"


@dataclass
class Response:
    """HTTP response data."""


@dataclass
class WebSocketRequest:
    """WebSocket request data."""


@dataclass
class WebSocketResponse:
    """WebSocket response data."""


@dataclass
class WebSocketFrame:
    """WebSocket message data.

    This represents an entire WebSocket message, not just a fragmented
    frame as the name suggests.
    """


@dataclass
class CachedResource:
    """Information about the cached resource."""


@dataclass
class Initiator:
    """Information about the request initiator."""


@dataclass
class Cookie:
    """Cookie object."""


class SetCookieBlockedReason(str, enum.Enum):
    """Types of reasons why a cookie may not be stored from a response."""

    SECUREONLY = "SecureOnly"
    SAMESITESTRICT = "SameSiteStrict"
    SAMESITELAX = "SameSiteLax"
    SAMESITEUNSPECIFIEDTREATEDASLAX = "SameSiteUnspecifiedTreatedAsLax"
    SAMESITENONEINSECURE = "SameSiteNoneInsecure"
    USERPREFERENCES = "UserPreferences"
    THIRDPARTYBLOCKEDINFIRSTPARTYSET = "ThirdPartyBlockedInFirstPartySet"
    SYNTAXERROR = "SyntaxError"
    SCHEMENOTSUPPORTED = "SchemeNotSupported"
    OVERWRITESECURE = "OverwriteSecure"
    INVALIDDOMAIN = "InvalidDomain"
    INVALIDPREFIX = "InvalidPrefix"
    UNKNOWNERROR = "UnknownError"
    SCHEMEFULSAMESITESTRICT = "SchemefulSameSiteStrict"
    SCHEMEFULSAMESITELAX = "SchemefulSameSiteLax"
    SCHEMEFULSAMESITEUNSPECIFIEDTREATEDASLAX = "SchemefulSameSiteUnspecifiedTreatedAsLax"
    SAMEPARTYFROMCROSSPARTYCONTEXT = "SamePartyFromCrossPartyContext"
    SAMEPARTYCONFLICTSWITHOTHERATTRIBUTES = "SamePartyConflictsWithOtherAttributes"
    NAMEVALUEPAIREXCEEDSMAXSIZE = "NameValuePairExceedsMaxSize"


class CookieBlockedReason(str, enum.Enum):
    """Types of reasons why a cookie may not be sent with a request."""

    SECUREONLY = "SecureOnly"
    NOTONPATH = "NotOnPath"
    DOMAINMISMATCH = "DomainMismatch"
    SAMESITESTRICT = "SameSiteStrict"
    SAMESITELAX = "SameSiteLax"
    SAMESITEUNSPECIFIEDTREATEDASLAX = "SameSiteUnspecifiedTreatedAsLax"
    SAMESITENONEINSECURE = "SameSiteNoneInsecure"
    USERPREFERENCES = "UserPreferences"
    THIRDPARTYBLOCKEDINFIRSTPARTYSET = "ThirdPartyBlockedInFirstPartySet"
    UNKNOWNERROR = "UnknownError"
    SCHEMEFULSAMESITESTRICT = "SchemefulSameSiteStrict"
    SCHEMEFULSAMESITELAX = "SchemefulSameSiteLax"
    SCHEMEFULSAMESITEUNSPECIFIEDTREATEDASLAX = "SchemefulSameSiteUnspecifiedTreatedAsLax"
    SAMEPARTYFROMCROSSPARTYCONTEXT = "SamePartyFromCrossPartyContext"
    NAMEVALUEPAIREXCEEDSMAXSIZE = "NameValuePairExceedsMaxSize"


@dataclass
class BlockedSetCookieWithReason:
    """A cookie which was not stored from a response with the corresponding
    reason."""


@dataclass
class BlockedCookieWithReason:
    """A cookie with was not sent with a request with the corresponding
    reason."""


@dataclass
class CookieParam:
    """Cookie parameter object."""


@dataclass
class AuthChallenge:
    """Authorization challenge for HTTP status code 401 or 407."""


@dataclass
class AuthChallengeResponse:
    """Response to an AuthChallenge."""


class InterceptionStage(str, enum.Enum):
    """Stages of the interception to begin intercepting.

    Request will intercept before the request is sent. Response will
    intercept after the response is received.
    """

    REQUEST = "Request"
    HEADERSRECEIVED = "HeadersReceived"


@dataclass
class RequestPattern:
    """Request pattern for interception."""


@dataclass
class SignedExchangeSignature:
    """Information about a signed exchange signature.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1
    """


@dataclass
class SignedExchangeHeader:
    """Information about a signed exchange header.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    """


class SignedExchangeErrorField(str, enum.Enum):
    """Field type for a signed exchange related error."""

    SIGNATURESIG = "signatureSig"
    SIGNATUREINTEGRITY = "signatureIntegrity"
    SIGNATURECERTURL = "signatureCertUrl"
    SIGNATURECERTSHA256 = "signatureCertSha256"
    SIGNATUREVALIDITYURL = "signatureValidityUrl"
    SIGNATURETIMESTAMPS = "signatureTimestamps"


@dataclass
class SignedExchangeError:
    """Information about a signed exchange response."""


@dataclass
class SignedExchangeInfo:
    """Information about a signed exchange response."""


class ContentEncoding(str, enum.Enum):
    """List of content encodings supported by the backend."""

    DEFLATE = "deflate"
    GZIP = "gzip"
    BR = "br"


class PrivateNetworkRequestPolicy(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    ALLOW = "Allow"
    BLOCKFROMINSECURETOMOREPRIVATE = "BlockFromInsecureToMorePrivate"
    WARNFROMINSECURETOMOREPRIVATE = "WarnFromInsecureToMorePrivate"
    PREFLIGHTBLOCK = "PreflightBlock"
    PREFLIGHTWARN = "PreflightWarn"


class IPAddressSpace(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    LOCAL = "Local"
    PRIVATE = "Private"
    PUBLIC = "Public"
    UNKNOWN = "Unknown"


@dataclass
class ConnectTiming:
    """Description is missing from the devtools protocol document."""


@dataclass
class ClientSecurityState:
    """Description is missing from the devtools protocol document."""


class CrossOriginOpenerPolicyValue(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    SAMEORIGIN = "SameOrigin"
    SAMEORIGINALLOWPOPUPS = "SameOriginAllowPopups"
    RESTRICTPROPERTIES = "RestrictProperties"
    UNSAFENONE = "UnsafeNone"
    SAMEORIGINPLUSCOEP = "SameOriginPlusCoep"
    RESTRICTPROPERTIESPLUSCOEP = "RestrictPropertiesPlusCoep"


@dataclass
class CrossOriginOpenerPolicyStatus:
    """Description is missing from the devtools protocol document."""


class CrossOriginEmbedderPolicyValue(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    NONE = "None"
    CREDENTIALLESS = "Credentialless"
    REQUIRECORP = "RequireCorp"


@dataclass
class CrossOriginEmbedderPolicyStatus:
    """Description is missing from the devtools protocol document."""


@dataclass
class SecurityIsolationStatus:
    """Description is missing from the devtools protocol document."""


class ReportStatus(str, enum.Enum):
    """The status of a Reporting API report."""

    QUEUED = "Queued"
    PENDING = "Pending"
    MARKEDFORREMOVAL = "MarkedForRemoval"
    SUCCESS = "Success"


class ReportId(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class ReportingApiReport:
    """An object representing a report generated by the Reporting API."""


@dataclass
class ReportingApiEndpoint:
    """Description is missing from the devtools protocol document."""


@dataclass
class LoadNetworkResourcePageResult:
    """An object providing the result of a network resource load."""


@dataclass
class LoadNetworkResourceOptions:
    """An options object that may be extended later to better support CORS,
    CORB and streaming."""
