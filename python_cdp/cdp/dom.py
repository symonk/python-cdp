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
from dataclasses import dataclass


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


class ShadowRootType(str, enum.Enum):
    """Shadow root type."""

    USER_AGENT = "user_agent"
    OPEN = "open"
    CLOSED = "closed"


class CompatibilityMode(str, enum.Enum):
    """Document compatibility mode."""

    QUIRKSMODE = "QuirksMode"
    LIMITEDQUIRKSMODE = "LimitedQuirksMode"
    NOQUIRKSMODE = "NoQuirksMode"


class PhysicalAxes(str, enum.Enum):
    """ContainerSelector physical axes."""

    HORIZONTAL = "Horizontal"
    VERTICAL = "Vertical"
    BOTH = "Both"


class LogicalAxes(str, enum.Enum):
    """ContainerSelector logical axes."""

    INLINE = "Inline"
    BLOCK = "Block"
    BOTH = "Both"


@dataclass
class Node:
    """DOM interaction is implemented in terms of mirror objects that represent
    the actual DOM nodes.

    DOMNode is a base node mirror type.
    """


@dataclass
class RGBA:
    """A structure holding an RGBA color."""


@dataclass
class Quad:
    """An array of quad vertices, x immediately followed by y for each point,
    points clock-wise."""


@dataclass
class BoxModel:
    """Box model."""


@dataclass
class ShapeOutsideInfo:
    """CSS Shape Outside details."""


@dataclass
class Rect:
    """Rectangle."""


@dataclass
class CSSComputedStyleProperty:
    """Description is missing from the devtools protocol document."""
