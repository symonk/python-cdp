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


@dataclass
class InheritedStyleEntry:
    """Inherited CSS rule collection from ancestor node."""


@dataclass
class InheritedPseudoElementMatches:
    """Inherited pseudo element matches from pseudos of an ancestor node."""


@dataclass
class RuleMatch:
    """Match data for a CSS rule."""


@dataclass
class Value:
    """Data for a simple selector (these are delimited by commas in a selector
    list)."""


@dataclass
class SelectorList:
    """Selector list data."""


@dataclass
class CSSStyleSheetHeader:
    """CSS stylesheet metainformation."""


@dataclass
class CSSRule:
    """CSS rule representation."""


@dataclass
class RuleUsage:
    """CSS coverage information."""


@dataclass
class SourceRange:
    """Text range within a resource.

    All numbers are zero-based.
    """


@dataclass
class ShorthandEntry:
    """Description is missing from the devtools protocol document."""


@dataclass
class CSSComputedStyleProperty:
    """Description is missing from the devtools protocol document."""


@dataclass
class CSSStyle:
    """CSS style representation."""


@dataclass
class CSSProperty:
    """CSS property declaration data."""


@dataclass
class CSSMedia:
    """CSS media rule descriptor."""


@dataclass
class MediaQuery:
    """Media query descriptor."""


@dataclass
class MediaQueryExpression:
    """Media query expression descriptor."""


@dataclass
class CSSContainerQuery:
    """CSS container query rule descriptor."""


@dataclass
class CSSSupports:
    """CSS Supports at-rule descriptor."""


@dataclass
class CSSScope:
    """CSS Scope at-rule descriptor."""


@dataclass
class CSSLayer:
    """CSS Layer at-rule descriptor."""


@dataclass
class CSSLayerData:
    """CSS Layer data."""


@dataclass
class PlatformFontUsage:
    """Information about amount of glyphs that were rendered with given
    font."""


@dataclass
class FontVariationAxis:
    """Information about font variation axes for variable fonts."""


@dataclass
class FontFace:
    """Properties of a web font: https://www.w3.org/TR/2008/REC-
    CSS2-20080411/fonts.html#font-descriptions and additional information such
    as platformFontFamily and fontVariationAxes."""


@dataclass
class CSSKeyframesRule:
    """CSS keyframes rule representation."""


@dataclass
class CSSKeyframeRule:
    """CSS keyframe rule representation."""


@dataclass
class StyleDeclarationEdit:
    """A descriptor of operation to mutate style declaration text."""
