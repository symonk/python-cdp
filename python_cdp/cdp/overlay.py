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
from . import page
from .utils import memoize_event


@dataclass
class SourceOrderConfig:
    """Configuration data for drawing the source order of an elements children."""

    # the color to outline the givent element in.# noqa
    parent_outline_color: dom.RGBA
    # the color to outline the child elements in.# noqa
    child_outline_color: dom.RGBA


@dataclass
class GridHighlightConfig:
    """Configuration data for the highlighting of Grid elements."""

    # Whether the extension lines from grid cells to the rulers should be shown(default: false).# noqa
    show_grid_extension_lines: typing.Optional[bool]
    # Show Positive line number labels (default: false).# noqa
    show_positive_line_numbers: typing.Optional[bool]
    # Show Negative line number labels (default: false).# noqa
    show_negative_line_numbers: typing.Optional[bool]
    # Show area name labels (default: false).# noqa
    show_area_names: typing.Optional[bool]
    # Show line name labels (default: false).# noqa
    show_line_names: typing.Optional[bool]
    # Show track size labels (default: false).# noqa
    show_track_sizes: typing.Optional[bool]
    # The grid container border highlight color (default: transparent).# noqa
    grid_border_color: typing.Optional[dom.RGBA]
    # The cell border color (default: transparent). Deprecated, please userowLineColor and columnLineColor instead.# noqa
    cell_border_color: typing.Optional[dom.RGBA]
    # The row line color (default: transparent).# noqa
    row_line_color: typing.Optional[dom.RGBA]
    # The column line color (default: transparent).# noqa
    column_line_color: typing.Optional[dom.RGBA]
    # Whether the grid border is dashed (default: false).# noqa
    grid_border_dash: typing.Optional[bool]
    # Whether the cell border is dashed (default: false). Deprecated, please usrowLineDash and columnLineDash instead.# noqa
    cell_border_dash: typing.Optional[bool]
    # Whether row lines are dashed (default: false).# noqa
    row_line_dash: typing.Optional[bool]
    # Whether column lines are dashed (default: false).# noqa
    column_line_dash: typing.Optional[bool]
    # The row gap highlight fill color (default: transparent).# noqa
    row_gap_color: typing.Optional[dom.RGBA]
    # The row gap hatching fill color (default: transparent).# noqa
    row_hatch_color: typing.Optional[dom.RGBA]
    # The column gap highlight fill color (default: transparent).# noqa
    column_gap_color: typing.Optional[dom.RGBA]
    # The column gap hatching fill color (default: transparent).# noqa
    column_hatch_color: typing.Optional[dom.RGBA]
    # The named grid areas border color (Default: transparent).# noqa
    area_border_color: typing.Optional[dom.RGBA]
    # The grid container background color (Default: transparent).# noqa
    grid_background_color: typing.Optional[dom.RGBA]


@dataclass
class FlexContainerHighlightConfig:
    """Configuration data for the highlighting of Flex container elements."""

    # The style of the container border# noqa
    container_border: typing.Optional[LineStyle]
    # The style of the separator between lines# noqa
    line_separator: typing.Optional[LineStyle]
    # The style of the separator between items# noqa
    item_separator: typing.Optional[LineStyle]
    # Style of content-distribution space on the main axis (justify-content).# noqa
    main_distributed_space: typing.Optional[BoxStyle]
    # Style of content-distribution space on the cross axis (align-content).# noqa
    cross_distributed_space: typing.Optional[BoxStyle]
    # Style of empty space caused by row gaps (gap/row-gap).# noqa
    row_gap_space: typing.Optional[BoxStyle]
    # Style of empty space caused by columns gaps (gap/column-gap).# noqa
    column_gap_space: typing.Optional[BoxStyle]
    # Style of the self-alignment line (align-items).# noqa
    cross_alignment: typing.Optional[LineStyle]


@dataclass
class FlexItemHighlightConfig:
    """Configuration data for the highlighting of Flex item elements."""

    # Style of the box representing the item's base size# noqa
    base_size_box: typing.Optional[BoxStyle]
    # Style of the border around the box representing the item's base size# noqa
    base_size_border: typing.Optional[LineStyle]
    # Style of the arrow representing if the item grew or shrank# noqa
    flexibility_arrow: typing.Optional[LineStyle]


@dataclass
class LineStyle:
    """Style information for drawing a line."""

    # The color of the line (default: transparent)# noqa
    color: typing.Optional[dom.RGBA]
    # The line pattern (default: solid)# noqa
    pattern: typing.Optional[typing.List[typing.Literal["dashed", "dotted"]]]


