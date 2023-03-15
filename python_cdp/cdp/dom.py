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
from dataclasses import dataclass
import typing
import enum

from . import page
from . import runtime


@dataclass
class NodeId:
    """ Unique DOM node identifier. """


@dataclass
class BackendNodeId:
    """ Unique DOM node identifier used to reference a node that may not have been pushed to the
front-end. """


@dataclass
class BackendNode:
    """ Backend node with a friendly name. """
    #: `Node`'s nodeType.# noqa
    node_type: int
    #: `Node`'s nodeName.# noqa
    node_name: str
    #: Description is missing from the devtools protocol document.# noqa
    backend_node_id: BackendNodeId


class PseudoType(str, enum.Enum):
    """ Pseudo element type. """

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
    """ Shadow root type. """

    USER_AGENT = "user_agent"
    OPEN = "open"
    CLOSED = "closed"


    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CompatibilityMode(str, enum.Enum):
    """ Document compatibility mode. """

    QUIRKSMODE = "QuirksMode"
    LIMITEDQUIRKSMODE = "LimitedQuirksMode"
    NOQUIRKSMODE = "NoQuirksMode"


    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PhysicalAxes(str, enum.Enum):
    """ ContainerSelector physical axes """

    HORIZONTAL = "Horizontal"
    VERTICAL = "Vertical"
    BOTH = "Both"


    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class LogicalAxes(str, enum.Enum):
    """ ContainerSelector logical axes """

    INLINE = "Inline"
    BLOCK = "Block"
    BOTH = "Both"


    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class Node:
    """ DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes.
DOMNode is a base node mirror type. """
    #: Node identifier that is passed into the rest of the DOM messages as the`nodeId`. Backend will only push node with given `id` once. It is aware of allrequested nodes and will only fire DOM events for nodes known to the client.# noqa
    node_id: NodeId
    #: The BackendNodeId for this node.# noqa
    backend_node_id: BackendNodeId
    #: `Node`'s nodeType.# noqa
    node_type: int
    #: `Node`'s nodeName.# noqa
    node_name: str
    #: `Node`'s localName.# noqa
    local_name: str
    #: `Node`'s nodeValue.# noqa
    node_value: str
    #: The id of the parent node if any.# noqa
    parent_id: typing.Optional[NodeId] = None
    #: Child count for `Container` nodes.# noqa
    child_node_count: typing.Optional[int] = None
    #: Child nodes of this node when requested with children.# noqa
    children: typing.Optional[typing.List[Node]] = None
    #: Attributes of the `Element` node in the form of flat array `[name1,value1, name2, value2]`.# noqa
    attributes: typing.Optional[typing.List[str]] = None
    #: Document URL that `Document` or `FrameOwner` node points to.# noqa
    document_url: typing.Optional[str] = None
    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.# noqa
    base_url: typing.Optional[str] = None
    #: `DocumentType`'s publicId.# noqa
    public_id: typing.Optional[str] = None
    #: `DocumentType`'s systemId.# noqa
    system_id: typing.Optional[str] = None
    #: `DocumentType`'s internalSubset.# noqa
    internal_subset: typing.Optional[str] = None
    #: `Document`'s XML version in case of XML documents.# noqa
    xml_version: typing.Optional[str] = None
    #: `Attr`'s name.# noqa
    name: typing.Optional[str] = None
    #: `Attr`'s value.# noqa
    value: typing.Optional[str] = None
    #: Pseudo element type for this node.# noqa
    pseudo_type: typing.Optional[PseudoType] = None
    #: Pseudo element identifier for this node. Only present if there is a validpseudoType.# noqa
    pseudo_identifier: typing.Optional[str] = None
    #: Shadow root type.# noqa
    shadow_root_type: typing.Optional[ShadowRootType] = None
    #: Frame ID for frame owner elements.# noqa
    frame_id: typing.Optional[page.FrameId] = None
    #: Content document for frame owner elements.# noqa
    content_document: typing.Optional[Node] = None
    #: Shadow root list for given element host.# noqa
    shadow_roots: typing.Optional[typing.List[Node]] = None
    #: Content document fragment for template elements.# noqa
    template_content: typing.Optional[Node] = None
    #: Pseudo elements associated with this node.# noqa
    pseudo_elements: typing.Optional[typing.List[Node]] = None
    #: Deprecated, as the HTML Imports API has been removed (crbug.com/937746).This property used to return the imported document for the HTMLImport links. Theproperty is always undefined now.# noqa
    imported_document: typing.Optional[Node] = None
    #: Distributed nodes for given insertion point.# noqa
    distributed_nodes: typing.Optional[typing.List[BackendNode]] = None
    #: Whether the node is SVG.# noqa
    is_svg: typing.Optional[bool] = None
    #: Description is missing from the devtools protocol document.# noqa
    compatibility_mode: typing.Optional[CompatibilityMode] = None
    #: Description is missing from the devtools protocol document.# noqa
    assigned_slot: typing.Optional[BackendNode] = None


@dataclass
class RGBA:
    """ A structure holding an RGBA color. """
    #: The red component, in the [0-255] range.# noqa
    r: int
    #: The green component, in the [0-255] range.# noqa
    g: int
    #: The blue component, in the [0-255] range.# noqa
    b: int
    #: The alpha component, in the [0-1] range (default: 1).# noqa
    a: typing.Optional[float] = None


@dataclass
class Quad:
    """ An array of quad vertices, x immediately followed by y for each point, points clock-wise. """


@dataclass
class BoxModel:
    """ Box model. """
    #: Content box# noqa
    content: Quad
    #: Padding box# noqa
    padding: Quad
    #: Border box# noqa
    border: Quad
    #: Margin box# noqa
    margin: Quad
    #: Node width# noqa
    width: int
    #: Node height# noqa
    height: int
    #: Shape outside coordinates# noqa
    shape_outside: typing.Optional[ShapeOutsideInfo] = None


@dataclass
class ShapeOutsideInfo:
    """ CSS Shape Outside details. """
    #: Shape bounds# noqa
    bounds: Quad
    #: Shape coordinate details# noqa
    shape: typing.Any
    #: Margin shape bounds# noqa
    margin_shape: typing.Any


@dataclass
class Rect:
    """ Rectangle. """
    #: X coordinate# noqa
    x: float
    #: Y coordinate# noqa
    y: float
    #: Rectangle width# noqa
    width: float
    #: Rectangle height# noqa
    height: float


@dataclass
class CSSComputedStyleProperty:
    """ Description is missing from the devtools protocol document. """
    #: Computed style property name.# noqa
    name: str
    #: Computed style property value.# noqa
    value: str
