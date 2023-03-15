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

from . import io
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
    request_time: float
    #: Started resolving proxy.# noqa
    proxy_start: float
    #: Finished resolving proxy.# noqa
    proxy_end: float
    #: Started DNS address resolve.# noqa
    dns_start: float
    #: Finished DNS address resolve.# noqa
    dns_end: float
    #: Started connecting to the remote host.# noqa
    connect_start: float
    #: Connected to the remote host.# noqa
    connect_end: float
    #: Started SSL handshake.# noqa
    ssl_start: float
    #: Finished SSL handshake.# noqa
    ssl_end: float
    #: Started running ServiceWorker.# noqa
    worker_start: float
    #: Finished Starting ServiceWorker.# noqa
    worker_ready: float
    #: Started fetch event.# noqa
    worker_fetch_start: float
    #: Settled fetch event respondWith promise.# noqa
    worker_respond_with_settled: float
    #: Started sending request.# noqa
    send_start: float
    #: Finished sending request.# noqa
    send_end: float
    #: Time the server started pushing request.# noqa
    push_start: float
    #: Time the server finished pushing request.# noqa
    push_end: float
    #: Finished receiving response headers.# noqa
    receive_headers_end: float


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
    #: HTTP request method.# noqa
    method: str
    #: HTTP request headers.# noqa
    headers: Headers
    #: Priority of the resource request at the time request is sent.# noqa
    initial_priority: ResourcePriority
    #: The referrer policy of the request, as defined inhttps://www.w3.org/TR/referrer-policy/# noqa
    referrer_policy: str
    #: Fragment of the requested URL starting with hash, if present.# noqa
    url_fragment: typing.Optional[str] = None
    #: HTTP POST request data.# noqa
    post_data: typing.Optional[str] = None
    #: True when the request has POST data. Note that postData might still beomitted when this flag is true when the data is too long.# noqa
    has_post_data: typing.Optional[bool] = None
    #: Request body elements. This will be converted from base64 to binary# noqa
    post_data_entries: typing.Optional[typing.List[PostDataEntry]] = None
    #: The mixed content type of the request.# noqa
    mixed_content_type: typing.Optional[security.MixedContentType] = None
    #: Whether is loaded via link preload.# noqa
    is_link_preload: typing.Optional[bool] = None
    #: Set for requests when the TrustToken API is used. Contains the parameterspassed by the developer (e.g. via "fetch") as understood by the backend.# noqa
    trust_token_params: typing.Optional[TrustTokenParams] = None
    #: True if this resource request is considered to be the 'same site' as therequest correspondinfg to the main frame.# noqa
    is_same_site: typing.Optional[bool] = None


@dataclass
class SignedCertificateTimestamp:
    """Details of a signed certificate timestamp (SCT)."""

    #: Validation status.# noqa
    status: str
    #: Origin.# noqa
    origin: str
    #: Log name / description.# noqa
    log_description: str
    #: Log ID.# noqa
    log_id: str
    #: Issuance date. Unlike TimeSinceEpoch, this contains the number ofmilliseconds since January 1, 1970, UTC, not the number of seconds.# noqa
    timestamp: float
    #: Hash algorithm.# noqa
    hash_algorithm: str
    #: Signature algorithm.# noqa
    signature_algorithm: str
    #: Signature data.# noqa
    signature_data: str


