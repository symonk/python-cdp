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

    # `Node`'s nodeType.# noqa
    node_type: int
    # `Node`'s nodeName.# noqa
    node_name: str
    # Description is missing from the devtools protocol document.# noqa
    backend_node_id: BackendNodeId


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

    # Node identifier that is passed into the rest of the DOM messages as the`nodeId`. Backend will only push node with given `id` once. It is aware of allrequested nodes and will only fire DOM events for nodes known to the client.# noqa
    node_id: NodeId
    # The BackendNodeId for this node.# noqa
    backend_node_id: BackendNodeId
    # `Node`'s nodeType.# noqa
    node_type: int
    # `Node`'s nodeName.# noqa
    node_name: str
    # `Node`'s localName.# noqa
    local_name: str
    # `Node`'s nodeValue.# noqa
    node_value: str
    # The id of the parent node if any.# noqa
    parent_id: typing.Optional[NodeId] = None
    # Child count for `Container` nodes.# noqa
    child_node_count: typing.Optional[int] = None
    # Child nodes of this node when requested with children.# noqa
    children: typing.Optional[typing.List[Node]] = None
    # Attributes of the `Element` node in the form of flat array `[name1,value1, name2, value2]`.# noqa
    attributes: typing.Optional[typing.List[str]] = None
    # Document URL that `Document` or `FrameOwner` node points to.# noqa
    document_url: typing.Optional[str] = None
    # Base URL that `Document` or `FrameOwner` node uses for URL completion.# noqa
    base_url: typing.Optional[str] = None
    # `DocumentType`'s publicId.# noqa
    public_id: typing.Optional[str] = None
    # `DocumentType`'s systemId.# noqa
    system_id: typing.Optional[str] = None
    # `DocumentType`'s internalSubset.# noqa
    internal_subset: typing.Optional[str] = None
    # `Document`'s XML version in case of XML documents.# noqa
    xml_version: typing.Optional[str] = None
    # `Attr`'s name.# noqa
    name: typing.Optional[str] = None
    # `Attr`'s value.# noqa
    value: typing.Optional[str] = None
    # Pseudo element type for this node.# noqa
    pseudo_type: typing.Optional[PseudoType] = None
    # Pseudo element identifier for this node. Only present if there is a validpseudoType.# noqa
    pseudo_identifier: typing.Optional[str] = None
    # Shadow root type.# noqa
    shadow_root_type: typing.Optional[ShadowRootType] = None
    # Frame ID for frame owner elements.# noqa
    frame_id: typing.Optional[page.FrameId] = None
    # Content document for frame owner elements.# noqa
    content_document: typing.Optional[Node] = None
    # Shadow root list for given element host.# noqa
    shadow_roots: typing.Optional[typing.List[Node]] = None
    # Content document fragment for template elements.# noqa
    template_content: typing.Optional[Node] = None
    # Pseudo elements associated with this node.# noqa
    pseudo_elements: typing.Optional[typing.List[Node]] = None
    # Deprecated, as the HTML Imports API has been removed (crbug.com/937746).This property used to return the imported document for the HTMLImport links. Theproperty is always undefined now.# noqa
    imported_document: typing.Optional[Node] = None
    # Distributed nodes for given insertion point.# noqa
    distributed_nodes: typing.Optional[typing.List[BackendNode]] = None
    # Whether the node is SVG.# noqa
    is_svg: typing.Optional[bool] = None
    # Description is missing from the devtools protocol document.# noqa
    compatibility_mode: typing.Optional[CompatibilityMode] = None
    # Description is missing from the devtools protocol document.# noqa
    assigned_slot: typing.Optional[BackendNode] = None


@dataclass
class RGBA:
    """A structure holding an RGBA color."""

    # The red component, in the [0-255] range.# noqa
    r: int
    # The green component, in the [0-255] range.# noqa
    g: int
    # The blue component, in the [0-255] range.# noqa
    b: int
    # The alpha component, in the [0-1] range (default: 1).# noqa
    a: typing.Optional[float] = None


@dataclass
class Quad:
    """An array of quad vertices, x immediately followed by y for each point,
    points clock-wise."""


@dataclass
class BoxModel:
    """Box model."""

    # Content box# noqa
    content: Quad
    # Padding box# noqa
    padding: Quad
    # Border box# noqa
    border: Quad
    # Margin box# noqa
    margin: Quad
    # Node width# noqa
    width: int
    # Node height# noqa
    height: int
    # Shape outside coordinates# noqa
    shape_outside: typing.Optional[ShapeOutsideInfo] = None


@dataclass
class ShapeOutsideInfo:
    """CSS Shape Outside details."""

    # Shape bounds# noqa
    bounds: Quad
    # Shape coordinate details# noqa
    shape: typing.Any
    # Margin shape bounds# noqa
    margin_shape: typing.Any


@dataclass
class Rect:
    """Rectangle."""

    # X coordinate# noqa
    x: float
    # Y coordinate# noqa
    y: float
    # Rectangle width# noqa
    width: float
    # Rectangle height# noqa
    height: float


@dataclass
class CSSComputedStyleProperty:
    """Description is missing from the devtools protocol document."""

    # Computed style property name.# noqa
    name: str
    # Computed style property value.# noqa
    value: str


@dataclass
@memoize_event("DOM.attributeModified")
class AttributeModified:
    """Fired when `Element`'s attribute is modified."""

    nodeId: typing.Any
    name: typing.Any
    value: typing.Any


