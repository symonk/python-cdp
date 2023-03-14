# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Overlay`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Overlay/

from __future__ import annotations

import enum
from dataclasses import dataclass


@dataclass
class SourceOrderConfig:
    """Configuration data for drawing the source order of an elements
    children."""

    #: the color to outline the givent element in.
    parentOutlineColor: str
    #: the color to outline the child elements in.
    childOutlineColor: str


@dataclass
class GridHighlightConfig:
    """Configuration data for the highlighting of Grid elements."""

    #: Whether the extension lines from grid cells to the rulers should be shown(default: false).
    showGridExtensionLines: str
    #: Show Positive line number labels (default: false).
    showPositiveLineNumbers: str
    #: Show Negative line number labels (default: false).
    showNegativeLineNumbers: str
    #: Show area name labels (default: false).
    showAreaNames: str
    #: Show line name labels (default: false).
    showLineNames: str
    #: Show track size labels (default: false).
    showTrackSizes: str
    #: The grid container border highlight color (default: transparent).
    gridBorderColor: str
    #: The cell border color (default: transparent). Deprecated, please userowLineColor and columnLineColor instead.
    cellBorderColor: str
    #: The row line color (default: transparent).
    rowLineColor: str
    #: The column line color (default: transparent).
    columnLineColor: str
    #: Whether the grid border is dashed (default: false).
    gridBorderDash: str
    #: Whether the cell border is dashed (default: false). Deprecated, please usrowLineDash and columnLineDash instead.
    cellBorderDash: str
    #: Whether row lines are dashed (default: false).
    rowLineDash: str
    #: Whether column lines are dashed (default: false).
    columnLineDash: str
    #: The row gap highlight fill color (default: transparent).
    rowGapColor: str
    #: The row gap hatching fill color (default: transparent).
    rowHatchColor: str
    #: The column gap highlight fill color (default: transparent).
    columnGapColor: str
    #: The column gap hatching fill color (default: transparent).
    columnHatchColor: str
    #: The named grid areas border color (Default: transparent).
    areaBorderColor: str
    #: The grid container background color (Default: transparent).
    gridBackgroundColor: str


@dataclass
class FlexContainerHighlightConfig:
    """Configuration data for the highlighting of Flex container elements."""

    #: The style of the container border
    containerBorder: str
    #: The style of the separator between lines
    lineSeparator: str
    #: The style of the separator between items
    itemSeparator: str
    #: Style of content-distribution space on the main axis (justify-content).
    mainDistributedSpace: str
    #: Style of content-distribution space on the cross axis (align-content).
    crossDistributedSpace: str
    #: Style of empty space caused by row gaps (gap/row-gap).
    rowGapSpace: str
    #: Style of empty space caused by columns gaps (gap/column-gap).
    columnGapSpace: str
    #: Style of the self-alignment line (align-items).
    crossAlignment: str


@dataclass
class FlexItemHighlightConfig:
    """Configuration data for the highlighting of Flex item elements."""

    #: Style of the box representing the item's base size
    baseSizeBox: str
    #: Style of the border around the box representing the item's base size
    baseSizeBorder: str
    #: Style of the arrow representing if the item grew or shrank
    flexibilityArrow: str


@dataclass
class LineStyle:
    """Style information for drawing a line."""

    #: The color of the line (default: transparent)
    color: str
    #: The line pattern (default: solid)
    pattern: str


@dataclass
class BoxStyle:
    """Style information for drawing a box."""

    #: The background color for the box (default: transparent)
    fillColor: str
    #: The hatching color for the box (default: transparent)
    hatchColor: str