@dataclass
class SecurityDetails:
    """Security details about a request."""

    #: Protocol name (e.g. "TLS 1.2" or "QUIC").# noqa
    protocol: str
    #: Key Exchange used by the connection, or the empty string if notapplicable.# noqa
    key_exchange: str
    #: Cipher name.# noqa
    cipher: str
    #: Certificate ID value.# noqa
    certificate_id: security.CertificateId
    #: Certificate subject name.# noqa
    subject_name: str
    #: Subject Alternative Name (SAN) DNS names and IP addresses.# noqa
    san_list: str
    #: Name of the issuing CA.# noqa
    issuer: str
    #: Certificate valid from date.# noqa
    valid_from: TimeSinceEpoch
    #: Certificate valid to (expiration) date# noqa
    valid_to: TimeSinceEpoch
    #: List of signed certificate timestamps (SCTs).# noqa
    signed_certificate_timestamp_list: SignedCertificateTimestamp
    #: Whether the request complied with Certificate Transparency policy# noqa
    certificate_transparency_compliance: CertificateTransparencyCompliance
    #: Whether the connection used Encrypted ClientHello# noqa
    encrypted_client_hello: bool
    #: (EC)DH group used by the connection, if applicable.# noqa
    key_exchange_group: typing.Optional[str] = None
    #: TLS MAC. Note that AEAD ciphers do not have separate MACs.# noqa
    mac: typing.Optional[str] = None
    #: The signature algorithm used by the server in the TLS server signature,represented as a TLS SignatureScheme code point. Omitted if not applicable ornot known.# noqa
    server_signature_algorithm: typing.Optional[int] = None


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
    cors_error: CorsError
    #: Description is missing from the devtools protocol document.# noqa
    failed_parameter: str


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
    refresh_policy: str
    #: Origins of issuers from whom to request tokens or redemption records.# noqa
    issuers: typing.Optional[typing.List[str]] = None


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
    status_text: str
    #: HTTP response headers.# noqa
    headers: Headers
    #: Resource mimeType as determined by the browser.# noqa
    mime_type: str
    #: Specifies whether physical connection was actually reused for thisrequest.# noqa
    connection_reused: bool
    #: Physical connection id that was actually used for this request.# noqa
    connection_id: float
    #: Total number of bytes received for this request so far.# noqa
    encoded_data_length: float
    #: Security state of the request resource.# noqa
    security_state: security.SecurityState
    #: HTTP response headers text. This has been replaced by the headers inNetwork.responseReceivedExtraInfo.# noqa
    headers_text: typing.Optional[str] = None
    #: Refined HTTP request headers that were actually transmitted over thenetwork.# noqa
    request_headers: typing.Optional[Headers] = None
    #: HTTP request headers text. This has been replaced by the headers inNetwork.requestWillBeSentExtraInfo.# noqa
    request_headers_text: typing.Optional[str] = None
    #: Remote IP address.# noqa
    remote_ip_address: typing.Optional[str] = None
    #: Remote port.# noqa
    remote_port: typing.Optional[int] = None
    #: Specifies that the request was served from the disk cache.# noqa
    from_disk_cache: typing.Optional[bool] = None
    #: Specifies that the request was served from the ServiceWorker.# noqa
    from_service_worker: typing.Optional[bool] = None
    #: Specifies that the request was served from the prefetch cache.# noqa
    from_prefetch_cache: typing.Optional[bool] = None
    #: Timing information for the given request.# noqa
    timing: typing.Optional[ResourceTiming] = None
    #: Response source of response from ServiceWorker.# noqa
    service_worker_response_source: typing.Optional[ServiceWorkerResponseSource] = None
    #: The time at which the returned response was generated.# noqa
    response_time: typing.Optional[TimeSinceEpoch] = None
    #: Cache Storage Cache Name.# noqa
    cache_storage_cache_name: typing.Optional[str] = None
    #: Protocol used to fetch this request.# noqa
    protocol: typing.Optional[str] = None
    #: The reason why Chrome uses a specific transport protocol for HTTPsemantics.# noqa
    alternate_protocol_usage: typing.Optional[AlternateProtocolUsage] = None
    #: Security details for the request.# noqa
    security_details: typing.Optional[SecurityDetails] = None


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
    status_text: str
    #: HTTP response headers.# noqa
    headers: Headers
    #: HTTP response headers text.# noqa
    headers_text: typing.Optional[str] = None
    #: HTTP request headers.# noqa
    request_headers: typing.Optional[Headers] = None
    #: HTTP request headers text.# noqa
    request_headers_text: typing.Optional[str] = None


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
    payload_data: str


