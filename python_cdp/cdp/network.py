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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


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
    """The underlying connection technology that the browser is
    supposedlyusing."""

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
    """Represents the cookie's 'SameSite'
    status:https://tools.ietf.org/html/draft-west-first-party-cookies."""

    STRICT = "Strict"
    LAX = "Lax"
    NONE = "None"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookiePriority(str, enum.Enum):
    """Represents the cookie's 'Priority'
    status:https://tools.ietf.org/html/draft-west-cookie-priority-00."""

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookieSourceScheme(str, enum.Enum):
    """Represents the source scheme of the origin that originally set
    thecookie.

    A value of "Unset" allows protocol clients to emulate legacy
    cookiescope for the scheme. This is a temporary ability and it will
    be removed in thefuture.
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

    #: Timing's requestTime is a baseline in seconds, while the other numbersare ticks in milliseconds relatively to this requestTime.
    requestTime: str
    #: Started resolving proxy.
    proxyStart: str
    #: Finished resolving proxy.
    proxyEnd: str
    #: Started DNS address resolve.
    dnsStart: str
    #: Finished DNS address resolve.
    dnsEnd: str
    #: Started connecting to the remote host.
    connectStart: str
    #: Connected to the remote host.
    connectEnd: str
    #: Started SSL handshake.
    sslStart: str
    #: Finished SSL handshake.
    sslEnd: str
    #: Started running ServiceWorker.
    workerStart: str
    #: Finished Starting ServiceWorker.
    workerReady: str
    #: Started fetch event.
    workerFetchStart: str
    #: Settled fetch event respondWith promise.
    workerRespondWithSettled: str
    #: Started sending request.
    sendStart: str
    #: Finished sending request.
    sendEnd: str
    #: Time the server started pushing request.
    pushStart: str
    #: Time the server finished pushing request.
    pushEnd: str
    #: Finished receiving response headers.
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

    #: Description is missing from the devtools protocol document.
    bytes: str


@dataclass
class Request:
    """HTTP request data."""

    #: Request URL (without fragment).
    url: str
    #: Fragment of the requested URL starting with hash, if present.
    urlFragment: str
    #: HTTP request method.
    method: str
    #: HTTP request headers.
    headers: str
    #: HTTP POST request data.
    postData: str
    #: True when the request has POST data. Note that postData might still beomitted when this flag is true when the data is too long.
    hasPostData: str
    #: Request body elements. This will be converted from base64 to binary
    postDataEntries: str
    #: The mixed content type of the request.
    mixedContentType: str
    #: Priority of the resource request at the time request is sent.
    initialPriority: str
    #: The referrer policy of the request, as defined inhttps://www.w3.org/TR/referrer-policy/
    referrerPolicy: str
    #: Whether is loaded via link preload.
    isLinkPreload: str
    #: Set for requests when the TrustToken API is used. Contains the parameterspassed by the developer (e.g. via "fetch") as understood by the backend.
    trustTokenParams: str
    #: True if this resource request is considered to be the 'same site' as therequest correspondinfg to the main frame.
    isSameSite: str


@dataclass
class SignedCertificateTimestamp:
    """Details of a signed certificate timestamp (SCT)."""

    #: Validation status.
    status: str
    #: Origin.
    origin: str
    #: Log name / description.
    logDescription: str
    #: Log ID.
    logId: str
    #: Issuance date. Unlike TimeSinceEpoch, this contains the number ofmilliseconds since January 1, 1970, UTC, not the number of seconds.
    timestamp: str
    #: Hash algorithm.
    hashAlgorithm: str
    #: Signature algorithm.
    signatureAlgorithm: str
    #: Signature data.
    signatureData: str


@dataclass
class SecurityDetails:
    """Security details about a request."""

    #: Protocol name (e.g. "TLS 1.2" or "QUIC").
    protocol: str
    #: Key Exchange used by the connection, or the empty string if notapplicable.
    keyExchange: str
    #: (EC)DH group used by the connection, if applicable.
    keyExchangeGroup: str
    #: Cipher name.
    cipher: str
    #: TLS MAC. Note that AEAD ciphers do not have separate MACs.
    mac: str
    #: Certificate ID value.
    certificateId: str
    #: Certificate subject name.
    subjectName: str
    #: Subject Alternative Name (SAN) DNS names and IP addresses.
    sanList: str
    #: Name of the issuing CA.
    issuer: str
    #: Certificate valid from date.
    validFrom: str
    #: Certificate valid to (expiration) date
    validTo: str
    #: List of signed certificate timestamps (SCTs).
    signedCertificateTimestampList: str
    #: Whether the request complied with Certificate Transparency policy
    certificateTransparencyCompliance: str
    #: The signature algorithm used by the server in the TLS server signature,represented as a TLS SignatureScheme code point. Omitted if not applicable ornot known.
    serverSignatureAlgorithm: str
    #: Whether the connection used Encrypted ClientHello
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

    #: Description is missing from the devtools protocol document.
    corsError: str
    #: Description is missing from the devtools protocol document.
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

    #: Description is missing from the devtools protocol document.
    operation: str
    #: Only set for "token-redemption" operation and determine whether torequest a fresh SRR or use a still valid cached SRR.
    refreshPolicy: str
    #: Origins of issuers from whom to request tokens or redemption records.
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
    """The reason why Chrome uses a specific transport protocol for
    HTTPsemantics."""

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

    #: Response URL. This URL can be different from CachedResource.url in caseof redirect.
    url: str
    #: HTTP response status code.
    status: str
    #: HTTP response status text.
    statusText: str
    #: HTTP response headers.
    headers: str
    #: HTTP response headers text. This has been replaced by the headers inNetwork.responseReceivedExtraInfo.
    headersText: str
    #: Resource mimeType as determined by the browser.
    mimeType: str
    #: Refined HTTP request headers that were actually transmitted over thenetwork.
    requestHeaders: str
    #: HTTP request headers text. This has been replaced by the headers inNetwork.requestWillBeSentExtraInfo.
    requestHeadersText: str
    #: Specifies whether physical connection was actually reused for thisrequest.
    connectionReused: str
    #: Physical connection id that was actually used for this request.
    connectionId: str
    #: Remote IP address.
    remoteIPAddress: str
    #: Remote port.
    remotePort: str
    #: Specifies that the request was served from the disk cache.
    fromDiskCache: str
    #: Specifies that the request was served from the ServiceWorker.
    fromServiceWorker: str
    #: Specifies that the request was served from the prefetch cache.
    fromPrefetchCache: str
    #: Total number of bytes received for this request so far.
    encodedDataLength: str
    #: Timing information for the given request.
    timing: str
    #: Response source of response from ServiceWorker.
    serviceWorkerResponseSource: str
    #: The time at which the returned response was generated.
    responseTime: str
    #: Cache Storage Cache Name.
    cacheStorageCacheName: str
    #: Protocol used to fetch this request.
    protocol: str
    #: The reason why Chrome uses a specific transport protocol for HTTPsemantics.
    alternateProtocolUsage: str
    #: Security state of the request resource.
    securityState: str
    #: Security details for the request.
    securityDetails: str


@dataclass
class WebSocketRequest:
    """WebSocket request data."""

    #: HTTP request headers.
    headers: str


@dataclass
class WebSocketResponse:
    """WebSocket response data."""

    #: HTTP response status code.
    status: str
    #: HTTP response status text.
    statusText: str
    #: HTTP response headers.
    headers: str
    #: HTTP response headers text.
    headersText: str
    #: HTTP request headers.
    requestHeaders: str
    #: HTTP request headers text.
    requestHeadersText: str


@dataclass
class WebSocketFrame:
    """WebSocket message data.

    This represents an entire WebSocket message, not just a fragmented
    frame as the name suggests.
    """

    #: WebSocket message opcode.
    opcode: str
    #: WebSocket message mask.
    mask: str
    #: WebSocket message payload data. If the opcode is 1, this is a textmessage and payloadData is a UTF-8 string. If the opcode isn't 1, thenpayloadData is a base64 encoded string representing binary data.
    payloadData: str


@dataclass
class CachedResource:
    """Information about the cached resource."""

    #: Resource URL. This is the url of the original network request.
    url: str
    #: Type of this resource.
    type: str
    #: Cached response data.
    response: str
    #: Cached response body size.
    bodySize: str


@dataclass
class Initiator:
    """Information about the request initiator."""

    #: Type of this initiator.
    type: str
    #: Initiator JavaScript stack trace, set for Script only.
    stack: str
    #: Initiator URL, set for Parser type or for Script type (when script isimporting module) or for SignedExchange type.
    url: str
    #: Initiator line number, set for Parser type or for Script type (whenscript is importing module) (0-based).
    lineNumber: str
    #: Initiator column number, set for Parser type or for Script type (whenscript is importing module) (0-based).
    columnNumber: str
    #: Set if another request triggered this request (e.g. preflight).
    requestId: str


@dataclass
class Cookie:
    """Cookie object."""

    #: Cookie name.
    name: str
    #: Cookie value.
    value: str
    #: Cookie domain.
    domain: str
    #: Cookie path.
    path: str
    #: Cookie expiration date as the number of seconds since the UNIX epoch.
    expires: str
    #: Cookie size.
    size: str
    #: True if cookie is http-only.
    httpOnly: str
    #: True if cookie is secure.
    secure: str
    #: True in case of session cookie.
    session: str
    #: Cookie SameSite type.
    sameSite: str
    #: Cookie Priority
    priority: str
    #: True if cookie is SameParty.
    sameParty: str
    #: Cookie source scheme type.
    sourceScheme: str
    #: Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates anunspecified port. An unspecified port value allows protocol clients to emulatelegacy cookie scope for the port. This is a temporary ability and it will beremoved in the future.
    sourcePort: str
    #: Cookie partition key. The site of the top-level URL the browser wasvisiting at the start of the request to the endpoint that set the cookie.
    partitionKey: str
    #: True if cookie partition key is opaque.
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

    #: The reason(s) this cookie was blocked.
    blockedReasons: str
    #: The string representing this individual cookie as it would appear in theheader. This is not the entire "cookie" or "set-cookie" header which could havemultiple cookies.
    cookieLine: str
    #: The cookie object which represents the cookie which was not stored. It isoptional because sometimes complete cookie information is not available, such asin the case of parsing errors.
    cookie: str


@dataclass
class BlockedCookieWithReason:
    """A cookie with was not sent with a request with the corresponding
    reason."""

    #: The reason(s) the cookie was blocked.
    blockedReasons: str
    #: The cookie object representing the cookie which was not sent.
    cookie: str


@dataclass
class CookieParam:
    """Cookie parameter object."""

    #: Cookie name.
    name: str
    #: Cookie value.
    value: str
    #: The request-URI to associate with the setting of the cookie. This valuecan affect the default domain, path, source port, and source scheme values ofthe created cookie.
    url: str
    #: Cookie domain.
    domain: str
    #: Cookie path.
    path: str
    #: True if cookie is secure.
    secure: str
    #: True if cookie is http-only.
    httpOnly: str
    #: Cookie SameSite type.
    sameSite: str
    #: Cookie expiration date, session cookie if not set
    expires: str
    #: Cookie Priority.
    priority: str
    #: True if cookie is SameParty.
    sameParty: str
    #: Cookie source scheme type.
    sourceScheme: str
    #: Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates anunspecified port. An unspecified port value allows protocol clients to emulatelegacy cookie scope for the port. This is a temporary ability and it will beremoved in the future.
    sourcePort: str
    #: Cookie partition key. The site of the top-level URL the browser wasvisiting at the start of the request to the endpoint that set the cookie. If notset, the cookie will be set as not partitioned.
    partitionKey: str


@dataclass
class AuthChallenge:
    """Authorization challenge for HTTP status code 401 or 407."""

    #: Source of the authentication challenge.
    source: str
    #: Origin of the challenger.
    origin: str
    #: The authentication scheme used, such as basic or digest
    scheme: str
    #: The realm of the challenge. May be empty.
    realm: str


@dataclass
class AuthChallengeResponse:
    """Response to an AuthChallenge."""

    #: The decision on what to do in response to the authorization challenge.Default means deferring to the default behavior of the net stack, which willlikely either the Cancel authentication or display a popup dialog box.
    response: str
    #: The username to provide, possibly empty. Should only be set if responseis ProvideCredentials.
    username: str
    #: The password to provide, possibly empty. Should only be set if responseis ProvideCredentials.
    password: str


class InterceptionStage(str, enum.Enum):
    """Stages of the interception to begin intercepting.

    Request will interceptbefore the request is sent. Response will
    intercept after the response isreceived.
    """

    REQUEST = "Request"
    HEADERSRECEIVED = "HeadersReceived"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class RequestPattern:
    """Request pattern for interception."""

    #: Wildcards (`'*'` -> zero or more, `'?'` -> exactly one) are allowed.Escape character is backslash. Omitting is equivalent to `"*"`.
    urlPattern: str
    #: If set, only requests for matching resource types will be intercepted.
    resourceType: str
    #: Stage at which to begin intercepting requests. Default is Request.
    interceptionStage: str


@dataclass
class SignedExchangeSignature:
    """Information about a signed exchange signature.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1
    """

    #: Signed exchange signature label.
    label: str
    #: The hex string of signed exchange signature.
    signature: str
    #: Signed exchange signature integrity.
    integrity: str
    #: Signed exchange signature cert Url.
    certUrl: str
    #: The hex string of signed exchange signature cert sha256.
    certSha256: str
    #: Signed exchange signature validity Url.
    validityUrl: str
    #: Signed exchange signature date.
    date: str
    #: Signed exchange signature expires.
    expires: str
    #: The encoded certificates.
    certificates: str


@dataclass
class SignedExchangeHeader:
    """Information about a signed exchange header.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    """

    #: Signed exchange request URL.
    requestUrl: str
    #: Signed exchange response code.
    responseCode: str
    #: Signed exchange response headers.
    responseHeaders: str
    #: Signed exchange response signature.
    signatures: str
    #: Signed exchange header integrity hash in the form of"sha256-<base64-hash-value>".
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

    #: Error message.
    message: str
    #: The index of the signature which caused the error.
    signatureIndex: str
    #: The field which caused the error.
    errorField: str


@dataclass
class SignedExchangeInfo:
    """Information about a signed exchange response."""

    #: The outer response of signed HTTP exchange which was received fromnetwork.
    outerResponse: str
    #: Information about the signed exchange header.
    header: str
    #: Security details for the signed exchange header.
    securityDetails: str
    #: Errors occurred while handling the signed exchagne.
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

    #: Timing's requestTime is a baseline in seconds, while the other numbersare ticks in milliseconds relatively to this requestTime. MatchesResourceTiming's requestTime for the same request (but not for redirectedrequests).
    requestTime: str


@dataclass
class ClientSecurityState:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.
    initiatorIsSecureContext: str
    #: Description is missing from the devtools protocol document.
    initiatorIPAddressSpace: str
    #: Description is missing from the devtools protocol document.
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

    #: Description is missing from the devtools protocol document.
    value: str
    #: Description is missing from the devtools protocol document.
    reportOnlyValue: str
    #: Description is missing from the devtools protocol document.
    reportingEndpoint: str
    #: Description is missing from the devtools protocol document.
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

    #: Description is missing from the devtools protocol document.
    value: str
    #: Description is missing from the devtools protocol document.
    reportOnlyValue: str
    #: Description is missing from the devtools protocol document.
    reportingEndpoint: str
    #: Description is missing from the devtools protocol document.
    reportOnlyReportingEndpoint: str


@dataclass
class SecurityIsolationStatus:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.
    coop: str
    #: Description is missing from the devtools protocol document.
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

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class ReportingApiReport:
    """An object representing a report generated by the Reporting API."""

    #: Description is missing from the devtools protocol document.
    id: str
    #: The URL of the document that triggered the report.
    initiatorUrl: str
    #: The name of the endpoint group that should be used to deliver the report.
    destination: str
    #: The type of the report (specifies the set of data that is contained inthe report body).
    type: str
    #: When the report was generated.
    timestamp: str
    #: How many uploads deep the related request was.
    depth: str
    #: The number of delivery attempts made so far, not including an activeattempt.
    completedAttempts: str
    #: Description is missing from the devtools protocol document.
    body: str
    #: Description is missing from the devtools protocol document.
    status: str


@dataclass
class ReportingApiEndpoint:
    """Description is missing from the devtools protocol document."""

    #: The URL of the endpoint to which reports may be delivered.
    url: str
    #: Name of the endpoint group.
    groupName: str


@dataclass
class LoadNetworkResourcePageResult:
    """An object providing the result of a network resource load."""

    #: Description is missing from the devtools protocol document.
    success: str
    #: Optional values used for error reporting.
    netError: str
    #: Description is missing from the devtools protocol document.
    netErrorName: str
    #: Description is missing from the devtools protocol document.
    httpStatusCode: str
    #: If successful, one of the following two fields holds the result.
    stream: str
    #: Response headers.
    headers: str


@dataclass
class LoadNetworkResourceOptions:
    """An options object that may be extended later to better support CORS,
    CORB and streaming."""

    #: Description is missing from the devtools protocol document.
    disableCache: str
    #: Description is missing from the devtools protocol document.
    includeCredentials: str
