# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Fetch`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Fetch/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import network


class RequestId(str):
    """Unique request identifier."""

    def to_json(self) -> RequestId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class RequestStage(str, enum.Enum):
    """Stages of the request to handle.

    Request will intercept before the request is sent. Response will
    intercept after the response is received (but before response body
    is received).
    """

    REQUEST = "Request"
    RESPONSE = "Response"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class RequestPattern:
    """Description is missing from the devtools protocol document."""

    #: Wildcards (`'*'` -> zero or more, `'?'` -> exactly one) are allowed.Escape character is backslash. Omitting is equivalent to `"*"`.# noqa
    url_pattern: typing.Optional[str] = None
    #: If set, only requests for matching resource types will be intercepted.# noqa
    resource_type: typing.Optional[network.ResourceType] = None
    #: Stage at which to begin intercepting requests. Default is Request.# noqa
    request_stage: typing.Optional[RequestStage] = None


@dataclass
class HeaderEntry:
    """Response HTTP header entry."""

    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    value: str


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


def disable() -> None:
    """Disables the fetch domain.

    # noqa
    """
    ...


def enable() -> None:
    """Enables issuing of requestPaused events.

    A request will be paused until client calls one of failRequest,
    fulfillRequest or continueRequest/continueWithAuth. # noqa
    """
    ...


def fail_request() -> None:
    """Causes the request to fail with specified reason.

    # noqa
    """
    ...


def fulfill_request() -> None:
    """Provides response to the request.

    # noqa
    """
    ...


def continue_request() -> None:
    """Continues the request, optionally modifying some of its parameters.

    # noqa
    """
    ...


def continue_with_auth() -> None:
    """Continues a request supplying authChallengeResponse following
    authRequired event.

    # noqa
    """
    ...


def continue_response() -> None:
    """Continues loading of the paused response, optionally modifying the
    response headers.

    If either responseCode or headers are modified, all of them must be
    present. # noqa
    """
    ...


def get_response_body() -> None:
    """Causes the body of the response to be received from the server and
    returned as a single string.

    May only be issued for a request that is paused in the Response
    stage and is mutually exclusive with
    takeResponseBodyForInterceptionAsStream. Calling other methods that
    affect the request or disabling fetch domain before body is received
    results in an undefined behavior. # noqa
    """
    ...


def take_response_body_as_stream() -> None:
    """Returns a handle to the stream representing the response body.

    The request must be paused in the HeadersReceived stage. Note that
    after this command the request can't be continued as is -- client
    either needs to cancel it or to provide the response body. The
    stream only supports sequential read, IO.read will fail if the
    position is specified. This method is mutually exclusive with
    getResponseBody. Calling other methods that affect the request or
    disabling fetch domain before body is received results in an
    undefined behavior. # noqa
    """
    ...
