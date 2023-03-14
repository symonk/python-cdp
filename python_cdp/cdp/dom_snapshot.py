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

from dataclasses import dataclass


@dataclass
class DOMNode:
    """A Node in the DOM tree."""

    #: `Node`'s nodeType.
    nodeType: str
    #: `Node`'s nodeName.
    nodeName: str
    #: `Node`'s nodeValue.
    nodeValue: str
    #: Only set for textarea elements, contains the text value.
    textValue: str
    #: Only set for input elements, contains the input's associated text value.
    inputValue: str
    #: Only set for radio and checkbox input elements, indicates if the elementhas been checked
    inputChecked: str
    #: Only set for option elements, indicates if the element has been selected
    optionSelected: str
    #: `Node`'s id, corresponds to DOM.Node.backendNodeId.
    backendNodeId: str
    #: The indexes of the node's child nodes in the `domNodes` array returned by`getSnapshot`, if any.
    childNodeIndexes: str
    #: Attributes of an `Element` node.
    attributes: str
    #: Indexes of pseudo elements associated with this node in the `domNodes`array returned by `getSnapshot`, if any.
    pseudoElementIndexes: str
    #: The index of the node's related layout tree node in the `layoutTreeNodes`array returned by `getSnapshot`, if any.
    layoutNodeIndex: str
    #: Document URL that `Document` or `FrameOwner` node points to.
    documentURL: str
    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.
    baseURL: str
    #: Only set for documents, contains the document's content language.
    contentLanguage: str
    #: Only set for documents, contains the document's character set encoding.
    documentEncoding: str
    #: `DocumentType` node's publicId.
    publicId: str
    #: `DocumentType` node's systemId.
    systemId: str
    #: Frame ID for frame owner elements and also for the document node.
    frameId: str
    #: The index of a frame owner element's content document in the `domNodes`array returned by `getSnapshot`, if any.
    contentDocumentIndex: str
    #: Type of a pseudo element node.
    pseudoType: str
    #: Shadow root type.
    shadowRootType: str
    #: Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked.
    isClickable: str
    #: Details of the node's event listeners, if any.
    eventListeners: str
    #: The selected url for nodes with a srcset attribute.
    currentSourceURL: str
    #: The url of the script (if any) that generates this node.
    originURL: str
    #: Scroll offsets, set when this node is a Document.
    scrollOffsetX: str
    #: Description is missing from the devtools protocol document.
    scrollOffsetY: str


@dataclass
class InlineTextBox:
    """Details of post layout rendered text positions.

    The exact layout should not be regarded as stable and may change
    between versions.
    """

    #: The bounding box in document coordinates. Note that scroll offset of thedocument is ignored.
    boundingBox: str
    #: The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.
    startCharacterIndex: str
    #: The number of characters in this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.
    numCharacters: str


@dataclass
class LayoutTreeNode:
    """Details of an element in the DOM tree with a LayoutObject."""

    #: The index of the related DOM node in the `domNodes` array returned by`getSnapshot`.
    domNodeIndex: str
    #: The bounding box in document coordinates. Note that scroll offset of thedocument is ignored.
    boundingBox: str
    #: Contents of the LayoutText, if any.
    layoutText: str
    #: The post-layout inline text nodes, if any.
    inlineTextNodes: str
    #: Index into the `computedStyles` array returned by `getSnapshot`.
    styleIndex: str
    #: Global paint order index, which is determined by the stacking order ofthe nodes. Nodes that are painted together will have the same index. Onlyprovided if includePaintOrder in getSnapshot was true.
    paintOrder: str
    #: Set to true to indicate the element begins a new stacking context.
    isStackingContext: str


@dataclass
class ComputedStyle:
    """A subset of the full ComputedStyle as defined by the request
    whitelist."""

    #: Name/value pairs of computed style properties.
    properties: str


@dataclass
class NameValue:
    """A name/value pair."""

    #: Attribute/property name.
    name: str
    #: Attribute/property value.
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

    #: Description is missing from the devtools protocol document.
    index: str
    #: Description is missing from the devtools protocol document.
    value: str


@dataclass
class RareBooleanData:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.
    index: str


