# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Target`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Target/

from __future__ import annotations

from dataclasses import dataclass


class TargetID(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


class SessionID(str):
    """Unique identifier of attached debugging session."""

    def to_json(self) -> str:
        return self


@dataclass
class TargetInfo:
    """Description is missing from the devtools protocol document."""


@dataclass
class FilterEntry:
    """A filter used by target query/discovery/auto-attach operations."""


@dataclass
class TargetFilter:
    """The entries in TargetFilter are matched sequentially against targets and
    the first entry that matches determines if the target is included or not,
    depending on the value of `exclude` field in the entry. If filter is not
    specified, the one assumed is.

    [{type: "browser", exclude: true}, {type: "tab", exclude: true}, {}]
    (i.e. include everything but `browser` and `tab`).
    """


@dataclass
class RemoteLocation:
    """Description is missing from the devtools protocol document."""
