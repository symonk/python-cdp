# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `WebAuthn`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/WebAuthn/

from __future__ import annotations
from dataclasses import dataclass

class AuthenticatorId(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
class AuthenticatorProtocol(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
class Ctap2Version(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
class AuthenticatorTransport(str):
    """ Description is missing from the devtools protocol document. """

    def to_json(self) -> str:
        return self
    
@dataclass
class VirtualAuthenticatorOptions:
    """ Description is missing from the devtools protocol document. """

@dataclass
class Credential:
    """ Description is missing from the devtools protocol document. """
