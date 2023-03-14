# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Accessibility`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Accessibility/

from __future__ import annotations

from dataclasses import dataclass


class AXNodeId(str):
    """Unique accessibility node identifier."""

    def to_json(self) -> str:
        return self


class AXValueType(str):
    """Enum of possible property types."""

    def to_json(self) -> str:
        return self


class AXValueSourceType(str):
    """Enum of possible property sources."""

    def to_json(self) -> str:
        return self


class AXValueNativeSourceType(str):
    """Enum of possible native property sources (as a subtype of a particular
    AXValueSourceType)."""

    def to_json(self) -> str:
        return self


@dataclass
class AXValueSource:
    """A single source for a computed AX property."""


@dataclass
class AXRelatedNode:
    """Description is missing from the devtools protocol document."""


@dataclass
class AXProperty:
    """Description is missing from the devtools protocol document."""


@dataclass
class AXValue:
    """A single computed AX property."""


class AXPropertyName(str):
    """Values of AXProperty name:

    - from 'busy' to 'roledescription': states which apply to every AX node
    - from 'live' to 'root': attributes which apply to nodes in live regions
    - from 'autocomplete' to 'valuetext': attributes which apply to widgets
    - from 'checked' to 'selected': states which apply to widgets
    - from 'activedescendant' to 'owns' - relationships between elements other than parent/child/sibling.
    """

    def to_json(self) -> str:
        return self


@dataclass
class AXNode:
    """A node in the accessibility tree."""
