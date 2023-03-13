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

from dataclasses import dataclass


@dataclass
class ResourceType:
    """Resource type as it was perceived by the rendering engine."""

    ...


@dataclass
class LoaderId:
    """Unique loader identifier."""

    ...


@dataclass
class RequestId:
    """Unique request identifier."""

    ...


@dataclass
class InterceptionId:
    """Unique intercepted request identifier."""

    ...


@dataclass
class ErrorReason:
    """Network level fetch failure reason."""

    ...


@dataclass
class TimeSinceEpoch:
    """UTC time in seconds, counted from January 1, 1970."""

    ...


@dataclass
class MonotonicTime:
    """Monotonically increasing time in seconds since an arbitrary point in the
    past."""

    ...


@dataclass
class Headers:
    """Request / response headers as keys / values of JSON object."""

    ...


@dataclass
class ConnectionType:
    """The underlying connection technology that the browser is supposedly
    using."""

    ...


@dataclass
class CookieSameSite:
    """Represents the cookie's 'SameSite' status:

    https://tools.ietf.org/html/draft-west-first-party-cookies
    """

    ...


@dataclass
class CookiePriority:
    """Represents the cookie's 'Priority' status:

    https://tools.ietf.org/html/draft-west-cookie-priority-00
    """

    ...


@dataclass
class CookieSourceScheme:
    """Represents the source scheme of the origin that originally set the
    cookie.

    A value of "Unset" allows protocol clients to emulate legacy cookie
    scope for the scheme. This is a temporary ability and it will be
    removed in the future.
    """

    ...


@dataclass
class ResourceTiming:
    """Timing information for the request."""

    ...


@dataclass
class ResourcePriority:
    """Loading priority of a resource request."""

    ...


@dataclass
class PostDataEntry:
    """Post data entry for HTTP request."""

    ...


@dataclass
class Request:
    """HTTP request data."""

    ...


@dataclass
class SignedCertificateTimestamp:
    """Details of a signed certificate timestamp (SCT)."""

    ...


@dataclass
class SecurityDetails:
    """Security details about a request."""

    ...


@dataclass
class CertificateTransparencyCompliance:
    """Whether the request complied with Certificate Transparency policy."""

    ...


@dataclass
class BlockedReason:
    """The reason why request was blocked."""

    ...


@dataclass
class CorsError:
    """The reason why request was blocked."""

    ...


@dataclass
class CorsErrorStatus:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ServiceWorkerResponseSource:
    """Source of serviceworker response."""

    ...


@dataclass
class TrustTokenParams:
    """Determines what type of Trust Token operation is executed and depending
    on the type, some additional parameters.

    The values
    are specified in third_party/blink/renderer/core/fetch/trust_token.idl.
    """

    ...


@dataclass
class TrustTokenOperationType:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class AlternateProtocolUsage:
    """The reason why Chrome uses a specific transport protocol for HTTP
    semantics."""

    ...


@dataclass
class Response:
    """HTTP response data."""

    ...


@dataclass
class WebSocketRequest:
    """WebSocket request data."""

    ...


@dataclass
class WebSocketResponse:
    """WebSocket response data."""

    ...


@dataclass
class WebSocketFrame:
    """WebSocket message data.

    This represents an entire WebSocket message, not just a fragmented
    frame as the name suggests.
    """

    ...


@dataclass
class CachedResource:
    """Information about the cached resource."""

    ...


@dataclass
class Initiator:
    """Information about the request initiator."""

    ...


@dataclass
class Cookie:
    """Cookie object."""

    ...


@dataclass
class SetCookieBlockedReason:
    """Types of reasons why a cookie may not be stored from a response."""

    ...


@dataclass
class CookieBlockedReason:
    """Types of reasons why a cookie may not be sent with a request."""

    ...


@dataclass
class BlockedSetCookieWithReason:
    """A cookie which was not stored from a response with the corresponding
    reason."""

    ...


@dataclass
class BlockedCookieWithReason:
    """A cookie with was not sent with a request with the corresponding
    reason."""

    ...


@dataclass
class CookieParam:
    """Cookie parameter object."""

    ...


@dataclass
class AuthChallenge:
    """Authorization challenge for HTTP status code 401 or 407."""

    ...


@dataclass
class AuthChallengeResponse:
    """Response to an AuthChallenge."""

    ...


@dataclass
class InterceptionStage:
    """Stages of the interception to begin intercepting.

    Request will intercept before the request is sent. Response will
    intercept after the response is received.
    """

    ...


@dataclass
class RequestPattern:
    """Request pattern for interception."""

    ...


@dataclass
class SignedExchangeSignature:
    """Information about a signed exchange signature.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1
    """

    ...


@dataclass
class SignedExchangeHeader:
    """Information about a signed exchange header.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    """

    ...


@dataclass
class SignedExchangeErrorField:
    """Field type for a signed exchange related error."""

    ...


@dataclass
class SignedExchangeError:
    """Information about a signed exchange response."""

    ...


@dataclass
class SignedExchangeInfo:
    """Information about a signed exchange response."""

    ...


@dataclass
class ContentEncoding:
    """List of content encodings supported by the backend."""

    ...


@dataclass
class PrivateNetworkRequestPolicy:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class IPAddressSpace:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ConnectTiming:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ClientSecurityState:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class CrossOriginOpenerPolicyValue:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class CrossOriginOpenerPolicyStatus:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class CrossOriginEmbedderPolicyValue:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class CrossOriginEmbedderPolicyStatus:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class SecurityIsolationStatus:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ReportStatus:
    """The status of a Reporting API report."""

    ...


@dataclass
class ReportId:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ReportingApiReport:
    """An object representing a report generated by the Reporting API."""

    ...


@dataclass
class ReportingApiEndpoint:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class LoadNetworkResourcePageResult:
    """An object providing the result of a network resource load."""

    ...


@dataclass
class LoadNetworkResourceOptions:
    """An options object that may be extended later to better support CORS,
    CORB and streaming."""

    ...
