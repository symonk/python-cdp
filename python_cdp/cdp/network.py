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
    requestTime: str
    #: Started resolving proxy.# noqa
    proxyStart: str
    #: Finished resolving proxy.# noqa
    proxyEnd: str
    #: Started DNS address resolve.# noqa
    dnsStart: str
    #: Finished DNS address resolve.# noqa
    dnsEnd: str
    #: Started connecting to the remote host.# noqa
    connectStart: str
    #: Connected to the remote host.# noqa
    connectEnd: str
    #: Started SSL handshake.# noqa
    sslStart: str
    #: Finished SSL handshake.# noqa
    sslEnd: str
    #: Started running ServiceWorker.# noqa
    workerStart: str
    #: Finished Starting ServiceWorker.# noqa
    workerReady: str
    #: Started fetch event.# noqa
    workerFetchStart: str
    #: Settled fetch event respondWith promise.# noqa
    workerRespondWithSettled: str
    #: Started sending request.# noqa
    sendStart: str
    #: Finished sending request.# noqa
    sendEnd: str
    #: Time the server started pushing request.# noqa
    pushStart: str
    #: Time the server finished pushing request.# noqa
    pushEnd: str
    #: Finished receiving response headers.# noqa
    receiveHeadersEnd: str


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
    bytes: str


@dataclass
class Request:
    """HTTP request data."""

    #: Request URL (without fragment).# noqa
    url: str
    #: Fragment of the requested URL starting with hash, if present.# noqa
    urlFragment: str
    #: HTTP request method.# noqa
    method: str
    #: HTTP request headers.# noqa
    headers: str
    #: HTTP POST request data.# noqa
    postData: str
    #: True when the request has POST data. Note that postData might still beomitted when this flag is true when the data is too long.# noqa
    hasPostData: str
    #: Request body elements. This will be converted from base64 to binary# noqa
    postDataEntries: str
    #: The mixed content type of the request.# noqa
    mixedContentType: str
    #: Priority of the resource request at the time request is sent.# noqa
    initialPriority: str
    #: The referrer policy of the request, as defined inhttps://www.w3.org/TR/referrer-policy/# noqa
    referrerPolicy: str
    #: Whether is loaded via link preload.# noqa
    isLinkPreload: str
    #: Set for requests when the TrustToken API is used. Contains the parameterspassed by the developer (e.g. via "fetch") as understood by the backend.# noqa
    trustTokenParams: str
    #: True if this resource request is considered to be the 'same site' as therequest correspondinfg to the main frame.# noqa
    isSameSite: str


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
    timestamp: str
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
    keyExchangeGroup: str
    #: Cipher name.# noqa
    cipher: str
    #: TLS MAC. Note that AEAD ciphers do not have separate MACs.# noqa
    mac: str
    #: Certificate ID value.# noqa
    certificateId: str
    #: Certificate subject name.# noqa
    subjectName: str
    #: Subject Alternative Name (SAN) DNS names and IP addresses.# noqa
    sanList: str
    #: Name of the issuing CA.# noqa
    issuer: str
    #: Certificate valid from date.# noqa
    validFrom: str
    #: Certificate valid to (expiration) date# noqa
    validTo: str
    #: List of signed certificate timestamps (SCTs).# noqa
    signedCertificateTimestampList: str
    #: Whether the request complied with Certificate Transparency policy# noqa
    certificateTransparencyCompliance: str
    #: The signature algorithm used by the server in the TLS server signature,represented as a TLS SignatureScheme code point. Omitted if not applicable ornot known.# noqa
    serverSignatureAlgorithm: str
    #: Whether the connection used Encrypted ClientHello# noqa
    encryptedClientHello: str


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
    corsError: str
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
    operation: str
    #: Only set for "token-redemption" operation and determine whether torequest a fresh SRR or use a still valid cached SRR.# noqa
    refreshPolicy: str
    #: Origins of issuers from whom to request tokens or redemption records.# noqa
    issuers: str


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
    status: str
    #: HTTP response status text.# noqa
    statusText: str
    #: HTTP response headers.# noqa
    headers: str
    #: HTTP response headers text. This has been replaced by the headers inNetwork.responseReceivedExtraInfo.# noqa
    headersText: str
    #: Resource mimeType as determined by the browser.# noqa
    mimeType: str
    #: Refined HTTP request headers that were actually transmitted over thenetwork.# noqa
    requestHeaders: str
    #: HTTP request headers text. This has been replaced by the headers inNetwork.requestWillBeSentExtraInfo.# noqa
    requestHeadersText: str
    #: Specifies whether physical connection was actually reused for thisrequest.# noqa
    connectionReused: str
    #: Physical connection id that was actually used for this request.# noqa
    connectionId: str
    #: Remote IP address.# noqa
    remoteIPAddress: str
    #: Remote port.# noqa
    remotePort: str
    #: Specifies that the request was served from the disk cache.# noqa
    fromDiskCache: str
    #: Specifies that the request was served from the ServiceWorker.# noqa
    fromServiceWorker: str
    #: Specifies that the request was served from the prefetch cache.# noqa
    fromPrefetchCache: str
    #: Total number of bytes received for this request so far.# noqa
    encodedDataLength: str
    #: Timing information for the given request.# noqa
    timing: str
    #: Response source of response from ServiceWorker.# noqa
    serviceWorkerResponseSource: str
    #: The time at which the returned response was generated.# noqa
    responseTime: str
    #: Cache Storage Cache Name.# noqa
    cacheStorageCacheName: str
    #: Protocol used to fetch this request.# noqa
    protocol: str
    #: The reason why Chrome uses a specific transport protocol for HTTPsemantics.# noqa
    alternateProtocolUsage: str
    #: Security state of the request resource.# noqa
    securityState: str
    #: Security details for the request.# noqa
    securityDetails: str