@dataclass
class BoxStyle:
    """Style information for drawing a box."""

    # The background color for the box (default: transparent)# noqa
    fill_color: typing.Optional[dom.RGBA]
    # The hatching color for the box (default: transparent)# noqa
    hatch_color: typing.Optional[dom.RGBA]


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

    # Whether the node info tooltip should be shown (default: false).# noqa
    show_info: typing.Optional[bool]
    # Whether the node styles in the tooltip (default: false).# noqa
    show_styles: typing.Optional[bool]
    # Whether the rulers should be shown (default: false).# noqa
    show_rulers: typing.Optional[bool]
    # Whether the a11y info should be shown (default: true).# noqa
    show_accessibility_info: typing.Optional[bool]
    # Whether the extension lines from node to the rulers should be shown(default: false).# noqa
    show_extension_lines: typing.Optional[bool]
    # The content box highlight fill color (default: transparent).# noqa
    content_color: typing.Optional[dom.RGBA]
    # The padding highlight fill color (default: transparent).# noqa
    padding_color: typing.Optional[dom.RGBA]
    # The border highlight fill color (default: transparent).# noqa
    border_color: typing.Optional[dom.RGBA]
    # The margin highlight fill color (default: transparent).# noqa
    margin_color: typing.Optional[dom.RGBA]
    # The event target element highlight fill color (default: transparent).# noqa
    event_target_color: typing.Optional[dom.RGBA]
    # The shape outside fill color (default: transparent).# noqa
    shape_color: typing.Optional[dom.RGBA]
    # The shape margin fill color (default: transparent).# noqa
    shape_margin_color: typing.Optional[dom.RGBA]
    # The grid layout color (default: transparent).# noqa
    css_grid_color: typing.Optional[dom.RGBA]
    # The color format used to format color styles (default: hex).# noqa
    color_format: typing.Optional[ColorFormat]
    # The grid layout highlight configuration (default: all transparent).# noqa
    grid_highlight_config: typing.Optional[GridHighlightConfig]
    # The flex container highlight configuration (default: all transparent).# noqa
    flex_container_highlight_config: typing.Optional[FlexContainerHighlightConfig]
    # The flex item highlight configuration (default: all transparent).# noqa
    flex_item_highlight_config: typing.Optional[FlexItemHighlightConfig]
    # The contrast algorithm to use for the contrast ratio (default: aa).# noqa
    contrast_algorithm: typing.Optional[ContrastAlgorithm]
    # The container query container highlight configuration (default: alltransparent).# noqa
    container_query_container_highlight_config: typing.Optional[ContainerQueryContainerHighlightConfig]


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

    # A descriptor for the highlight appearance.# noqa
    grid_highlight_config: GridHighlightConfig
    # Identifier of the node to highlight.# noqa
    node_id: dom.NodeId


@dataclass
class FlexNodeHighlightConfig:
    """Description is missing from the devtools protocol document."""

    # A descriptor for the highlight appearance of flex containers.# noqa
    flex_container_highlight_config: FlexContainerHighlightConfig
    # Identifier of the node to highlight.# noqa
    node_id: dom.NodeId


@dataclass
class ScrollSnapContainerHighlightConfig:
    """Description is missing from the devtools protocol document."""

    # The style of the snapport border (default: transparent)# noqa
    snapport_border: typing.Optional[LineStyle]
    # The style of the snap area border (default: transparent)# noqa
    snap_area_border: typing.Optional[LineStyle]
    # The margin highlight fill color (default: transparent).# noqa
    scroll_margin_color: typing.Optional[dom.RGBA]
    # The padding highlight fill color (default: transparent).# noqa
    scroll_padding_color: typing.Optional[dom.RGBA]


@dataclass
class ScrollSnapHighlightConfig:
    """Description is missing from the devtools protocol document."""

    # A descriptor for the highlight appearance of scroll snap containers.# noqa
    scroll_snap_container_highlight_config: ScrollSnapContainerHighlightConfig
    # Identifier of the node to highlight.# noqa
    node_id: dom.NodeId


@dataclass
class HingeConfig:
    """Configuration for dual screen hinge."""

    # A rectangle represent hinge# noqa
    rect: dom.Rect
    # The content box highlight fill color (default: a dark color).# noqa
    content_color: typing.Optional[dom.RGBA]
    # The content box highlight outline color (default: transparent).# noqa
    outline_color: typing.Optional[dom.RGBA]


@dataclass
class ContainerQueryHighlightConfig:
    """Description is missing from the devtools protocol document."""

    # A descriptor for the highlight appearance of container query containers.# noqa
    container_query_container_highlight_config: ContainerQueryContainerHighlightConfig
    # Identifier of the container node to highlight.# noqa
    node_id: dom.NodeId


@dataclass
class ContainerQueryContainerHighlightConfig:
    """Description is missing from the devtools protocol document."""

    # The style of the container border.# noqa
    container_border: typing.Optional[LineStyle]
    # The style of the descendants' borders.# noqa
    descendant_border: typing.Optional[LineStyle]


@dataclass
class IsolatedElementHighlightConfig:
    """Description is missing from the devtools protocol document."""

    # A descriptor for the highlight appearance of an element in isolation mode.# noqa
    isolation_mode_highlight_config: IsolationModeHighlightConfig
    # Identifier of the isolated element to highlight.# noqa
    node_id: dom.NodeId


