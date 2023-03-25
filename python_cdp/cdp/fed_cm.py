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

from .utils import memoize_event


class LoginState(str, enum.Enum):
    """Whether this is a sign-up or sign-in action for this account, i.e. whether this account has ever been used to
    sign in to this RP before."""

    SIGN_IN = "sign_in"
    SIGN_UP = "sign_up"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class Account:
    """Corresponds to IdentityRequestAccount."""

    # Description is missing from the devtools protocol document. # noqa
    account_id: str
    # Description is missing from the devtools protocol document. # noqa
    email: str
    # Description is missing from the devtools protocol document. # noqa
    name: str
    # Description is missing from the devtools protocol document. # noqa
    given_name: str
    # Description is missing from the devtools protocol document. # noqa
    picture_url: str
    # Description is missing from the devtools protocol document. # noqa
    idp_config_url: str
    # Description is missing from the devtools protocol document. # noqa
    idp_signin_url: str
    # Description is missing from the devtools protocol document. # noqa
    login_state: LoginState
    # These two are only set if the loginState is signUp # noqa
    terms_of_service_url: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    privacy_policy_url: typing.Optional[str]


@dataclass
@memoize_event("FedCm.dialogShown")
class DialogShown:
    """Description is missing from the devtools protocol document."""

    dialog_id: str
    accounts: typing.List[Account]
    title: str
    subtitle: typing.Optional[str]


async def enable() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def disable() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def select_account() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def dismiss_dialog() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def reset_cooldown() -> None:
    """Resets the cooldown time, if any, to allow the next FedCM call to show a dialog even if one was recently
    dismissed by the user.

    # noqa
    """
    ...
