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
import typing
from dataclasses import dataclass

from . import dom
from . import page
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


@dataclass
class PseudoElementMatches:
    """CSS rule collection for a single pseudo style."""

    # Pseudo element type. # noqa
    pseudo_type: dom.PseudoType
    # Matches of CSS rules applicable to the pseudo style. # noqa
    matches: RuleMatch
    # Pseudo element custom ident. # noqa
    pseudo_identifier: typing.Optional[str]


@dataclass
class InheritedStyleEntry:
    """Inherited CSS rule collection from ancestor node."""

    # Matches of CSS rules matching the ancestor node in the style inheritancechain. # noqa
    matched_css_rules: RuleMatch
    # The ancestor node's inline style, if any, in the style inheritance chain. # noqa
    inline_style: typing.Optional[CSSStyle]


@dataclass
class InheritedPseudoElementMatches:
    """Inherited pseudo element matches from pseudos of an ancestor node."""

    # Matches of pseudo styles from the pseudos of an ancestor node. # noqa
    pseudo_elements: PseudoElementMatches


@dataclass
class RuleMatch:
    """Match data for a CSS rule."""

    # CSS rule in the match. # noqa
    rule: CSSRule
    # Matching selector indices in the rule's selectorList selectors (0-based). # noqa
    matching_selectors: int


@dataclass
class Value:
    """Data for a simple selector (these are delimited by commas in a selector list)."""

    # Value text. # noqa
    text: str
    # Value range in the underlying resource (if available). # noqa
    range: typing.Optional[SourceRange]
    # Specificity of the selector. # noqa
    specificity: typing.Optional[Specificity]


@dataclass
class Specificity:
    """Specificity:
    https://drafts.csswg.org/selectors/#specificity-rules"""

    # The a component, which represents the number of ID selectors. # noqa
    a: int
    # The b component, which represents the number of class selectors,attributes selectors, and pseudo-classes. # noqa
    b: int
    # The c component, which represents the number of type selectors and pseudo-elements. # noqa
    c: int


@dataclass
class SelectorList:
    """Selector list data."""

    # Selectors in the list. # noqa
    selectors: Value
    # Rule selector text. # noqa
    text: str


@dataclass
class CSSStyleSheetHeader:
    """CSS stylesheet metainformation."""

    # The stylesheet identifier. # noqa
    style_sheet_id: StyleSheetId
    # Owner frame identifier. # noqa
    frame_id: page.FrameId
    # Stylesheet resource URL. Empty if this is a constructed stylesheet createdusing new CSSStyleSheet() (but non-empty if this is a constructed sylesheetimported as a CSS module script). # noqa
    source_url: str
    # Stylesheet origin. # noqa
    origin: StyleSheetOrigin
    # Stylesheet title. # noqa
    title: str
    # Denotes whether the stylesheet is disabled. # noqa
    disabled: bool
    # Whether this stylesheet is created for STYLE tag by parser. This flag isnot set for document.written STYLE tags. # noqa
    is_inline: bool
    # Whether this stylesheet is mutable. Inline stylesheets become mutableafter they have been modified via CSSOM API. <link> element's stylesheets becomemutable only if DevTools modifies them. Constructed stylesheets (newCSSStyleSheet()) are mutable immediately after creation. # noqa
    is_mutable: bool
    # True if this stylesheet is created through new CSSStyleSheet() or importedas a CSS module script. # noqa
    is_constructed: bool
    # Line offset of the stylesheet within the resource (zero based). # noqa
    start_line: float
    # Column offset of the stylesheet within the resource (zero based). # noqa
    start_column: float
    # Size of the content (in characters). # noqa
    length: float
    # Line offset of the end of the stylesheet within the resource (zero based). # noqa
    end_line: float
    # Column offset of the end of the stylesheet within the resource (zerobased). # noqa
    end_column: float
    # URL of source map associated with the stylesheet (if any). # noqa
    source_map_url: typing.Optional[str]
    # The backend id for the owner node of the stylesheet. # noqa
    owner_node: typing.Optional[dom.BackendNodeId]
    # Whether the sourceURL field value comes from the sourceURL comment. # noqa
    has_source_url: typing.Optional[bool]
    # If the style sheet was loaded from a network resource, this indicates whenthe resource failed to load # noqa
    loading_failed: typing.Optional[bool]


