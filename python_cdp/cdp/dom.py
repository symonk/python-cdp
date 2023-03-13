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

from dataclasses import dataclass


@dataclass
class NodeId:
    """Unique DOM node identifier."""

    ...


@dataclass
class BackendNodeId:
    """Unique DOM node identifier used to reference a node that may not have
    been pushed to the front-end."""

    ...


@dataclass
class BackendNode:
    """Backend node with a friendly name."""

    ...


@dataclass
class PseudoType:
    """Pseudo element type."""

    ...


@dataclass
class ShadowRootType:
    """Shadow root type."""

    ...


@dataclass
class CompatibilityMode:
    """Document compatibility mode."""

    ...


@dataclass
class PhysicalAxes:
    """ContainerSelector physical axes."""

    ...


@dataclass
class LogicalAxes:
    """ContainerSelector logical axes."""

    ...


@dataclass
class Node:
    """DOM interaction is implemented in terms of mirror objects that represent
    the actual DOM nodes.

    DOMNode is a base node mirror type.
    """

    ...


@dataclass
class RGBA:
    """A structure holding an RGBA color."""

    ...


@dataclass
class Quad:
    """An array of quad vertices, x immediately followed by y for each point,
    points clock-wise."""

    ...


@dataclass
class BoxModel:
    """Box model."""

    ...


@dataclass
class ShapeOutsideInfo:
    """CSS Shape Outside details."""

    ...


@dataclass
class Rect:
    """Rectangle."""

    ...


@dataclass
class CSSComputedStyleProperty:
    """Description is missing from the devtools protocol document."""

    ...
