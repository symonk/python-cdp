# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `FedCm`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/FedCm/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass


class LoginState(str, enum.Enum):
    """Whether this is a sign-up or sign-in action for this account, i.e.
    whether this account has ever been used to sign in to this RP before."""

    SIGNIN = "SignIn"
    SIGNUP = "SignUp"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class Account:
    """Corresponds to IdentityRequestAccount."""

    #: Description is missing from the devtools protocol document.# noqa
    accountId: str
    #: Description is missing from the devtools protocol document.# noqa
    email: str
    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    givenName: str
    #: Description is missing from the devtools protocol document.# noqa
    pictureUrl: str
    #: Description is missing from the devtools protocol document.# noqa
    idpConfigUrl: str
    #: Description is missing from the devtools protocol document.# noqa
    idpSigninUrl: str
    #: Description is missing from the devtools protocol document.# noqa
    loginState: LoginState
    #: These two are only set if the loginState is signUp# noqa
    termsOfServiceUrl: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    privacyPolicyUrl: typing.Optional[str] = None
