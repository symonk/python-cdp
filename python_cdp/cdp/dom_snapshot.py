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

    ...


@dataclass
class InlineTextBox:
    """Details of post layout rendered text positions.

    The exact layout should not be regarded as stable and may change
    between versions.
    """

    ...


@dataclass
class LayoutTreeNode:
    """Details of an element in the DOM tree with a LayoutObject."""

    ...


@dataclass
class ComputedStyle:
    """A subset of the full ComputedStyle as defined by the request
    whitelist."""

    ...


@dataclass
class NameValue:
    """A name/value pair."""

    ...


@dataclass
class StringIndex:
    """Index of the string in the strings table."""

    ...


@dataclass
class ArrayOfStrings:
    """Index of the string in the strings table."""

    ...


@dataclass
class RareStringData:
    """Data that is only present on rare nodes."""

    ...


@dataclass
class RareBooleanData:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class RareIntegerData:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class Rectangle:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class DocumentSnapshot:
    """Document snapshot."""

    ...


@dataclass
class NodeTreeSnapshot:
    """Table containing nodes."""

    ...


@dataclass
class LayoutTreeSnapshot:
    """Table of details of an element in the DOM tree with a LayoutObject."""

    ...


@dataclass
class TextBoxSnapshot:
    """Table of details of the post layout rendered text positions.

    The exact layout should not be regarded as stable and may change
    between versions.
    """

    ...
