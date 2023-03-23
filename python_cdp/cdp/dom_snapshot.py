# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `DOMSnapshot`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot/

from __future__ import annotations

import typing
from dataclasses import dataclass

from . import dom
from . import dom_debugger
from . import page


@dataclass
class DOMNode:
    """A Node in the DOM tree."""

    # `Node`'s nodeType. # noqa
    node_type: int
    # `Node`'s nodeName. # noqa
    node_name: str
    # `Node`'s nodeValue. # noqa
    node_value: str
    # `Node`'s id, corresponds to DOM.Node.backendNodeId. # noqa
    backend_node_id: dom.BackendNodeId
    # Only set for textarea elements, contains the text value. # noqa
    text_value: typing.Optional[str]
    # Only set for input elements, contains the input's associated text value. # noqa
    input_value: typing.Optional[str]
    # Only set for radio and checkbox input elements, indicates if the elementhas been checked # noqa
    input_checked: typing.Optional[bool]
    # Only set for option elements, indicates if the element has been selected # noqa
    option_selected: typing.Optional[bool]
    # The indexes of the node's child nodes in the `domNodes` array returned by`getSnapshot`, if any. # noqa
    child_node_indexes: typing.Optional[int]
    # Attributes of an `Element` node. # noqa
    attributes: typing.Optional[NameValue]
    # Indexes of pseudo elements associated with this node in the `domNodes`array returned by `getSnapshot`, if any. # noqa
    pseudo_element_indexes: typing.Optional[int]
    # The index of the node's related layout tree node in the `layoutTreeNodes`array returned by `getSnapshot`, if any. # noqa
    layout_node_index: typing.Optional[int]
    # Document URL that `Document` or `FrameOwner` node points to. # noqa
    document_url: typing.Optional[str]
    # Base URL that `Document` or `FrameOwner` node uses for URL completion. # noqa
    base_url: typing.Optional[str]
    # Only set for documents, contains the document's content language. # noqa
    content_language: typing.Optional[str]
    # Only set for documents, contains the document's character set encoding. # noqa
    document_encoding: typing.Optional[str]
    # `DocumentType` node's publicId. # noqa
    public_id: typing.Optional[str]
    # `DocumentType` node's systemId. # noqa
    system_id: typing.Optional[str]
    # Frame ID for frame owner elements and also for the document node. # noqa
    frame_id: typing.Optional[page.FrameId]
    # The index of a frame owner element's content document in the `domNodes`array returned by `getSnapshot`, if any. # noqa
    content_document_index: typing.Optional[int]
    # Type of a pseudo element node. # noqa
    pseudo_type: typing.Optional[dom.PseudoType]
    # Shadow root type. # noqa
    shadow_root_type: typing.Optional[dom.ShadowRootType]
    # Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked. # noqa
    is_clickable: typing.Optional[bool]
    # Details of the node's event listeners, if any. # noqa
    event_listeners: typing.Optional[dom_debugger.EventListener]
    # The selected url for nodes with a srcset attribute. # noqa
    current_source_url: typing.Optional[str]
    # The url of the script (if any) that generates this node. # noqa
    origin_url: typing.Optional[str]
    # Scroll offsets, set when this node is a Document. # noqa
    scroll_offset_x: typing.Optional[float]
    # Description is missing from the devtools protocol document. # noqa
    scroll_offset_y: typing.Optional[float]


@dataclass
class InlineTextBox:
    """Details of post layout rendered text positions.

    The exact layout should not be regarded as stable and may change between versions.
    """

    # The bounding box in document coordinates. Note that scroll offset of thedocument is ignored. # noqa
    bounding_box: dom.Rect
    # The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2. # noqa
    start_character_index: int
    # The number of characters in this post layout textbox substring. Charactersthat would be represented as a surrogate pair in UTF-16 have length 2. # noqa
    num_characters: int


