# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Performance`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Performance/

from __future__ import annotations
from dataclasses import dataclass
import typing




@dataclass
class Metric:
    """ Run-time execution metric. """
    #: Metric name.# noqa
    name: str
    #: Metric value.# noqa
    value: float