@dataclass
class WebSocketRequest:
    """WebSocket request data."""

    #: HTTP request headers.# noqa
    headers: str


@dataclass
class WebSocketResponse:
    """WebSocket response data."""

    #: HTTP response status code.# noqa
    status: str
    #: HTTP response status text.# noqa
    statusText: str
    #: HTTP response headers.# noqa
    headers: str
    #: HTTP response headers text.# noqa
    headersText: str
    #: HTTP request headers.# noqa
    requestHeaders: str
    #: HTTP request headers text.# noqa
    requestHeadersText: str


@dataclass
class WebSocketFrame:
    """WebSocket message data.

    This represents an entire WebSocket message, not just a fragmented
    frame as the name suggests.
    """

    #: WebSocket message opcode.# noqa
    opcode: str
    #: WebSocket message mask.# noqa
    mask: str
    #: WebSocket message payload data. If the opcode is 1, this is a textmessage and payloadData is a UTF-8 string. If the opcode isn't 1, thenpayloadData is a base64 encoded string representing binary data.# noqa
    payloadData: str


@dataclass
class CachedResource:
    """Information about the cached resource."""

    #: Resource URL. This is the url of the original network request.# noqa
    url: str
    #: Type of this resource.# noqa
    type: str
    #: Cached response data.# noqa
    response: str
    #: Cached response body size.# noqa
    bodySize: str


@dataclass
class Initiator:
    """Information about the request initiator."""

    #: Type of this initiator.# noqa
    type: str
    #: Initiator JavaScript stack trace, set for Script only.# noqa
    stack: str
    #: Initiator URL, set for Parser type or for Script type (when script isimporting module) or for SignedExchange type.# noqa
    url: str
    #: Initiator line number, set for Parser type or for Script type (whenscript is importing module) (0-based).# noqa
    lineNumber: str
    #: Initiator column number, set for Parser type or for Script type (whenscript is importing module) (0-based).# noqa
    columnNumber: str
    #: Set if another request triggered this request (e.g. preflight).# noqa
    requestId: str


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
    expires: str
    #: Cookie size.# noqa
    size: str
    #: True if cookie is http-only.# noqa
    httpOnly: str
    #: True if cookie is secure.# noqa
    secure: str
    #: True in case of session cookie.# noqa
    session: str
    #: Cookie SameSite type.# noqa
    sameSite: str
    #: Cookie Priority# noqa
    priority: str
    #: True if cookie is SameParty.# noqa
    sameParty: str
    #: Cookie source scheme type.# noqa
    sourceScheme: str
    #: Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates anunspecified port. An unspecified port value allows protocol clients to emulatelegacy cookie scope for the port. This is a temporary ability and it will beremoved in the future.# noqa
    sourcePort: str
    #: Cookie partition key. The site of the top-level URL the browser wasvisiting at the start of the request to the endpoint that set the cookie.# noqa
    partitionKey: str
    #: True if cookie partition key is opaque.# noqa
    partitionKeyOpaque: str


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
    blockedReasons: str
    #: The string representing this individual cookie as it would appear in theheader. This is not the entire "cookie" or "set-cookie" header which could havemultiple cookies.# noqa
    cookieLine: str
    #: The cookie object which represents the cookie which was not stored. It isoptional because sometimes complete cookie information is not available, such asin the case of parsing errors.# noqa
    cookie: str


@dataclass
class BlockedCookieWithReason:
    """A cookie with was not sent with a request with the corresponding
    reason."""

    #: The reason(s) the cookie was blocked.# noqa
    blockedReasons: str
    #: The cookie object representing the cookie which was not sent.# noqa
    cookie: str