@dataclass
class CSSRule:
    """CSS rule representation."""

    # Rule selector data. # noqa
    selector_list: SelectorList
    # Parent stylesheet's origin. # noqa
    origin: StyleSheetOrigin
    # Associated style declaration. # noqa
    style: CSSStyle
    # The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. # noqa
    style_sheet_id: typing.Optional[StyleSheetId]
    # Array of selectors from ancestor style rules, sorted by distance from thecurrent rule. # noqa
    nesting_selectors: typing.Optional[str]
    # Media list array (for rules involving media queries). The array enumeratesmedia queries starting with the innermost one, going outwards. # noqa
    media: typing.Optional[CSSMedia]
    # Container query list array (for rules involving container queries). Thearray enumerates container queries starting with the innermost one, goingoutwards. # noqa
    container_queries: typing.Optional[CSSContainerQuery]
    # @supports CSS at-rule array. The array enumerates @supports at-rulesstarting with the innermost one, going outwards. # noqa
    supports: typing.Optional[CSSSupports]
    # Cascade layer array. Contains the layer hierarchy that this rule belongsto starting with the innermost layer and going outwards. # noqa
    layers: typing.Optional[CSSLayer]
    # @scope CSS at-rule array. The array enumerates @scope at-rules startingwith the innermost one, going outwards. # noqa
    scopes: typing.Optional[CSSScope]


@dataclass
class RuleUsage:
    """CSS coverage information."""

    # The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. # noqa
    style_sheet_id: StyleSheetId
    # Offset of the start of the rule (including selector) from the beginning ofthe stylesheet. # noqa
    start_offset: float
    # Offset of the end of the rule body from the beginning of the stylesheet. # noqa
    end_offset: float
    # Indicates whether the rule was actually used by some element in the page. # noqa
    used: bool


@dataclass
class SourceRange:
    """Text range within a resource.

    All numbers are zero-based.
    """

    # Start line of range. # noqa
    start_line: int
    # Start column of range (inclusive). # noqa
    start_column: int
    # End line of range # noqa
    end_line: int
    # End column of range (exclusive). # noqa
    end_column: int


@dataclass
class ShorthandEntry:
    """Description is missing from the devtools protocol document."""

    # Shorthand name. # noqa
    name: str
    # Shorthand value. # noqa
    value: str
    # Whether the property has "!important" annotation (implies `false` ifabsent). # noqa
    important: typing.Optional[bool]


@dataclass
class CSSComputedStyleProperty:
    """Description is missing from the devtools protocol document."""

    # Computed style property name. # noqa
    name: str
    # Computed style property value. # noqa
    value: str


@dataclass
class CSSStyle:
    """CSS style representation."""

    # CSS properties in the style. # noqa
    css_properties: CSSProperty
    # Computed values for all shorthands found in the style. # noqa
    shorthand_entries: ShorthandEntry
    # The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. # noqa
    style_sheet_id: typing.Optional[StyleSheetId]
    # Style declaration text (if available). # noqa
    css_text: typing.Optional[str]
    # Style declaration range in the enclosing stylesheet (if available). # noqa
    range: typing.Optional[SourceRange]


@dataclass
class CSSProperty:
    """CSS property declaration data."""

    # The property name. # noqa
    name: str
    # The property value. # noqa
    value: str
    # Whether the property has "!important" annotation (implies `false` ifabsent). # noqa
    important: typing.Optional[bool]
    # Whether the property is implicit (implies `false` if absent). # noqa
    implicit: typing.Optional[bool]
    # The full property text as specified in the style. # noqa
    text: typing.Optional[str]
    # Whether the property is understood by the browser (implies `true` ifabsent). # noqa
    parsed_ok: typing.Optional[bool]
    # Whether the property is disabled by the user (present for source-basedproperties only). # noqa
    disabled: typing.Optional[bool]
    # The entire property range in the enclosing style declaration (ifavailable). # noqa
    range: typing.Optional[SourceRange]
    # Parsed longhand components of this property if it is a shorthand. Thisfield will be empty if the given property is not a shorthand. # noqa
    longhand_properties: typing.Optional[CSSProperty]