class ContrastAlgorithm(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    AA = "aa"
    AAA = "aaa"
    APCA = "apca"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class HighlightConfig:
    """Configuration data for the highlighting of page elements."""

    #: Whether the node info tooltip should be shown (default: false).
    showInfo: str
    #: Whether the node styles in the tooltip (default: false).
    showStyles: str
    #: Whether the rulers should be shown (default: false).
    showRulers: str
    #: Whether the a11y info should be shown (default: true).
    showAccessibilityInfo: str
    #: Whether the extension lines from node to the rulers should be shown(default: false).
    showExtensionLines: str
    #: The content box highlight fill color (default: transparent).
    contentColor: str
    #: The padding highlight fill color (default: transparent).
    paddingColor: str
    #: The border highlight fill color (default: transparent).
    borderColor: str
    #: The margin highlight fill color (default: transparent).
    marginColor: str
    #: The event target element highlight fill color (default: transparent).
    eventTargetColor: str
    #: The shape outside fill color (default: transparent).
    shapeColor: str
    #: The shape margin fill color (default: transparent).
    shapeMarginColor: str
    #: The grid layout color (default: transparent).
    cssGridColor: str
    #: The color format used to format color styles (default: hex).
    colorFormat: str
    #: The grid layout highlight configuration (default: all transparent).
    gridHighlightConfig: str
    #: The flex container highlight configuration (default: all transparent).
    flexContainerHighlightConfig: str
    #: The flex item highlight configuration (default: all transparent).
    flexItemHighlightConfig: str
    #: The contrast algorithm to use for the contrast ratio (default: aa).
    contrastAlgorithm: str
    #: The container query container highlight configuration (default: alltransparent).
    containerQueryContainerHighlightConfig: str


class ColorFormat(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    RGB = "rgb"
    HSL = "hsl"
    HWB = "hwb"
    HEX = "hex"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class GridNodeHighlightConfig:
    """Configurations for Persistent Grid Highlight."""

    #: A descriptor for the highlight appearance.
    gridHighlightConfig: str
    #: Identifier of the node to highlight.
    nodeId: str


@dataclass
class FlexNodeHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: A descriptor for the highlight appearance of flex containers.
    flexContainerHighlightConfig: str
    #: Identifier of the node to highlight.
    nodeId: str


@dataclass
class ScrollSnapContainerHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: The style of the snapport border (default: transparent)
    snapportBorder: str
    #: The style of the snap area border (default: transparent)
    snapAreaBorder: str
    #: The margin highlight fill color (default: transparent).
    scrollMarginColor: str
    #: The padding highlight fill color (default: transparent).
    scrollPaddingColor: str


@dataclass
class ScrollSnapHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: A descriptor for the highlight appearance of scroll snap containers.
    scrollSnapContainerHighlightConfig: str
    #: Identifier of the node to highlight.
    nodeId: str


@dataclass
class HingeConfig:
    """Configuration for dual screen hinge."""

    #: A rectangle represent hinge
    rect: str
    #: The content box highlight fill color (default: a dark color).
    contentColor: str
    #: The content box highlight outline color (default: transparent).
    outlineColor: str


@dataclass
class ContainerQueryHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: A descriptor for the highlight appearance of container query containers.
    containerQueryContainerHighlightConfig: str
    #: Identifier of the container node to highlight.
    nodeId: str


@dataclass
class ContainerQueryContainerHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: The style of the container border.
    containerBorder: str
    #: The style of the descendants' borders.
    descendantBorder: str


@dataclass
class IsolatedElementHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: A descriptor for the highlight appearance of an element in isolationmode.
    isolationModeHighlightConfig: str
    #: Identifier of the isolated element to highlight.
    nodeId: str


@dataclass
class IsolationModeHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: The fill color of the resizers (default: transparent).
    resizerColor: str
    #: The fill color for resizer handles (default: transparent).
    resizerHandleColor: str
    #: The fill color for the mask covering non-isolated elements (default:transparent).
    maskColor: str


class InspectMode(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    SEARCHFORNODE = "searchForNode"
    SEARCHFORUASHADOWDOM = "searchForUAShadowDOM"
    CAPTUREAREASCREENSHOT = "captureAreaScreenshot"
    SHOWDISTANCES = "showDistances"
    NONE = "none"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)
