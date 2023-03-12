""" *** AUTO GENERATED FILE ***
This file was automatically generated by python-cdp.  Do not modify this file
as it is overwritten when new versions of the devtools protocol are released.  Instead modify the
code generator in https://github.com/symonk/python-cdp (or your fork) instead.  For documentation
on how to modify the generation process refer to the CONTRIBUTING.md file in the root of the
repository."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Headers:
    """Request / response headers as keys / values of JSON object."""


@dataclass
class ResourceTiming:
    """Timing information for the request."""


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


@dataclass
class CorsErrorStatus:
    """Missing description in devtools protocol."""


@dataclass
class TrustTokenParams:
    """Determines what type of Trust Token operation is executed and depending
    on the type, some additional parameters.

    The values
    are specified in third_party/blink/renderer/core/fetch/trust_token.idl.
    """


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


@dataclass
class RequestPattern:
    """Request pattern for interception."""


@dataclass
class SignedExchangeSignature:
    """Information about a signed exchange signature.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-
    signed-exchanges-impl.html#rfc.section.3.1
    """


@dataclass
class SignedExchangeHeader:
    """Information about a signed exchange header.

    https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-
    signed-exchanges-impl.html#cbor-representation
    """


@dataclass
class SignedExchangeError:
    """Information about a signed exchange response."""


@dataclass
class SignedExchangeInfo:
    """Information about a signed exchange response."""


@dataclass
class ConnectTiming:
    """Missing description in devtools protocol."""


@dataclass
class ClientSecurityState:
    """Missing description in devtools protocol."""


@dataclass
class CrossOriginOpenerPolicyStatus:
    """Missing description in devtools protocol."""


@dataclass
class CrossOriginEmbedderPolicyStatus:
    """Missing description in devtools protocol."""


@dataclass
class SecurityIsolationStatus:
    """Missing description in devtools protocol."""


@dataclass
class ReportingApiReport:
    """An object representing a report generated by the Reporting API."""


@dataclass
class ReportingApiEndpoint:
    """Missing description in devtools protocol."""


@dataclass
class LoadNetworkResourcePageResult:
    """An object providing the result of a network resource load."""


@dataclass
class LoadNetworkResourceOptions:
    """An options object that may be extended later to better support CORS,
    CORB and streaming."""