@dataclass
class LayoutTreeNode:
    """Details of an element in the DOM tree with a LayoutObject."""

    # The index of the related DOM node in the `domNodes` array returned by`getSnapshot`. # noqa
    dom_node_index: int
    # The bounding box in document coordinates. Note that scroll offset of thedocument is ignored. # noqa
    bounding_box: dom.Rect
    # Contents of the LayoutText, if any. # noqa
    layout_text: typing.Optional[str]
    # The post-layout inline text nodes, if any. # noqa
    inline_text_nodes: typing.Optional[InlineTextBox]
    # Index into the `computedStyles` array returned by `getSnapshot`. # noqa
    style_index: typing.Optional[int]
    # Global paint order index, which is determined by the stacking order of thenodes. Nodes that are painted together will have the same index. Only providedif includePaintOrder in getSnapshot was true. # noqa
    paint_order: typing.Optional[int]
    # Set to true to indicate the element begins a new stacking context. # noqa
    is_stacking_context: typing.Optional[bool]


@dataclass
class ComputedStyle:
    """A subset of the full ComputedStyle as defined by the request whitelist."""

    # Name/value pairs of computed style properties. # noqa
    properties: NameValue


@dataclass
class NameValue:
    """A name/value pair."""

    # Attribute/property name. # noqa
    name: str
    # Attribute/property value. # noqa
    value: str


class StringIndex(int):
    """Index of the string in the strings table."""

    def to_json(self) -> StringIndex:
        return self

    @classmethod
    def from_json(cls, value: int) -> StringIndex:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class ArrayOfStrings:
    """Index of the string in the strings table."""


@dataclass
class RareStringData:
    """Data that is only present on rare nodes."""

    # Description is missing from the devtools protocol document. # noqa
    index: int
    # Description is missing from the devtools protocol document. # noqa
    value: StringIndex


@dataclass
class RareBooleanData:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document. # noqa
    index: int


@dataclass
class RareIntegerData:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document. # noqa
    index: int
    # Description is missing from the devtools protocol document. # noqa
    value: int


@dataclass
class Rectangle:
    """Description is missing from the devtools protocol document."""


@dataclass
class DocumentSnapshot:
    """Document snapshot."""

    # Document URL that `Document` or `FrameOwner` node points to. # noqa
    document_url: StringIndex
    # Document title. # noqa
    title: StringIndex
    # Base URL that `Document` or `FrameOwner` node uses for URL completion. # noqa
    base_url: StringIndex
    # Contains the document's content language. # noqa
    content_language: StringIndex
    # Contains the document's character set encoding. # noqa
    encoding_name: StringIndex
    # `DocumentType` node's publicId. # noqa
    public_id: StringIndex
    # `DocumentType` node's systemId. # noqa
    system_id: StringIndex
    # Frame ID for frame owner elements and also for the document node. # noqa
    frame_id: StringIndex
    # A table with dom nodes. # noqa
    nodes: NodeTreeSnapshot
    # The nodes in the layout tree. # noqa
    layout: LayoutTreeSnapshot
    # The post-layout inline text nodes. # noqa
    text_boxes: TextBoxSnapshot
    # Horizontal scroll offset. # noqa
    scroll_offset_x: typing.Optional[float]
    # Vertical scroll offset. # noqa
    scroll_offset_y: typing.Optional[float]
    # Document content width. # noqa
    content_width: typing.Optional[float]
    # Document content height. # noqa
    content_height: typing.Optional[float]


