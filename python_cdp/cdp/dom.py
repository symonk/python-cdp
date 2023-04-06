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
import typing
from dataclasses import dataclass

from . import page
from .utils import memoize_event


class NodeId(int):
    """Unique DOM node identifier."""

    def to_json(self) -> NodeId:
        return self

    @classmethod
    def from_json(cls, value: int) -> NodeId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class BackendNodeId(int):
    """Unique DOM node identifier used to reference a node that may not have been pushed to the front-end."""

    def to_json(self) -> BackendNodeId:
        return self

    @classmethod
    def from_json(cls, value: int) -> BackendNodeId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class BackendNode:
    """Backend node with a friendly name."""

    # `Node`'s nodeType. # noqa
    node_type: int
    # `Node`'s nodeName. # noqa
    node_name: str
    # Description is missing from the devtools protocol document. # noqa
    backend_node_id: BackendNodeId


class PseudoType(str, enum.Enum):
    """Pseudo element type."""

    FIRST_LINE = "first-line"
    FIRST_LETTER = "first-letter"
    BEFORE = "before"
    AFTER = "after"
    MARKER = "marker"
    BACKDROP = "backdrop"
    SELECTION = "selection"
    TARGET_TEXT = "target-text"
    SPELLING_ERROR = "spelling-error"
    GRAMMAR_ERROR = "grammar-error"
    HIGHLIGHT = "highlight"
    FIRST_LINE_INHERITED = "first-line-inherited"
    SCROLLBAR = "scrollbar"
    SCROLLBAR_THUMB = "scrollbar-thumb"
    SCROLLBAR_BUTTON = "scrollbar-button"
    SCROLLBAR_TRACK = "scrollbar-track"
    SCROLLBAR_TRACK_PIECE = "scrollbar-track-piece"
    SCROLLBAR_CORNER = "scrollbar-corner"
    RESIZER = "resizer"
    INPUT_LIST_BUTTON = "input-list-button"
    VIEW_TRANSITION = "view-transition"
    VIEW_TRANSITION_GROUP = "view-transition-group"
    VIEW_TRANSITION_IMAGE_PAIR = "view-transition-image-pair"
    VIEW_TRANSITION_OLD = "view-transition-old"
    VIEW_TRANSITION_NEW = "view-transition-new"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ShadowRootType(str, enum.Enum):
    """Shadow root type."""

    USER_AGENT = "user-agent"
    OPEN = "open"
    CLOSED = "closed"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CompatibilityMode(str, enum.Enum):
    """Document compatibility mode."""

    QUIRKS_MODE = "quirks_mode"
    LIMITED_QUIRKS_MODE = "limited_quirks_mode"
    NO_QUIRKS_MODE = "no_quirks_mode"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PhysicalAxes(str, enum.Enum):
    """ContainerSelector physical axes."""

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    BOTH = "both"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class LogicalAxes(str, enum.Enum):
    """ContainerSelector logical axes."""

    INLINE = "inline"
    BLOCK = "block"
    BOTH = "both"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class Node:
    """DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes.

    DOMNode is a base node mirror type.
    """

    # Node identifier that is passed into the rest of the DOM messages as the`nodeId`. Backend will only push node with given `id` once. It is aware of allrequested nodes and will only fire DOM events for nodes known to the client. # noqa
    node_id: NodeId
    # The BackendNodeId for this node. # noqa
    backend_node_id: BackendNodeId
    # `Node`'s nodeType. # noqa
    node_type: int
    # `Node`'s nodeName. # noqa
    node_name: str
    # `Node`'s localName. # noqa
    local_name: str
    # `Node`'s nodeValue. # noqa
    node_value: str
    # The id of the parent node if any. # noqa
    parent_id: typing.Optional[NodeId]
    # Child count for `Container` nodes. # noqa
    child_node_count: typing.Optional[int]
    # Child nodes of this node when requested with children. # noqa
    children: typing.Optional[Node]
    # Attributes of the `Element` node in the form of flat array `[name1,value1, name2, value2]`. # noqa
    attributes: typing.Optional[str]
    # Document URL that `Document` or `FrameOwner` node points to. # noqa
    document_url: typing.Optional[str]
    # Base URL that `Document` or `FrameOwner` node uses for URL completion. # noqa
    base_url: typing.Optional[str]
    # `DocumentType`'s publicId. # noqa
    public_id: typing.Optional[str]
    # `DocumentType`'s systemId. # noqa
    system_id: typing.Optional[str]
    # `DocumentType`'s internalSubset. # noqa
    internal_subset: typing.Optional[str]
    # `Document`'s XML version in case of XML documents. # noqa
    xml_version: typing.Optional[str]
    # `Attr`'s name. # noqa
    name: typing.Optional[str]
    # `Attr`'s value. # noqa
    value: typing.Optional[str]
    # Pseudo element type for this node. # noqa
    pseudo_type: typing.Optional[PseudoType]
    # Pseudo element identifier for this node. Only present if there is a validpseudoType. # noqa
    pseudo_identifier: typing.Optional[str]
    # Shadow root type. # noqa
    shadow_root_type: typing.Optional[ShadowRootType]
    # Frame ID for frame owner elements. # noqa
    frame_id: typing.Optional[page.FrameId]
    # Content document for frame owner elements. # noqa
    content_document: typing.Optional[Node]
    # Shadow root list for given element host. # noqa
    shadow_roots: typing.Optional[Node]
    # Content document fragment for template elements. # noqa
    template_content: typing.Optional[Node]
    # Pseudo elements associated with this node. # noqa
    pseudo_elements: typing.Optional[Node]
    # Deprecated, as the HTML Imports API has been removed (crbug.com/937746).This property used to return the imported document for the HTMLImport links. Theproperty is always undefined now. # noqa
    imported_document: typing.Optional[Node]
    # Distributed nodes for given insertion point. # noqa
    distributed_nodes: typing.Optional[BackendNode]
    # Whether the node is SVG. # noqa
    is_svg: typing.Optional[bool]
    # Description is missing from the devtools protocol document. # noqa
    compatibility_mode: typing.Optional[CompatibilityMode]
    # Description is missing from the devtools protocol document. # noqa
    assigned_slot: typing.Optional[BackendNode]