@dataclass
class CachedResource:
    """Information about the cached resource."""

    #: Resource URL. This is the url of the original network request.# noqa
    url: str
    #: Type of this resource.# noqa
    type: ResourceType
    #: Cached response body size.# noqa
    body_size: float
    #: Cached response data.# noqa
    response: typing.Optional[Response] = None


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
    line_number: typing.Optional[float] = None
    #: Initiator column number, set for Parser type or for Script type (whenscript is importing module) (0-based).# noqa
    column_number: typing.Optional[float] = None
    #: Set if another request triggered this request (e.g. preflight).# noqa
    request_id: typing.Optional[RequestId] = None


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
    http_only: bool
    #: True if cookie is secure.# noqa
    secure: bool
    #: True in case of session cookie.# noqa
    session: bool
    #: Cookie Priority# noqa
    priority: CookiePriority
    #: True if cookie is SameParty.# noqa
    same_party: bool
    #: Cookie source scheme type.# noqa
    source_scheme: CookieSourceScheme
    #: Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates anunspecified port. An unspecified port value allows protocol clients to emulatelegacy cookie scope for the port. This is a temporary ability and it will beremoved in the future.# noqa
    source_port: int
    #: Cookie SameSite type.# noqa
    same_site: typing.Optional[CookieSameSite] = None
    #: Cookie partition key. The site of the top-level URL the browser wasvisiting at the start of the request to the endpoint that set the cookie.# noqa
    partition_key: typing.Optional[str] = None
    #: True if cookie partition key is opaque.# noqa
    partition_key_opaque: typing.Optional[bool] = None


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
    blocked_reasons: SetCookieBlockedReason
    #: The string representing this individual cookie as it would appear in theheader. This is not the entire "cookie" or "set-cookie" header which could havemultiple cookies.# noqa
    cookie_line: str
    #: The cookie object which represents the cookie which was not stored. It isoptional because sometimes complete cookie information is not available, such asin the case of parsing errors.# noqa
    cookie: typing.Optional[Cookie] = None


@dataclass
class BlockedCookieWithReason:
    """A cookie with was not sent with a request with the corresponding
    reason."""

    #: The reason(s) the cookie was blocked.# noqa
    blocked_reasons: CookieBlockedReason
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
    http_only: typing.Optional[bool] = None
    #: Cookie SameSite type.# noqa
    same_site: typing.Optional[CookieSameSite] = None
    #: Cookie expiration date, session cookie if not set# noqa
    expires: typing.Optional[TimeSinceEpoch] = None
    #: Cookie Priority.# noqa
    priority: typing.Optional[CookiePriority] = None
    #: True if cookie is SameParty.# noqa
    same_party: typing.Optional[bool] = None
    #: Cookie source scheme type.# noqa
    source_scheme: typing.Optional[CookieSourceScheme] = None
    #: Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates anunspecified port. An unspecified port value allows protocol clients to emulatelegacy cookie scope for the port. This is a temporary ability and it will beremoved in the future.# noqa
    source_port: typing.Optional[int] = None
    #: Cookie partition key. The site of the top-level URL the browser wasvisiting at the start of the request to the endpoint that set the cookie. If notset, the cookie will be set as not partitioned.# noqa
    partition_key: typing.Optional[str] = None


@dataclass
class AuthChallenge:
    """Authorization challenge for HTTP status code 401 or 407."""

    #: Origin of the challenger.# noqa
    origin: str
    #: The authentication scheme used, such as basic or digest# noqa
    scheme: str
    #: The realm of the challenge. May be empty.# noqa
    realm: str
    #: Source of the authentication challenge.# noqa
    source: typing.Optional[str] = None


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
    url_pattern: typing.Optional[str] = None
    #: If set, only requests for matching resource types will be intercepted.# noqa
    resource_type: typing.Optional[ResourceType] = None
    #: Stage at which to begin intercepting requests. Default is Request.# noqa
    interception_stage: typing.Optional[InterceptionStage] = None


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
    #: Signed exchange signature validity Url.# noqa
    validity_url: str
    #: Signed exchange signature date.# noqa
    date: int
    #: Signed exchange signature expires.# noqa
    expires: int
    #: Signed exchange signature cert Url.# noqa
    cert_url: typing.Optional[str] = None
    #: The hex string of signed exchange signature cert sha256.# noqa
    cert_sha256: typing.Optional[str] = None
    #: The encoded certificates.# noqa
    certificates: typing.Optional[typing.List[str]] = None


