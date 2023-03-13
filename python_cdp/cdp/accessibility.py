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


@dataclass
class AXNodeId:
    """Unique accessibility node identifier."""


@dataclass
class AXValueType:
    """Enum of possible property types."""


@dataclass
class AXValueSourceType:
    """Enum of possible property sources."""


@dataclass
class AXValueNativeSourceType:
    """Enum of possible native property sources (as a subtype of a particular
    AXValueSourceType)."""


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


@dataclass
class AXPropertyName:
    """Values of AXProperty name:

    - from 'busy' to 'roledescription': states which apply to every AX node
    - from 'live' to 'root': attributes which apply to nodes in live regions
    - from 'autocomplete' to 'valuetext': attributes which apply to widgets
    - from 'checked' to 'selected': states which apply to widgets
    - from 'activedescendant' to 'owns' - relationships between elements other than parent/child/sibling.
    """


@dataclass
class AXNode:
    """A node in the accessibility tree."""
