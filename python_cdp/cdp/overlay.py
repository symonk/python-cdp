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

from dataclasses import dataclass


@dataclass
class SourceOrderConfig:
    """Configuration data for drawing the source order of an elements
    children."""

    ...


@dataclass
class GridHighlightConfig:
    """Configuration data for the highlighting of Grid elements."""

    ...


@dataclass
class FlexContainerHighlightConfig:
    """Configuration data for the highlighting of Flex container elements."""

    ...


@dataclass
class FlexItemHighlightConfig:
    """Configuration data for the highlighting of Flex item elements."""

    ...


@dataclass
class LineStyle:
    """Style information for drawing a line."""

    ...


@dataclass
class BoxStyle:
    """Style information for drawing a box."""

    ...


class ContrastAlgorithm(str):
    """Description is missing from the devtools protocol document.."""

    def to_json(self) -> str:
        return self


@dataclass
class HighlightConfig:
    """Configuration data for the highlighting of page elements."""

    ...


class ColorFormat(str):
    """Description is missing from the devtools protocol document.."""

    def to_json(self) -> str:
        return self


@dataclass
class GridNodeHighlightConfig:
    """Configurations for Persistent Grid Highlight."""

    ...


@dataclass
class FlexNodeHighlightConfig:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ScrollSnapContainerHighlightConfig:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ScrollSnapHighlightConfig:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class HingeConfig:
    """Configuration for dual screen hinge."""

    ...


@dataclass
class ContainerQueryHighlightConfig:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ContainerQueryContainerHighlightConfig:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class IsolatedElementHighlightConfig:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class IsolationModeHighlightConfig:
    """Description is missing from the devtools protocol document."""

    ...


class InspectMode(str):
    """Description is missing from the devtools protocol document.."""

    def to_json(self) -> str:
        return self
