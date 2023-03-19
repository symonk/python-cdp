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

from .utils import memoize_event


class ResourceType(str, enum.Enum):
    """Resource type as it was perceived by the rendering engine."""

    _DOCUMENT = "document"
    _STYLESHEET = "stylesheet"
    _IMAGE = "image"
    _MEDIA = "media"
    _FONT = "font"
    _SCRIPT = "script"
    _TEXT_TRACK = "text_track"
    _X_H_R = "xhr"
    _FETCH = "fetch"
    _PREFETCH = "prefetch"
    _EVENT_SOURCE = "event_source"
    _WEB_SOCKET = "web_socket"
    _MANIFEST = "manifest"
    _SIGNED_EXCHANGE = "signed_exchange"
    _PING = "ping"
    _C_S_P_VIOLATION_REPORT = "csp_violation_report"
    _PREFLIGHT = "preflight"
    _OTHER = "other"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class LoaderId(str):
    """Unique loader identifier."""

    def to_json(self) -> LoaderId:
        return self

    @classmethod
    def from_json(cls, value: str) -> LoaderId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class RequestId(str):
    """Unique request identifier."""

    def to_json(self) -> RequestId:
        return self

    @classmethod
    def from_json(cls, value: str) -> RequestId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class InterceptionId(str):
    """Unique intercepted request identifier."""

    def to_json(self) -> InterceptionId:
        return self

    @classmethod
    def from_json(cls, value: str) -> InterceptionId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ErrorReason(str, enum.Enum):
    """Network level fetch failure reason."""

    _FAILED = "failed"
    _ABORTED = "aborted"
    _TIMED_OUT = "timed_out"
    _ACCESS_DENIED = "access_denied"
    _CONNECTION_CLOSED = "connection_closed"
    _CONNECTION_RESET = "connection_reset"
    _CONNECTION_REFUSED = "connection_refused"
    _CONNECTION_ABORTED = "connection_aborted"
    _CONNECTION_FAILED = "connection_failed"
    _NAME_NOT_RESOLVED = "name_not_resolved"
    _INTERNET_DISCONNECTED = "internet_disconnected"
    _ADDRESS_UNREACHABLE = "address_unreachable"
    _BLOCKED_BY_CLIENT = "blocked_by_client"
    _BLOCKED_BY_RESPONSE = "blocked_by_response"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class TimeSinceEpoch(float):
    """UTC time in seconds, counted from January 1, 1970."""

    def to_json(self) -> TimeSinceEpoch:
        return self

    @classmethod
    def from_json(cls, value: float) -> TimeSinceEpoch:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class MonotonicTime(float):
    """Monotonically increasing time in seconds since an arbitrary point in the past."""

    def to_json(self) -> MonotonicTime:
        return self

    @classmethod
    def from_json(cls, value: float) -> MonotonicTime:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Headers(None):
    """Request / response headers as keys / values of JSON object."""

    def to_json(self) -> Headers:
        return self

    @classmethod
    def from_json(cls, value: None) -> Headers:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ConnectionType(str, enum.Enum):
    """The underlying connection technology that the browser is supposedly using."""

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

    _STRICT = "strict"
    _LAX = "lax"
    _NONE = "none"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookiePriority(str, enum.Enum):
    """Represents the cookie's 'Priority' status:

    https://tools.ietf.org/html/draft-west-cookie-priority-00
    """

    _LOW = "low"
    _MEDIUM = "medium"
    _HIGH = "high"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookieSourceScheme(str, enum.Enum):
    """Represents the source scheme of the origin that originally set the cookie.

    A value of "Unset" allows protocol clients to emulate legacy cookie scope for the scheme. This is a temporary
    ability and it will be removed in the future.
    """

    _UNSET = "unset"
    _NON_SECURE = "non_secure"
    _SECURE = "secure"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ResourceTiming(None):
    """Timing information for the request."""

    def to_json(self) -> ResourceTiming:
        return self

    @classmethod
    def from_json(cls, value: None) -> ResourceTiming:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ResourcePriority(str, enum.Enum):
    """Loading priority of a resource request."""

    _VERY_LOW = "very_low"
    _LOW = "low"
    _MEDIUM = "medium"
    _HIGH = "high"
    _VERY_HIGH = "very_high"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PostDataEntry(None):
    """Post data entry for HTTP request."""

    def to_json(self) -> PostDataEntry:
        return self

    @classmethod
    def from_json(cls, value: None) -> PostDataEntry:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Request(None):
    """HTTP request data."""

    def to_json(self) -> Request:
        return self

    @classmethod
    def from_json(cls, value: None) -> Request:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SignedCertificateTimestamp(None):
    """Details of a signed certificate timestamp (SCT)."""

    def to_json(self) -> SignedCertificateTimestamp:
        return self

    @classmethod
    def from_json(cls, value: None) -> SignedCertificateTimestamp:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SecurityDetails(None):
    """Security details about a request."""

    def to_json(self) -> SecurityDetails:
        return self

    @classmethod
    def from_json(cls, value: None) -> SecurityDetails:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CertificateTransparencyCompliance(str, enum.Enum):
    """Whether the request complied with Certificate Transparency policy."""

    UNKNOWN = "unknown"
    NOT_COMPLIANT = "not-compliant"
    COMPLIANT = "compliant"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class BlockedReason(str, enum.Enum):
    """The reason why request was blocked."""

    OTHER = "other"
    CSP = "csp"
    MIXED_CONTENT = "mixed-content"
    ORIGIN = "origin"
    INSPECTOR = "inspector"
    SUBRESOURCE_FILTER = "subresource-filter"
    CONTENT_TYPE = "content-type"
    COEP_FRAME_RESOURCE_NEEDS_COEP_HEADER = "coep-frame-resource-needs-coep-header"
    COOP_SANDBOXED_IFRAME_CANNOT_NAVIGATE_TO_COOP_PAGE = "coop-sandboxed-iframe-cannot-navigate-to-coop-page"
    CORP_NOT_SAME_ORIGIN = "corp-not-same-origin"
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP = (
        "corp-not-same-origin-after-defaulted-to-same-origin-by-coep"
    )
    CORP_NOT_SAME_SITE = "corp-not-same-site"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CorsError(str, enum.Enum):
    """The reason why request was blocked."""

    _DISALLOWED_BY_MODE = "disallowed_by_mode"
    _INVALID_RESPONSE = "invalid_response"
    _WILDCARD_ORIGIN_NOT_ALLOWED = "wildcard_origin_not_allowed"
    _MISSING_ALLOW_ORIGIN_HEADER = "missing_allow_origin_header"
    _MULTIPLE_ALLOW_ORIGIN_VALUES = "multiple_allow_origin_values"
    _INVALID_ALLOW_ORIGIN_VALUE = "invalid_allow_origin_value"
    _ALLOW_ORIGIN_MISMATCH = "allow_origin_mismatch"
    _INVALID_ALLOW_CREDENTIALS = "invalid_allow_credentials"
    _CORS_DISABLED_SCHEME = "cors_disabled_scheme"
    _PREFLIGHT_INVALID_STATUS = "preflight_invalid_status"
    _PREFLIGHT_DISALLOWED_REDIRECT = "preflight_disallowed_redirect"
    _PREFLIGHT_WILDCARD_ORIGIN_NOT_ALLOWED = "preflight_wildcard_origin_not_allowed"
    _PREFLIGHT_MISSING_ALLOW_ORIGIN_HEADER = "preflight_missing_allow_origin_header"
    _PREFLIGHT_MULTIPLE_ALLOW_ORIGIN_VALUES = "preflight_multiple_allow_origin_values"
    _PREFLIGHT_INVALID_ALLOW_ORIGIN_VALUE = "preflight_invalid_allow_origin_value"
    _PREFLIGHT_ALLOW_ORIGIN_MISMATCH = "preflight_allow_origin_mismatch"
    _PREFLIGHT_INVALID_ALLOW_CREDENTIALS = "preflight_invalid_allow_credentials"
    _PREFLIGHT_MISSING_ALLOW_EXTERNAL = "preflight_missing_allow_external"
    _PREFLIGHT_INVALID_ALLOW_EXTERNAL = "preflight_invalid_allow_external"
    _PREFLIGHT_MISSING_ALLOW_PRIVATE_NETWORK = "preflight_missing_allow_private_network"
    _PREFLIGHT_INVALID_ALLOW_PRIVATE_NETWORK = "preflight_invalid_allow_private_network"
    _INVALID_ALLOW_METHODS_PREFLIGHT_RESPONSE = "invalid_allow_methods_preflight_response"
    _INVALID_ALLOW_HEADERS_PREFLIGHT_RESPONSE = "invalid_allow_headers_preflight_response"
    _METHOD_DISALLOWED_BY_PREFLIGHT_RESPONSE = "method_disallowed_by_preflight_response"
    _HEADER_DISALLOWED_BY_PREFLIGHT_RESPONSE = "header_disallowed_by_preflight_response"
    _REDIRECT_CONTAINS_CREDENTIALS = "redirect_contains_credentials"
    _INSECURE_PRIVATE_NETWORK = "insecure_private_network"
    _INVALID_PRIVATE_NETWORK_ACCESS = "invalid_private_network_access"
    _UNEXPECTED_PRIVATE_NETWORK_ACCESS = "unexpected_private_network_access"
    _NO_CORS_REDIRECT_MODE_NOT_FOLLOW = "no_cors_redirect_mode_not_follow"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CorsErrorStatus(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> CorsErrorStatus:
        return self

    @classmethod
    def from_json(cls, value: None) -> CorsErrorStatus:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ServiceWorkerResponseSource(str, enum.Enum):
    """Source of serviceworker response."""

    CACHE_STORAGE = "cache-storage"
    HTTP_CACHE = "http-cache"
    FALLBACK_CODE = "fallback-code"
    NETWORK = "network"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class TrustTokenParams(None):
    """Determines what type of Trust Token operation is executed and depending on the type, some additional parameters.

    The values
    are specified in third_party/blink/renderer/core/fetch/trust_token.idl.
    """

    def to_json(self) -> TrustTokenParams:
        return self

    @classmethod
    def from_json(cls, value: None) -> TrustTokenParams:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class TrustTokenOperationType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _ISSUANCE = "issuance"
    _REDEMPTION = "redemption"
    _SIGNING = "signing"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class AlternateProtocolUsage(str, enum.Enum):
    """The reason why Chrome uses a specific transport protocol for HTTP semantics."""

    ALTERNATIVE_JOB_WON_WITHOUT_RACE = "alternative_job_won_without_race"
    ALTERNATIVE_JOB_WON_RACE = "alternative_job_won_race"
    MAIN_JOB_WON_RACE = "main_job_won_race"
    MAPPING_MISSING = "mapping_missing"
    BROKEN = "broken"
    DNS_ALPN_H3_JOB_WON_WITHOUT_RACE = "dns_alpn_h3_job_won_without_race"
    DNS_ALPN_H3_JOB_WON_RACE = "dns_alpn_h3_job_won_race"
    UNSPECIFIED_REASON = "unspecified_reason"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class Response(None):
    """HTTP response data."""

    def to_json(self) -> Response:
        return self

    @classmethod
    def from_json(cls, value: None) -> Response:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class WebSocketRequest(None):
    """WebSocket request data."""

    def to_json(self) -> WebSocketRequest:
        return self

    @classmethod
    def from_json(cls, value: None) -> WebSocketRequest:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class WebSocketResponse(None):
    """WebSocket response data."""

    def to_json(self) -> WebSocketResponse:
        return self

    @classmethod
    def from_json(cls, value: None) -> WebSocketResponse:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class WebSocketFrame(None):
    """WebSocket message data.

    This represents an entire WebSocket message, not just a fragmented frame as the name suggests.
    """

    def to_json(self) -> WebSocketFrame:
        return self

    @classmethod
    def from_json(cls, value: None) -> WebSocketFrame:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CachedResource(None):
    """Information about the cached resource."""

    def to_json(self) -> CachedResource:
        return self

    @classmethod
    def from_json(cls, value: None) -> CachedResource:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Initiator(None):
    """Information about the request initiator."""

    def to_json(self) -> Initiator:
        return self

    @classmethod
    def from_json(cls, value: None) -> Initiator:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Cookie(None):
    """Cookie object."""

    def to_json(self) -> Cookie:
        return self

    @classmethod
    def from_json(cls, value: None) -> Cookie:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SetCookieBlockedReason(str, enum.Enum):
    """Types of reasons why a cookie may not be stored from a response."""

    _SECURE_ONLY = "secure_only"
    _SAME_SITE_STRICT = "same_site_strict"
    _SAME_SITE_LAX = "same_site_lax"
    _SAME_SITE_UNSPECIFIED_TREATED_AS_LAX = "same_site_unspecified_treated_as_lax"
    _SAME_SITE_NONE_INSECURE = "same_site_none_insecure"
    _USER_PREFERENCES = "user_preferences"
    _THIRD_PARTY_BLOCKED_IN_FIRST_PARTY_SET = "third_party_blocked_in_first_party_set"
    _SYNTAX_ERROR = "syntax_error"
    _SCHEME_NOT_SUPPORTED = "scheme_not_supported"
    _OVERWRITE_SECURE = "overwrite_secure"
    _INVALID_DOMAIN = "invalid_domain"
    _INVALID_PREFIX = "invalid_prefix"
    _UNKNOWN_ERROR = "unknown_error"
    _SCHEMEFUL_SAME_SITE_STRICT = "schemeful_same_site_strict"
    _SCHEMEFUL_SAME_SITE_LAX = "schemeful_same_site_lax"
    _SCHEMEFUL_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX = "schemeful_same_site_unspecified_treated_as_lax"
    _SAME_PARTY_FROM_CROSS_PARTY_CONTEXT = "same_party_from_cross_party_context"
    _SAME_PARTY_CONFLICTS_WITH_OTHER_ATTRIBUTES = "same_party_conflicts_with_other_attributes"
    _NAME_VALUE_PAIR_EXCEEDS_MAX_SIZE = "name_value_pair_exceeds_max_size"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookieBlockedReason(str, enum.Enum):
    """Types of reasons why a cookie may not be sent with a request."""

    _SECURE_ONLY = "secure_only"
    _NOT_ON_PATH = "not_on_path"
    _DOMAIN_MISMATCH = "domain_mismatch"
    _SAME_SITE_STRICT = "same_site_strict"
    _SAME_SITE_LAX = "same_site_lax"
    _SAME_SITE_UNSPECIFIED_TREATED_AS_LAX = "same_site_unspecified_treated_as_lax"
    _SAME_SITE_NONE_INSECURE = "same_site_none_insecure"
    _USER_PREFERENCES = "user_preferences"
    _THIRD_PARTY_BLOCKED_IN_FIRST_PARTY_SET = "third_party_blocked_in_first_party_set"
    _UNKNOWN_ERROR = "unknown_error"
    _SCHEMEFUL_SAME_SITE_STRICT = "schemeful_same_site_strict"
    _SCHEMEFUL_SAME_SITE_LAX = "schemeful_same_site_lax"
    _SCHEMEFUL_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX = "schemeful_same_site_unspecified_treated_as_lax"
    _SAME_PARTY_FROM_CROSS_PARTY_CONTEXT = "same_party_from_cross_party_context"
    _NAME_VALUE_PAIR_EXCEEDS_MAX_SIZE = "name_value_pair_exceeds_max_size"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class BlockedSetCookieWithReason(None):
    """A cookie which was not stored from a response with the corresponding reason."""

    def to_json(self) -> BlockedSetCookieWithReason:
        return self

    @classmethod
    def from_json(cls, value: None) -> BlockedSetCookieWithReason:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class BlockedCookieWithReason(None):
    """A cookie with was not sent with a request with the corresponding reason."""

    def to_json(self) -> BlockedCookieWithReason:
        return self

    @classmethod
    def from_json(cls, value: None) -> BlockedCookieWithReason:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CookieParam(None):
    """Cookie parameter object."""

    def to_json(self) -> CookieParam:
        return self

    @classmethod
    def from_json(cls, value: None) -> CookieParam:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class AuthChallenge(None):
    """Authorization challenge for HTTP status code 401 or 407."""

    def to_json(self) -> AuthChallenge:
        return self

    @classmethod
    def from_json(cls, value: None) -> AuthChallenge:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class AuthChallengeResponse(None):
    """Response to an AuthChallenge."""

    def to_json(self) -> AuthChallengeResponse:
        return self

    @classmethod
    def from_json(cls, value: None) -> AuthChallengeResponse:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class InterceptionStage(str, enum.Enum):
    """Stages of the interception to begin intercepting.

    Request will intercept before the request is sent. Response will intercept after the response is received.
    """

    _REQUEST = "request"
    _HEADERS_RECEIVED = "headers_received"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class RequestPattern(None):
    """Request pattern for interception."""

    def to_json(self) -> RequestPattern:
        return self

    @classmethod
    def from_json(cls, value: None) -> RequestPattern:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SignedExchangeSignature(None):
    """Information about a signed exchange signature.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1
    """

    def to_json(self) -> SignedExchangeSignature:
        return self

    @classmethod
    def from_json(cls, value: None) -> SignedExchangeSignature:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SignedExchangeHeader(None):
    """Information about a signed exchange header.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    """

    def to_json(self) -> SignedExchangeHeader:
        return self

    @classmethod
    def from_json(cls, value: None) -> SignedExchangeHeader:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SignedExchangeErrorField(str, enum.Enum):
    """Field type for a signed exchange related error."""

    SIGNATURE_SIG = "signature_sig"
    SIGNATURE_INTEGRITY = "signature_integrity"
    SIGNATURE_CERT_URL = "signature_cert_url"
    SIGNATURE_CERT_SHA256 = "signature_cert_sha256"
    SIGNATURE_VALIDITY_URL = "signature_validity_url"
    SIGNATURE_TIMESTAMPS = "signature_timestamps"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class SignedExchangeError(None):
    """Information about a signed exchange response."""

    def to_json(self) -> SignedExchangeError:
        return self

    @classmethod
    def from_json(cls, value: None) -> SignedExchangeError:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SignedExchangeInfo(None):
    """Information about a signed exchange response."""

    def to_json(self) -> SignedExchangeInfo:
        return self

    @classmethod
    def from_json(cls, value: None) -> SignedExchangeInfo:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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

    _ALLOW = "allow"
    _BLOCK_FROM_INSECURE_TO_MORE_PRIVATE = "block_from_insecure_to_more_private"
    _WARN_FROM_INSECURE_TO_MORE_PRIVATE = "warn_from_insecure_to_more_private"
    _PREFLIGHT_BLOCK = "preflight_block"
    _PREFLIGHT_WARN = "preflight_warn"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class IPAddressSpace(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _LOCAL = "local"
    _PRIVATE = "private"
    _PUBLIC = "public"
    _UNKNOWN = "unknown"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ConnectTiming(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> ConnectTiming:
        return self

    @classmethod
    def from_json(cls, value: None) -> ConnectTiming:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ClientSecurityState(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> ClientSecurityState:
        return self

    @classmethod
    def from_json(cls, value: None) -> ClientSecurityState:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CrossOriginOpenerPolicyValue(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _SAME_ORIGIN = "same_origin"
    _SAME_ORIGIN_ALLOW_POPUPS = "same_origin_allow_popups"
    _RESTRICT_PROPERTIES = "restrict_properties"
    _UNSAFE_NONE = "unsafe_none"
    _SAME_ORIGIN_PLUS_COEP = "same_origin_plus_coep"
    _RESTRICT_PROPERTIES_PLUS_COEP = "restrict_properties_plus_coep"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CrossOriginOpenerPolicyStatus(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> CrossOriginOpenerPolicyStatus:
        return self

    @classmethod
    def from_json(cls, value: None) -> CrossOriginOpenerPolicyStatus:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CrossOriginEmbedderPolicyValue(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _NONE = "none"
    _CREDENTIALLESS = "credentialless"
    _REQUIRE_CORP = "require_corp"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CrossOriginEmbedderPolicyStatus(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> CrossOriginEmbedderPolicyStatus:
        return self

    @classmethod
    def from_json(cls, value: None) -> CrossOriginEmbedderPolicyStatus:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SecurityIsolationStatus(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> SecurityIsolationStatus:
        return self

    @classmethod
    def from_json(cls, value: None) -> SecurityIsolationStatus:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ReportStatus(str, enum.Enum):
    """The status of a Reporting API report."""

    _QUEUED = "queued"
    _PENDING = "pending"
    _MARKED_FOR_REMOVAL = "marked_for_removal"
    _SUCCESS = "success"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ReportId(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> ReportId:
        return self

    @classmethod
    def from_json(cls, value: str) -> ReportId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ReportingApiReport(None):
    """An object representing a report generated by the Reporting API."""

    def to_json(self) -> ReportingApiReport:
        return self

    @classmethod
    def from_json(cls, value: None) -> ReportingApiReport:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ReportingApiEndpoint(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> ReportingApiEndpoint:
        return self

    @classmethod
    def from_json(cls, value: None) -> ReportingApiEndpoint:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class LoadNetworkResourcePageResult(None):
    """An object providing the result of a network resource load."""

    def to_json(self) -> LoadNetworkResourcePageResult:
        return self

    @classmethod
    def from_json(cls, value: None) -> LoadNetworkResourcePageResult:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class LoadNetworkResourceOptions(None):
    """An options object that may be extended later to better support CORS, CORB and streaming."""

    def to_json(self) -> LoadNetworkResourceOptions:
        return self

    @classmethod
    def from_json(cls, value: None) -> LoadNetworkResourceOptions:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("Network.dataReceived")
class DataReceived:
    """Fired when data chunk was received over the network."""

    request_id: RequestId
    timestamp: MonotonicTime
    data_length: int
    encoded_data_length: int


@dataclass
@memoize_event("Network.eventSourceMessageReceived")
class EventSourceMessageReceived:
    """Fired when EventSource message is received."""

    request_id: RequestId
    timestamp: MonotonicTime
    event_name: str
    event_id: str
    data: str


@dataclass
@memoize_event("Network.loadingFailed")
class LoadingFailed:
    """Fired when HTTP request has failed to load."""

    request_id: RequestId
    timestamp: MonotonicTime
    type: ResourceType
    error_text: str
    canceled: typing.Optional[bool]
    blocked_reason: BlockedReason
    cors_error_status: CorsErrorStatus


@dataclass
@memoize_event("Network.loadingFinished")
class LoadingFinished:
    """Fired when HTTP request has finished loading."""

    request_id: RequestId
    timestamp: MonotonicTime
    encoded_data_length: float
    should_report_corb_blocking: typing.Optional[bool]


@dataclass
@memoize_event("Network.requestIntercepted")
class RequestIntercepted:
    """Details of an intercepted HTTP request, which must be either allowed, blocked, modified or mocked.

    Deprecated, use Fetch.requestPaused instead.
    """

    interception_id: InterceptionId
    request: Request
    frame_id: page.FrameId
    resource_type: ResourceType
    is_navigation_request: bool
    is_download: typing.Optional[bool]
    redirect_url: typing.Optional[str]
    auth_challenge: AuthChallenge
    response_error_reason: ErrorReason
    response_status_code: typing.Optional[int]
    response_headers: Headers
    request_id: RequestId


@dataclass
@memoize_event("Network.requestServedFromCache")
class RequestServedFromCache:
    """Fired if request ended up loading from cache."""

    request_id: RequestId


@dataclass
@memoize_event("Network.requestWillBeSent")
class RequestWillBeSent:
    """Fired when page is about to send HTTP request."""

    request_id: RequestId
    loader_id: LoaderId
    document_url: str
    request: Request
    timestamp: MonotonicTime
    wall_time: TimeSinceEpoch
    initiator: Initiator
    redirect_has_extra_info: bool
    redirect_response: Response
    type: ResourceType
    frame_id: typing.Optional[page.FrameId]
    has_user_gesture: typing.Optional[bool]


@dataclass
@memoize_event("Network.resourceChangedPriority")
class ResourceChangedPriority:
    """Fired when resource loading priority is changed."""

    request_id: RequestId
    new_priority: ResourcePriority
    timestamp: MonotonicTime


@dataclass
@memoize_event("Network.signedExchangeReceived")
class SignedExchangeReceived:
    """Fired when a signed exchange was received over the network."""

    request_id: RequestId
    info: SignedExchangeInfo


@dataclass
@memoize_event("Network.responseReceived")
class ResponseReceived:
    """Fired when HTTP response is available."""

    request_id: RequestId
    loader_id: LoaderId
    timestamp: MonotonicTime
    type: ResourceType
    response: Response
    has_extra_info: bool
    frame_id: typing.Optional[page.FrameId]


@dataclass
@memoize_event("Network.webSocketClosed")
class WebSocketClosed:
    """Fired when WebSocket is closed."""

    request_id: RequestId
    timestamp: MonotonicTime


@dataclass
@memoize_event("Network.webSocketCreated")
class WebSocketCreated:
    """Fired upon WebSocket creation."""

    request_id: RequestId
    url: str
    initiator: Initiator


@dataclass
@memoize_event("Network.webSocketFrameError")
class WebSocketFrameError:
    """Fired when WebSocket message error occurs."""

    request_id: RequestId
    timestamp: MonotonicTime
    error_message: str


@dataclass
@memoize_event("Network.webSocketFrameReceived")
class WebSocketFrameReceived:
    """Fired when WebSocket message is received."""

    request_id: RequestId
    timestamp: MonotonicTime
    response: WebSocketFrame


@dataclass
@memoize_event("Network.webSocketFrameSent")
class WebSocketFrameSent:
    """Fired when WebSocket message is sent."""

    request_id: RequestId
    timestamp: MonotonicTime
    response: WebSocketFrame


@dataclass
@memoize_event("Network.webSocketHandshakeResponseReceived")
class WebSocketHandshakeResponseReceived:
    """Fired when WebSocket handshake response becomes available."""

    request_id: RequestId
    timestamp: MonotonicTime
    response: WebSocketResponse


@dataclass
@memoize_event("Network.webSocketWillSendHandshakeRequest")
class WebSocketWillSendHandshakeRequest:
    """Fired when WebSocket is about to initiate handshake."""

    request_id: RequestId
    timestamp: MonotonicTime
    wall_time: TimeSinceEpoch
    request: WebSocketRequest


@dataclass
@memoize_event("Network.webTransportCreated")
class WebTransportCreated:
    """Fired upon WebTransport creation."""

    transport_id: RequestId
    url: str
    timestamp: MonotonicTime
    initiator: Initiator


@dataclass
@memoize_event("Network.webTransportConnectionEstablished")
class WebTransportConnectionEstablished:
    """Fired when WebTransport handshake is finished."""

    transport_id: RequestId
    timestamp: MonotonicTime


@dataclass
@memoize_event("Network.webTransportClosed")
class WebTransportClosed:
    """Fired when WebTransport is disposed."""

    transport_id: RequestId
    timestamp: MonotonicTime


@dataclass
@memoize_event("Network.requestWillBeSentExtraInfo")
class RequestWillBeSentExtraInfo:
    """Fired when additional information about a requestWillBeSent event is available from the network stack.

    Not every requestWillBeSent event will have an additional requestWillBeSentExtraInfo fired for it, and there is no
    guarantee whether requestWillBeSent or requestWillBeSentExtraInfo will be fired first for the same request.
    """

    request_id: RequestId
    associated_cookies: typing.List[BlockedCookieWithReason]
    headers: Headers
    connect_timing: ConnectTiming
    client_security_state: ClientSecurityState
    site_has_cookie_in_other_partition: typing.Optional[bool]


@dataclass
@memoize_event("Network.responseReceivedExtraInfo")
class ResponseReceivedExtraInfo:
    """Fired when additional information about a responseReceived event is available from the network stack.

    Not every responseReceived event will have an additional responseReceivedExtraInfo for it, and
    responseReceivedExtraInfo may be fired before or after responseReceived.
    """

    request_id: RequestId
    blocked_cookies: typing.List[BlockedSetCookieWithReason]
    headers: Headers
    resource_ip_address_space: IPAddressSpace
    status_code: int
    headers_text: typing.Optional[str]
    cookie_partition_key: typing.Optional[str]
    cookie_partition_key_opaque: typing.Optional[bool]


@dataclass
@memoize_event("Network.trustTokenOperationDone")
class TrustTokenOperationDone:
    """Fired exactly once for each Trust Token operation.

    Depending on the type of the operation and whether the operation succeeded or failed, the event is fired before the
    corresponding request was sent or after the response was received.
    """

    status: typing.Literal[
        "ok",
        "invalid_argument",
        "failed_precondition",
        "resource_exhausted",
        "already_exists",
        "unavailable",
        "unauthorized",
        "bad_response",
        "internal_error",
        "unknown_error",
        "fulfilled_locally",
    ]
    type: TrustTokenOperationType
    request_id: RequestId
    top_level_origin: typing.Optional[str]
    issuer_origin: typing.Optional[str]
    issued_token_count: typing.Optional[int]


@dataclass
@memoize_event("Network.subresourceWebBundleMetadataReceived")
class SubresourceWebBundleMetadataReceived:
    """Fired once when parsing the .wbn file has succeeded.

    The event contains the information about the web bundle contents.
    """

    request_id: RequestId
    urls: typing.List[str]


@dataclass
@memoize_event("Network.subresourceWebBundleMetadataError")
class SubresourceWebBundleMetadataError:
    """Fired once when parsing the .wbn file has failed."""

    request_id: RequestId
    error_message: str


@dataclass
@memoize_event("Network.subresourceWebBundleInnerResponseParsed")
class SubresourceWebBundleInnerResponseParsed:
    """Fired when handling requests for resources within a .wbn file.

    Note: this will only be fired for resources that are requested by the webpage.
    """

    inner_request_id: RequestId
    inner_request_url: str
    bundle_request_id: RequestId


@dataclass
@memoize_event("Network.subresourceWebBundleInnerResponseError")
class SubresourceWebBundleInnerResponseError:
    """Fired when request for resources within a .wbn file failed."""

    inner_request_id: RequestId
    inner_request_url: str
    error_message: str
    bundle_request_id: RequestId


@dataclass
@memoize_event("Network.reportingApiReportAdded")
class ReportingApiReportAdded:
    """Is sent whenever a new report is added.

    And after 'enableReportingApi' for all existing reports.
    """

    report: ReportingApiReport


@dataclass
@memoize_event("Network.reportingApiReportUpdated")
class ReportingApiReportUpdated:
    """Description is missing from the devtools protocol document."""

    report: ReportingApiReport


@dataclass
@memoize_event("Network.reportingApiEndpointsChangedForOrigin")
class ReportingApiEndpointsChangedForOrigin:
    """Description is missing from the devtools protocol document."""

    origin: str
    endpoints: typing.List[ReportingApiEndpoint]


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
    """Response to Network.requestIntercepted which either modifies the request to continue with any modifications, or
    blocks it, or completes it with the provided response bytes.

    If a network fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted event
    will be sent with the same InterceptionId. Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and
    Fetch.failRequest instead. # noqa
    """
    ...


async def delete_cookies() -> None:
    """Deletes browser cookies with matching name and url or domain/path pair.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables network tracking, prevents network events from being sent to the client.

    # noqa
    """
    ...


async def emulate_network_conditions() -> None:
    """Activates emulation of network conditions.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables network tracking, network events will now be delivered to the client.

    # noqa
    """
    ...


async def get_all_cookies() -> None:
    """Returns all browser cookies.

    Depending on the backend support, will return detailed cookie information in the `cookies` field. Deprecated. Use
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

    Depending on the backend support, will return detailed cookie information in the `cookies` field. # noqa
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

    Note that after this command, the intercepted request can't be continued as is -- you either need to cancel it or to
    provide the response body. The stream only supports sequential read, IO.read will fail if the position is specified.
    # noqa
    """
    ...


async def replay_xhr() -> None:
    """This method sends a new XMLHttpRequest which is identical to the original one.

    The following parameters should be identical: method, url, async, request body, extra headers, withCredentials
    attribute, user, password. # noqa
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
    """Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.

    # noqa
    """
    ...


async def set_cookies() -> None:
    """Sets given cookies.

    # noqa
    """
    ...


async def set_extra_http_headers() -> None:
    """Specifies whether to always send extra HTTP headers with the requests from this page.

    # noqa
    """
    ...


async def set_attach_debug_stack() -> None:
    """Specifies whether to attach a page script stack id in requests # noqa."""
    ...


async def set_request_interception() -> None:
    """Sets the requests to intercept that match the provided patterns and optionally resource types.

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
    """Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the
    client.

    Enabling triggers 'reportingApiReportAdded' for all existing reports. # noqa
    """
    ...


async def load_network_resource() -> None:
    """Fetches the resource and returns the content.

    # noqa
    """
    ...
