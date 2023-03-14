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
    nodeType: int
    #: `Node`'s nodeName.# noqa
    nodeName: str
    #: `Node`'s nodeValue.# noqa
    nodeValue: str
    #: `Node`'s id, corresponds to DOM.Node.backendNodeId.# noqa
    backendNodeId: dom.BackendNodeId
    #: Only set for textarea elements, contains the text value.# noqa
    textValue: typing.Optional[str] = None
    #: Only set for input elements, contains the input's associated text value.# noqa
    inputValue: typing.Optional[str] = None
    #: Only set for radio and checkbox input elements, indicates if the elementhas been checked# noqa
    inputChecked: typing.Optional[bool] = None
    #: Only set for option elements, indicates if the element has been selected# noqa
    optionSelected: typing.Optional[bool] = None
    #: The indexes of the node's child nodes in the `domNodes` array returned by`getSnapshot`, if any.# noqa
    childNodeIndexes: typing.Optional[int] = None
    #: Attributes of an `Element` node.# noqa
    attributes: typing.Optional[NameValue] = None
    #: Indexes of pseudo elements associated with this node in the `domNodes`array returned by `getSnapshot`, if any.# noqa
    pseudoElementIndexes: typing.Optional[int] = None
    #: The index of the node's related layout tree node in the `layoutTreeNodes`array returned by `getSnapshot`, if any.# noqa
    layoutNodeIndex: typing.Optional[int] = None
    #: Document URL that `Document` or `FrameOwner` node points to.# noqa
    documentURL: typing.Optional[str] = None
    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.# noqa
    baseURL: typing.Optional[str] = None
    #: Only set for documents, contains the document's content language.# noqa
    contentLanguage: typing.Optional[str] = None
    #: Only set for documents, contains the document's character set encoding.# noqa
    documentEncoding: typing.Optional[str] = None
    #: `DocumentType` node's publicId.# noqa
    publicId: typing.Optional[str] = None
    #: `DocumentType` node's systemId.# noqa
    systemId: typing.Optional[str] = None
    #: Frame ID for frame owner elements and also for the document node.# noqa
    frameId: typing.Optional[page.FrameId] = None
    #: The index of a frame owner element's content document in the `domNodes`array returned by `getSnapshot`, if any.# noqa
    contentDocumentIndex: typing.Optional[int] = None
    #: Type of a pseudo element node.# noqa
    pseudoType: typing.Optional[dom.PseudoType] = None
    #: Shadow root type.# noqa
    shadowRootType: typing.Optional[dom.ShadowRootType] = None
    #: Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked.# noqa
    isClickable: typing.Optional[bool] = None
    #: Details of the node's event listeners, if any.# noqa
    eventListeners: typing.Optional[dom_debugger.EventListener] = None
    #: The selected url for nodes with a srcset attribute.# noqa
    currentSourceURL: typing.Optional[str] = None
    #: The url of the script (if any) that generates this node.# noqa
    originURL: typing.Optional[str] = None
    #: Scroll offsets, set when this node is a Document.# noqa
    scrollOffsetX: typing.Optional[float] = None
    #: Description is missing from the devtools protocol document.# noqa
    scrollOffsetY: typing.Optional[float] = None


@dataclass
class InlineTextBox:
    """Details of post layout rendered text positions.

    The exact layout should not be regarded as stable and may change
    between versions.
    """

    #: The bounding box in document coordinates. Note that scroll offset of thedocument is ignored.# noqa
    boundingBox: dom.Rect
    #: The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    startCharacterIndex: int
    #: The number of characters in this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    numCharacters: int


@dataclass
class LayoutTreeNode:
    """Details of an element in the DOM tree with a LayoutObject."""

    #: The index of the related DOM node in the `domNodes` array returned by`getSnapshot`.# noqa
    domNodeIndex: int
    #: The bounding box in document coordinates. Note that scroll offset of thedocument is ignored.# noqa
    boundingBox: dom.Rect
    #: Contents of the LayoutText, if any.# noqa
    layoutText: typing.Optional[str] = None
    #: The post-layout inline text nodes, if any.# noqa
    inlineTextNodes: typing.Optional[InlineTextBox] = None
    #: Index into the `computedStyles` array returned by `getSnapshot`.# noqa
    styleIndex: typing.Optional[int] = None
    #: Global paint order index, which is determined by the stacking order ofthe nodes. Nodes that are painted together will have the same index. Onlyprovided if includePaintOrder in getSnapshot was true.# noqa
    paintOrder: typing.Optional[int] = None
    #: Set to true to indicate the element begins a new stacking context.# noqa
    isStackingContext: typing.Optional[bool] = None


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
    documentURL: StringIndex
    #: Document title.# noqa
    title: StringIndex
    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.# noqa
    baseURL: StringIndex
    #: Contains the document's content language.# noqa
    contentLanguage: StringIndex
    #: Contains the document's character set encoding.# noqa
    encodingName: StringIndex
    #: `DocumentType` node's publicId.# noqa
    publicId: StringIndex
    #: `DocumentType` node's systemId.# noqa
    systemId: StringIndex
    #: Frame ID for frame owner elements and also for the document node.# noqa
    frameId: StringIndex
    #: A table with dom nodes.# noqa
    nodes: NodeTreeSnapshot
    #: The nodes in the layout tree.# noqa
    layout: LayoutTreeSnapshot
    #: The post-layout inline text nodes.# noqa
    textBoxes: TextBoxSnapshot
    #: Horizontal scroll offset.# noqa
    scrollOffsetX: typing.Optional[float] = None
    #: Vertical scroll offset.# noqa
    scrollOffsetY: typing.Optional[float] = None
    #: Document content width.# noqa
    contentWidth: typing.Optional[float] = None
    #: Document content height.# noqa
    contentHeight: typing.Optional[float] = None