@dataclass
class RGBA:
    """A structure holding an RGBA color."""

    # The red component, in the [0-255] range. # noqa
    r: int
    # The green component, in the [0-255] range. # noqa
    g: int
    # The blue component, in the [0-255] range. # noqa
    b: int
    # The alpha component, in the [0-1] range (default: 1). # noqa
    a: typing.Optional[float]


@dataclass
class Quad:
    """An array of quad vertices, x immediately followed by y for each point, points clock-wise."""


@dataclass
class BoxModel:
    """Box model."""

    # Content box # noqa
    content: Quad
    # Padding box # noqa
    padding: Quad
    # Border box # noqa
    border: Quad
    # Margin box # noqa
    margin: Quad
    # Node width # noqa
    width: int
    # Node height # noqa
    height: int
    # Shape outside coordinates # noqa
    shape_outside: typing.Optional[ShapeOutsideInfo]


@dataclass
class ShapeOutsideInfo:
    """CSS Shape Outside details."""

    # Shape bounds # noqa
    bounds: Quad
    # Shape coordinate details # noqa
    shape: typing.Any
    # Margin shape bounds # noqa
    margin_shape: typing.Any


@dataclass
class Rect:
    """Rectangle."""

    # X coordinate # noqa
    x: float
    # Y coordinate # noqa
    y: float
    # Rectangle width # noqa
    width: float
    # Rectangle height # noqa
    height: float


@dataclass
class CSSComputedStyleProperty:
    """Description is missing from the devtools protocol document."""

    # Computed style property name. # noqa
    name: str
    # Computed style property value. # noqa
    value: str


@dataclass
@memoize_event("DOM.attributeModified")
class AttributeModified:
    """Fired when `Element`'s attribute is modified."""

    node_id: NodeId
    name: str
    value: str


@dataclass
@memoize_event("DOM.attributeRemoved")
class AttributeRemoved:
    """Fired when `Element`'s attribute is removed."""

    node_id: NodeId
    name: str


@dataclass
@memoize_event("DOM.characterDataModified")
class CharacterDataModified:
    """Mirrors `DOMCharacterDataModified` event."""

    node_id: NodeId
    character_data: str


@dataclass
@memoize_event("DOM.childNodeCountUpdated")
class ChildNodeCountUpdated:
    """Fired when `Container`'s child node count has changed."""

    node_id: NodeId
    child_node_count: int


@dataclass
@memoize_event("DOM.childNodeInserted")
class ChildNodeInserted:
    """Mirrors `DOMNodeInserted` event."""

    parent_node_id: NodeId
    previous_node_id: NodeId
    node: Node