@dataclass
class CSSMedia:
    """CSS media rule descriptor."""

    # Media query text. # noqa
    text: str
    # Source of the media query: "mediaRule" if specified by a @media rule,"importRule" if specified by an @import rule, "linkedSheet" if specified by a"media" attribute in a linked stylesheet's LINK tag, "inlineSheet" if specifiedby a "media" attribute in an inline stylesheet's STYLE tag. # noqa
    source: typing.List[typing.Literal["mediaRule", "importRule", "linkedSheet", "inlineSheet"]]
    # URL of the document containing the media query description. # noqa
    source_url: typing.Optional[str]
    # The associated rule (@media or @import) header range in the enclosingstylesheet (if available). # noqa
    range: typing.Optional[SourceRange]
    # Identifier of the stylesheet containing this object (if exists). # noqa
    style_sheet_id: typing.Optional[StyleSheetId]
    # Array of media queries. # noqa
    media_list: typing.Optional[MediaQuery]


@dataclass
class MediaQuery:
    """Media query descriptor."""

    # Array of media query expressions. # noqa
    expressions: MediaQueryExpression
    # Whether the media query condition is satisfied. # noqa
    active: bool


@dataclass
class MediaQueryExpression:
    """Media query expression descriptor."""

    # Media query expression value. # noqa
    value: float
    # Media query expression units. # noqa
    unit: str
    # Media query expression feature. # noqa
    feature: str
    # The associated range of the value text in the enclosing stylesheet (ifavailable). # noqa
    value_range: typing.Optional[SourceRange]
    # Computed length of media query expression (if applicable). # noqa
    computed_length: typing.Optional[float]


@dataclass
class CSSContainerQuery:
    """CSS container query rule descriptor."""

    # Container query text. # noqa
    text: str
    # The associated rule header range in the enclosing stylesheet (ifavailable). # noqa
    range: typing.Optional[SourceRange]
    # Identifier of the stylesheet containing this object (if exists). # noqa
    style_sheet_id: typing.Optional[StyleSheetId]
    # Optional name for the container. # noqa
    name: typing.Optional[str]
    # Optional physical axes queried for the container. # noqa
    physical_axes: typing.Optional[dom.PhysicalAxes]
    # Optional logical axes queried for the container. # noqa
    logical_axes: typing.Optional[dom.LogicalAxes]


@dataclass
class CSSSupports:
    """CSS Supports at-rule descriptor."""

    # Supports rule text. # noqa
    text: str
    # Whether the supports condition is satisfied. # noqa
    active: bool
    # The associated rule header range in the enclosing stylesheet (ifavailable). # noqa
    range: typing.Optional[SourceRange]
    # Identifier of the stylesheet containing this object (if exists). # noqa
    style_sheet_id: typing.Optional[StyleSheetId]


@dataclass
class CSSScope:
    """CSS Scope at-rule descriptor."""

    # Scope rule text. # noqa
    text: str
    # The associated rule header range in the enclosing stylesheet (ifavailable). # noqa
    range: typing.Optional[SourceRange]
    # Identifier of the stylesheet containing this object (if exists). # noqa
    style_sheet_id: typing.Optional[StyleSheetId]


@dataclass
class CSSLayer:
    """CSS Layer at-rule descriptor."""

    # Layer name. # noqa
    text: str
    # The associated rule header range in the enclosing stylesheet (ifavailable). # noqa
    range: typing.Optional[SourceRange]
    # Identifier of the stylesheet containing this object (if exists). # noqa
    style_sheet_id: typing.Optional[StyleSheetId]


@dataclass
class CSSLayerData:
    """CSS Layer data."""

    # Layer name. # noqa
    name: str
    # Layer order. The order determines the order of the layer in the cascadeorder. A higher number has higher priority in the cascade order. # noqa
    order: float
    # Direct sub-layers # noqa
    sub_layers: typing.Optional[CSSLayerData]


