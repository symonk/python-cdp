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

    #: `Node`'s nodeType.# noqa
    nodeType: str
    #: `Node`'s nodeName.# noqa
    nodeName: str
    #: `Node`'s nodeValue.# noqa
    nodeValue: str
    #: Only set for textarea elements, contains the text value.# noqa
    textValue: str
    #: Only set for input elements, contains the input's associated text value.# noqa
    inputValue: str
    #: Only set for radio and checkbox input elements, indicates if the elementhas been checked# noqa
    inputChecked: str
    #: Only set for option elements, indicates if the element has been selected# noqa
    optionSelected: str
    #: `Node`'s id, corresponds to DOM.Node.backendNodeId.# noqa
    backendNodeId: str
    #: The indexes of the node's child nodes in the `domNodes` array returned by`getSnapshot`, if any.# noqa
    childNodeIndexes: str
    #: Attributes of an `Element` node.# noqa
    attributes: str
    #: Indexes of pseudo elements associated with this node in the `domNodes`array returned by `getSnapshot`, if any.# noqa
    pseudoElementIndexes: str
    #: The index of the node's related layout tree node in the `layoutTreeNodes`array returned by `getSnapshot`, if any.# noqa
    layoutNodeIndex: str
    #: Document URL that `Document` or `FrameOwner` node points to.# noqa
    documentURL: str
    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.# noqa
    baseURL: str
    #: Only set for documents, contains the document's content language.# noqa
    contentLanguage: str
    #: Only set for documents, contains the document's character set encoding.# noqa
    documentEncoding: str
    #: `DocumentType` node's publicId.# noqa
    publicId: str
    #: `DocumentType` node's systemId.# noqa
    systemId: str
    #: Frame ID for frame owner elements and also for the document node.# noqa
    frameId: str
    #: The index of a frame owner element's content document in the `domNodes`array returned by `getSnapshot`, if any.# noqa
    contentDocumentIndex: str
    #: Type of a pseudo element node.# noqa
    pseudoType: str
    #: Shadow root type.# noqa
    shadowRootType: str
    #: Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked.# noqa
    isClickable: str
    #: Details of the node's event listeners, if any.# noqa
    eventListeners: str
    #: The selected url for nodes with a srcset attribute.# noqa
    currentSourceURL: str
    #: The url of the script (if any) that generates this node.# noqa
    originURL: str
    #: Scroll offsets, set when this node is a Document.# noqa
    scrollOffsetX: str
    #: Description is missing from the devtools protocol document.# noqa
    scrollOffsetY: str


@dataclass
class InlineTextBox:
    """Details of post layout rendered text positions.

    The exact layout should not be regarded as stable and may change
    between versions.
    """

    #: The bounding box in document coordinates. Note that scroll offset of thedocument is ignored.# noqa
    boundingBox: str
    #: The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    startCharacterIndex: str
    #: The number of characters in this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    numCharacters: str


@dataclass
class LayoutTreeNode:
    """Details of an element in the DOM tree with a LayoutObject."""

    #: The index of the related DOM node in the `domNodes` array returned by`getSnapshot`.# noqa
    domNodeIndex: str
    #: The bounding box in document coordinates. Note that scroll offset of thedocument is ignored.# noqa
    boundingBox: str
    #: Contents of the LayoutText, if any.# noqa
    layoutText: str
    #: The post-layout inline text nodes, if any.# noqa
    inlineTextNodes: str
    #: Index into the `computedStyles` array returned by `getSnapshot`.# noqa
    styleIndex: str
    #: Global paint order index, which is determined by the stacking order ofthe nodes. Nodes that are painted together will have the same index. Onlyprovided if includePaintOrder in getSnapshot was true.# noqa
    paintOrder: str
    #: Set to true to indicate the element begins a new stacking context.# noqa
    isStackingContext: str


@dataclass
class ComputedStyle:
    """A subset of the full ComputedStyle as defined by the request
    whitelist."""

    #: Name/value pairs of computed style properties.# noqa
    properties: str


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
    index: str
    #: Description is missing from the devtools protocol document.# noqa
    value: str


@dataclass
class RareBooleanData:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    index: str


@dataclass
class RareIntegerData:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    index: str
    #: Description is missing from the devtools protocol document.# noqa
    value: str


@dataclass
class Rectangle:
    """Description is missing from the devtools protocol document."""