@dataclass
class CookieParam:
    """Cookie parameter object."""

    #: Cookie name.# noqa
    name: str
    #: Cookie value.# noqa
    value: str
    #: The request-URI to associate with the setting of the cookie. This valuecan affect the default domain, path, source port, and source scheme values ofthe created cookie.# noqa
    url: str
    #: Cookie domain.# noqa
    domain: str
    #: Cookie path.# noqa
    path: str
    #: True if cookie is secure.# noqa
    secure: str
    #: True if cookie is http-only.# noqa
    httpOnly: str
    #: Cookie SameSite type.# noqa
    sameSite: str
    #: Cookie expiration date, session cookie if not set# noqa
    expires: str
    #: Cookie Priority.# noqa
    priority: str
    #: True if cookie is SameParty.# noqa
    sameParty: str
    #: Cookie source scheme type.# noqa
    sourceScheme: str
    #: Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates anunspecified port. An unspecified port value allows protocol clients to emulatelegacy cookie scope for the port. This is a temporary ability and it will beremoved in the future.# noqa
    sourcePort: str
    #: Cookie partition key. The site of the top-level URL the browser wasvisiting at the start of the request to the endpoint that set the cookie. If notset, the cookie will be set as not partitioned.# noqa
    partitionKey: str


@dataclass
class AuthChallenge:
    """Authorization challenge for HTTP status code 401 or 407."""

    #: Source of the authentication challenge.# noqa
    source: str
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
    username: str
    #: The password to provide, possibly empty. Should only be set if responseis ProvideCredentials.# noqa
    password: str


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
    urlPattern: str
    #: If set, only requests for matching resource types will be intercepted.# noqa
    resourceType: str
    #: Stage at which to begin intercepting requests. Default is Request.# noqa
    interceptionStage: str


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
    certUrl: str
    #: The hex string of signed exchange signature cert sha256.# noqa
    certSha256: str
    #: Signed exchange signature validity Url.# noqa
    validityUrl: str
    #: Signed exchange signature date.# noqa
    date: str
    #: Signed exchange signature expires.# noqa
    expires: str
    #: The encoded certificates.# noqa
    certificates: str


@dataclass
class SignedExchangeHeader:
    """Information about a signed exchange header.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    """

    #: Signed exchange request URL.# noqa
    requestUrl: str
    #: Signed exchange response code.# noqa
    responseCode: str
    #: Signed exchange response headers.# noqa
    responseHeaders: str
    #: Signed exchange response signature.# noqa
    signatures: str
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
    signatureIndex: str
    #: The field which caused the error.# noqa
    errorField: str


@dataclass
class SignedExchangeInfo:
    """Information about a signed exchange response."""

    #: The outer response of signed HTTP exchange which was received fromnetwork.# noqa
    outerResponse: str
    #: Information about the signed exchange header.# noqa
    header: str
    #: Security details for the signed exchange header.# noqa
    securityDetails: str
    #: Errors occurred while handling the signed exchagne.# noqa
    errors: str


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
    requestTime: str


@dataclass
class ClientSecurityState:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    initiatorIsSecureContext: str
    #: Description is missing from the devtools protocol document.# noqa
    initiatorIPAddressSpace: str
    #: Description is missing from the devtools protocol document.# noqa
    privateNetworkRequestPolicy: str


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
    value: str
    #: Description is missing from the devtools protocol document.# noqa
    reportOnlyValue: str
    #: Description is missing from the devtools protocol document.# noqa
    reportingEndpoint: str
    #: Description is missing from the devtools protocol document.# noqa
    reportOnlyReportingEndpoint: str


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
    value: str
    #: Description is missing from the devtools protocol document.# noqa
    reportOnlyValue: str
    #: Description is missing from the devtools protocol document.# noqa
    reportingEndpoint: str
    #: Description is missing from the devtools protocol document.# noqa
    reportOnlyReportingEndpoint: str


@dataclass
class SecurityIsolationStatus:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    coop: str
    #: Description is missing from the devtools protocol document.# noqa
    coep: str


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
    id: str
    #: The URL of the document that triggered the report.# noqa
    initiatorUrl: str
    #: The name of the endpoint group that should be used to deliver the report.# noqa
    destination: str
    #: The type of the report (specifies the set of data that is contained inthe report body).# noqa
    type: str
    #: When the report was generated.# noqa
    timestamp: str
    #: How many uploads deep the related request was.# noqa
    depth: str
    #: The number of delivery attempts made so far, not including an activeattempt.# noqa
    completedAttempts: str
    #: Description is missing from the devtools protocol document.# noqa
    body: str
    #: Description is missing from the devtools protocol document.# noqa
    status: str


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
    success: str
    #: Optional values used for error reporting.# noqa
    netError: str
    #: Description is missing from the devtools protocol document.# noqa
    netErrorName: str
    #: Description is missing from the devtools protocol document.# noqa
    httpStatusCode: str
    #: If successful, one of the following two fields holds the result.# noqa
    stream: str
    #: Response headers.# noqa
    headers: str


@dataclass
class LoadNetworkResourceOptions:
    """An options object that may be extended later to better support CORS,
    CORB and streaming."""

    #: Description is missing from the devtools protocol document.# noqa
    disableCache: str
    #: Description is missing from the devtools protocol document.# noqa
    includeCredentials: str
