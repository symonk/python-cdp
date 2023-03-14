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
import typing
from dataclasses import dataclass

from . import dom


@dataclass
class SourceOrderConfig:
    """Configuration data for drawing the source order of an elements
    children."""

    #: the color to outline the givent element in.# noqa
    parentOutlineColor: dom.RGBA
    #: the color to outline the child elements in.# noqa
    childOutlineColor: dom.RGBA


@dataclass
class GridHighlightConfig:
    """Configuration data for the highlighting of Grid elements."""

    #: Whether the extension lines from grid cells to the rulers should be shown(default: false).# noqa
    showGridExtensionLines: typing.Optional[bool] = None
    #: Show Positive line number labels (default: false).# noqa
    showPositiveLineNumbers: typing.Optional[bool] = None
    #: Show Negative line number labels (default: false).# noqa
    showNegativeLineNumbers: typing.Optional[bool] = None
    #: Show area name labels (default: false).# noqa
    showAreaNames: typing.Optional[bool] = None
    #: Show line name labels (default: false).# noqa
    showLineNames: typing.Optional[bool] = None
    #: Show track size labels (default: false).# noqa
    showTrackSizes: typing.Optional[bool] = None
    #: The grid container border highlight color (default: transparent).# noqa
    gridBorderColor: typing.Optional[dom.RGBA] = None
    #: The cell border color (default: transparent). Deprecated, please userowLineColor and columnLineColor instead.# noqa
    cellBorderColor: typing.Optional[dom.RGBA] = None
    #: The row line color (default: transparent).# noqa
    rowLineColor: typing.Optional[dom.RGBA] = None
    #: The column line color (default: transparent).# noqa
    columnLineColor: typing.Optional[dom.RGBA] = None
    #: Whether the grid border is dashed (default: false).# noqa
    gridBorderDash: typing.Optional[bool] = None
    #: Whether the cell border is dashed (default: false). Deprecated, please usrowLineDash and columnLineDash instead.# noqa
    cellBorderDash: typing.Optional[bool] = None
    #: Whether row lines are dashed (default: false).# noqa
    rowLineDash: typing.Optional[bool] = None
    #: Whether column lines are dashed (default: false).# noqa
    columnLineDash: typing.Optional[bool] = None
    #: The row gap highlight fill color (default: transparent).# noqa
    rowGapColor: typing.Optional[dom.RGBA] = None
    #: The row gap hatching fill color (default: transparent).# noqa
    rowHatchColor: typing.Optional[dom.RGBA] = None
    #: The column gap highlight fill color (default: transparent).# noqa
    columnGapColor: typing.Optional[dom.RGBA] = None
    #: The column gap hatching fill color (default: transparent).# noqa
    columnHatchColor: typing.Optional[dom.RGBA] = None
    #: The named grid areas border color (Default: transparent).# noqa
    areaBorderColor: typing.Optional[dom.RGBA] = None
    #: The grid container background color (Default: transparent).# noqa
    gridBackgroundColor: typing.Optional[dom.RGBA] = None


@dataclass
class FlexContainerHighlightConfig:
    """Configuration data for the highlighting of Flex container elements."""

    #: The style of the container border# noqa
    containerBorder: typing.Optional[LineStyle] = None
    #: The style of the separator between lines# noqa
    lineSeparator: typing.Optional[LineStyle] = None
    #: The style of the separator between items# noqa
    itemSeparator: typing.Optional[LineStyle] = None
    #: Style of content-distribution space on the main axis (justify-content).# noqa
    mainDistributedSpace: typing.Optional[BoxStyle] = None
    #: Style of content-distribution space on the cross axis (align-content).# noqa
    crossDistributedSpace: typing.Optional[BoxStyle] = None
    #: Style of empty space caused by row gaps (gap/row-gap).# noqa
    rowGapSpace: typing.Optional[BoxStyle] = None
    #: Style of empty space caused by columns gaps (gap/column-gap).# noqa
    columnGapSpace: typing.Optional[BoxStyle] = None
    #: Style of the self-alignment line (align-items).# noqa
    crossAlignment: typing.Optional[LineStyle] = None


@dataclass
class FlexItemHighlightConfig:
    """Configuration data for the highlighting of Flex item elements."""

    #: Style of the box representing the item's base size# noqa
    baseSizeBox: typing.Optional[BoxStyle] = None
    #: Style of the border around the box representing the item's base size# noqa
    baseSizeBorder: typing.Optional[LineStyle] = None
    #: Style of the arrow representing if the item grew or shrank# noqa
    flexibilityArrow: typing.Optional[LineStyle] = None


@dataclass
class LineStyle:
    """Style information for drawing a line."""

    #: The color of the line (default: transparent)# noqa
    color: typing.Optional[dom.RGBA] = None
    #: The line pattern (default: solid)# noqa
    pattern: typing.Optional[str] = None