@dataclass
class IsolationModeHighlightConfig:
    """Description is missing from the devtools protocol document."""

    # The fill color of the resizers (default: transparent).# noqa
    resizer_color: typing.Optional[dom.RGBA]
    # The fill color for resizer handles (default: transparent).# noqa
    resizer_handle_color: typing.Optional[dom.RGBA]
    # The fill color for the mask covering non-isolated elements (default:transparent).# noqa
    mask_color: typing.Optional[dom.RGBA]


class InspectMode(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    SEARCH_FOR_NODE = "search_for_node"
    SEARCH_FOR_U_A_SHADOW_D_O_M = "search_for_ua_shadow_dom"
    CAPTURE_AREA_SCREENSHOT = "capture_area_screenshot"
    SHOW_DISTANCES = "show_distances"
    NONE = "none"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
@memoize_event("Overlay.inspectNodeRequested")
class InspectNodeRequested:
    """Fired when the node should be inspected.

    This happens after call to `setInspectMode` or when user manually inspects an element.
    """

    backend_node_id: dom.BackendNodeId


@dataclass
@memoize_event("Overlay.nodeHighlightRequested")
class NodeHighlightRequested:
    """Fired when the node should be highlighted.

    This happens after call to `setInspectMode`.
    """

    node_id: dom.NodeId


@dataclass
@memoize_event("Overlay.screenshotRequested")
class ScreenshotRequested:
    """Fired when user asks to capture screenshot of some area on the page."""

    viewport: page.Viewport


@dataclass
@memoize_event("Overlay.inspectModeCanceled")
class InspectModeCanceled:
    """Fired when user cancels the inspect mode."""


async def disable() -> None:
    """Disables domain notifications.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables domain notifications.

    # noqa
    """
    ...


async def get_highlight_object_for_test() -> None:
    """For testing.

    # noqa
    """
    ...


async def get_grid_highlight_objects_for_test() -> None:
    """For Persistent Grid testing.

    # noqa
    """
    ...


async def get_source_order_highlight_object_for_test() -> None:
    """For Source Order Viewer testing.

    # noqa
    """
    ...


async def hide_highlight() -> None:
    """Hides any highlight.

    # noqa
    """
    ...


async def highlight_frame() -> None:
    """Highlights owner element of the frame with given id.

    Deprecated: Doesn't work reliablity and cannot be fixed due to process
    separatation (the owner node might be in a different process). Determine
    the owner node in the client and use highlightNode. # noqa
    """
    ...


async def highlight_node() -> None:
    """Highlights DOM node with given id or with the given JavaScript object wrapper.

    Either nodeId or objectId must be specified. # noqa
    """
    ...


async def highlight_quad() -> None:
    """Highlights given quad.

    Coordinates are absolute with respect to the main frame viewport. # noqa
    """
    ...


async def highlight_rect() -> None:
    """Highlights given rectangle.

    Coordinates are absolute with respect to the main frame viewport. # noqa
    """
    ...


async def highlight_source_order() -> None:
    """Highlights the source order of the children of the DOM node with given id or with the given JavaScript object
    wrapper.

    Either nodeId or objectId must be specified. # noqa
    """
    ...


async def set_inspect_mode() -> None:
    """Enters the 'inspect' mode.

    In this mode, elements that user is hovering over are highlighted. Backend then generates 'inspectNodeRequested'
    event upon element selection. # noqa
    """
    ...


async def set_show_ad_highlights() -> None:
    """Highlights owner element of all frames detected to be ads.

    # noqa
    """
    ...


async def set_paused_in_debugger_message() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def set_show_debug_borders() -> None:
    """Requests that backend shows debug borders on layers # noqa."""
    ...


async def set_show_fps_counter() -> None:
    """Requests that backend shows the FPS counter # noqa."""
    ...


async def set_show_grid_overlays() -> None:
    """Highlight multiple elements with the CSS Grid overlay.

    # noqa
    """
    ...


async def set_show_flex_overlays() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def set_show_scroll_snap_overlays() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def set_show_container_query_overlays() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def set_show_paint_rects() -> None:
    """Requests that backend shows paint rectangles # noqa."""
    ...


async def set_show_layout_shift_regions() -> None:
    """Requests that backend shows layout shift regions # noqa."""
    ...


async def set_show_scroll_bottleneck_rects() -> None:
    """Requests that backend shows scroll bottleneck rects # noqa."""
    ...


async def set_show_hit_test_borders() -> None:
    """Deprecated, no longer has any effect.

    # noqa
    """
    ...


async def set_show_web_vitals() -> None:
    """Request that backend shows an overlay with web vital metrics.

    # noqa
    """
    ...


async def set_show_viewport_size_on_resize() -> None:
    """Paints viewport size upon main frame resize.

    # noqa
    """
    ...


async def set_show_hinge() -> None:
    """Add a dual screen device hinge # noqa."""
    ...


async def set_show_isolated_elements() -> None:
    """Show elements in isolation mode with overlays.

    # noqa
    """
    ...
