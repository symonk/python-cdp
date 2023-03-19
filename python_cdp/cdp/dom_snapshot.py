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


class DOMNode(None):
    """A Node in the DOM tree."""

    def to_json(self) -> DOMNode:
        return self

    @classmethod
    def from_json(cls, value: None) -> DOMNode:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class InlineTextBox(None):
    """Details of post layout rendered text positions.

    The exact layout should not be regarded as stable and may change between versions.
    """

    def to_json(self) -> InlineTextBox:
        return self

    @classmethod
    def from_json(cls, value: None) -> InlineTextBox:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class LayoutTreeNode(None):
    """Details of an element in the DOM tree with a LayoutObject."""

    def to_json(self) -> LayoutTreeNode:
        return self

    @classmethod
    def from_json(cls, value: None) -> LayoutTreeNode:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ComputedStyle(None):
    """A subset of the full ComputedStyle as defined by the request whitelist."""

    def to_json(self) -> ComputedStyle:
        return self

    @classmethod
    def from_json(cls, value: None) -> ComputedStyle:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class NameValue(None):
    """A name/value pair."""

    def to_json(self) -> NameValue:
        return self

    @classmethod
    def from_json(cls, value: None) -> NameValue:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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


class RareStringData(None):
    """Data that is only present on rare nodes."""

    def to_json(self) -> RareStringData:
        return self

    @classmethod
    def from_json(cls, value: None) -> RareStringData:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class RareBooleanData(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> RareBooleanData:
        return self

    @classmethod
    def from_json(cls, value: None) -> RareBooleanData:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class RareIntegerData(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> RareIntegerData:
        return self

    @classmethod
    def from_json(cls, value: None) -> RareIntegerData:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class Rectangle:
    """Description is missing from the devtools protocol document."""


class DocumentSnapshot(None):
    """Document snapshot."""

    def to_json(self) -> DocumentSnapshot:
        return self

    @classmethod
    def from_json(cls, value: None) -> DocumentSnapshot:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class NodeTreeSnapshot(None):
    """Table containing nodes."""

    def to_json(self) -> NodeTreeSnapshot:
        return self

    @classmethod
    def from_json(cls, value: None) -> NodeTreeSnapshot:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class LayoutTreeSnapshot(None):
    """Table of details of an element in the DOM tree with a LayoutObject."""

    def to_json(self) -> LayoutTreeSnapshot:
        return self

    @classmethod
    def from_json(cls, value: None) -> LayoutTreeSnapshot:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class TextBoxSnapshot(None):
    """Table of details of the post layout rendered text positions.

    The exact layout should not be regarded as stable and may change between versions.
    """

    def to_json(self) -> TextBoxSnapshot:
        return self

    @classmethod
    def from_json(cls, value: None) -> TextBoxSnapshot:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