@dataclass
class NodeTreeSnapshot:
    """Table containing nodes."""

    # Parent node index. # noqa
    parent_index: typing.Optional[int]
    # `Node`'s nodeType. # noqa
    node_type: typing.Optional[int]
    # Type of the shadow root the `Node` is in. String values are equal to the`ShadowRootType` enum. # noqa
    shadow_root_type: typing.Optional[RareStringData]
    # `Node`'s nodeName. # noqa
    node_name: typing.Optional[StringIndex]
    # `Node`'s nodeValue. # noqa
    node_value: typing.Optional[StringIndex]
    # `Node`'s id, corresponds to DOM.Node.backendNodeId. # noqa
    backend_node_id: typing.Optional[dom.BackendNodeId]
    # Attributes of an `Element` node. Flatten name, value pairs. # noqa
    attributes: typing.Optional[ArrayOfStrings]
    # Only set for textarea elements, contains the text value. # noqa
    text_value: typing.Optional[RareStringData]
    # Only set for input elements, contains the input's associated text value. # noqa
    input_value: typing.Optional[RareStringData]
    # Only set for radio and checkbox input elements, indicates if the elementhas been checked # noqa
    input_checked: typing.Optional[RareBooleanData]
    # Only set for option elements, indicates if the element has been selected # noqa
    option_selected: typing.Optional[RareBooleanData]
    # The index of the document in the list of the snapshot documents. # noqa
    content_document_index: typing.Optional[RareIntegerData]
    # Type of a pseudo element node. # noqa
    pseudo_type: typing.Optional[RareStringData]
    # Pseudo element identifier for this node. Only present if there is a validpseudoType. # noqa
    pseudo_identifier: typing.Optional[RareStringData]
    # Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked. # noqa
    is_clickable: typing.Optional[RareBooleanData]
    # The selected url for nodes with a srcset attribute. # noqa
    current_source_url: typing.Optional[RareStringData]
    # The url of the script (if any) that generates this node. # noqa
    origin_url: typing.Optional[RareStringData]


@dataclass
class LayoutTreeSnapshot:
    """Table of details of an element in the DOM tree with a LayoutObject."""

    # Index of the corresponding node in the `NodeTreeSnapshot` array returnedby `captureSnapshot`. # noqa
    node_index: int
    # Array of indexes specifying computed style strings, filtered according tothe `computedStyles` parameter passed to `captureSnapshot`. # noqa
    styles: ArrayOfStrings
    # The absolute position bounding box. # noqa
    bounds: Rectangle
    # Contents of the LayoutText, if any. # noqa
    text: StringIndex
    # Stacking context information. # noqa
    stacking_contexts: RareBooleanData
    # Global paint order index, which is determined by the stacking order of thenodes. Nodes that are painted together will have the same index. Only providedif includePaintOrder in captureSnapshot was true. # noqa
    paint_orders: typing.Optional[int]
    # The offset rect of nodes. Only available when includeDOMRects is set totrue # noqa
    offset_rects: typing.Optional[Rectangle]
    # The scroll rect of nodes. Only available when includeDOMRects is set totrue # noqa
    scroll_rects: typing.Optional[Rectangle]
    # The client rect of nodes. Only available when includeDOMRects is set totrue # noqa
    client_rects: typing.Optional[Rectangle]
    # The list of background colors that are blended with colors of overlappingelements. # noqa
    blended_background_colors: typing.Optional[StringIndex]
    # The list of computed text opacities. # noqa
    text_color_opacities: typing.Optional[float]


@dataclass
class TextBoxSnapshot:
    """Table of details of the post layout rendered text positions.

    The exact layout should not be regarded as stable and may change between versions.
    """

    # Index of the layout tree node that owns this box collection. # noqa
    layout_index: int
    # The absolute position bounding box. # noqa
    bounds: Rectangle
    # The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2. # noqa
    start: int
    # The number of characters in this post layout textbox substring. Charactersthat would be represented as a surrogate pair in UTF-16 have length 2. # noqa
    length: int


async def disable() -> None:
    """Disables DOM snapshot agent for the given page.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables DOM snapshot agent for the given page.

    # noqa
    """
    ...


async def get_snapshot() -> None:
    """Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents,
    and imported documents) in a flattened array, as well as layout and white-listed computed style information for the
    nodes.

    Shadow DOM in the returned DOM tree is flattened. # noqa
    """
    ...


async def capture_snapshot() -> None:
    """Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents,
    and imported documents) in a flattened array, as well as layout and white-listed computed style information for the
    nodes.

    Shadow DOM in the returned DOM tree is flattened. # noqa
    """
    ...
