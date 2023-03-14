# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Emulation`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Emulation/

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ScreenOrientation:
    """ Screen orientation. """

@dataclass
class DisplayFeature:
    """ Description is missing from the devtools protocol document. """

@dataclass
class MediaFeature:
    """ Description is missing from the devtools protocol document. """

class VirtualTimePolicy(str):
    """ advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to
allow the next delayed task (if any) to run; pause: The virtual time base may not advance;
pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending
resource fetches. """

    def to_json(self) -> str:
        return self
    
@dataclass
class UserAgentBrandVersion:
    """ Used to specify User Agent Cient Hints to emulate. See https://wicg.github.io/ua-client-hints """

@dataclass
class UserAgentMetadata:
    """ Used to specify User Agent Cient Hints to emulate. See https://wicg.github.io/ua-client-hints
Missing optional values will be filled in by the target with what it would normally use. """

class DisabledImageType(str):
    """ Enum of image types that can be disabled. """

    def to_json(self) -> str:
        return self
    