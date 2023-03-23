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
import typing
from dataclasses import dataclass

from . import dom
from . import page
from .utils import memoize_event


class AXNodeId(str):
    """Unique accessibility node identifier."""

    def to_json(self) -> AXNodeId:
        return self

    @classmethod
    def from_json(cls, value: str) -> AXNodeId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class AXValueType(str, enum.Enum):
    """Enum of possible property types."""

    BOOLEAN = "boolean"
    TRISTATE = "tristate"
    BOOLEAN_OR_UNDEFINED = "boolean_or_undefined"
    IDREF = "idref"
    IDREF_LIST = "idref_list"
    INTEGER = "integer"
    NODE = "node"
    NODE_LIST = "node_list"
    NUMBER = "number"
    STRING = "string"
    COMPUTED_STRING = "computed_string"
    TOKEN = "token"
    TOKEN_LIST = "token_list"
    DOM_RELATION = "dom_relation"
    ROLE = "role"
    INTERNAL_ROLE = "internal_role"
    VALUE_UNDEFINED = "value_undefined"

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
    RELATED_ELEMENT = "related_element"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class AXValueNativeSourceType(str, enum.Enum):
    """Enum of possible native property sources (as a subtype of a particular AXValueSourceType)."""

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

    # What type of source this is. # noqa
    type: AXValueSourceType
    # The value of this property source. # noqa
    value: typing.Optional[AXValue]
    # The name of the relevant attribute, if any. # noqa
    attribute: typing.Optional[str]
    # The value of the relevant attribute, if any. # noqa
    attribute_value: typing.Optional[AXValue]
    # Whether this source is superseded by a higher priority source. # noqa
    superseded: typing.Optional[bool]
    # The native markup source for this value, e.g. a <label> element. # noqa
    native_source: typing.Optional[AXValueNativeSourceType]
    # The value, such as a node or node list, of the native source. # noqa
    native_source_value: typing.Optional[AXValue]
    # Whether the value for this property is invalid. # noqa
    invalid: typing.Optional[bool]
    # Reason for the value being invalid, if it is. # noqa
    invalid_reason: typing.Optional[str]


@dataclass
class AXRelatedNode:
    """Description is missing from the devtools protocol document."""

    # The BackendNodeId of the related DOM node. # noqa
    backend_dom_node_id: dom.BackendNodeId
    # The IDRef value provided, if any. # noqa
    idref: typing.Optional[str]
    # The text alternative of this node in the current context. # noqa
    text: typing.Optional[str]


@dataclass
class AXProperty:
    """Description is missing from the devtools protocol document."""

    # The name of this property. # noqa
    name: AXPropertyName
    # The value of this property. # noqa
    value: AXValue


@dataclass
class AXValue:
    """A single computed AX property."""

    # The type of this value. # noqa
    type: AXValueType
    # The computed value of this property. # noqa
    value: typing.Any
    # One or more related nodes, if applicable. # noqa
    related_nodes: typing.Optional[AXRelatedNode]
    # The sources which contributed to the computation of this property. # noqa
    sources: typing.Optional[AXValueSource]


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
    HIDDEN_ROOT = "hidden_root"
    INVALID = "invalid"
    KEYSHORTCUTS = "keyshortcuts"
    SETTABLE = "settable"
    ROLEDESCRIPTION = "roledescription"
    LIVE = "live"
    ATOMIC = "atomic"
    RELEVANT = "relevant"
    ROOT = "root"
    AUTOCOMPLETE = "autocomplete"
    HAS_POPUP = "has_popup"
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

    # Unique identifier for this node. # noqa
    node_id: AXNodeId
    # Whether this node is ignored for accessibility # noqa
    ignored: bool
    # Collection of reasons why this node is hidden. # noqa
    ignored_reasons: typing.Optional[AXProperty]
    # This `Node`'s role, whether explicit or implicit. # noqa
    role: typing.Optional[AXValue]
    # This `Node`'s Chrome raw role. # noqa
    chrome_role: typing.Optional[AXValue]
    # The accessible name for this `Node`. # noqa
    name: typing.Optional[AXValue]
    # The accessible description for this `Node`. # noqa
    description: typing.Optional[AXValue]
    # The value for this `Node`. # noqa
    value: typing.Optional[AXValue]
    # All other properties # noqa
    properties: typing.Optional[AXProperty]
    # ID for this node's parent. # noqa
    parent_id: typing.Optional[AXNodeId]
    # IDs for each of this node's child nodes. # noqa
    child_ids: typing.Optional[AXNodeId]
    # The backend ID for the associated DOM node, if any. # noqa
    backend_dom_node_id: typing.Optional[dom.BackendNodeId]
    # The frame ID for the frame associated with this nodes document. # noqa
    frame_id: typing.Optional[page.FrameId]


@dataclass
@memoize_event("Accessibility.loadComplete")
class LoadComplete:
    """The loadComplete event mirrors the load complete event sent by the browser to assistive technology when the web
    page has finished loading."""

    root: AXNode


@dataclass
@memoize_event("Accessibility.nodesUpdated")
class NodesUpdated:
    """The nodesUpdated event is sent every time a previously requested node has changed the in tree."""

    nodes: typing.List[AXNode]


async def disable() -> None:
    """Disables the accessibility domain.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls.

    This turns on accessibility for the page, which can impact performance until accessibility is disabled. # noqa
    """
    ...


async def get_partial_ax_tree() -> None:
    """Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.

    # noqa
    """
    ...


async def get_full_ax_tree() -> None:
    """Fetches the entire accessibility tree for the root Document # noqa."""
    ...


async def get_root_ax_node() -> None:
    """Fetches the root node.

    Requires `enable()` to have been called previously. # noqa
    """
    ...


async def get_ax_node_and_ancestors() -> None:
    """Fetches a node and all ancestors up to and including the root.

    Requires `enable()` to have been called previously. # noqa
    """
    ...


async def get_child_ax_nodes() -> None:
    """Fetches a particular accessibility node by AXNodeId.

    Requires `enable()` to have been called previously. # noqa
    """
    ...


async def query_ax_tree() -> None:
    """Query a DOM node's accessibility subtree for accessible name and role.

    This command computes the name and role for all nodes in the subtree, including those that are ignored for
    accessibility, and returns those that mactch the specified name and role. If no DOM node is specified, or the DOM
    node does not exist, the command returns an error. If neither `accessibleName` or `role` is specified, it returns
    all the accessibility nodes in the subtree. # noqa
    """
    ...
