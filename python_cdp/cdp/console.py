# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Console`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Console/

from __future__ import annotations

import typing
from dataclasses import dataclass

from .utils import memoize_event


@dataclass
class ConsoleMessage:
    """Console message."""

    # Message source.# noqa


str
# Message severity.# noqa
str
# Message text.# noqa
str
# URL of the message origin.# noqa
typing.Optional[str]
# Line number in the resource that generated this message (1-based).# noqa
typing.Optional[int]
# Column number in the resource that generated this message (1-based).# noqa
typing.Optional[int]


@dataclass
@memoize_event("Console.messageAdded")
class MessageAdded:
    """Issued when new console message is added."""

    message: ConsoleMessage


async def clear_messages() -> None:
    """Does nothing.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables console domain, prevents further console messages from being reported to the client.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables console domain, sends the messages collected so far to the client by means of the `messageAdded`
    notification.

    # noqa
    """
    ...
