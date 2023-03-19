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
from . import page


@dataclass
class DOMNode:
    """A Node in the DOM tree."""

    # `Node`'s nodeType.# noqa


int
# `Node`'s nodeName.# noqa
str
# `Node`'s nodeValue.# noqa
str
# `Node`'s id, corresponds to DOM.Node.backendNodeId.# noqa
dom.BackendNodeId
# Only set for textarea elements, contains the text value.# noqa
typing.Optional[str]
# Only set for input elements, contains the input's associated text value.# noqa
typing.Optional[str]
# Only set for radio and checkbox input elements, indicates if the elementhas been checked# noqa
typing.Optional[bool]
# Only set for option elements, indicates if the element has been selected# noqa
typing.Optional[bool]
# The indexes of the node's child nodes in the `domNodes` array returned by`getSnapshot`, if any.# noqa
typing.Optional[typing.List[int]]
# Attributes of an `Element` node.# noqa
typing.Optional[typing.List[NameValue]]
# Indexes of pseudo elements associated with this node in the `domNodes`array returned by `getSnapshot`, if any.# noqa
typing.Optional[typing.List[int]]
# The index of the node's related layout tree node in the `layoutTreeNodes`array returned by `getSnapshot`, if any.# noqa
typing.Optional[int]
# Document URL that `Document` or `FrameOwner` node points to.# noqa
typing.Optional[str]
# Base URL that `Document` or `FrameOwner` node uses for URL completion.# noqa
typing.Optional[str]
# Only set for documents, contains the document's content language.# noqa
typing.Optional[str]
# Only set for documents, contains the document's character set encoding.# noqa
typing.Optional[str]
# `DocumentType` node's publicId.# noqa
typing.Optional[str]
# `DocumentType` node's systemId.# noqa
typing.Optional[str]
# Frame ID for frame owner elements and also for the document node.# noqa
typing.Optional[page.FrameId]
# The index of a frame owner element's content document in the `domNodes`array returned by `getSnapshot`, if any.# noqa
typing.Optional[int]
# Type of a pseudo element node.# noqa
typing.Optional[dom.PseudoType]
# Shadow root type.# noqa
typing.Optional[dom.ShadowRootType]
# Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked.# noqa
typing.Optional[bool]
# Details of the node's event listeners, if any.# noqa
typing.Optional[typing.List[DOMDebugger.EventListener]]
# The selected url for nodes with a srcset attribute.# noqa
typing.Optional[str]
# The url of the script (if any) that generates this node.# noqa
typing.Optional[str]
# Scroll offsets, set when this node is a Document.# noqa
typing.Optional[float]
# Description is missing from the devtools protocol document.# noqa
typing.Optional[float]


@dataclass
class InlineTextBox:
    """Details of post layout rendered text positions.

    The exact layout should not be regarded as stable and may change between versions.
    """

    # The bounding box in document coordinates. Note that scroll offset of thedocument is ignored.# noqa


dom.Rect
# The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
int
# The number of characters in this post layout textbox substring. Charactersthat would be represented as a surrogate pair in UTF-16 have length 2.# noqa
int


@dataclass
class LayoutTreeNode:
    """Details of an element in the DOM tree with a LayoutObject."""

    # The index of the related DOM node in the `domNodes` array returned by`getSnapshot`.# noqa


int
# The bounding box in document coordinates. Note that scroll offset of thedocument is ignored.# noqa
dom.Rect
# Contents of the LayoutText, if any.# noqa
typing.Optional[str]
# The post-layout inline text nodes, if any.# noqa
typing.Optional[typing.List[InlineTextBox]]
# Index into the `computedStyles` array returned by `getSnapshot`.# noqa
typing.Optional[int]
# Global paint order index, which is determined by the stacking order of thenodes. Nodes that are painted together will have the same index. Only providedif includePaintOrder in getSnapshot was true.# noqa
typing.Optional[int]
# Set to true to indicate the element begins a new stacking context.# noqa
typing.Optional[bool]


@dataclass
class ComputedStyle:
    """A subset of the full ComputedStyle as defined by the request whitelist."""

    # Name/value pairs of computed style properties.# noqa


typing.List[NameValue]


@dataclass
class NameValue:
    """A name/value pair."""

    # Attribute/property name.# noqa


str
# Attribute/property value.# noqa
str


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

    # Description is missing from the devtools protocol document.# noqa


typing.List[int]
# Description is missing from the devtools protocol document.# noqa
typing.List[StringIndex]


@dataclass
class RareBooleanData:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa


typing.List[int]


@dataclass
class RareIntegerData:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa


typing.List[int]
# Description is missing from the devtools protocol document.# noqa
typing.List[int]


@dataclass
class Rectangle:
    """Description is missing from the devtools protocol document."""