@dataclass
@memoize_event("DOM.childNodeRemoved")
class ChildNodeRemoved:
    """Mirrors `DOMNodeRemoved` event."""

    parent_node_id: NodeId
    node_id: NodeId


@dataclass
@memoize_event("DOM.distributedNodesUpdated")
class DistributedNodesUpdated:
    """Called when distribution is changed."""

    insertion_point_id: NodeId
    distributed_nodes: typing.List[BackendNode]


@dataclass
@memoize_event("DOM.documentUpdated")
class DocumentUpdated:
    """Fired when `Document` has been totally updated.

    Node ids are no longer valid.
    """


@dataclass
@memoize_event("DOM.inlineStyleInvalidated")
class InlineStyleInvalidated:
    """Fired when `Element`'s inline style is modified via a CSS property modification."""

    node_ids: typing.List[NodeId]


@dataclass
@memoize_event("DOM.pseudoElementAdded")
class PseudoElementAdded:
    """Called when a pseudo element is added to an element."""

    parent_id: NodeId
    pseudo_element: Node


@dataclass
@memoize_event("DOM.topLayerElementsUpdated")
class TopLayerElementsUpdated:
    """Called when top layer elements are changed."""


@dataclass
@memoize_event("DOM.pseudoElementRemoved")
class PseudoElementRemoved:
    """Called when a pseudo element is removed from an element."""

    parent_id: NodeId
    pseudo_element_id: NodeId


@dataclass
@memoize_event("DOM.setChildNodes")
class SetChildNodes:
    """Fired when backend wants to provide client with the missing DOM structure.

    This happens upon most of the calls requesting node ids.
    """

    parent_id: NodeId
    nodes: typing.List[Node]


@dataclass
@memoize_event("DOM.shadowRootPopped")
class ShadowRootPopped:
    """Called when shadow root is popped from the element."""

    host_id: NodeId
    root_id: NodeId


@dataclass
@memoize_event("DOM.shadowRootPushed")
class ShadowRootPushed:
    """Called when shadow root is pushed into the element."""

    host_id: NodeId
    root: Node


async def collect_class_names_from_subtree() -> None:
    """Collects class names for the node with given id and all of it's child nodes.

    # noqa
    """
    ...


async def copy_to() -> None:
    """Creates a deep copy of the specified node and places it into the target container before the given anchor.

    # noqa
    """
    ...


async def describe_node() -> None:
    """Describes node given its id, does not require domain to be enabled.

    Does not start tracking any objects, can be used for automation. # noqa
    """
    ...


async def scroll_into_view_if_needed() -> None:
    """Scrolls the specified rect of the given node into view if not already visible.

    Note: exactly one between nodeId, backendNodeId and objectId should be passed
    to identify the node. # noqa
    """
    ...


async def disable() -> None:
    """Disables DOM agent for the given page.

    # noqa
    """
    ...


async def discard_search_results() -> None:
    """Discards search results from the session with the given id.

    `getSearchResults` should no longer be called for that search. # noqa
    """
    ...


async def enable() -> None:
    """Enables DOM agent for the given page.

    # noqa
    """
    ...


async def focus() -> None:
    """Focuses the given element.

    # noqa
    """
    ...


async def get_attributes() -> None:
    """Returns attributes for the specified node.

    # noqa
    """
    ...


async def get_box_model() -> None:
    """Returns boxes for the given node.

    # noqa
    """
    ...


async def get_content_quads() -> None:
    """Returns quads that describe node position on the page.

    This method might return multiple quads for inline nodes. # noqa
    """
    ...


async def get_document() -> None:
    """Returns the root DOM node (and optionally the subtree) to the caller.

    Implicitly enables the DOM domain events for the current target. # noqa
    """
    ...


async def get_flattened_document() -> None:
    """Returns the root DOM node (and optionally the subtree) to the caller.

    Deprecated, as it is not designed to work well with the rest of the DOM agent. Use DOMSnapshot.captureSnapshot
    instead. # noqa
    """
    ...


async def get_nodes_for_subtree_by_style() -> None:
    """Finds nodes with a given computed style in a subtree.

    # noqa
    """
    ...


async def get_node_for_location() -> None:
    """Returns node id at given location.

    Depending on whether DOM domain is enabled, nodeId is either returned or not. # noqa
    """
    ...


async def get_outer_html() -> None:
    """Returns node's HTML markup.

    # noqa
    """
    ...


async def get_relayout_boundary() -> None:
    """Returns the id of the nearest ancestor that is a relayout boundary.

    # noqa
    """
    ...