@dataclass
class DocumentSnapshot:
    """Document snapshot."""

    #: Document URL that `Document` or `FrameOwner` node points to.# noqa
    documentURL: str
    #: Document title.# noqa
    title: str
    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.# noqa
    baseURL: str
    #: Contains the document's content language.# noqa
    contentLanguage: str
    #: Contains the document's character set encoding.# noqa
    encodingName: str
    #: `DocumentType` node's publicId.# noqa
    publicId: str
    #: `DocumentType` node's systemId.# noqa
    systemId: str
    #: Frame ID for frame owner elements and also for the document node.# noqa
    frameId: str
    #: A table with dom nodes.# noqa
    nodes: str
    #: The nodes in the layout tree.# noqa
    layout: str
    #: The post-layout inline text nodes.# noqa
    textBoxes: str
    #: Horizontal scroll offset.# noqa
    scrollOffsetX: str
    #: Vertical scroll offset.# noqa
    scrollOffsetY: str
    #: Document content width.# noqa
    contentWidth: str
    #: Document content height.# noqa
    contentHeight: str


@dataclass
class NodeTreeSnapshot:
    """Table containing nodes."""

    #: Parent node index.# noqa
    parentIndex: str
    #: `Node`'s nodeType.# noqa
    nodeType: str
    #: Type of the shadow root the `Node` is in. String values are equal to the`ShadowRootType` enum.# noqa
    shadowRootType: str
    #: `Node`'s nodeName.# noqa
    nodeName: str
    #: `Node`'s nodeValue.# noqa
    nodeValue: str
    #: `Node`'s id, corresponds to DOM.Node.backendNodeId.# noqa
    backendNodeId: str
    #: Attributes of an `Element` node. Flatten name, value pairs.# noqa
    attributes: str
    #: Only set for textarea elements, contains the text value.# noqa
    textValue: str
    #: Only set for input elements, contains the input's associated text value.# noqa
    inputValue: str
    #: Only set for radio and checkbox input elements, indicates if the elementhas been checked# noqa
    inputChecked: str
    #: Only set for option elements, indicates if the element has been selected# noqa
    optionSelected: str
    #: The index of the document in the list of the snapshot documents.# noqa
    contentDocumentIndex: str
    #: Type of a pseudo element node.# noqa
    pseudoType: str
    #: Pseudo element identifier for this node. Only present if there is a validpseudoType.# noqa
    pseudoIdentifier: str
    #: Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked.# noqa
    isClickable: str
    #: The selected url for nodes with a srcset attribute.# noqa
    currentSourceURL: str
    #: The url of the script (if any) that generates this node.# noqa
    originURL: str


@dataclass
class LayoutTreeSnapshot:
    """Table of details of an element in the DOM tree with a LayoutObject."""

    #: Index of the corresponding node in the `NodeTreeSnapshot` array returnedby `captureSnapshot`.# noqa
    nodeIndex: str
    #: Array of indexes specifying computed style strings, filtered according tothe `computedStyles` parameter passed to `captureSnapshot`.# noqa
    styles: str
    #: The absolute position bounding box.# noqa
    bounds: str
    #: Contents of the LayoutText, if any.# noqa
    text: str
    #: Stacking context information.# noqa
    stackingContexts: str
    #: Global paint order index, which is determined by the stacking order ofthe nodes. Nodes that are painted together will have the same index. Onlyprovided if includePaintOrder in captureSnapshot was true.# noqa
    paintOrders: str
    #: The offset rect of nodes. Only available when includeDOMRects is set totrue# noqa
    offsetRects: str
    #: The scroll rect of nodes. Only available when includeDOMRects is set totrue# noqa
    scrollRects: str
    #: The client rect of nodes. Only available when includeDOMRects is set totrue# noqa
    clientRects: str
    #: The list of background colors that are blended with colors of overlappingelements.# noqa
    blendedBackgroundColors: str
    #: The list of computed text opacities.# noqa
    textColorOpacities: str


@dataclass
class TextBoxSnapshot:
    """Table of details of the post layout rendered text positions.

    The exact layout should not be regarded as stable and may change
    between versions.
    """

    #: Index of the layout tree node that owns this box collection.# noqa
    layoutIndex: str
    #: The absolute position bounding box.# noqa
    bounds: str
    #: The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    start: str
    #: The number of characters in this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
    length: str
