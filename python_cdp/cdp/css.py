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


class StyleSheetId(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class StyleSheetOrigin(str, enum.Enum):
    """Stylesheet type: "injected" for stylesheets injected via
    extension,"user-agent" for user-agent stylesheets, "inspector" for
    stylesheets created bythe inspector (i.e. those holding the "via inspector"
    rules), "regular" forregular stylesheets."""

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

    #: Pseudo element type.
    pseudoType: str
    #: Pseudo element custom ident.
    pseudoIdentifier: str
    #: Matches of CSS rules applicable to the pseudo style.
    matches: str


@dataclass
class InheritedStyleEntry:
    """Inherited CSS rule collection from ancestor node."""

    #: The ancestor node's inline style, if any, in the style inheritance chain.
    inlineStyle: str
    #: Matches of CSS rules matching the ancestor node in the style inheritancechain.
    matchedCSSRules: str


@dataclass
class InheritedPseudoElementMatches:
    """Inherited pseudo element matches from pseudos of an ancestor node."""

    #: Matches of pseudo styles from the pseudos of an ancestor node.
    pseudoElements: str


@dataclass
class RuleMatch:
    """Match data for a CSS rule."""

    #: CSS rule in the match.
    rule: str
    #: Matching selector indices in the rule's selectorList selectors (0-based).
    matchingSelectors: str


@dataclass
class Value:
    """Data for a simple selector (these are delimited by commas in a selector
    list)."""

    #: Value text.
    text: str
    #: Value range in the underlying resource (if available).
    range: str


@dataclass
class SelectorList:
    """Selector list data."""

    #: Selectors in the list.
    selectors: str
    #: Rule selector text.
    text: str


@dataclass
class CSSStyleSheetHeader:
    """CSS stylesheet metainformation."""

    #: The stylesheet identifier.
    styleSheetId: str
    #: Owner frame identifier.
    frameId: str
    #: Stylesheet resource URL. Empty if this is a constructed stylesheetcreated using new CSSStyleSheet() (but non-empty if this is a constructedsylesheet imported as a CSS module script).
    sourceURL: str
    #: URL of source map associated with the stylesheet (if any).
    sourceMapURL: str
    #: Stylesheet origin.
    origin: str
    #: Stylesheet title.
    title: str
    #: The backend id for the owner node of the stylesheet.
    ownerNode: str
    #: Denotes whether the stylesheet is disabled.
    disabled: str
    #: Whether the sourceURL field value comes from the sourceURL comment.
    hasSourceURL: str
    #: Whether this stylesheet is created for STYLE tag by parser. This flag isnot set for document.written STYLE tags.
    isInline: str
    #: Whether this stylesheet is mutable. Inline stylesheets become mutableafter they have been modified via CSSOM API. <link> element's stylesheets becomemutable only if DevTools modifies them. Constructed stylesheets (newCSSStyleSheet()) are mutable immediately after creation.
    isMutable: str
    #: True if this stylesheet is created through new CSSStyleSheet() orimported as a CSS module script.
    isConstructed: str
    #: Line offset of the stylesheet within the resource (zero based).
    startLine: str
    #: Column offset of the stylesheet within the resource (zero based).
    startColumn: str
    #: Size of the content (in characters).
    length: str
    #: Line offset of the end of the stylesheet within the resource (zerobased).
    endLine: str
    #: Column offset of the end of the stylesheet within the resource (zerobased).
    endColumn: str


@dataclass
class CSSRule:
    """CSS rule representation."""

    #: The css style sheet identifier (absent for user agent stylesheet anduser-specified stylesheet rules) this rule came from.
    styleSheetId: str
    #: Rule selector data.
    selectorList: str
    #: Parent stylesheet's origin.
    origin: str
    #: Associated style declaration.
    style: str
    #: Media list array (for rules involving media queries). The arrayenumerates media queries starting with the innermost one, going outwards.
    media: str
    #: Container query list array (for rules involving container queries). Thearray enumerates container queries starting with the innermost one, goingoutwards.
    containerQueries: str
    #: @supports CSS at-rule array. The array enumerates @supports at-rulesstarting with the innermost one, going outwards.
    supports: str
    #: Cascade layer array. Contains the layer hierarchy that this rule belongsto starting with the innermost layer and going outwards.
    layers: str
    #: @scope CSS at-rule array. The array enumerates @scope at-rules startingwith the innermost one, going outwards.
    scopes: str


@dataclass
class RuleUsage:
    """CSS coverage information."""

    #: The css style sheet identifier (absent for user agent stylesheet anduser-specified stylesheet rules) this rule came from.
    styleSheetId: str
    #: Offset of the start of the rule (including selector) from the beginningof the stylesheet.
    startOffset: str
    #: Offset of the end of the rule body from the beginning of the stylesheet.
    endOffset: str
    #: Indicates whether the rule was actually used by some element in the page.
    used: str


@dataclass
class SourceRange:
    """Text range within a resource.

    All numbers are zero-based.
    """

    #: Start line of range.
    startLine: str
    #: Start column of range (inclusive).
    startColumn: str
    #: End line of range
    endLine: str
    #: End column of range (exclusive).
    endColumn: str


@dataclass
class ShorthandEntry:
    """Description is missing from the devtools protocol document."""

    #: Shorthand name.
    name: str
    #: Shorthand value.
    value: str
    #: Whether the property has "!important" annotation (implies `false` ifabsent).
    important: str


@dataclass
class CSSComputedStyleProperty:
    """Description is missing from the devtools protocol document."""

    #: Computed style property name.
    name: str
    #: Computed style property value.
    value: str


@dataclass
class CSSStyle:
    """CSS style representation."""

    #: The css style sheet identifier (absent for user agent stylesheet anduser-specified stylesheet rules) this rule came from.
    styleSheetId: str
    #: CSS properties in the style.
    cssProperties: str
    #: Computed values for all shorthands found in the style.
    shorthandEntries: str
    #: Style declaration text (if available).
    cssText: str
    #: Style declaration range in the enclosing stylesheet (if available).
    range: str


@dataclass
class CSSProperty:
    """CSS property declaration data."""

    #: The property name.
    name: str
    #: The property value.
    value: str
    #: Whether the property has "!important" annotation (implies `false` ifabsent).
    important: str
    #: Whether the property is implicit (implies `false` if absent).
    implicit: str
    #: The full property text as specified in the style.
    text: str
    #: Whether the property is understood by the browser (implies `true` ifabsent).
    parsedOk: str
    #: Whether the property is disabled by the user (present for source-basedproperties only).
    disabled: str
    #: The entire property range in the enclosing style declaration (ifavailable).
    range: str
    #: Parsed longhand components of this property if it is a shorthand. Thisfield will be empty if the given property is not a shorthand.
    longhandProperties: str


@dataclass
class CSSMedia:
    """CSS media rule descriptor."""

    #: Media query text.
    text: str
    #: Source of the media query: "mediaRule" if specified by a @media rule,"importRule" if specified by an @import rule, "linkedSheet" if specified by a"media" attribute in a linked stylesheet's LINK tag, "inlineSheet" if specifiedby a "media" attribute in an inline stylesheet's STYLE tag.
    source: str
    #: URL of the document containing the media query description.
    sourceURL: str
    #: The associated rule (@media or @import) header range in the enclosingstylesheet (if available).
    range: str
    #: Identifier of the stylesheet containing this object (if exists).
    styleSheetId: str
    #: Array of media queries.
    mediaList: str


@dataclass
class MediaQuery:
    """Media query descriptor."""

    #: Array of media query expressions.
    expressions: str
    #: Whether the media query condition is satisfied.
    active: str


@dataclass
class MediaQueryExpression:
    """Media query expression descriptor."""

    #: Media query expression value.
    value: str
    #: Media query expression units.
    unit: str
    #: Media query expression feature.
    feature: str
    #: The associated range of the value text in the enclosing stylesheet (ifavailable).
    valueRange: str
    #: Computed length of media query expression (if applicable).
    computedLength: str


@dataclass
class CSSContainerQuery:
    """CSS container query rule descriptor."""

    #: Container query text.
    text: str
    #: The associated rule header range in the enclosing stylesheet (ifavailable).
    range: str
    #: Identifier of the stylesheet containing this object (if exists).
    styleSheetId: str
    #: Optional name for the container.
    name: str
    #: Optional physical axes queried for the container.
    physicalAxes: str
    #: Optional logical axes queried for the container.
    logicalAxes: str


@dataclass
class CSSSupports:
    """CSS Supports at-rule descriptor."""

    #: Supports rule text.
    text: str
    #: Whether the supports condition is satisfied.
    active: str
    #: The associated rule header range in the enclosing stylesheet (ifavailable).
    range: str
    #: Identifier of the stylesheet containing this object (if exists).
    styleSheetId: str


@dataclass
class CSSScope:
    """CSS Scope at-rule descriptor."""

    #: Scope rule text.
    text: str
    #: The associated rule header range in the enclosing stylesheet (ifavailable).
    range: str
    #: Identifier of the stylesheet containing this object (if exists).
    styleSheetId: str


@dataclass
class CSSLayer:
    """CSS Layer at-rule descriptor."""

    #: Layer name.
    text: str
    #: The associated rule header range in the enclosing stylesheet (ifavailable).
    range: str
    #: Identifier of the stylesheet containing this object (if exists).
    styleSheetId: str


@dataclass
class CSSLayerData:
    """CSS Layer data."""

    #: Layer name.
    name: str
    #: Direct sub-layers
    subLayers: str
    #: Layer order. The order determines the order of the layer in the cascadeorder. A higher number has higher priority in the cascade order.
    order: str


@dataclass
class PlatformFontUsage:
    """Information about amount of glyphs that were rendered with given
    font."""

    #: Font's family name reported by platform.
    familyName: str
    #: Indicates if the font was downloaded or resolved locally.
    isCustomFont: str
    #: Amount of glyphs that were rendered with this font.
    glyphCount: str


@dataclass
class FontVariationAxis:
    """Information about font variation axes for variable fonts."""

    #: The font-variation-setting tag (a.k.a. "axis tag").
    tag: str
    #: Human-readable variation name in the default language (normally, "en").
    name: str
    #: The minimum value (inclusive) the font supports for this tag.
    minValue: str
    #: The maximum value (inclusive) the font supports for this tag.
    maxValue: str
    #: The default value.
    defaultValue: str


@dataclass
class FontFace:
    """Properties of a web font: https://www.w3.org/TR/2008/REC-
    CSS2-20080411/fonts.html#font-descriptions and additional information such
    as platformFontFamily and fontVariationAxes."""

    #: The font-family.
    fontFamily: str
    #: The font-style.
    fontStyle: str
    #: The font-variant.
    fontVariant: str
    #: The font-weight.
    fontWeight: str
    #: The font-stretch.
    fontStretch: str
    #: The font-display.
    fontDisplay: str
    #: The unicode-range.
    unicodeRange: str
    #: The src.
    src: str
    #: The resolved platform font family
    platformFontFamily: str
    #: Available variation settings (a.k.a. "axes").
    fontVariationAxes: str


@dataclass
class CSSKeyframesRule:
    """CSS keyframes rule representation."""

    #: Animation name.
    animationName: str
    #: List of keyframes.
    keyframes: str


@dataclass
class CSSKeyframeRule:
    """CSS keyframe rule representation."""

    #: The css style sheet identifier (absent for user agent stylesheet anduser-specified stylesheet rules) this rule came from.
    styleSheetId: str
    #: Parent stylesheet's origin.
    origin: str
    #: Associated key text.
    keyText: str
    #: Associated style declaration.
    style: str


@dataclass
class StyleDeclarationEdit:
    """A descriptor of operation to mutate style declaration text."""

    #: The css style sheet identifier.
    styleSheetId: str
    #: The range of the style text in the enclosing stylesheet.
    range: str
    #: New style text.
    text: str