async def get_search_results() -> None:
    """Returns search results from given `fromIndex` to given `toIndex` from the search with the given identifier.

    # noqa
    """
    ...


async def hide_highlight() -> None:
    """Hides any highlight.

    # noqa
    """
    ...


async def highlight_node() -> None:
    """Highlights DOM node.

    # noqa
    """
    ...


async def highlight_rect() -> None:
    """Highlights given rectangle.

    # noqa
    """
    ...


async def mark_undoable_state() -> None:
    """Marks last undoable state.

    # noqa
    """
    ...


async def move_to() -> None:
    """Moves node into the new container, places it before the given anchor.

    # noqa
    """
    ...


async def perform_search() -> None:
    """Searches for a given string in the DOM tree.

    Use `getSearchResults` to access search results or `cancelSearch` to end this search session. # noqa
    """
    ...


async def push_node_by_path_to_frontend() -> None:
    """Requests that the node is sent to the caller given its path.

    // FIXME, use XPath # noqa
    """
    ...


async def push_nodes_by_backend_ids_to_frontend() -> None:
    """Requests that a batch of nodes is sent to the caller given their backend node ids.

    # noqa
    """
    ...


async def query_selector() -> None:
    """Executes `querySelector` on a given node.

    # noqa
    """
    ...


async def query_selector_all() -> None:
    """Executes `querySelectorAll` on a given node.

    # noqa
    """
    ...


async def get_top_layer_elements() -> None:
    """Returns NodeIds of current top layer elements.

    Top layer is rendered closest to the user within a viewport, therefore its elements always appear on top of all
    other content. # noqa
    """
    ...


async def redo() -> None:
    """Re-does the last undone action.

    # noqa
    """
    ...


async def remove_attribute() -> None:
    """Removes attribute with given name from an element with given id.

    # noqa
    """
    ...


async def remove_node() -> None:
    """Removes node with given id.

    # noqa
    """
    ...


async def request_child_nodes() -> None:
    """Requests that children of the node with given id are returned to the caller in form of `setChildNodes` events
    where not only immediate children are retrieved, but all children down to the specified depth.

    # noqa
    """
    ...


async def request_node() -> None:
    """Requests that the node is sent to the caller given the JavaScript node object reference.

    All nodes that form the path from the node to the root are also sent to the client as a series of `setChildNodes`
    notifications. # noqa
    """
    ...


async def resolve_node() -> None:
    """Resolves the JavaScript node object for a given NodeId or BackendNodeId.

    # noqa
    """
    ...


async def set_attribute_value() -> None:
    """Sets attribute for an element with given id.

    # noqa
    """
    ...


async def set_attributes_as_text() -> None:
    """Sets attributes on element with given id.

    This method is useful when user edits some existing attribute value and types in several attribute name/value pairs.
    # noqa
    """
    ...


async def set_file_input_files() -> None:
    """Sets files for the given file input element.

    # noqa
    """
    ...


async def set_node_stack_traces_enabled() -> None:
    """Sets if stack traces should be captured for Nodes.

    See `Node.getNodeStackTraces`. Default is disabled. # noqa
    """
    ...


async def get_node_stack_traces() -> None:
    """Gets stack traces associated with a Node.

    As of now, only provides stack trace for Node creation. # noqa
    """
    ...


async def get_file_info() -> None:
    """Returns file information for the given File wrapper.

    # noqa
    """
    ...


async def set_inspected_node() -> None:
    """Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions).

    # noqa
    """
    ...


async def set_node_name() -> None:
    """Sets node name for a node with given id.

    # noqa
    """
    ...


async def set_node_value() -> None:
    """Sets node value for a node with given id.

    # noqa
    """
    ...


async def set_outer_html() -> None:
    """Sets node HTML markup, returns new node id.

    # noqa
    """
    ...


async def undo() -> None:
    """Undoes the last performed action.

    # noqa
    """
    ...


async def get_frame_owner() -> None:
    """Returns iframe node that owns iframe with the given domain.

    # noqa
    """
    ...


async def get_container_for_node() -> None:
    """Returns the query container of the given node based on container query
    conditions: containerName, physical, and logical axes. If no axes are
    provided, the style container is returned, which is the direct parent or the
    closest element with a matching container-name. # noqa"""
    ...


async def get_querying_descendants_for_container() -> None:
    """Returns the descendants of a container query container that have container queries against this container.

    # noqa
    """
    ...
