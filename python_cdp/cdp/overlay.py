""" *** AUTO GENERATED FILE ***
This file was automatically generated by python-cdp.  Do not modify this file
as it is overwritten when new versions of the devtools protocol are released.  Instead modify the
code generator in https://github.com/symonk/python-cdp (or your fork) instead.  For documentation
on how to modify the generation process refer to the CONTRIBUTING.md file in the root of the
repository."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class SourceOrderConfig:
    """Configuration data for drawing the source order of an elements
    children."""


@dataclass
class GridHighlightConfig:
    """Configuration data for the highlighting of Grid elements."""


@dataclass
class FlexContainerHighlightConfig:
    """Configuration data for the highlighting of Flex container elements."""


@dataclass
class FlexItemHighlightConfig:
    """Configuration data for the highlighting of Flex item elements."""


@dataclass
class LineStyle:
    """Style information for drawing a line."""


@dataclass
class BoxStyle:
    """Style information for drawing a box."""


@dataclass
class HighlightConfig:
    """Configuration data for the highlighting of page elements."""


@dataclass
class GridNodeHighlightConfig:
    """Configurations for Persistent Grid Highlight."""


@dataclass
class FlexNodeHighlightConfig:
    """Missing description in devtools protocol."""


@dataclass
class ScrollSnapContainerHighlightConfig:
    """Missing description in devtools protocol."""


@dataclass
class ScrollSnapHighlightConfig:
    """Missing description in devtools protocol."""


@dataclass
class HingeConfig:
    """Configuration for dual screen hinge."""


@dataclass
class ContainerQueryHighlightConfig:
    """Missing description in devtools protocol."""


@dataclass
class ContainerQueryContainerHighlightConfig:
    """Missing description in devtools protocol."""


@dataclass
class IsolatedElementHighlightConfig:
    """Missing description in devtools protocol."""


@dataclass
class IsolationModeHighlightConfig:
    """Missing description in devtools protocol."""