# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `CSS`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/CSS/

from __future__ import annotations

import enum
from dataclasses import dataclass

from .utils import memoize_event


class StyleSheetId(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> StyleSheetId:
        return self

    @classmethod
    def from_json(cls, value: str) -> StyleSheetId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class StyleSheetOrigin(str, enum.Enum):
    """Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent stylesheets,
    "inspector" for stylesheets created by the inspector (i.e. those holding the "via inspector" rules), "regular" for
    regular stylesheets."""

    INJECTED = "injected"
    USER_AGENT = "user-agent"
    INSPECTOR = "inspector"
    REGULAR = "regular"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PseudoElementMatches(None):
    """CSS rule collection for a single pseudo style."""

    def to_json(self) -> PseudoElementMatches:
        return self

    @classmethod
    def from_json(cls, value: None) -> PseudoElementMatches:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class InheritedStyleEntry(None):
    """Inherited CSS rule collection from ancestor node."""

    def to_json(self) -> InheritedStyleEntry:
        return self

    @classmethod
    def from_json(cls, value: None) -> InheritedStyleEntry:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class InheritedPseudoElementMatches(None):
    """Inherited pseudo element matches from pseudos of an ancestor node."""

    def to_json(self) -> InheritedPseudoElementMatches:
        return self

    @classmethod
    def from_json(cls, value: None) -> InheritedPseudoElementMatches:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class RuleMatch(None):
    """Match data for a CSS rule."""

    def to_json(self) -> RuleMatch:
        return self

    @classmethod
    def from_json(cls, value: None) -> RuleMatch:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Value(None):
    """Data for a simple selector (these are delimited by commas in a selector list)."""

    def to_json(self) -> Value:
        return self

    @classmethod
    def from_json(cls, value: None) -> Value:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SelectorList(None):
    """Selector list data."""

    def to_json(self) -> SelectorList:
        return self

    @classmethod
    def from_json(cls, value: None) -> SelectorList:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSStyleSheetHeader(None):
    """CSS stylesheet metainformation."""

    def to_json(self) -> CSSStyleSheetHeader:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSStyleSheetHeader:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSRule(None):
    """CSS rule representation."""

    def to_json(self) -> CSSRule:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSRule:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class RuleUsage(None):
    """CSS coverage information."""

    def to_json(self) -> RuleUsage:
        return self

    @classmethod
    def from_json(cls, value: None) -> RuleUsage:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SourceRange(None):
    """Text range within a resource.

    All numbers are zero-based.
    """

    def to_json(self) -> SourceRange:
        return self

    @classmethod
    def from_json(cls, value: None) -> SourceRange:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ShorthandEntry(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> ShorthandEntry:
        return self

    @classmethod
    def from_json(cls, value: None) -> ShorthandEntry:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSComputedStyleProperty(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> CSSComputedStyleProperty:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSComputedStyleProperty:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSStyle(None):
    """CSS style representation."""

    def to_json(self) -> CSSStyle:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSStyle:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSProperty(None):
    """CSS property declaration data."""

    def to_json(self) -> CSSProperty:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSProperty:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSMedia(None):
    """CSS media rule descriptor."""

    def to_json(self) -> CSSMedia:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSMedia:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class MediaQuery(None):
    """Media query descriptor."""

    def to_json(self) -> MediaQuery:
        return self

    @classmethod
    def from_json(cls, value: None) -> MediaQuery:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class MediaQueryExpression(None):
    """Media query expression descriptor."""

    def to_json(self) -> MediaQueryExpression:
        return self

    @classmethod
    def from_json(cls, value: None) -> MediaQueryExpression:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSContainerQuery(None):
    """CSS container query rule descriptor."""

    def to_json(self) -> CSSContainerQuery:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSContainerQuery:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSSupports(None):
    """CSS Supports at-rule descriptor."""

    def to_json(self) -> CSSSupports:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSSupports:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSScope(None):
    """CSS Scope at-rule descriptor."""

    def to_json(self) -> CSSScope:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSScope:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSLayer(None):
    """CSS Layer at-rule descriptor."""

    def to_json(self) -> CSSLayer:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSLayer:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSLayerData(None):
    """CSS Layer data."""

    def to_json(self) -> CSSLayerData:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSLayerData:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class PlatformFontUsage(None):
    """Information about amount of glyphs that were rendered with given font."""

    def to_json(self) -> PlatformFontUsage:
        return self

    @classmethod
    def from_json(cls, value: None) -> PlatformFontUsage:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class FontVariationAxis(None):
    """Information about font variation axes for variable fonts."""

    def to_json(self) -> FontVariationAxis:
        return self

    @classmethod
    def from_json(cls, value: None) -> FontVariationAxis:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class FontFace(None):
    """Properties of a web font: https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions and
    additional information such as platformFontFamily and fontVariationAxes."""

    def to_json(self) -> FontFace:
        return self

    @classmethod
    def from_json(cls, value: None) -> FontFace:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSKeyframesRule(None):
    """CSS keyframes rule representation."""

    def to_json(self) -> CSSKeyframesRule:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSKeyframesRule:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CSSKeyframeRule(None):
    """CSS keyframe rule representation."""

    def to_json(self) -> CSSKeyframeRule:
        return self

    @classmethod
    def from_json(cls, value: None) -> CSSKeyframeRule:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class StyleDeclarationEdit(None):
    """A descriptor of operation to mutate style declaration text."""

    def to_json(self) -> StyleDeclarationEdit:
        return self

    @classmethod
    def from_json(cls, value: None) -> StyleDeclarationEdit:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("CSS.fontsUpdated")
class FontsUpdated:
    """Fires whenever a web font is updated.

    A non-empty font parameter indicates a successfully loaded web font.
    """

    font: FontFace


@dataclass
@memoize_event("CSS.mediaQueryResultChanged")
class MediaQueryResultChanged:
    """Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current
    implementation considers only viewport-dependent media features."""


@dataclass
@memoize_event("CSS.styleSheetAdded")
class StyleSheetAdded:
    """Fired whenever an active document stylesheet is added."""

    header: CSSStyleSheetHeader


@dataclass
@memoize_event("CSS.styleSheetChanged")
class StyleSheetChanged:
    """Fired whenever a stylesheet is changed as a result of the client operation."""

    style_sheet_id: StyleSheetId


@dataclass
@memoize_event("CSS.styleSheetRemoved")
class StyleSheetRemoved:
    """Fired whenever an active document stylesheet is removed."""

    style_sheet_id: StyleSheetId


async def add_rule() -> None:
    """Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the position specified
    by `location`.

    # noqa
    """
    ...


async def collect_class_names() -> None:
    """Returns all class names from specified stylesheet.

    # noqa
    """
    ...


async def create_style_sheet() -> None:
    """Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables the CSS agent for the given page.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables the CSS agent for the given page.

    Clients should not assume that the CSS agent has been enabled until the result of this command is received. # noqa
    """
    ...


async def force_pseudo_state() -> None:
    """Ensures that the given node will have specified pseudo-classes whenever its style is computed by the browser.

    # noqa
    """
    ...


async def get_background_colors() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def get_computed_style_for_node() -> None:
    """Returns the computed style for a DOM node identified by `nodeId`.

    # noqa
    """
    ...


async def get_inline_styles_for_node() -> None:
    """Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM attributes) for
    a DOM node identified by `nodeId`.

    # noqa
    """
    ...


async def get_matched_styles_for_node() -> None:
    """Returns requested styles for a DOM node identified by `nodeId`.

    # noqa
    """
    ...


async def get_media_queries() -> None:
    """Returns all media queries parsed by the rendering engine.

    # noqa
    """
    ...


async def get_platform_fonts_for_node() -> None:
    """Requests information about platform fonts which we used to render child TextNodes in the given node.

    # noqa
    """
    ...


async def get_style_sheet_text() -> None:
    """Returns the current textual content for a stylesheet.

    # noqa
    """
    ...


async def get_layers_for_node() -> None:
    """Returns all layers parsed by the rendering engine for the tree scope of a node.

    Given a DOM element identified by nodeId, getLayersForNode returns the root layer for the nearest ancestor document
    or shadow root. The layer root contains the full layer tree for the tree scope and their ordering. # noqa
    """
    ...


async def track_computed_style_updates() -> None:
    """Starts tracking the given computed styles for updates.

    The specified array of properties replaces the one previously specified. Pass empty array to disable tracking. Use
    takeComputedStyleUpdates to retrieve the list of nodes that had properties modified. The changes to computed style
    properties are only tracked for nodes pushed to the front-end by the DOM agent. If no changes to the tracked
    properties occur after the node has been pushed to the front-end, no updates will be issued for the node. # noqa
    """
    ...


async def take_computed_style_updates() -> None:
    """Polls the next batch of computed style updates.

    # noqa
    """
    ...


async def set_effective_property_value_for_node() -> None:
    """Find a rule with the given active property for the given node and set the new value for this property # noqa."""
    ...


async def set_keyframe_key() -> None:
    """Modifies the keyframe rule key text.

    # noqa
    """
    ...


async def set_media_text() -> None:
    """Modifies the rule selector.

    # noqa
    """
    ...


async def set_container_query_text() -> None:
    """Modifies the expression of a container query.

    # noqa
    """
    ...


async def set_supports_text() -> None:
    """Modifies the expression of a supports at-rule.

    # noqa
    """
    ...


async def set_scope_text() -> None:
    """Modifies the expression of a scope at-rule.

    # noqa
    """
    ...


async def set_rule_selector() -> None:
    """Modifies the rule selector.

    # noqa
    """
    ...


async def set_style_sheet_text() -> None:
    """Sets the new stylesheet text.

    # noqa
    """
    ...


async def set_style_texts() -> None:
    """Applies specified style edits one after another in the given order.

    # noqa
    """
    ...


async def start_rule_usage_tracking() -> None:
    """Enables the selector recording.

    # noqa
    """
    ...


async def stop_rule_usage_tracking() -> None:
    """Stop tracking rule usage and return the list of rules that were used since last call to `takeCoverageDelta` (or
    since start of coverage instrumentation).

    # noqa
    """
    ...


async def take_coverage_delta() -> None:
    """Obtain list of rules that became used since last call to this method (or since start of coverage
    instrumentation).

    # noqa
    """
    ...


async def set_local_fonts_enabled() -> None:
    """Enables/disables rendering of local CSS fonts (enabled by default).

    # noqa
    """
    ...