@dataclass
class RareIntegerData:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.
    index: str
    #: Description is missing from the devtools protocol document.
    value: str


@dataclass
class Rectangle:
    """Description is missing from the devtools protocol document."""


@dataclass
class DocumentSnapshot:
    """Document snapshot."""

    #: Document URL that `Document` or `FrameOwner` node points to.
    documentURL: str
    #: Document title.
    title: str
    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.
    baseURL: str
    #: Contains the document's content language.
    contentLanguage: str
    #: Contains the document's character set encoding.
    encodingName: str
    #: `DocumentType` node's publicId.
    publicId: str
    #: `DocumentType` node's systemId.
    systemId: str
    #: Frame ID for frame owner elements and also for the document node.
    frameId: str
    #: A table with dom nodes.
    nodes: str
    #: The nodes in the layout tree.
    layout: str
    #: The post-layout inline text nodes.
    textBoxes: str
    #: Horizontal scroll offset.
    scrollOffsetX: str
    #: Vertical scroll offset.
    scrollOffsetY: str
    #: Document content width.
    contentWidth: str
    #: Document content height.
    contentHeight: str


@dataclass
class NodeTreeSnapshot:
    """Table containing nodes."""

    #: Parent node index.
    parentIndex: str
    #: `Node`'s nodeType.
    nodeType: str
    #: Type of the shadow root the `Node` is in. String values are equal to the`ShadowRootType` enum.
    shadowRootType: str
    #: `Node`'s nodeName.
    nodeName: str
    #: `Node`'s nodeValue.
    nodeValue: str
    #: `Node`'s id, corresponds to DOM.Node.backendNodeId.
    backendNodeId: str
    #: Attributes of an `Element` node. Flatten name, value pairs.
    attributes: str
    #: Only set for textarea elements, contains the text value.
    textValue: str
    #: Only set for input elements, contains the input's associated text value.
    inputValue: str
    #: Only set for radio and checkbox input elements, indicates if the elementhas been checked
    inputChecked: str
    #: Only set for option elements, indicates if the element has been selected
    optionSelected: str
    #: The index of the document in the list of the snapshot documents.
    contentDocumentIndex: str
    #: Type of a pseudo element node.
    pseudoType: str
    #: Pseudo element identifier for this node. Only present if there is a validpseudoType.
    pseudoIdentifier: str
    #: Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked.
    isClickable: str
    #: The selected url for nodes with a srcset attribute.
    currentSourceURL: str
    #: The url of the script (if any) that generates this node.
    originURL: str


@dataclass
class LayoutTreeSnapshot:
    """Table of details of an element in the DOM tree with a LayoutObject."""

    #: Index of the corresponding node in the `NodeTreeSnapshot` array returnedby `captureSnapshot`.
    nodeIndex: str
    #: Array of indexes specifying computed style strings, filtered according tothe `computedStyles` parameter passed to `captureSnapshot`.
    styles: str
    #: The absolute position bounding box.
    bounds: str
    #: Contents of the LayoutText, if any.
    text: str
    #: Stacking context information.
    stackingContexts: str
    #: Global paint order index, which is determined by the stacking order ofthe nodes. Nodes that are painted together will have the same index. Onlyprovided if includePaintOrder in captureSnapshot was true.
    paintOrders: str
    #: The offset rect of nodes. Only available when includeDOMRects is set totrue
    offsetRects: str
    #: The scroll rect of nodes. Only available when includeDOMRects is set totrue
    scrollRects: str
    #: The client rect of nodes. Only available when includeDOMRects is set totrue
    clientRects: str
    #: The list of background colors that are blended with colors of overlappingelements.
    blendedBackgroundColors: str
    #: The list of computed text opacities.
    textColorOpacities: str


@dataclass
class TextBoxSnapshot:
    """Table of details of the post layout rendered text positions.

    The exact layout should not be regarded as stable and may change
    between versions.
    """

    #: Index of the layout tree node that owns this box collection.
    layoutIndex: str
    #: The absolute position bounding box.
    bounds: str
    #: The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.
    start: str
    #: The number of characters in this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.
    length: str