@dataclass
class DocumentSnapshot:
    """Document snapshot."""

    # Document URL that `Document` or `FrameOwner` node points to.# noqa


StringIndex
# Document title.# noqa
StringIndex
# Base URL that `Document` or `FrameOwner` node uses for URL completion.# noqa
StringIndex
# Contains the document's content language.# noqa
StringIndex
# Contains the document's character set encoding.# noqa
StringIndex
# `DocumentType` node's publicId.# noqa
StringIndex
# `DocumentType` node's systemId.# noqa
StringIndex
# Frame ID for frame owner elements and also for the document node.# noqa
StringIndex
# A table with dom nodes.# noqa
NodeTreeSnapshot
# The nodes in the layout tree.# noqa
LayoutTreeSnapshot
# The post-layout inline text nodes.# noqa
TextBoxSnapshot
# Horizontal scroll offset.# noqa
typing.Optional[float]
# Vertical scroll offset.# noqa
typing.Optional[float]
# Document content width.# noqa
typing.Optional[float]
# Document content height.# noqa
typing.Optional[float]


@dataclass
class NodeTreeSnapshot:
    """Table containing nodes."""

    # Parent node index.# noqa


typing.Optional[typing.List[int]]
# `Node`'s nodeType.# noqa
typing.Optional[typing.List[int]]
# Type of the shadow root the `Node` is in. String values are equal to the`ShadowRootType` enum.# noqa
RareStringData
# `Node`'s nodeName.# noqa
typing.Optional[typing.List[StringIndex]]
# `Node`'s nodeValue.# noqa
typing.Optional[typing.List[StringIndex]]
# `Node`'s id, corresponds to DOM.Node.backendNodeId.# noqa
typing.Optional[typing.List[DOM.BackendNodeId]]
# Attributes of an `Element` node. Flatten name, value pairs.# noqa
typing.Optional[typing.List[ArrayOfStrings]]
# Only set for textarea elements, contains the text value.# noqa
RareStringData
# Only set for input elements, contains the input's associated text value.# noqa
RareStringData
# Only set for radio and checkbox input elements, indicates if the elementhas been checked# noqa
RareBooleanData
# Only set for option elements, indicates if the element has been selected# noqa
RareBooleanData
# The index of the document in the list of the snapshot documents.# noqa
RareIntegerData
# Type of a pseudo element node.# noqa
RareStringData
# Pseudo element identifier for this node. Only present if there is a validpseudoType.# noqa
RareStringData
# Whether this DOM node responds to mouse clicks. This includes nodes thathave had click event listeners attached via JavaScript as well as anchor tagsthat naturally navigate when clicked.# noqa
RareBooleanData
# The selected url for nodes with a srcset attribute.# noqa
RareStringData
# The url of the script (if any) that generates this node.# noqa
RareStringData


@dataclass
class LayoutTreeSnapshot:
    """Table of details of an element in the DOM tree with a LayoutObject."""

    # Index of the corresponding node in the `NodeTreeSnapshot` array returnedby `captureSnapshot`.# noqa


typing.List[int]
# Array of indexes specifying computed style strings, filtered according tothe `computedStyles` parameter passed to `captureSnapshot`.# noqa
typing.List[ArrayOfStrings]
# The absolute position bounding box.# noqa
typing.List[Rectangle]
# Contents of the LayoutText, if any.# noqa
typing.List[StringIndex]
# Stacking context information.# noqa
RareBooleanData
# Global paint order index, which is determined by the stacking order of thenodes. Nodes that are painted together will have the same index. Only providedif includePaintOrder in captureSnapshot was true.# noqa
typing.Optional[typing.List[int]]
# The offset rect of nodes. Only available when includeDOMRects is set totrue# noqa
typing.Optional[typing.List[Rectangle]]
# The scroll rect of nodes. Only available when includeDOMRects is set totrue# noqa
typing.Optional[typing.List[Rectangle]]
# The client rect of nodes. Only available when includeDOMRects is set totrue# noqa
typing.Optional[typing.List[Rectangle]]
# The list of background colors that are blended with colors of overlappingelements.# noqa
typing.Optional[typing.List[StringIndex]]
# The list of computed text opacities.# noqa
typing.Optional[typing.List[float]]


@dataclass
class TextBoxSnapshot:
    """Table of details of the post layout rendered text positions.

    The exact layout should not be regarded as stable and may change between versions.
    """

    # Index of the layout tree node that owns this box collection.# noqa


typing.List[int]
# The absolute position bounding box.# noqa
typing.List[Rectangle]
# The starting index in characters, for this post layout textbox substring.Characters that would be represented as a surrogate pair in UTF-16 have length2.# noqa
typing.List[int]
# The number of characters in this post layout textbox substring. Charactersthat would be represented as a surrogate pair in UTF-16 have length 2.# noqa
typing.List[int]


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
