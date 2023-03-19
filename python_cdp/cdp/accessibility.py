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


class AXValueSource(None):
    """A single source for a computed AX property."""

    def to_json(self) -> AXValueSource:
        return self

    @classmethod
    def from_json(cls, value: None) -> AXValueSource:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class AXRelatedNode(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> AXRelatedNode:
        return self

    @classmethod
    def from_json(cls, value: None) -> AXRelatedNode:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class AXProperty(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> AXProperty:
        return self

    @classmethod
    def from_json(cls, value: None) -> AXProperty:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class AXValue(None):
    """A single computed AX property."""

    def to_json(self) -> AXValue:
        return self

    @classmethod
    def from_json(cls, value: None) -> AXValue:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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


class AXNode(None):
    """A node in the accessibility tree."""

    def to_json(self) -> AXNode:
        return self

    @classmethod
    def from_json(cls, value: None) -> AXNode:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
