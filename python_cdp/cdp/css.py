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


class StyleSheetId(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> StyleSheetId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class StyleSheetOrigin(str, enum.Enum):
    """Stylesheet type: "injected" for stylesheets injected via extension,
    "user-agent" for user-agent stylesheets, "inspector" for stylesheets
    created by the inspector (i.e. those holding the "via inspector" rules),
    "regular" for regular stylesheets."""

    INJECTED = "injected"
    USER_AGENT = "user_agent"
    INSPECTOR = "inspector"
    REGULAR = "regular"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class PseudoElementMatches:
    """CSS rule collection for a single pseudo style."""

    #: Pseudo element type.# noqa
    pseudoType: dom.PseudoType
    #: Matches of CSS rules applicable to the pseudo style.# noqa
    matches: RuleMatch
    #: Pseudo element custom ident.# noqa
    pseudoIdentifier: typing.Optional[str] = None


@dataclass
class InheritedStyleEntry:
    """Inherited CSS rule collection from ancestor node."""

    #: Matches of CSS rules matching the ancestor node in the style inheritancechain.# noqa
    matchedCSSRules: RuleMatch
    #: The ancestor node's inline style, if any, in the style inheritance chain.# noqa
    inlineStyle: typing.Optional[CSSStyle] = None


@dataclass
class InheritedPseudoElementMatches:
    """Inherited pseudo element matches from pseudos of an ancestor node."""

    #: Matches of pseudo styles from the pseudos of an ancestor node.# noqa
    pseudoElements: PseudoElementMatches


@dataclass
class RuleMatch:
    """Match data for a CSS rule."""

    #: CSS rule in the match.# noqa
    rule: CSSRule
    #: Matching selector indices in the rule's selectorList selectors (0-based).# noqa
    matchingSelectors: int


@dataclass
class Value:
    """Data for a simple selector (these are delimited by commas in a selector
    list)."""

    #: Value text.# noqa
    text: str
    #: Value range in the underlying resource (if available).# noqa
    range: typing.Optional[SourceRange] = None


@dataclass
class SelectorList:
    """Selector list data."""

    #: Selectors in the list.# noqa
    selectors: Value
    #: Rule selector text.# noqa
    text: str


@dataclass
class CSSStyleSheetHeader:
    """CSS stylesheet metainformation."""

    #: The stylesheet identifier.# noqa
    styleSheetId: StyleSheetId
    #: Owner frame identifier.# noqa
    frameId: page.FrameId
    #: Stylesheet resource URL. Empty if this is a constructed stylesheetcreated using new CSSStyleSheet() (but non-empty if this is a constructedsylesheet imported as a CSS module script).# noqa
    sourceURL: str
    #: Stylesheet origin.# noqa
    origin: StyleSheetOrigin
    #: Stylesheet title.# noqa
    title: str
    #: Denotes whether the stylesheet is disabled.# noqa
    disabled: bool
    #: Whether this stylesheet is created for STYLE tag by parser. This flag isnot set for document.written STYLE tags.# noqa
    isInline: bool
    #: Whether this stylesheet is mutable. Inline stylesheets become mutableafter they have been modified via CSSOM API. <link> element's stylesheets becomemutable only if DevTools modifies them. Constructed stylesheets (newCSSStyleSheet()) are mutable immediately after creation.# noqa
    isMutable: bool
    #: True if this stylesheet is created through new CSSStyleSheet() orimported as a CSS module script.# noqa
    isConstructed: bool
    #: Line offset of the stylesheet within the resource (zero based).# noqa
    startLine: float
    #: Column offset of the stylesheet within the resource (zero based).# noqa
    startColumn: float
    #: Size of the content (in characters).# noqa
    length: float
    #: Line offset of the end of the stylesheet within the resource (zerobased).# noqa
    endLine: float
    #: Column offset of the end of the stylesheet within the resource (zerobased).# noqa
    endColumn: float
    #: URL of source map associated with the stylesheet (if any).# noqa
    sourceMapURL: typing.Optional[str] = None
    #: The backend id for the owner node of the stylesheet.# noqa
    ownerNode: typing.Optional[dom.BackendNodeId] = None
    #: Whether the sourceURL field value comes from the sourceURL comment.# noqa
    hasSourceURL: typing.Optional[bool] = None


@dataclass
class CSSRule:
    """CSS rule representation."""

    #: Rule selector data.# noqa
    selectorList: SelectorList
    #: Parent stylesheet's origin.# noqa
    origin: StyleSheetOrigin
    #: Associated style declaration.# noqa
    style: CSSStyle
    #: The css style sheet identifier (absent for user agent stylesheet anduser-specified stylesheet rules) this rule came from.# noqa
    styleSheetId: typing.Optional[StyleSheetId] = None
    #: Media list array (for rules involving media queries). The arrayenumerates media queries starting with the innermost one, going outwards.# noqa
    media: typing.Optional[CSSMedia] = None
    #: Container query list array (for rules involving container queries). Thearray enumerates container queries starting with the innermost one, goingoutwards.# noqa
    containerQueries: typing.Optional[CSSContainerQuery] = None
    #: @supports CSS at-rule array. The array enumerates @supports at-rulesstarting with the innermost one, going outwards.# noqa
    supports: typing.Optional[CSSSupports] = None
    #: Cascade layer array. Contains the layer hierarchy that this rule belongsto starting with the innermost layer and going outwards.# noqa
    layers: typing.Optional[CSSLayer] = None
    #: @scope CSS at-rule array. The array enumerates @scope at-rules startingwith the innermost one, going outwards.# noqa
    scopes: typing.Optional[CSSScope] = None


@dataclass
class RuleUsage:
    """CSS coverage information."""

    #: The css style sheet identifier (absent for user agent stylesheet anduser-specified stylesheet rules) this rule came from.# noqa
    styleSheetId: StyleSheetId
    #: Offset of the start of the rule (including selector) from the beginningof the stylesheet.# noqa
    startOffset: float
    #: Offset of the end of the rule body from the beginning of the stylesheet.# noqa
    endOffset: float
    #: Indicates whether the rule was actually used by some element in the page.# noqa
    used: bool


@dataclass
class SourceRange:
    """Text range within a resource.

    All numbers are zero-based.
    """

    #: Start line of range.# noqa
    startLine: int
    #: Start column of range (inclusive).# noqa
    startColumn: int
    #: End line of range# noqa
    endLine: int
    #: End column of range (exclusive).# noqa
    endColumn: int


@dataclass
class ShorthandEntry:
    """Description is missing from the devtools protocol document."""

    #: Shorthand name.# noqa
    name: str
    #: Shorthand value.# noqa
    value: str
    #: Whether the property has "!important" annotation (implies `false` ifabsent).# noqa
    important: typing.Optional[bool] = None


@dataclass
class CSSComputedStyleProperty:
    """Description is missing from the devtools protocol document."""

    #: Computed style property name.# noqa
    name: str
    #: Computed style property value.# noqa
    value: str


@dataclass
class CSSStyle:
    """CSS style representation."""

    #: CSS properties in the style.# noqa
    cssProperties: CSSProperty
    #: Computed values for all shorthands found in the style.# noqa
    shorthandEntries: ShorthandEntry
    #: The css style sheet identifier (absent for user agent stylesheet anduser-specified stylesheet rules) this rule came from.# noqa
    styleSheetId: typing.Optional[StyleSheetId] = None
    #: Style declaration text (if available).# noqa
    cssText: typing.Optional[str] = None
    #: Style declaration range in the enclosing stylesheet (if available).# noqa
    range: typing.Optional[SourceRange] = None


@dataclass
class CSSProperty:
    """CSS property declaration data."""

    #: The property name.# noqa
    name: str
    #: The property value.# noqa
    value: str
    #: Whether the property has "!important" annotation (implies `false` ifabsent).# noqa
    important: typing.Optional[bool] = None
    #: Whether the property is implicit (implies `false` if absent).# noqa
    implicit: typing.Optional[bool] = None
    #: The full property text as specified in the style.# noqa
    text: typing.Optional[str] = None
    #: Whether the property is understood by the browser (implies `true` ifabsent).# noqa
    parsedOk: typing.Optional[bool] = None
    #: Whether the property is disabled by the user (present for source-basedproperties only).# noqa
    disabled: typing.Optional[bool] = None
    #: The entire property range in the enclosing style declaration (ifavailable).# noqa
    range: typing.Optional[SourceRange] = None
    #: Parsed longhand components of this property if it is a shorthand. Thisfield will be empty if the given property is not a shorthand.# noqa
    longhandProperties: typing.Optional[CSSProperty] = None


@dataclass
class CSSMedia:
    """CSS media rule descriptor."""

    #: Media query text.# noqa
    text: str
    #: Source of the media query: "mediaRule" if specified by a @media rule,"importRule" if specified by an @import rule, "linkedSheet" if specified by a"media" attribute in a linked stylesheet's LINK tag, "inlineSheet" if specifiedby a "media" attribute in an inline stylesheet's STYLE tag.# noqa
    source: str
    #: URL of the document containing the media query description.# noqa
    sourceURL: typing.Optional[str] = None
    #: The associated rule (@media or @import) header range in the enclosingstylesheet (if available).# noqa
    range: typing.Optional[SourceRange] = None
    #: Identifier of the stylesheet containing this object (if exists).# noqa
    styleSheetId: typing.Optional[StyleSheetId] = None
    #: Array of media queries.# noqa
    mediaList: typing.Optional[MediaQuery] = None


@dataclass
class MediaQuery:
    """Media query descriptor."""

    #: Array of media query expressions.# noqa
    expressions: MediaQueryExpression
    #: Whether the media query condition is satisfied.# noqa
    active: bool


@dataclass
class MediaQueryExpression:
    """Media query expression descriptor."""

    #: Media query expression value.# noqa
    value: float
    #: Media query expression units.# noqa
    unit: str
    #: Media query expression feature.# noqa
    feature: str
    #: The associated range of the value text in the enclosing stylesheet (ifavailable).# noqa
    valueRange: typing.Optional[SourceRange] = None
    #: Computed length of media query expression (if applicable).# noqa
    computedLength: typing.Optional[float] = None


@dataclass
class CSSContainerQuery:
    """CSS container query rule descriptor."""

    #: Container query text.# noqa
    text: str
    #: The associated rule header range in the enclosing stylesheet (ifavailable).# noqa
    range: typing.Optional[SourceRange] = None
    #: Identifier of the stylesheet containing this object (if exists).# noqa
    styleSheetId: typing.Optional[StyleSheetId] = None
    #: Optional name for the container.# noqa
    name: typing.Optional[str] = None
    #: Optional physical axes queried for the container.# noqa
    physicalAxes: typing.Optional[dom.PhysicalAxes] = None
    #: Optional logical axes queried for the container.# noqa
    logicalAxes: typing.Optional[dom.LogicalAxes] = None


@dataclass
class CSSSupports:
    """CSS Supports at-rule descriptor."""

    #: Supports rule text.# noqa
    text: str
    #: Whether the supports condition is satisfied.# noqa
    active: bool
    #: The associated rule header range in the enclosing stylesheet (ifavailable).# noqa
    range: typing.Optional[SourceRange] = None
    #: Identifier of the stylesheet containing this object (if exists).# noqa
    styleSheetId: typing.Optional[StyleSheetId] = None


@dataclass
class CSSScope:
    """CSS Scope at-rule descriptor."""

    #: Scope rule text.# noqa
    text: str
    #: The associated rule header range in the enclosing stylesheet (ifavailable).# noqa
    range: typing.Optional[SourceRange] = None
    #: Identifier of the stylesheet containing this object (if exists).# noqa
    styleSheetId: typing.Optional[StyleSheetId] = None


@dataclass
class CSSLayer:
    """CSS Layer at-rule descriptor."""

    #: Layer name.# noqa
    text: str
    #: The associated rule header range in the enclosing stylesheet (ifavailable).# noqa
    range: typing.Optional[SourceRange] = None
    #: Identifier of the stylesheet containing this object (if exists).# noqa
    styleSheetId: typing.Optional[StyleSheetId] = None


@dataclass
class CSSLayerData:
    """CSS Layer data."""

    #: Layer name.# noqa
    name: str
    #: Layer order. The order determines the order of the layer in the cascadeorder. A higher number has higher priority in the cascade order.# noqa
    order: float
    #: Direct sub-layers# noqa
    subLayers: typing.Optional[CSSLayerData] = None


@dataclass
class PlatformFontUsage:
    """Information about amount of glyphs that were rendered with given
    font."""

    #: Font's family name reported by platform.# noqa
    familyName: str
    #: Indicates if the font was downloaded or resolved locally.# noqa
    isCustomFont: bool
    #: Amount of glyphs that were rendered with this font.# noqa
    glyphCount: float


@dataclass
class FontVariationAxis:
    """Information about font variation axes for variable fonts."""

    #: The font-variation-setting tag (a.k.a. "axis tag").# noqa
    tag: str
    #: Human-readable variation name in the default language (normally, "en").# noqa
    name: str
    #: The minimum value (inclusive) the font supports for this tag.# noqa
    minValue: float
    #: The maximum value (inclusive) the font supports for this tag.# noqa
    maxValue: float
    #: The default value.# noqa
    defaultValue: float


@dataclass
class FontFace:
    """Properties of a web font: https://www.w3.org/TR/2008/REC-
    CSS2-20080411/fonts.html#font-descriptions and additional information such
    as platformFontFamily and fontVariationAxes."""

    #: The font-family.# noqa
    fontFamily: str
    #: The font-style.# noqa
    fontStyle: str
    #: The font-variant.# noqa
    fontVariant: str
    #: The font-weight.# noqa
    fontWeight: str
    #: The font-stretch.# noqa
    fontStretch: str
    #: The font-display.# noqa
    fontDisplay: str
    #: The unicode-range.# noqa
    unicodeRange: str
    #: The src.# noqa
    src: str
    #: The resolved platform font family# noqa
    platformFontFamily: str
    #: Available variation settings (a.k.a. "axes").# noqa
    fontVariationAxes: typing.Optional[FontVariationAxis] = None


@dataclass
class CSSKeyframesRule:
    """CSS keyframes rule representation."""

    #: Animation name.# noqa
    animationName: Value
    #: List of keyframes.# noqa
    keyframes: CSSKeyframeRule


@dataclass
class CSSKeyframeRule:
    """CSS keyframe rule representation."""

    #: Parent stylesheet's origin.# noqa
    origin: StyleSheetOrigin
    #: Associated key text.# noqa
    keyText: Value
    #: Associated style declaration.# noqa
    style: CSSStyle
    #: The css style sheet identifier (absent for user agent stylesheet anduser-specified stylesheet rules) this rule came from.# noqa
    styleSheetId: typing.Optional[StyleSheetId] = None


@dataclass
class StyleDeclarationEdit:
    """A descriptor of operation to mutate style declaration text."""

    #: The css style sheet identifier.# noqa
    styleSheetId: StyleSheetId
    #: The range of the style text in the enclosing stylesheet.# noqa
    range: SourceRange
    #: New style text.# noqa
    text: str
