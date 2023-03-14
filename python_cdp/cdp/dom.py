# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `DOM`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/DOM/

from __future__ import annotations

import enum
from dataclasses import dataclass


@dataclass
class NodeId:
    """Unique DOM node identifier."""


@dataclass
class BackendNodeId:
    """Unique DOM node identifier used to reference a node that may not have
    been pushed to the front-end."""


@dataclass
class BackendNode:
    """Backend node with a friendly name."""

    #: `Node`'s nodeType.
    nodeType: str
    #: `Node`'s nodeName.
    nodeName: str
    #: Description is missing from the devtools protocol document.
    backendNodeId: str


class PseudoType(str, enum.Enum):
    """Pseudo element type."""

    FIRST_LINE = "first_line"
    FIRST_LETTER = "first_letter"
    BEFORE = "before"
    AFTER = "after"
    MARKER = "marker"
    BACKDROP = "backdrop"
    SELECTION = "selection"
    TARGET_TEXT = "target_text"
    SPELLING_ERROR = "spelling_error"
    GRAMMAR_ERROR = "grammar_error"
    HIGHLIGHT = "highlight"
    FIRST_LINE_INHERITED = "first_line_inherited"
    SCROLLBAR = "scrollbar"
    SCROLLBAR_THUMB = "scrollbar_thumb"
    SCROLLBAR_BUTTON = "scrollbar_button"
    SCROLLBAR_TRACK = "scrollbar_track"
    SCROLLBAR_TRACK_PIECE = "scrollbar_track_piece"
    SCROLLBAR_CORNER = "scrollbar_corner"
    RESIZER = "resizer"
    INPUT_LIST_BUTTON = "input_list_button"
    VIEW_TRANSITION = "view_transition"
    VIEW_TRANSITION_GROUP = "view_transition_group"
    VIEW_TRANSITION_IMAGE_PAIR = "view_transition_image_pair"
    VIEW_TRANSITION_OLD = "view_transition_old"
    VIEW_TRANSITION_NEW = "view_transition_new"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ShadowRootType(str, enum.Enum):
    """Shadow root type."""

    USER_AGENT = "user_agent"
    OPEN = "open"
    CLOSED = "closed"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CompatibilityMode(str, enum.Enum):
    """Document compatibility mode."""

    QUIRKSMODE = "QuirksMode"
    LIMITEDQUIRKSMODE = "LimitedQuirksMode"
    NOQUIRKSMODE = "NoQuirksMode"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PhysicalAxes(str, enum.Enum):
    """ContainerSelector physical axes."""

    HORIZONTAL = "Horizontal"
    VERTICAL = "Vertical"
    BOTH = "Both"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class LogicalAxes(str, enum.Enum):
    """ContainerSelector logical axes."""

    INLINE = "Inline"
    BLOCK = "Block"
    BOTH = "Both"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class Node:
    """DOM interaction is implemented in terms of mirror objects that represent
    the actual DOM nodes.

    DOMNode is a base node mirror type.
    """

    #: Node identifier that is passed into the rest of the DOM messages as the`nodeId`. Backend will only push node with given `id` once. It is aware of allrequested nodes and will only fire DOM events for nodes known to the client.
    nodeId: str
    #: The id of the parent node if any.
    parentId: str
    #: The BackendNodeId for this node.
    backendNodeId: str
    #: `Node`'s nodeType.
    nodeType: str
    #: `Node`'s nodeName.
    nodeName: str
    #: `Node`'s localName.
    localName: str
    #: `Node`'s nodeValue.
    nodeValue: str
    #: Child count for `Container` nodes.
    childNodeCount: str
    #: Child nodes of this node when requested with children.
    children: str
    #: Attributes of the `Element` node in the form of flat array `[name1,value1, name2, value2]`.
    attributes: str
    #: Document URL that `Document` or `FrameOwner` node points to.
    documentURL: str
    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.
    baseURL: str
    #: `DocumentType`'s publicId.
    publicId: str
    #: `DocumentType`'s systemId.
    systemId: str
    #: `DocumentType`'s internalSubset.
    internalSubset: str
    #: `Document`'s XML version in case of XML documents.
    xmlVersion: str
    #: `Attr`'s name.
    name: str
    #: `Attr`'s value.
    value: str
    #: Pseudo element type for this node.
    pseudoType: str
    #: Pseudo element identifier for this node. Only present if there is a validpseudoType.
    pseudoIdentifier: str
    #: Shadow root type.
    shadowRootType: str
    #: Frame ID for frame owner elements.
    frameId: str
    #: Content document for frame owner elements.
    contentDocument: str
    #: Shadow root list for given element host.
    shadowRoots: str
    #: Content document fragment for template elements.
    templateContent: str
    #: Pseudo elements associated with this node.
    pseudoElements: str
    #: Deprecated, as the HTML Imports API has been removed (crbug.com/937746).This property used to return the imported document for the HTMLImport links. Theproperty is always undefined now.
    importedDocument: str
    #: Distributed nodes for given insertion point.
    distributedNodes: str
    #: Whether the node is SVG.
    isSVG: str
    #: Description is missing from the devtools protocol document.
    compatibilityMode: str
    #: Description is missing from the devtools protocol document.
    assignedSlot: str


@dataclass
class RGBA:
    """A structure holding an RGBA color."""

    #: The red component, in the [0-255] range.
    r: str
    #: The green component, in the [0-255] range.
    g: str
    #: The blue component, in the [0-255] range.
    b: str
    #: The alpha component, in the [0-1] range (default: 1).
    a: str


@dataclass
class Quad:
    """An array of quad vertices, x immediately followed by y for each point,
    points clock-wise."""


@dataclass
class BoxModel:
    """Box model."""

    #: Content box
    content: str
    #: Padding box
    padding: str
    #: Border box
    border: str
    #: Margin box
    margin: str
    #: Node width
    width: str
    #: Node height
    height: str
    #: Shape outside coordinates
    shapeOutside: str


@dataclass
class ShapeOutsideInfo:
    """CSS Shape Outside details."""

    #: Shape bounds
    bounds: str
    #: Shape coordinate details
    shape: str
    #: Margin shape bounds
    marginShape: str


@dataclass
class Rect:
    """Rectangle."""

    #: X coordinate
    x: str
    #: Y coordinate
    y: str
    #: Rectangle width
    width: str
    #: Rectangle height
    height: str


@dataclass
class CSSComputedStyleProperty:
    """Description is missing from the devtools protocol document."""

    #: Computed style property name.
    name: str
    #: Computed style property value.
    value: str