@dataclass
class PlatformFontUsage:
    """Information about amount of glyphs that were rendered with given font."""

    # Font's family name reported by platform. # noqa
    family_name: str
    # Indicates if the font was downloaded or resolved locally. # noqa
    is_custom_font: bool
    # Amount of glyphs that were rendered with this font. # noqa
    glyph_count: float


@dataclass
class FontVariationAxis:
    """Information about font variation axes for variable fonts."""

    # The font-variation-setting tag (a.k.a. "axis tag"). # noqa
    tag: str
    # Human-readable variation name in the default language (normally, "en"). # noqa
    name: str
    # The minimum value (inclusive) the font supports for this tag. # noqa
    min_value: float
    # The maximum value (inclusive) the font supports for this tag. # noqa
    max_value: float
    # The default value. # noqa
    default_value: float


@dataclass
class FontFace:
    """Properties of a web font: https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions
    and additional information such as platformFontFamily and fontVariationAxes."""

    # The font-family. # noqa
    font_family: str
    # The font-style. # noqa
    font_style: str
    # The font-variant. # noqa
    font_variant: str
    # The font-weight. # noqa
    font_weight: str
    # The font-stretch. # noqa
    font_stretch: str
    # The font-display. # noqa
    font_display: str
    # The unicode-range. # noqa
    unicode_range: str
    # The src. # noqa
    src: str
    # The resolved platform font family # noqa
    platform_font_family: str
    # Available variation settings (a.k.a. "axes"). # noqa
    font_variation_axes: typing.Optional[FontVariationAxis]


@dataclass
class CSSTryRule:
    """CSS try rule representation."""

    # Parent stylesheet's origin. # noqa
    origin: StyleSheetOrigin
    # Associated style declaration. # noqa
    style: CSSStyle
    # The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. # noqa
    style_sheet_id: typing.Optional[StyleSheetId]


@dataclass
class CSSPositionFallbackRule:
    """CSS position-fallback rule representation."""

    # Description is missing from the devtools protocol document. # noqa
    name: Value
    # List of keyframes. # noqa
    try_rules: CSSTryRule


@dataclass
class CSSKeyframesRule:
    """CSS keyframes rule representation."""

    # Animation name. # noqa
    animation_name: Value
    # List of keyframes. # noqa
    keyframes: CSSKeyframeRule


@dataclass
class CSSKeyframeRule:
    """CSS keyframe rule representation."""

    # Parent stylesheet's origin. # noqa
    origin: StyleSheetOrigin
    # Associated key text. # noqa
    key_text: Value
    # Associated style declaration. # noqa
    style: CSSStyle
    # The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. # noqa
    style_sheet_id: typing.Optional[StyleSheetId]


@dataclass
class StyleDeclarationEdit:
    """A descriptor of operation to mutate style declaration text."""

    # The css style sheet identifier. # noqa
    style_sheet_id: StyleSheetId
    # The range of the style text in the enclosing stylesheet. # noqa
    range: SourceRange
    # New style text. # noqa
    text: str


@dataclass
@memoize_event("CSS.fontsUpdated")
class FontsUpdated:
    """Fires whenever a web font is updated.

    A non-empty font parameter indicates a successfully loaded web font.
    """

    font: typing.Optional[FontFace]


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
    """Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the
    position specified by `location`. # noqa"""
    ...


async def collect_class_names() -> None:
    """Returns all class names from specified stylesheet.

    # noqa
    """
    ...


async def create_style_sheet() -> None:
    """Creates a new special "via-inspector" stylesheet in the frame with given `frameId`. # noqa"""
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
    """Returns the computed style for a DOM node identified by `nodeId`. # noqa"""
    ...


async def get_inline_styles_for_node() -> None:
    """Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
    attributes) for a DOM node identified by `nodeId`. # noqa"""
    ...


async def get_matched_styles_for_node() -> None:
    """Returns requested styles for a DOM node identified by `nodeId`. # noqa"""
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
    """Stop tracking rule usage and return the list of rules that were used since last call to
    `takeCoverageDelta` (or since start of coverage instrumentation). # noqa"""
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
