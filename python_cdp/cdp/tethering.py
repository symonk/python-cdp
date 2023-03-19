# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Tethering`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Tethering/

from __future__ import annotations
from dataclasses import dataclass
import typing


from .utils import memoize_event

@dataclass
@memoize_event('Tethering.accepted')
class Accepted:
    """ Informs that port was successfully bound and got a specified connection id. """
    port: int
    connection_id: str



async def bind() -> None:
    """ Request browser port binding. # noqa """
    ...



async def unbind() -> None:
    """ Request browser port unbinding. # noqa """
    ...
