# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Autofill`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Autofill/

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CreditCard:
    """Description is missing from the devtools protocol document."""

    # 16-digit credit card number. # noqa
    number: str
    # Name of the credit card owner. # noqa
    name: str
    # 2-digit expiry month. # noqa
    expiry_month: str
    # 4-digit expiry year. # noqa
    expiry_year: str
    # 3-digit card verification code. # noqa
    cvc: str


@dataclass
class AddressField:
    """Description is missing from the devtools protocol document."""

    # address field name, for example GIVEN_NAME. # noqa
    name: str
    # address field name, for example Jon Doe. # noqa
    value: str


@dataclass
class Address:
    """Description is missing from the devtools protocol document."""

    # fields and values defining a test address. # noqa
    fields: AddressField


async def trigger() -> None:
    """Trigger autofill on a form identified by the fieldId.

    If the field and related form cannot be autofilled, returns an error. # noqa
    """
    ...


async def set_addresses() -> None:
    """Set addresses so that developers can verify their forms implementation.

    # noqa
    """
    ...