@dataclass
@memoize_event("DOM.attributeRemoved")
class AttributeRemoved:
    """Fired when `Element`'s attribute is removed."""

    nodeId: typing.Any
    name: typing.Any


@dataclass
@memoize_event("DOM.characterDataModified")
class CharacterDataModified:
    """Mirrors `DOMCharacterDataModified` event."""

    nodeId: typing.Any
    characterData: typing.Any


@dataclass
@memoize_event("DOM.childNodeCountUpdated")
class ChildNodeCountUpdated:
    """Fired when `Container`'s child node count has changed."""

    nodeId: typing.Any
    childNodeCount: typing.Any


@dataclass
@memoize_event("DOM.childNodeInserted")
class ChildNodeInserted:
    """Mirrors `DOMNodeInserted` event."""

    parentNodeId: typing.Any
    previousNodeId: typing.Any
    node: typing.Any


@dataclass
@memoize_event("DOM.childNodeRemoved")
class ChildNodeRemoved:
    """Mirrors `DOMNodeRemoved` event."""

    parentNodeId: typing.Any
    nodeId: typing.Any


@dataclass
@memoize_event("DOM.distributedNodesUpdated")
class DistributedNodesUpdated:
    """Called when distribution is changed."""

    insertionPointId: typing.Any
    distributedNodes: typing.Any


@dataclass
@memoize_event("DOM.documentUpdated")
class DocumentUpdated:
    """Fired when `Document` has been totally updated.

    Node ids are no longer valid.
    """


@dataclass
@memoize_event("DOM.inlineStyleInvalidated")
class InlineStyleInvalidated:
    """Fired when `Element`'s inline style is modified via a CSS property
    modification."""

    nodeIds: typing.Any


@dataclass
@memoize_event("DOM.pseudoElementAdded")
class PseudoElementAdded:
    """Called when a pseudo element is added to an element."""

    parentId: typing.Any
    pseudoElement: typing.Any


@dataclass
@memoize_event("DOM.topLayerElementsUpdated")
class TopLayerElementsUpdated:
    """Called when top layer elements are changed."""


@dataclass
@memoize_event("DOM.pseudoElementRemoved")
class PseudoElementRemoved:
    """Called when a pseudo element is removed from an element."""

    parentId: typing.Any
    pseudoElementId: typing.Any


@dataclass
@memoize_event("DOM.setChildNodes")
class SetChildNodes:
    """Fired when backend wants to provide client with the missing DOM
    structure.

    This happens upon most of the calls requesting node ids.
    """

    parentId: typing.Any
    nodes: typing.Any


@dataclass
@memoize_event("DOM.shadowRootPopped")
class ShadowRootPopped:
    """Called when shadow root is popped from the element."""

    hostId: typing.Any
    rootId: typing.Any


@dataclass
@memoize_event("DOM.shadowRootPushed")
class ShadowRootPushed:
    """Called when shadow root is pushed into the element."""

    hostId: typing.Any
    root: typing.Any


async def collect_class_names_from_subtree() -> None:
    """Collects class names for the node with given id and all of it's child
    nodes.

    # noqa
    """
    ...


async def copy_to() -> None:
    """Creates a deep copy of the specified node and places it into the target
    container before the given anchor.

    # noqa
    """
    ...


async def describe_node() -> None:
    """Describes node given its id, does not require domain to be enabled.

    Does not start tracking any objects, can be used for automation. #
    noqa
    """
    ...


async def scroll_into_view_if_needed() -> None:
    """Scrolls the specified rect of the given node into view if not already
    visible.

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

    `getSearchResults` should no longer be called for that search. #
    noqa
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

    Implicitly enables the DOM domain events for the current target. #
    noqa
    """
    ...


async def get_flattened_document() -> None:
    """Returns the root DOM node (and optionally the subtree) to the caller.

    Deprecated, as it is not designed to work well with the rest of the
    DOM agent. Use DOMSnapshot.captureSnapshot instead. # noqa
    """
    ...


async def get_nodes_for_subtree_by_style() -> None:
    """Finds nodes with a given computed style in a subtree.

    # noqa
    """
    ...


async def get_node_for_location() -> None:
    """Returns node id at given location.

    Depending on whether DOM domain is enabled, nodeId is either
    returned or not. # noqa
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
    """Returns search results from given `fromIndex` to given `toIndex` from
    the search with the given identifier.

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

    Use `getSearchResults` to access search results or `cancelSearch` to
    end this search session. # noqa
    """
    ...


async def push_node_by_path_to_frontend() -> None:
    """Requests that the node is sent to the caller given its path.

    // FIXME, use XPath # noqa
    """
    ...


async def push_nodes_by_backend_ids_to_frontend() -> None:
    """Requests that a batch of nodes is sent to the caller given their backend
    node ids.

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

    Top layer is rendered closest to the user within a viewport,
    therefore its elements always appear on top of all other content. #
    noqa
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
    """Requests that children of the node with given id are returned to the
    caller in form of `setChildNodes` events where not only immediate children
    are retrieved, but all children down to the specified depth.

    # noqa
    """
    ...


async def request_node() -> None:
    """Requests that the node is sent to the caller given the JavaScript node
    object reference.

    All nodes that form the path from the node to the root are also sent
    to the client as a series of `setChildNodes` notifications. # noqa
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

    This method is useful when user edits some existing attribute value
    and types in several attribute name/value pairs. # noqa
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
    """Enables console to refer to the node with given id via $x (see Command
    Line API for more details.

    $x functions). # noqa
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
    """Returns the descendants of a container query container that have
    container queries against this container.

    # noqa
    """
    ...
