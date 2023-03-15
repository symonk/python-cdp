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

    #: `Node`'s nodeType.# noqa
    node_type: int
    #: `Node`'s nodeName.# noqa
    node_name: str
    #: `Node`'s nodeValue.# noqa
    node_value: str
    #: `Node`'s id, corresponds to DOM.Node.backendNodeId.# noqa
    backend_node_id: dom.BackendNodeId
    #: Only set for textarea elements, contains the text value.# noqa
    text_value: typing.Optional[str] = None
    #: Only set for input elements, contains the input's associated text value.# noqa
    input_value: typing.Optional[str] = None
    #: Only set for radio and checkbox input elements, indicates if the elementhas been checked# noqa
    input_checked: typing.Optional[bool] = None
    #: Only set for option elements, indicates if the element has been selected# noqa
    option_selected: typing.Optional[bool] = None
    #: The indexes of the node's child nodes in the `domNodes` array returned by`getSnapshot`, if any.# noqa
    child_node_indexes: typing.Optional[typing.List[int]] = None
    #: Attributes of an `Element` node.# noqa
    attributes: typing.Optional[typing.List[NameValue]] = None
    #: Indexes of pseudo elements associated with this node in the `domNodes`array returned by `getSnapshot`, if any.# noqa
    pseudo_element_indexes: typing.Optional[typing.List[int]] = None
    #: The index of the node's related layout tree node in the `layoutTreeNodes`array returned by `getSnapshot`, if any.# noqa
    layout_node_index: typing.Optional[int] = None
    #: Document URL that `Document` or `FrameOwner` node points to.# noqa
    document_url: typing.Optional[str] = None
    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.# noqa
    base_url: typing.Optional[str] = None
    #: Only set for documents, contains the document's content language.# noqa
    content_language: typing.Optional[str] = None
    #: Only set for documents, contains the document's character set encoding.# noqa
    document_encoding: typing.Optional[str] = None
    #: `DocumentType` node's publicId.# noqa
    public_id: typing.Optional[str] = None
    #: `DocumentType` node's systemId.# noqa
    system_id: typing.Optional[str] = None
    #: Frame ID for frame owner elements and also for the document node.# noqa
    frame_id: typing.Optional[page.FrameId] = None
    #: The index of a frame owner element's content document in the `domNodes`array returned by `getSnapshot`, if any.# noqa
    content_document_index: typing.Optional[int] = None
    #: Type of a pseudo element node.# noqa
    pseudo_type: typing.Optional[dom.PseudoType] = None
    #: Shadow root type.# noqa
    shadow_root_type: typing.Optional[dom.ShadowRootType] = None
    #: Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked.# noqa
    is_clickable: typing.Optional[bool] = None
    #: Details of the node's event listeners, if any.# noqa
    event_listeners: typing.Optional[typing.List[dom_debugger.EventListener]] = None
    #: The selected url for nodes with a srcset attribute.# noqa
    current_source_url: typing.Optional[str] = None
    #: The url of the script (if any) that generates this node.# noqa
    origin_url: typing.Optional[str] = None
    #: Scroll offsets, set when this node is a Document.# noqa
    scroll_offset_x: typing.Optional[float] = None
    #: Description is missing from the devtools protocol document.# noqa
    scroll_offset_y: typing.Optional[float] = None


@dataclass
class InlineTextBox:
    """Details of post layout rendered text positions.

    The exact layout should not be regarded as stable and may change
    between versions.
    """

    #: The bounding box in document coordinates. Note that scroll offset of thedocument is ignored.# noqa
    bounding_box: dom.Rect
    #: The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    start_character_index: int
    #: The number of characters in this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    num_characters: int


@dataclass
class LayoutTreeNode:
    """Details of an element in the DOM tree with a LayoutObject."""

    #: The index of the related DOM node in the `domNodes` array returned by`getSnapshot`.# noqa
    dom_node_index: int
    #: The bounding box in document coordinates. Note that scroll offset of thedocument is ignored.# noqa
    bounding_box: dom.Rect
    #: Contents of the LayoutText, if any.# noqa
    layout_text: typing.Optional[str] = None
    #: The post-layout inline text nodes, if any.# noqa
    inline_text_nodes: typing.Optional[typing.List[InlineTextBox]] = None
    #: Index into the `computedStyles` array returned by `getSnapshot`.# noqa
    style_index: typing.Optional[int] = None
    #: Global paint order index, which is determined by the stacking order ofthe nodes. Nodes that are painted together will have the same index. Onlyprovided if includePaintOrder in getSnapshot was true.# noqa
    paint_order: typing.Optional[int] = None
    #: Set to true to indicate the element begins a new stacking context.# noqa
    is_stacking_context: typing.Optional[bool] = None


@dataclass
class ComputedStyle:
    """A subset of the full ComputedStyle as defined by the request
    whitelist."""

    #: Name/value pairs of computed style properties.# noqa
    properties: NameValue


@dataclass
class NameValue:
    """A name/value pair."""

    #: Attribute/property name.# noqa
    name: str
    #: Attribute/property value.# noqa
    value: str


@dataclass
class StringIndex:
    """Index of the string in the strings table."""


@dataclass
class ArrayOfStrings:
    """Index of the string in the strings table."""


@dataclass
class RareStringData:
    """Data that is only present on rare nodes."""

    #: Description is missing from the devtools protocol document.# noqa
    index: int
    #: Description is missing from the devtools protocol document.# noqa
    value: StringIndex


@dataclass
class RareBooleanData:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    index: int


@dataclass
class RareIntegerData:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    index: int
    #: Description is missing from the devtools protocol document.# noqa
    value: int


