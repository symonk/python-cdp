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
from dataclasses import dataclass


class RequestId(str):
    """Unique request identifier."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


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


@dataclass
class HeaderEntry:
    """Response HTTP header entry."""


@dataclass
class AuthChallenge:
    """Authorization challenge for HTTP status code 401 or 407."""


@dataclass
class AuthChallengeResponse:
    """Response to an AuthChallenge."""
