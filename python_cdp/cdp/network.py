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
import typing
from dataclasses import dataclass

from . import runtime
from . import security


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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class LoaderId(str):
    """Unique loader identifier."""

    def to_json(self) -> LoaderId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class RequestId(str):
    """Unique request identifier."""

    def to_json(self) -> RequestId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class InterceptionId(str):
    """Unique intercepted request identifier."""

    def to_json(self) -> InterceptionId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class TimeSinceEpoch(float):
    """UTC time in seconds, counted from January 1, 1970."""

    def to_json(self) -> TimeSinceEpoch:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class MonotonicTime(float):
    """Monotonically increasing time in seconds since an arbitrary point in the
    past."""

    def to_json(self) -> MonotonicTime:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookieSameSite(str, enum.Enum):
    """Represents the cookie's 'SameSite' status:

    https://tools.ietf.org/html/draft-west-first-party-cookies
    """

    STRICT = "Strict"
    LAX = "Lax"
    NONE = "None"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookiePriority(str, enum.Enum):
    """Represents the cookie's 'Priority' status:

    https://tools.ietf.org/html/draft-west-cookie-priority-00
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class ResourceTiming:
    """Timing information for the request."""

    #: Timing's requestTime is a baseline in seconds, while the other numbersare ticks in milliseconds relatively to this requestTime.# noqa
    requestTime: float
    #: Started resolving proxy.# noqa
    proxyStart: float
    #: Finished resolving proxy.# noqa
    proxyEnd: float
    #: Started DNS address resolve.# noqa
    dnsStart: float
    #: Finished DNS address resolve.# noqa
    dnsEnd: float
    #: Started connecting to the remote host.# noqa
    connectStart: float
    #: Connected to the remote host.# noqa
    connectEnd: float
    #: Started SSL handshake.# noqa
    sslStart: float
    #: Finished SSL handshake.# noqa
    sslEnd: float
    #: Started running ServiceWorker.# noqa
    workerStart: float
    #: Finished Starting ServiceWorker.# noqa
    workerReady: float
    #: Started fetch event.# noqa
    workerFetchStart: float
    #: Settled fetch event respondWith promise.# noqa
    workerRespondWithSettled: float
    #: Started sending request.# noqa
    sendStart: float
    #: Finished sending request.# noqa
    sendEnd: float
    #: Time the server started pushing request.# noqa
    pushStart: float
    #: Time the server finished pushing request.# noqa
    pushEnd: float
    #: Finished receiving response headers.# noqa
    receiveHeadersEnd: float


class ResourcePriority(str, enum.Enum):
    """Loading priority of a resource request."""

    VERYLOW = "VeryLow"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    VERYHIGH = "VeryHigh"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class PostDataEntry:
    """Post data entry for HTTP request."""

    #: Description is missing from the devtools protocol document.# noqa
    bytes: typing.Optional[str] = None


@dataclass
class Request:
    """HTTP request data."""

    #: Request URL (without fragment).# noqa
    url: str
    #: Fragment of the requested URL starting with hash, if present.# noqa
    urlFragment: typing.Optional[str] = None
    #: HTTP request method.# noqa
    method: str
    #: HTTP request headers.# noqa
    headers: Headers
    #: HTTP POST request data.# noqa
    postData: typing.Optional[str] = None
    #: True when the request has POST data. Note that postData might still beomitted when this flag is true when the data is too long.# noqa
    hasPostData: typing.Optional[bool] = None
    #: Request body elements. This will be converted from base64 to binary# noqa
    postDataEntries: typing.Optional[PostDataEntry] = None
    #: The mixed content type of the request.# noqa
    mixedContentType: typing.Optional[security.MixedContentType] = None
    #: Priority of the resource request at the time request is sent.# noqa
    initialPriority: ResourcePriority
    #: The referrer policy of the request, as defined inhttps://www.w3.org/TR/referrer-policy/# noqa
    referrerPolicy: str
    #: Whether is loaded via link preload.# noqa
    isLinkPreload: typing.Optional[bool] = None
    #: Set for requests when the TrustToken API is used. Contains the parameterspassed by the developer (e.g. via "fetch") as understood by the backend.# noqa
    trustTokenParams: typing.Optional[TrustTokenParams] = None
    #: True if this resource request is considered to be the 'same site' as therequest correspondinfg to the main frame.# noqa
    isSameSite: typing.Optional[bool] = None


@dataclass
class SignedCertificateTimestamp:
    """Details of a signed certificate timestamp (SCT)."""

    #: Validation status.# noqa
    status: str
    #: Origin.# noqa
    origin: str
    #: Log name / description.# noqa
    logDescription: str
    #: Log ID.# noqa
    logId: str
    #: Issuance date. Unlike TimeSinceEpoch, this contains the number ofmilliseconds since January 1, 1970, UTC, not the number of seconds.# noqa
    timestamp: float
    #: Hash algorithm.# noqa
    hashAlgorithm: str
    #: Signature algorithm.# noqa
    signatureAlgorithm: str
    #: Signature data.# noqa
    signatureData: str


@dataclass
class SecurityDetails:
    """Security details about a request."""

    #: Protocol name (e.g. "TLS 1.2" or "QUIC").# noqa
    protocol: str
    #: Key Exchange used by the connection, or the empty string if notapplicable.# noqa
    keyExchange: str
    #: (EC)DH group used by the connection, if applicable.# noqa
    keyExchangeGroup: typing.Optional[str] = None
    #: Cipher name.# noqa
    cipher: str
    #: TLS MAC. Note that AEAD ciphers do not have separate MACs.# noqa
    mac: typing.Optional[str] = None
    #: Certificate ID value.# noqa
    certificateId: security.CertificateId
    #: Certificate subject name.# noqa
    subjectName: str
    #: Subject Alternative Name (SAN) DNS names and IP addresses.# noqa
    sanList: str
    #: Name of the issuing CA.# noqa
    issuer: str
    #: Certificate valid from date.# noqa
    validFrom: TimeSinceEpoch
    #: Certificate valid to (expiration) date# noqa
    validTo: TimeSinceEpoch
    #: List of signed certificate timestamps (SCTs).# noqa
    signedCertificateTimestampList: SignedCertificateTimestamp
    #: Whether the request complied with Certificate Transparency policy# noqa
    certificateTransparencyCompliance: CertificateTransparencyCompliance
    #: The signature algorithm used by the server in the TLS server signature,represented as a TLS SignatureScheme code point. Omitted if not applicable ornot known.# noqa
    serverSignatureAlgorithm: typing.Optional[int] = None
    #: Whether the connection used Encrypted ClientHello# noqa
    encryptedClientHello: bool


class CertificateTransparencyCompliance(str, enum.Enum):
    """Whether the request complied with Certificate Transparency policy."""

    UNKNOWN = "unknown"
    NOT_COMPLIANT = "not_compliant"
    COMPLIANT = "compliant"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class CorsErrorStatus:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    corsError: CorsError
    #: Description is missing from the devtools protocol document.# noqa
    failedParameter: str


class ServiceWorkerResponseSource(str, enum.Enum):
    """Source of serviceworker response."""

    CACHE_STORAGE = "cache_storage"
    HTTP_CACHE = "http_cache"
    FALLBACK_CODE = "fallback_code"
    NETWORK = "network"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class TrustTokenParams:
    """Determines what type of Trust Token operation is executed and depending
    on the type, some additional parameters.

    The values
    are specified in third_party/blink/renderer/core/fetch/trust_token.idl.
    """

    #: Description is missing from the devtools protocol document.# noqa
    operation: TrustTokenOperationType
    #: Only set for "token-redemption" operation and determine whether torequest a fresh SRR or use a still valid cached SRR.# noqa
    refreshPolicy: str
    #: Origins of issuers from whom to request tokens or redemption records.# noqa
    issuers: typing.Optional[str] = None


class TrustTokenOperationType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    ISSUANCE = "Issuance"
    REDEMPTION = "Redemption"
    SIGNING = "Signing"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class Response:
    """HTTP response data."""

    #: Response URL. This URL can be different from CachedResource.url in caseof redirect.# noqa
    url: str
    #: HTTP response status code.# noqa
    status: int
    #: HTTP response status text.# noqa
    statusText: str
    #: HTTP response headers.# noqa
    headers: Headers
    #: HTTP response headers text. This has been replaced by the headers inNetwork.responseReceivedExtraInfo.# noqa
    headersText: typing.Optional[str] = None
    #: Resource mimeType as determined by the browser.# noqa
    mimeType: str
    #: Refined HTTP request headers that were actually transmitted over thenetwork.# noqa
    requestHeaders: typing.Optional[Headers] = None
    #: HTTP request headers text. This has been replaced by the headers inNetwork.requestWillBeSentExtraInfo.# noqa
    requestHeadersText: typing.Optional[str] = None
    #: Specifies whether physical connection was actually reused for thisrequest.# noqa
    connectionReused: bool
    #: Physical connection id that was actually used for this request.# noqa
    connectionId: float
    #: Remote IP address.# noqa
    remoteIPAddress: typing.Optional[str] = None
    #: Remote port.# noqa
    remotePort: typing.Optional[int] = None
    #: Specifies that the request was served from the disk cache.# noqa
    fromDiskCache: typing.Optional[bool] = None
    #: Specifies that the request was served from the ServiceWorker.# noqa
    fromServiceWorker: typing.Optional[bool] = None
    #: Specifies that the request was served from the prefetch cache.# noqa
    fromPrefetchCache: typing.Optional[bool] = None
    #: Total number of bytes received for this request so far.# noqa
    encodedDataLength: float
    #: Timing information for the given request.# noqa
    timing: typing.Optional[ResourceTiming] = None
    #: Response source of response from ServiceWorker.# noqa
    serviceWorkerResponseSource: typing.Optional[ServiceWorkerResponseSource] = None
    #: The time at which the returned response was generated.# noqa
    responseTime: typing.Optional[TimeSinceEpoch] = None
    #: Cache Storage Cache Name.# noqa
    cacheStorageCacheName: typing.Optional[str] = None
    #: Protocol used to fetch this request.# noqa
    protocol: typing.Optional[str] = None
    #: The reason why Chrome uses a specific transport protocol for HTTPsemantics.# noqa
    alternateProtocolUsage: typing.Optional[AlternateProtocolUsage] = None
    #: Security state of the request resource.# noqa
    securityState: security.SecurityState
    #: Security details for the request.# noqa
    securityDetails: typing.Optional[SecurityDetails] = None


@dataclass
class WebSocketRequest:
    """WebSocket request data."""

    #: HTTP request headers.# noqa
    headers: Headers


@dataclass
class WebSocketResponse:
    """WebSocket response data."""

    #: HTTP response status code.# noqa
    status: int
    #: HTTP response status text.# noqa
    statusText: str
    #: HTTP response headers.# noqa
    headers: Headers
    #: HTTP response headers text.# noqa
    headersText: typing.Optional[str] = None
    #: HTTP request headers.# noqa
    requestHeaders: typing.Optional[Headers] = None
    #: HTTP request headers text.# noqa
    requestHeadersText: typing.Optional[str] = None


@dataclass
class WebSocketFrame:
    """WebSocket message data.

    This represents an entire WebSocket message, not just a fragmented
    frame as the name suggests.
    """

    #: WebSocket message opcode.# noqa
    opcode: float
    #: WebSocket message mask.# noqa
    mask: bool
    #: WebSocket message payload data. If the opcode is 1, this is a textmessage and payloadData is a UTF-8 string. If the opcode isn't 1, thenpayloadData is a base64 encoded string representing binary data.# noqa
    payloadData: str


@dataclass
class CachedResource:
    """Information about the cached resource."""

    #: Resource URL. This is the url of the original network request.# noqa
    url: str
    #: Type of this resource.# noqa
    type: ResourceType
    #: Cached response data.# noqa
    response: typing.Optional[Response] = None
    #: Cached response body size.# noqa
    bodySize: float


@dataclass
class Initiator:
    """Information about the request initiator."""

    #: Type of this initiator.# noqa
    type: str
    #: Initiator JavaScript stack trace, set for Script only.# noqa
    stack: typing.Optional[runtime.StackTrace] = None
    #: Initiator URL, set for Parser type or for Script type (when script isimporting module) or for SignedExchange type.# noqa
    url: typing.Optional[str] = None
    #: Initiator line number, set for Parser type or for Script type (whenscript is importing module) (0-based).# noqa
    lineNumber: typing.Optional[float] = None
    #: Initiator column number, set for Parser type or for Script type (whenscript is importing module) (0-based).# noqa
    columnNumber: typing.Optional[float] = None
    #: Set if another request triggered this request (e.g. preflight).# noqa
    requestId: typing.Optional[RequestId] = None


@dataclass
class Cookie:
    """Cookie object."""

    #: Cookie name.# noqa
    name: str
    #: Cookie value.# noqa
    value: str
    #: Cookie domain.# noqa
    domain: str
    #: Cookie path.# noqa
    path: str
    #: Cookie expiration date as the number of seconds since the UNIX epoch.# noqa
    expires: float
    #: Cookie size.# noqa
    size: int
    #: True if cookie is http-only.# noqa
    httpOnly: bool
    #: True if cookie is secure.# noqa
    secure: bool
    #: True in case of session cookie.# noqa
    session: bool
    #: Cookie SameSite type.# noqa
    sameSite: typing.Optional[CookieSameSite] = None
    #: Cookie Priority# noqa
    priority: CookiePriority
    #: True if cookie is SameParty.# noqa
    sameParty: bool
    #: Cookie source scheme type.# noqa
    sourceScheme: CookieSourceScheme
    #: Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates anunspecified port. An unspecified port value allows protocol clients to emulatelegacy cookie scope for the port. This is a temporary ability and it will beremoved in the future.# noqa
    sourcePort: int
    #: Cookie partition key. The site of the top-level URL the browser wasvisiting at the start of the request to the endpoint that set the cookie.# noqa
    partitionKey: typing.Optional[str] = None
    #: True if cookie partition key is opaque.# noqa
    partitionKeyOpaque: typing.Optional[bool] = None


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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class BlockedSetCookieWithReason:
    """A cookie which was not stored from a response with the corresponding
    reason."""

    #: The reason(s) this cookie was blocked.# noqa
    blockedReasons: SetCookieBlockedReason
    #: The string representing this individual cookie as it would appear in theheader. This is not the entire "cookie" or "set-cookie" header which could havemultiple cookies.# noqa
    cookieLine: str
    #: The cookie object which represents the cookie which was not stored. It isoptional because sometimes complete cookie information is not available, such asin the case of parsing errors.# noqa
    cookie: typing.Optional[Cookie] = None


@dataclass
class BlockedCookieWithReason:
    """A cookie with was not sent with a request with the corresponding
    reason."""

    #: The reason(s) the cookie was blocked.# noqa
    blockedReasons: CookieBlockedReason
    #: The cookie object representing the cookie which was not sent.# noqa
    cookie: Cookie


@dataclass
class CookieParam:
    """Cookie parameter object."""

    #: Cookie name.# noqa
    name: str
    #: Cookie value.# noqa
    value: str
    #: The request-URI to associate with the setting of the cookie. This valuecan affect the default domain, path, source port, and source scheme values ofthe created cookie.# noqa
    url: typing.Optional[str] = None
    #: Cookie domain.# noqa
    domain: typing.Optional[str] = None
    #: Cookie path.# noqa
    path: typing.Optional[str] = None
    #: True if cookie is secure.# noqa
    secure: typing.Optional[bool] = None
    #: True if cookie is http-only.# noqa
    httpOnly: typing.Optional[bool] = None
    #: Cookie SameSite type.# noqa
    sameSite: typing.Optional[CookieSameSite] = None
    #: Cookie expiration date, session cookie if not set# noqa
    expires: typing.Optional[TimeSinceEpoch] = None
    #: Cookie Priority.# noqa
    priority: typing.Optional[CookiePriority] = None
    #: True if cookie is SameParty.# noqa
    sameParty: typing.Optional[bool] = None
    #: Cookie source scheme type.# noqa
    sourceScheme: typing.Optional[CookieSourceScheme] = None
    #: Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates anunspecified port. An unspecified port value allows protocol clients to emulatelegacy cookie scope for the port. This is a temporary ability and it will beremoved in the future.# noqa
    sourcePort: typing.Optional[int] = None
    #: Cookie partition key. The site of the top-level URL the browser wasvisiting at the start of the request to the endpoint that set the cookie. If notset, the cookie will be set as not partitioned.# noqa
    partitionKey: typing.Optional[str] = None


@dataclass
class AuthChallenge:
    """Authorization challenge for HTTP status code 401 or 407."""

    #: Source of the authentication challenge.# noqa
    source: typing.Optional[str] = None
    #: Origin of the challenger.# noqa
    origin: str
    #: The authentication scheme used, such as basic or digest# noqa
    scheme: str
    #: The realm of the challenge. May be empty.# noqa
    realm: str


@dataclass
class AuthChallengeResponse:
    """Response to an AuthChallenge."""

    #: The decision on what to do in response to the authorization challenge.Default means deferring to the default behavior of the net stack, which willlikely either the Cancel authentication or display a popup dialog box.# noqa
    response: str
    #: The username to provide, possibly empty. Should only be set if responseis ProvideCredentials.# noqa
    username: typing.Optional[str] = None
    #: The password to provide, possibly empty. Should only be set if responseis ProvideCredentials.# noqa
    password: typing.Optional[str] = None


class InterceptionStage(str, enum.Enum):
    """Stages of the interception to begin intercepting.

    Request will intercept before the request is sent. Response will
    intercept after the response is received.
    """

    REQUEST = "Request"
    HEADERSRECEIVED = "HeadersReceived"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class RequestPattern:
    """Request pattern for interception."""

    #: Wildcards (`'*'` -> zero or more, `'?'` -> exactly one) are allowed.Escape character is backslash. Omitting is equivalent to `"*"`.# noqa
    urlPattern: typing.Optional[str] = None
    #: If set, only requests for matching resource types will be intercepted.# noqa
    resourceType: typing.Optional[ResourceType] = None
    #: Stage at which to begin intercepting requests. Default is Request.# noqa
    interceptionStage: typing.Optional[InterceptionStage] = None


@dataclass
class SignedExchangeSignature:
    """Information about a signed exchange signature.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1
    """

    #: Signed exchange signature label.# noqa
    label: str
    #: The hex string of signed exchange signature.# noqa
    signature: str
    #: Signed exchange signature integrity.# noqa
    integrity: str
    #: Signed exchange signature cert Url.# noqa
    certUrl: typing.Optional[str] = None
    #: The hex string of signed exchange signature cert sha256.# noqa
    certSha256: typing.Optional[str] = None
    #: Signed exchange signature validity Url.# noqa
    validityUrl: str
    #: Signed exchange signature date.# noqa
    date: int
    #: Signed exchange signature expires.# noqa
    expires: int
    #: The encoded certificates.# noqa
    certificates: typing.Optional[str] = None


@dataclass
class SignedExchangeHeader:
    """Information about a signed exchange header.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    """

    #: Signed exchange request URL.# noqa
    requestUrl: str
    #: Signed exchange response code.# noqa
    responseCode: int
    #: Signed exchange response headers.# noqa
    responseHeaders: Headers
    #: Signed exchange response signature.# noqa
    signatures: SignedExchangeSignature
    #: Signed exchange header integrity hash in the form of"sha256-<base64-hash-value>".# noqa
    headerIntegrity: str


class SignedExchangeErrorField(str, enum.Enum):
    """Field type for a signed exchange related error."""

    SIGNATURESIG = "signatureSig"
    SIGNATUREINTEGRITY = "signatureIntegrity"
    SIGNATURECERTURL = "signatureCertUrl"
    SIGNATURECERTSHA256 = "signatureCertSha256"
    SIGNATUREVALIDITYURL = "signatureValidityUrl"
    SIGNATURETIMESTAMPS = "signatureTimestamps"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SignedExchangeError:
    """Information about a signed exchange response."""

    #: Error message.# noqa
    message: str
    #: The index of the signature which caused the error.# noqa
    signatureIndex: typing.Optional[int] = None
    #: The field which caused the error.# noqa
    errorField: typing.Optional[SignedExchangeErrorField] = None


@dataclass
class SignedExchangeInfo:
    """Information about a signed exchange response."""

    #: The outer response of signed HTTP exchange which was received fromnetwork.# noqa
    outerResponse: Response
    #: Information about the signed exchange header.# noqa
    header: typing.Optional[SignedExchangeHeader] = None
    #: Security details for the signed exchange header.# noqa
    securityDetails: typing.Optional[SecurityDetails] = None
    #: Errors occurred while handling the signed exchagne.# noqa
    errors: typing.Optional[SignedExchangeError] = None


class ContentEncoding(str, enum.Enum):
    """List of content encodings supported by the backend."""

    DEFLATE = "deflate"
    GZIP = "gzip"
    BR = "br"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PrivateNetworkRequestPolicy(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    ALLOW = "Allow"
    BLOCKFROMINSECURETOMOREPRIVATE = "BlockFromInsecureToMorePrivate"
    WARNFROMINSECURETOMOREPRIVATE = "WarnFromInsecureToMorePrivate"
    PREFLIGHTBLOCK = "PreflightBlock"
    PREFLIGHTWARN = "PreflightWarn"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class IPAddressSpace(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    LOCAL = "Local"
    PRIVATE = "Private"
    PUBLIC = "Public"
    UNKNOWN = "Unknown"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class ConnectTiming:
    """Description is missing from the devtools protocol document."""

    #: Timing's requestTime is a baseline in seconds, while the other numbersare ticks in milliseconds relatively to this requestTime. MatchesResourceTiming's requestTime for the same request (but not for redirectedrequests).# noqa
    requestTime: float


@dataclass
class ClientSecurityState:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    initiatorIsSecureContext: bool
    #: Description is missing from the devtools protocol document.# noqa
    initiatorIPAddressSpace: IPAddressSpace
    #: Description is missing from the devtools protocol document.# noqa
    privateNetworkRequestPolicy: PrivateNetworkRequestPolicy


class CrossOriginOpenerPolicyValue(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    SAMEORIGIN = "SameOrigin"
    SAMEORIGINALLOWPOPUPS = "SameOriginAllowPopups"
    RESTRICTPROPERTIES = "RestrictProperties"
    UNSAFENONE = "UnsafeNone"
    SAMEORIGINPLUSCOEP = "SameOriginPlusCoep"
    RESTRICTPROPERTIESPLUSCOEP = "RestrictPropertiesPlusCoep"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class CrossOriginOpenerPolicyStatus:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    value: CrossOriginOpenerPolicyValue
    #: Description is missing from the devtools protocol document.# noqa
    reportOnlyValue: CrossOriginOpenerPolicyValue
    #: Description is missing from the devtools protocol document.# noqa
    reportingEndpoint: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    reportOnlyReportingEndpoint: typing.Optional[str] = None


class CrossOriginEmbedderPolicyValue(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    NONE = "None"
    CREDENTIALLESS = "Credentialless"
    REQUIRECORP = "RequireCorp"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class CrossOriginEmbedderPolicyStatus:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    value: CrossOriginEmbedderPolicyValue
    #: Description is missing from the devtools protocol document.# noqa
    reportOnlyValue: CrossOriginEmbedderPolicyValue
    #: Description is missing from the devtools protocol document.# noqa
    reportingEndpoint: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    reportOnlyReportingEndpoint: typing.Optional[str] = None


@dataclass
class SecurityIsolationStatus:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    coop: typing.Optional[CrossOriginOpenerPolicyStatus] = None
    #: Description is missing from the devtools protocol document.# noqa
    coep: typing.Optional[CrossOriginEmbedderPolicyStatus] = None


class ReportStatus(str, enum.Enum):
    """The status of a Reporting API report."""

    QUEUED = "Queued"
    PENDING = "Pending"
    MARKEDFORREMOVAL = "MarkedForRemoval"
    SUCCESS = "Success"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ReportId(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> ReportId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class ReportingApiReport:
    """An object representing a report generated by the Reporting API."""

    #: Description is missing from the devtools protocol document.# noqa
    id: ReportId
    #: The URL of the document that triggered the report.# noqa
    initiatorUrl: str
    #: The name of the endpoint group that should be used to deliver the report.# noqa
    destination: str
    #: The type of the report (specifies the set of data that is contained inthe report body).# noqa
    type: str
    #: When the report was generated.# noqa
    timestamp: network.TimeSinceEpoch
    #: How many uploads deep the related request was.# noqa
    depth: int
    #: The number of delivery attempts made so far, not including an activeattempt.# noqa
    completedAttempts: int
    #: Description is missing from the devtools protocol document.# noqa
    body: object
    #: Description is missing from the devtools protocol document.# noqa
    status: ReportStatus


@dataclass
class ReportingApiEndpoint:
    """Description is missing from the devtools protocol document."""

    #: The URL of the endpoint to which reports may be delivered.# noqa
    url: str
    #: Name of the endpoint group.# noqa
    groupName: str


@dataclass
class LoadNetworkResourcePageResult:
    """An object providing the result of a network resource load."""

    #: Description is missing from the devtools protocol document.# noqa
    success: bool
    #: Optional values used for error reporting.# noqa
    netError: typing.Optional[float] = None
    #: Description is missing from the devtools protocol document.# noqa
    netErrorName: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    httpStatusCode: typing.Optional[float] = None
    #: If successful, one of the following two fields holds the result.# noqa
    stream: typing.Optional[io.StreamHandle] = None
    #: Response headers.# noqa
    headers: typing.Optional[network.Headers] = None


@dataclass
class LoadNetworkResourceOptions:
    """An options object that may be extended later to better support CORS,
    CORB and streaming."""

    #: Description is missing from the devtools protocol document.# noqa
    disableCache: bool
    #: Description is missing from the devtools protocol document.# noqa
    includeCredentials: bool
