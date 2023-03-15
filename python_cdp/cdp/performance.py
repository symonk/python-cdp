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


@dataclass
class Metric:
    """Run-time execution metric."""

    #: Metric name.# noqa
    name: str
    #: Metric value.# noqa
    value: float


def disable() -> None:
    """Disable collecting and reporting metrics.

    # noqa
    """
    ...


def enable() -> None:
    """Enable collecting and reporting metrics.

    # noqa
    """
    ...


def set_time_domain() -> None:
    """Sets time domain to use for collecting and reporting duration metrics.

    Note that this must be called before enabling metrics collection.
    Calling this method while metrics collection is enabled returns an
    error. # noqa
    """
    ...


def get_metrics() -> None:
    """Retrieve current values of run-time metrics.

    # noqa
    """
    ...
