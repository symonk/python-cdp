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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class AXValueSourceType(str, enum.Enum):
    """Enum of possible property sources."""

    ATTRIBUTE = "attribute"
    IMPLICIT = "implicit"
    STYLE = "style"
    CONTENTS = "contents"
    PLACEHOLDER = "placeholder"
    RELATEDELEMENT = "relatedElement"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class AXValueNativeSourceType(str, enum.Enum):
    """Enum of possible native property sources (as a subtype of a
    particularAXValueSourceType)."""

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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class AXValueSource:
    """A single source for a computed AX property."""

    #: What type of source this is.
    type: str
    #: The value of this property source.
    value: str
    #: The name of the relevant attribute, if any.
    attribute: str
    #: The value of the relevant attribute, if any.
    attributeValue: str
    #: Whether this source is superseded by a higher priority source.
    superseded: str
    #: The native markup source for this value, e.g. a <label> element.
    nativeSource: str
    #: The value, such as a node or node list, of the native source.
    nativeSourceValue: str
    #: Whether the value for this property is invalid.
    invalid: str
    #: Reason for the value being invalid, if it is.
    invalidReason: str


@dataclass
class AXRelatedNode:
    """Description is missing from the devtools protocol document."""

    #: The BackendNodeId of the related DOM node.
    backendDOMNodeId: str
    #: The IDRef value provided, if any.
    idref: str
    #: The text alternative of this node in the current context.
    text: str


@dataclass
class AXProperty:
    """Description is missing from the devtools protocol document."""

    #: The name of this property.
    name: str
    #: The value of this property.
    value: str


@dataclass
class AXValue:
    """A single computed AX property."""

    #: The type of this value.
    type: str
    #: The computed value of this property.
    value: str
    #: One or more related nodes, if applicable.
    relatedNodes: str
    #: The sources which contributed to the computation of this property.
    sources: str


class AXPropertyName(str, enum.Enum):
    """Values of AXProperty name: - from 'busy' to 'roledescription': stateswhich apply to every AX node - from 'live' to 'root': attributes which apply tonodes in live regions - from 'autocomplete' to 'valuetext': attributes whichapply to widgets - from 'checked' to 'selected': states which apply to widgets -from 'activedescendant' to 'owns' - relationships between elements other thanparent/child/sibling."""

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

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class AXNode:
    """A node in the accessibility tree."""

    #: Unique identifier for this node.
    nodeId: str
    #: Whether this node is ignored for accessibility
    ignored: str
    #: Collection of reasons why this node is hidden.
    ignoredReasons: str
    #: This `Node`'s role, whether explicit or implicit.
    role: str
    #: This `Node`'s Chrome raw role.
    chromeRole: str
    #: The accessible name for this `Node`.
    name: str
    #: The accessible description for this `Node`.
    description: str
    #: The value for this `Node`.
    value: str
    #: All other properties
    properties: str
    #: ID for this node's parent.
    parentId: str
    #: IDs for each of this node's child nodes.
    childIds: str
    #: The backend ID for the associated DOM node, if any.
    backendDOMNodeId: str
    #: The frame ID for the frame associated with this nodes document.
    frameId: str
