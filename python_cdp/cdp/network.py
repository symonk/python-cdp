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


class ResourceType(str):
    """Resource type as it was perceived by the rendering engine."""

    def to_json(self) -> str:
        return self


class LoaderId(str):
    """Unique loader identifier."""

    def to_json(self) -> str:
        return self


class RequestId(str):
    """Unique request identifier."""

    def to_json(self) -> str:
        return self


class InterceptionId(str):
    """Unique intercepted request identifier."""

    def to_json(self) -> str:
        return self


class ErrorReason(str):
    """Network level fetch failure reason."""

    def to_json(self) -> str:
        return self


class TimeSinceEpoch(float):
    """UTC time in seconds, counted from January 1, 1970."""

    def to_json(self) -> float:
        return self


class MonotonicTime(float):
    """Monotonically increasing time in seconds since an arbitrary point in the
    past."""

    def to_json(self) -> float:
        return self


@dataclass
class Headers:
    """Request / response headers as keys / values of JSON object."""


class ConnectionType(str):
    """The underlying connection technology that the browser is supposedly
    using."""

    def to_json(self) -> str:
        return self


class CookieSameSite(str):
    """Represents the cookie's 'SameSite' status:

    https://tools.ietf.org/html/draft-west-first-party-cookies
    """

    def to_json(self) -> str:
        return self


class CookiePriority(str):
    """Represents the cookie's 'Priority' status:

    https://tools.ietf.org/html/draft-west-cookie-priority-00
    """

    def to_json(self) -> str:
        return self


class CookieSourceScheme(str):
    """Represents the source scheme of the origin that originally set the
    cookie.

    A value of "Unset" allows protocol clients to emulate legacy cookie
    scope for the scheme. This is a temporary ability and it will be
    removed in the future.
    """

    def to_json(self) -> str:
        return self


@dataclass
class ResourceTiming:
    """Timing information for the request."""


class ResourcePriority(str):
    """Loading priority of a resource request."""

    def to_json(self) -> str:
        return self


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


class CertificateTransparencyCompliance(str):
    """Whether the request complied with Certificate Transparency policy."""

    def to_json(self) -> str:
        return self


class BlockedReason(str):
    """The reason why request was blocked."""

    def to_json(self) -> str:
        return self


class CorsError(str):
    """The reason why request was blocked."""

    def to_json(self) -> str:
        return self


@dataclass
class CorsErrorStatus:
    """Description is missing from the devtools protocol document."""


class ServiceWorkerResponseSource(str):
    """Source of serviceworker response."""

    def to_json(self) -> str:
        return self


@dataclass
class TrustTokenParams:
    """Determines what type of Trust Token operation is executed and depending
    on the type, some additional parameters.

    The values
    are specified in third_party/blink/renderer/core/fetch/trust_token.idl.
    """


class TrustTokenOperationType(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


class AlternateProtocolUsage(str):
    """The reason why Chrome uses a specific transport protocol for HTTP
    semantics."""

    def to_json(self) -> str:
        return self


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


class SetCookieBlockedReason(str):
    """Types of reasons why a cookie may not be stored from a response."""

    def to_json(self) -> str:
        return self


class CookieBlockedReason(str):
    """Types of reasons why a cookie may not be sent with a request."""

    def to_json(self) -> str:
        return self


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


class InterceptionStage(str):
    """Stages of the interception to begin intercepting.

    Request will intercept before the request is sent. Response will
    intercept after the response is received.
    """

    def to_json(self) -> str:
        return self


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


class SignedExchangeErrorField(str):
    """Field type for a signed exchange related error."""

    def to_json(self) -> str:
        return self


@dataclass
class SignedExchangeError:
    """Information about a signed exchange response."""


@dataclass
class SignedExchangeInfo:
    """Information about a signed exchange response."""


class ContentEncoding(str):
    """List of content encodings supported by the backend."""

    def to_json(self) -> str:
        return self


class PrivateNetworkRequestPolicy(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


class IPAddressSpace(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


@dataclass
class ConnectTiming:
    """Description is missing from the devtools protocol document."""


@dataclass
class ClientSecurityState:
    """Description is missing from the devtools protocol document."""


class CrossOriginOpenerPolicyValue(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


@dataclass
class CrossOriginOpenerPolicyStatus:
    """Description is missing from the devtools protocol document."""


class CrossOriginEmbedderPolicyValue(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


@dataclass
class CrossOriginEmbedderPolicyStatus:
    """Description is missing from the devtools protocol document."""


@dataclass
class SecurityIsolationStatus:
    """Description is missing from the devtools protocol document."""


class ReportStatus(str):
    """The status of a Reporting API report."""

    def to_json(self) -> str:
        return self


class ReportId(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


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
