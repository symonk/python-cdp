# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Cast`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Cast/

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Sink:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.
    name: str
    #: Description is missing from the devtools protocol document.
    id: str
    #: Text describing the current session. Present only if there is an activesession on the sink.
    session: str
