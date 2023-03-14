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

import enum
from dataclasses import dataclass


class AXNodeId(str):
    """Unique accessibility node identifier."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class AXValueType(str, enum.Enum):
    """Enum of possible property types."""

    BOOLEAN = "boolean"
    TRISTATE = "tristate"
    BOOLEANORUNDEFINED = "booleanOrUndefined"
    IDREF = "idref"
    IDREFLIST = "idrefList"
    INTEGER = "integer"
    NODE = "node"
    NODELIST = "nodeList"
    NUMBER = "number"
    STRING = "string"
    COMPUTEDSTRING = "computedString"
    TOKEN = "token"
    TOKENLIST = "tokenList"
    DOMRELATION = "domRelation"
    ROLE = "role"
    INTERNALROLE = "internalRole"
    VALUEUNDEFINED = "valueUndefined"


class AXValueSourceType(str, enum.Enum):
    """Enum of possible property sources."""

    ATTRIBUTE = "attribute"
    IMPLICIT = "implicit"
    STYLE = "style"
    CONTENTS = "contents"
    PLACEHOLDER = "placeholder"
    RELATEDELEMENT = "relatedElement"


class AXValueNativeSourceType(str, enum.Enum):
    """Enum of possible native property sources (as a subtype of a particular
    AXValueSourceType)."""

    DESCRIPTION = "description"
    FIGCAPTION = "figcaption"
    LABEL = "label"
    LABELFOR = "labelfor"
    LABELWRAPPED = "labelwrapped"
    LEGEND = "legend"
    RUBYANNOTATION = "rubyannotation"
    TABLECAPTION = "tablecaption"
    TITLE = "title"
    OTHER = "other"


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


class AXPropertyName(str, enum.Enum):
    """Values of AXProperty name:

    - from 'busy' to 'roledescription': states which apply to every AX node
    - from 'live' to 'root': attributes which apply to nodes in live regions
    - from 'autocomplete' to 'valuetext': attributes which apply to widgets
    - from 'checked' to 'selected': states which apply to widgets
    - from 'activedescendant' to 'owns' - relationships between elements other than parent/child/sibling.
    """

    BUSY = "busy"
    DISABLED = "disabled"
    EDITABLE = "editable"
    FOCUSABLE = "focusable"
    FOCUSED = "focused"
    HIDDEN = "hidden"
    HIDDENROOT = "hiddenRoot"
    INVALID = "invalid"
    KEYSHORTCUTS = "keyshortcuts"
    SETTABLE = "settable"
    ROLEDESCRIPTION = "roledescription"
    LIVE = "live"
    ATOMIC = "atomic"
    RELEVANT = "relevant"
    ROOT = "root"
    AUTOCOMPLETE = "autocomplete"
    HASPOPUP = "hasPopup"
    LEVEL = "level"
    MULTISELECTABLE = "multiselectable"
    ORIENTATION = "orientation"
    MULTILINE = "multiline"
    READONLY = "readonly"
    REQUIRED = "required"
    VALUEMIN = "valuemin"
    VALUEMAX = "valuemax"
    VALUETEXT = "valuetext"
    CHECKED = "checked"
    EXPANDED = "expanded"
    MODAL = "modal"
    PRESSED = "pressed"
    SELECTED = "selected"
    ACTIVEDESCENDANT = "activedescendant"
    CONTROLS = "controls"
    DESCRIBEDBY = "describedby"
    DETAILS = "details"
    ERRORMESSAGE = "errormessage"
    FLOWTO = "flowto"
    LABELLEDBY = "labelledby"
    OWNS = "owns"


@dataclass
class AXNode:
    """A node in the accessibility tree."""