@dataclass
class NodeTreeSnapshot:
    """Table containing nodes."""

    #: Parent node index.# noqa
    parentIndex: typing.Optional[int] = None
    #: `Node`'s nodeType.# noqa
    nodeType: typing.Optional[int] = None
    #: Type of the shadow root the `Node` is in. String values are equal to the`ShadowRootType` enum.# noqa
    shadowRootType: typing.Optional[RareStringData] = None
    #: `Node`'s nodeName.# noqa
    nodeName: typing.Optional[StringIndex] = None
    #: `Node`'s nodeValue.# noqa
    nodeValue: typing.Optional[StringIndex] = None
    #: `Node`'s id, corresponds to DOM.Node.backendNodeId.# noqa
    backendNodeId: typing.Optional[dom.BackendNodeId] = None
    #: Attributes of an `Element` node. Flatten name, value pairs.# noqa
    attributes: typing.Optional[ArrayOfStrings] = None
    #: Only set for textarea elements, contains the text value.# noqa
    textValue: typing.Optional[RareStringData] = None
    #: Only set for input elements, contains the input's associated text value.# noqa
    inputValue: typing.Optional[RareStringData] = None
    #: Only set for radio and checkbox input elements, indicates if the elementhas been checked# noqa
    inputChecked: typing.Optional[RareBooleanData] = None
    #: Only set for option elements, indicates if the element has been selected# noqa
    optionSelected: typing.Optional[RareBooleanData] = None
    #: The index of the document in the list of the snapshot documents.# noqa
    contentDocumentIndex: typing.Optional[RareIntegerData] = None
    #: Type of a pseudo element node.# noqa
    pseudoType: typing.Optional[RareStringData] = None
    #: Pseudo element identifier for this node. Only present if there is a validpseudoType.# noqa
    pseudoIdentifier: typing.Optional[RareStringData] = None
    #: Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked.# noqa
    isClickable: typing.Optional[RareBooleanData] = None
    #: The selected url for nodes with a srcset attribute.# noqa
    currentSourceURL: typing.Optional[RareStringData] = None
    #: The url of the script (if any) that generates this node.# noqa
    originURL: typing.Optional[RareStringData] = None


@dataclass
class LayoutTreeSnapshot:
    """Table of details of an element in the DOM tree with a LayoutObject."""

    #: Index of the corresponding node in the `NodeTreeSnapshot` array returnedby `captureSnapshot`.# noqa
    nodeIndex: int
    #: Array of indexes specifying computed style strings, filtered according tothe `computedStyles` parameter passed to `captureSnapshot`.# noqa
    styles: ArrayOfStrings
    #: The absolute position bounding box.# noqa
    bounds: Rectangle
    #: Contents of the LayoutText, if any.# noqa
    text: StringIndex
    #: Stacking context information.# noqa
    stackingContexts: RareBooleanData
    #: Global paint order index, which is determined by the stacking order ofthe nodes. Nodes that are painted together will have the same index. Onlyprovided if includePaintOrder in captureSnapshot was true.# noqa
    paintOrders: typing.Optional[int] = None
    #: The offset rect of nodes. Only available when includeDOMRects is set totrue# noqa
    offsetRects: typing.Optional[Rectangle] = None
    #: The scroll rect of nodes. Only available when includeDOMRects is set totrue# noqa
    scrollRects: typing.Optional[Rectangle] = None
    #: The client rect of nodes. Only available when includeDOMRects is set totrue# noqa
    clientRects: typing.Optional[Rectangle] = None
    #: The list of background colors that are blended with colors of overlappingelements.# noqa
    blendedBackgroundColors: typing.Optional[StringIndex] = None
    #: The list of computed text opacities.# noqa
    textColorOpacities: typing.Optional[float] = None


@dataclass
class TextBoxSnapshot:
    """Table of details of the post layout rendered text positions.

    The exact layout should not be regarded as stable and may change
    between versions.
    """

    #: Index of the layout tree node that owns this box collection.# noqa
    layoutIndex: int
    #: The absolute position bounding box.# noqa
    bounds: Rectangle
    #: The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    start: int
    #: The number of characters in this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    length: int