@dataclass
class BoxStyle:
    """Style information for drawing a box."""

    #: The background color for the box (default: transparent)# noqa
    fillColor: typing.Optional[dom.RGBA] = None
    #: The hatching color for the box (default: transparent)# noqa
    hatchColor: typing.Optional[dom.RGBA] = None


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

    #: Whether the node info tooltip should be shown (default: false).# noqa
    showInfo: typing.Optional[bool] = None
    #: Whether the node styles in the tooltip (default: false).# noqa
    showStyles: typing.Optional[bool] = None
    #: Whether the rulers should be shown (default: false).# noqa
    showRulers: typing.Optional[bool] = None
    #: Whether the a11y info should be shown (default: true).# noqa
    showAccessibilityInfo: typing.Optional[bool] = None
    #: Whether the extension lines from node to the rulers should be shown(default: false).# noqa
    showExtensionLines: typing.Optional[bool] = None
    #: The content box highlight fill color (default: transparent).# noqa
    contentColor: typing.Optional[dom.RGBA] = None
    #: The padding highlight fill color (default: transparent).# noqa
    paddingColor: typing.Optional[dom.RGBA] = None
    #: The border highlight fill color (default: transparent).# noqa
    borderColor: typing.Optional[dom.RGBA] = None
    #: The margin highlight fill color (default: transparent).# noqa
    marginColor: typing.Optional[dom.RGBA] = None
    #: The event target element highlight fill color (default: transparent).# noqa
    eventTargetColor: typing.Optional[dom.RGBA] = None
    #: The shape outside fill color (default: transparent).# noqa
    shapeColor: typing.Optional[dom.RGBA] = None
    #: The shape margin fill color (default: transparent).# noqa
    shapeMarginColor: typing.Optional[dom.RGBA] = None
    #: The grid layout color (default: transparent).# noqa
    cssGridColor: typing.Optional[dom.RGBA] = None
    #: The color format used to format color styles (default: hex).# noqa
    colorFormat: typing.Optional[ColorFormat] = None
    #: The grid layout highlight configuration (default: all transparent).# noqa
    gridHighlightConfig: typing.Optional[GridHighlightConfig] = None
    #: The flex container highlight configuration (default: all transparent).# noqa
    flexContainerHighlightConfig: typing.Optional[FlexContainerHighlightConfig] = None
    #: The flex item highlight configuration (default: all transparent).# noqa
    flexItemHighlightConfig: typing.Optional[FlexItemHighlightConfig] = None
    #: The contrast algorithm to use for the contrast ratio (default: aa).# noqa
    contrastAlgorithm: typing.Optional[ContrastAlgorithm] = None
    #: The container query container highlight configuration (default: alltransparent).# noqa
    containerQueryContainerHighlightConfig: typing.Optional[ContainerQueryContainerHighlightConfig] = None


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

    #: A descriptor for the highlight appearance.# noqa
    gridHighlightConfig: GridHighlightConfig
    #: Identifier of the node to highlight.# noqa
    nodeId: dom.NodeId


@dataclass
class FlexNodeHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: A descriptor for the highlight appearance of flex containers.# noqa
    flexContainerHighlightConfig: FlexContainerHighlightConfig
    #: Identifier of the node to highlight.# noqa
    nodeId: dom.NodeId


@dataclass
class ScrollSnapContainerHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: The style of the snapport border (default: transparent)# noqa
    snapportBorder: typing.Optional[LineStyle] = None
    #: The style of the snap area border (default: transparent)# noqa
    snapAreaBorder: typing.Optional[LineStyle] = None
    #: The margin highlight fill color (default: transparent).# noqa
    scrollMarginColor: typing.Optional[dom.RGBA] = None
    #: The padding highlight fill color (default: transparent).# noqa
    scrollPaddingColor: typing.Optional[dom.RGBA] = None


@dataclass
class ScrollSnapHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: A descriptor for the highlight appearance of scroll snap containers.# noqa
    scrollSnapContainerHighlightConfig: ScrollSnapContainerHighlightConfig
    #: Identifier of the node to highlight.# noqa
    nodeId: dom.NodeId


@dataclass
class HingeConfig:
    """Configuration for dual screen hinge."""

    #: A rectangle represent hinge# noqa
    rect: dom.Rect
    #: The content box highlight fill color (default: a dark color).# noqa
    contentColor: typing.Optional[dom.RGBA] = None
    #: The content box highlight outline color (default: transparent).# noqa
    outlineColor: typing.Optional[dom.RGBA] = None


@dataclass
class ContainerQueryHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: A descriptor for the highlight appearance of container query containers.# noqa
    containerQueryContainerHighlightConfig: ContainerQueryContainerHighlightConfig
    #: Identifier of the container node to highlight.# noqa
    nodeId: dom.NodeId


@dataclass
class ContainerQueryContainerHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: The style of the container border.# noqa
    containerBorder: typing.Optional[LineStyle] = None
    #: The style of the descendants' borders.# noqa
    descendantBorder: typing.Optional[LineStyle] = None


@dataclass
class IsolatedElementHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: A descriptor for the highlight appearance of an element in isolationmode.# noqa
    isolationModeHighlightConfig: IsolationModeHighlightConfig
    #: Identifier of the isolated element to highlight.# noqa
    nodeId: dom.NodeId


@dataclass
class IsolationModeHighlightConfig:
    """Description is missing from the devtools protocol document."""

    #: The fill color of the resizers (default: transparent).# noqa
    resizerColor: typing.Optional[dom.RGBA] = None
    #: The fill color for resizer handles (default: transparent).# noqa
    resizerHandleColor: typing.Optional[dom.RGBA] = None
    #: The fill color for the mask covering non-isolated elements (default:transparent).# noqa
    maskColor: typing.Optional[dom.RGBA] = None


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