@dataclass
class SignedExchangeHeader:
    """Information about a signed exchange header.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    """

    #: Signed exchange request URL.# noqa
    request_url: str
    #: Signed exchange response code.# noqa
    response_code: int
    #: Signed exchange response headers.# noqa
    response_headers: Headers
    #: Signed exchange response signature.# noqa
    signatures: SignedExchangeSignature
    #: Signed exchange header integrity hash in the form of"sha256-<base64-hash-value>".# noqa
    header_integrity: str


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
    signature_index: typing.Optional[int] = None
    #: The field which caused the error.# noqa
    error_field: typing.Optional[SignedExchangeErrorField] = None


@dataclass
class SignedExchangeInfo:
    """Information about a signed exchange response."""

    #: The outer response of signed HTTP exchange which was received fromnetwork.# noqa
    outer_response: Response
    #: Information about the signed exchange header.# noqa
    header: typing.Optional[SignedExchangeHeader] = None
    #: Security details for the signed exchange header.# noqa
    security_details: typing.Optional[SecurityDetails] = None
    #: Errors occurred while handling the signed exchagne.# noqa
    errors: typing.Optional[typing.List[SignedExchangeError]] = None


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
    request_time: float


@dataclass
class ClientSecurityState:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    initiator_is_secure_context: bool
    #: Description is missing from the devtools protocol document.# noqa
    initiator_ip_address_space: IPAddressSpace
    #: Description is missing from the devtools protocol document.# noqa
    private_network_request_policy: PrivateNetworkRequestPolicy


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
    report_only_value: CrossOriginOpenerPolicyValue
    #: Description is missing from the devtools protocol document.# noqa
    reporting_endpoint: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    report_only_reporting_endpoint: typing.Optional[str] = None


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
    report_only_value: CrossOriginEmbedderPolicyValue
    #: Description is missing from the devtools protocol document.# noqa
    reporting_endpoint: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    report_only_reporting_endpoint: typing.Optional[str] = None


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
    initiator_url: str
    #: The name of the endpoint group that should be used to deliver the report.# noqa
    destination: str
    #: The type of the report (specifies the set of data that is contained inthe report body).# noqa
    type: str
    #: When the report was generated.# noqa
    timestamp: TimeSinceEpoch
    #: How many uploads deep the related request was.# noqa
    depth: int
    #: The number of delivery attempts made so far, not including an activeattempt.# noqa
    completed_attempts: int
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
    group_name: str


@dataclass
class LoadNetworkResourcePageResult:
    """An object providing the result of a network resource load."""

    #: Description is missing from the devtools protocol document.# noqa
    success: bool
    #: Optional values used for error reporting.# noqa
    net_error: typing.Optional[float] = None
    #: Description is missing from the devtools protocol document.# noqa
    net_error_name: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    http_status_code: typing.Optional[float] = None
    #: If successful, one of the following two fields holds the result.# noqa
    stream: typing.Optional[io.StreamHandle] = None
    #: Response headers.# noqa
    headers: typing.Optional[Headers] = None


@dataclass
class LoadNetworkResourceOptions:
    """An options object that may be extended later to better support CORS,
    CORB and streaming."""

    #: Description is missing from the devtools protocol document.# noqa
    disable_cache: bool
    #: Description is missing from the devtools protocol document.# noqa
    include_credentials: bool


async def set_accepted_encodings() -> None:
    """Sets a list of content encodings that will be accepted.

    Empty list means no encoding is accepted. # noqa
    """
    ...


async def clear_accepted_encodings_override() -> None:
    """Clears accepted encodings set by setAcceptedEncodings # noqa."""
    ...


async def can_clear_browser_cache() -> None:
    """Tells whether clearing browser cache is supported.

    # noqa
    """
    ...


async def can_clear_browser_cookies() -> None:
    """Tells whether clearing browser cookies is supported.

    # noqa
    """
    ...


async def can_emulate_network_conditions() -> None:
    """Tells whether emulation of network conditions is supported.

    # noqa
    """
    ...


async def clear_browser_cache() -> None:
    """Clears browser cache.

    # noqa
    """
    ...


