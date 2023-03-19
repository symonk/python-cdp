# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Schema`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Schema/

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Domain:
    """Description of the protocol domain."""

    # Domain name.# noqa
    name: str
    # Domain version.# noqa
    version: str


async def get_domains() -> None:
    """Returns supported domains.

    # noqa
    """
    ...
