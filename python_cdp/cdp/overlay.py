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

from . import dom
from . import page
from .utils import memoize_event


class SourceOrderConfig(None):
    """Configuration data for drawing the source order of an elements children."""

    def to_json(self) -> SourceOrderConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> SourceOrderConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class GridHighlightConfig(None):
    """Configuration data for the highlighting of Grid elements."""

    def to_json(self) -> GridHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> GridHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class FlexContainerHighlightConfig(None):
    """Configuration data for the highlighting of Flex container elements."""

    def to_json(self) -> FlexContainerHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> FlexContainerHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class FlexItemHighlightConfig(None):
    """Configuration data for the highlighting of Flex item elements."""

    def to_json(self) -> FlexItemHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> FlexItemHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class LineStyle(None):
    """Style information for drawing a line."""

    def to_json(self) -> LineStyle:
        return self

    @classmethod
    def from_json(cls, value: None) -> LineStyle:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class BoxStyle(None):
    """Style information for drawing a box."""

    def to_json(self) -> BoxStyle:
        return self

    @classmethod
    def from_json(cls, value: None) -> BoxStyle:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ContrastAlgorithm(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    AA = "aa"
    AAA = "aaa"
    APCA = "apca"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class HighlightConfig(None):
    """Configuration data for the highlighting of page elements."""

    def to_json(self) -> HighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> HighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ColorFormat(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    RGB = "rgb"
    HSL = "hsl"
    HWB = "hwb"
    HEX = "hex"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class GridNodeHighlightConfig(None):
    """Configurations for Persistent Grid Highlight."""

    def to_json(self) -> GridNodeHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> GridNodeHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class FlexNodeHighlightConfig(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> FlexNodeHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> FlexNodeHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ScrollSnapContainerHighlightConfig(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> ScrollSnapContainerHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> ScrollSnapContainerHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ScrollSnapHighlightConfig(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> ScrollSnapHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> ScrollSnapHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class HingeConfig(None):
    """Configuration for dual screen hinge."""

    def to_json(self) -> HingeConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> HingeConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ContainerQueryHighlightConfig(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> ContainerQueryHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> ContainerQueryHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ContainerQueryContainerHighlightConfig(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> ContainerQueryContainerHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> ContainerQueryContainerHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class IsolatedElementHighlightConfig(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> IsolatedElementHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> IsolatedElementHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class IsolationModeHighlightConfig(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> IsolationModeHighlightConfig:
        return self

    @classmethod
    def from_json(cls, value: None) -> IsolationModeHighlightConfig:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