async def clear_browser_cookies() -> None:
    """Clears browser cookies.

    # noqa
    """
    ...


async def continue_intercepted_request() -> None:
    """Response to Network.requestIntercepted which either modifies the request
    to continue with any modifications, or blocks it, or completes it with the
    provided response bytes.

    If a network fetch occurs as a result which encounters a redirect an
    additional Network.requestIntercepted event will be sent with the
    same InterceptionId. Deprecated, use Fetch.continueRequest,
    Fetch.fulfillRequest and Fetch.failRequest instead. # noqa
    """
    ...


async def delete_cookies() -> None:
    """Deletes browser cookies with matching name and url or domain/path pair.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables network tracking, prevents network events from being sent to
    the client.

    # noqa
    """
    ...


async def emulate_network_conditions() -> None:
    """Activates emulation of network conditions.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables network tracking, network events will now be delivered to the
    client.

    # noqa
    """
    ...


async def get_all_cookies() -> None:
    """Returns all browser cookies.

    Depending on the backend support, will return detailed cookie
    information in the `cookies` field. Deprecated. Use
    Storage.getCookies instead. # noqa
    """
    ...


async def get_certificate() -> None:
    """Returns the DER-encoded certificate.

    # noqa
    """
    ...


async def get_cookies() -> None:
    """Returns all browser cookies for the current URL.

    Depending on the backend support, will return detailed cookie
    information in the `cookies` field. # noqa
    """
    ...


async def get_response_body() -> None:
    """Returns content served for the given request.

    # noqa
    """
    ...


async def get_request_post_data() -> None:
    """Returns post data sent with the request.

    Returns an error when no data was sent with the request. # noqa
    """
    ...


async def get_response_body_for_interception() -> None:
    """Returns content served for the given currently intercepted request.

    # noqa
    """
    ...


async def take_response_body_for_interception_as_stream() -> None:
    """Returns a handle to the stream representing the response body.

    Note that after this command, the intercepted request can't be
    continued as is -- you either need to cancel it or to provide the
    response body. The stream only supports sequential read, IO.read
    will fail if the position is specified. # noqa
    """
    ...


async def replay_xhr() -> None:
    """This method sends a new XMLHttpRequest which is identical to the
    original one.

    The following parameters should be identical: method, url, async,
    request body, extra headers, withCredentials attribute, user,
    password. # noqa
    """
    ...


async def search_in_response_body() -> None:
    """Searches for given string in response content.

    # noqa
    """
    ...


async def set_blocked_ur_ls() -> None:
    """Blocks URLs from loading.

    # noqa
    """
    ...


async def set_bypass_service_worker() -> None:
    """Toggles ignoring of service worker for each request.

    # noqa
    """
    ...


async def set_cache_disabled() -> None:
    """Toggles ignoring cache for each request.

    If `true`, cache will not be used. # noqa
    """
    ...


async def set_cookie() -> None:
    """Sets a cookie with the given cookie data; may overwrite equivalent
    cookies if they exist.

    # noqa
    """
    ...


async def set_cookies() -> None:
    """Sets given cookies.

    # noqa
    """
    ...


async def set_extra_http_headers() -> None:
    """Specifies whether to always send extra HTTP headers with the requests
    from this page.

    # noqa
    """
    ...


async def set_attach_debug_stack() -> None:
    """Specifies whether to attach a page script stack id in requests #
    noqa."""
    ...


async def set_request_interception() -> None:
    """Sets the requests to intercept that match the provided patterns and
    optionally resource types.

    Deprecated, please use Fetch.enable instead. # noqa
    """
    ...


async def set_user_agent_override() -> None:
    """Allows overriding user agent with the given string.

    # noqa
    """
    ...


async def get_security_isolation_status() -> None:
    """Returns information about the COEP/COOP isolation status.

    # noqa
    """
    ...


async def enable_reporting_api() -> None:
    """Enables tracking for the Reporting API, events generated by the
    Reporting API will now be delivered to the client.

    Enabling triggers 'reportingApiReportAdded' for all existing
    reports. # noqa
    """
    ...


async def load_network_resource() -> None:
    """Fetches the resource and returns the content.

    # noqa
    """
    ...
