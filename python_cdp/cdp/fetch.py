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
    urlPattern: typing.Optional[str] = None
    #: If set, only requests for matching resource types will be intercepted.# noqa
    resourceType: typing.Optional[network.ResourceType] = None
    #: Stage at which to begin intercepting requests. Default is Request.# noqa
    requestStage: typing.Optional[RequestStage] = None


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