@dataclass
class Rectangle:
    """Description is missing from the devtools protocol document."""


@dataclass
class DocumentSnapshot:
    """Document snapshot."""

    #: Document URL that `Document` or `FrameOwner` node points to.# noqa
    document_url: StringIndex
    #: Document title.# noqa
    title: StringIndex
    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.# noqa
    base_url: StringIndex
    #: Contains the document's content language.# noqa
    content_language: StringIndex
    #: Contains the document's character set encoding.# noqa
    encoding_name: StringIndex
    #: `DocumentType` node's publicId.# noqa
    public_id: StringIndex
    #: `DocumentType` node's systemId.# noqa
    system_id: StringIndex
    #: Frame ID for frame owner elements and also for the document node.# noqa
    frame_id: StringIndex
    #: A table with dom nodes.# noqa
    nodes: NodeTreeSnapshot
    #: The nodes in the layout tree.# noqa
    layout: LayoutTreeSnapshot
    #: The post-layout inline text nodes.# noqa
    text_boxes: TextBoxSnapshot
    #: Horizontal scroll offset.# noqa
    scroll_offset_x: typing.Optional[float] = None
    #: Vertical scroll offset.# noqa
    scroll_offset_y: typing.Optional[float] = None
    #: Document content width.# noqa
    content_width: typing.Optional[float] = None
    #: Document content height.# noqa
    content_height: typing.Optional[float] = None


@dataclass
class NodeTreeSnapshot:
    """Table containing nodes."""

    #: Parent node index.# noqa
    parent_index: typing.Optional[typing.List[int]] = None
    #: `Node`'s nodeType.# noqa
    node_type: typing.Optional[typing.List[int]] = None
    #: Type of the shadow root the `Node` is in. String values are equal to the`ShadowRootType` enum.# noqa
    shadow_root_type: typing.Optional[RareStringData] = None
    #: `Node`'s nodeName.# noqa
    node_name: typing.Optional[typing.List[StringIndex]] = None
    #: `Node`'s nodeValue.# noqa
    node_value: typing.Optional[typing.List[StringIndex]] = None
    #: `Node`'s id, corresponds to DOM.Node.backendNodeId.# noqa
    backend_node_id: typing.Optional[typing.List[dom.BackendNodeId]] = None
    #: Attributes of an `Element` node. Flatten name, value pairs.# noqa
    attributes: typing.Optional[typing.List[ArrayOfStrings]] = None
    #: Only set for textarea elements, contains the text value.# noqa
    text_value: typing.Optional[RareStringData] = None
    #: Only set for input elements, contains the input's associated text value.# noqa
    input_value: typing.Optional[RareStringData] = None
    #: Only set for radio and checkbox input elements, indicates if the elementhas been checked# noqa
    input_checked: typing.Optional[RareBooleanData] = None
    #: Only set for option elements, indicates if the element has been selected# noqa
    option_selected: typing.Optional[RareBooleanData] = None
    #: The index of the document in the list of the snapshot documents.# noqa
    content_document_index: typing.Optional[RareIntegerData] = None
    #: Type of a pseudo element node.# noqa
    pseudo_type: typing.Optional[RareStringData] = None
    #: Pseudo element identifier for this node. Only present if there is a validpseudoType.# noqa
    pseudo_identifier: typing.Optional[RareStringData] = None
    #: Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked.# noqa
    is_clickable: typing.Optional[RareBooleanData] = None
    #: The selected url for nodes with a srcset attribute.# noqa
    current_source_url: typing.Optional[RareStringData] = None
    #: The url of the script (if any) that generates this node.# noqa
    origin_url: typing.Optional[RareStringData] = None


@dataclass
class LayoutTreeSnapshot:
    """Table of details of an element in the DOM tree with a LayoutObject."""

    #: Index of the corresponding node in the `NodeTreeSnapshot` array returnedby `captureSnapshot`.# noqa
    node_index: int
    #: Array of indexes specifying computed style strings, filtered according tothe `computedStyles` parameter passed to `captureSnapshot`.# noqa
    styles: ArrayOfStrings
    #: The absolute position bounding box.# noqa
    bounds: Rectangle
    #: Contents of the LayoutText, if any.# noqa
    text: StringIndex
    #: Stacking context information.# noqa
    stacking_contexts: RareBooleanData
    #: Global paint order index, which is determined by the stacking order ofthe nodes. Nodes that are painted together will have the same index. Onlyprovided if includePaintOrder in captureSnapshot was true.# noqa
    paint_orders: typing.Optional[typing.List[int]] = None
    #: The offset rect of nodes. Only available when includeDOMRects is set totrue# noqa
    offset_rects: typing.Optional[typing.List[Rectangle]] = None
    #: The scroll rect of nodes. Only available when includeDOMRects is set totrue# noqa
    scroll_rects: typing.Optional[typing.List[Rectangle]] = None
    #: The client rect of nodes. Only available when includeDOMRects is set totrue# noqa
    client_rects: typing.Optional[typing.List[Rectangle]] = None
    #: The list of background colors that are blended with colors of overlappingelements.# noqa
    blended_background_colors: typing.Optional[typing.List[StringIndex]] = None
    #: The list of computed text opacities.# noqa
    text_color_opacities: typing.Optional[typing.List[float]] = None


@dataclass
class TextBoxSnapshot:
    """Table of details of the post layout rendered text positions.

    The exact layout should not be regarded as stable and may change
    between versions.
    """

    #: Index of the layout tree node that owns this box collection.# noqa
    layout_index: int
    #: The absolute position bounding box.# noqa
    bounds: Rectangle
    #: The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    start: int
    #: The number of characters in this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    length: int
