""" *** AUTO GENERATED FILE ***
This file was automatically generated by python-cdp.  Do not modify this file
as it is overwritten when new versions of the devtools protocol are released.  Instead modify the
code generator in https://github.com/symonk/python-cdp (or your fork) instead.  For documentation
on how to modify the generation process refer to the CONTRIBUTING.md file in the root of the
repository."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class AdFrameStatus:
    """Indicates whether a frame has been identified as an ad and why."""


@dataclass
class AdScriptId:
    """Identifies the bottom-most script which caused the frame to be labelled
    as an ad."""


@dataclass
class PermissionsPolicyBlockLocator:
    """Missing description in devtools protocol."""


@dataclass
class PermissionsPolicyFeatureState:
    """Missing description in devtools protocol."""


@dataclass
class OriginTrialToken:
    """Missing description in devtools protocol."""


@dataclass
class OriginTrialTokenWithStatus:
    """Missing description in devtools protocol."""


@dataclass
class OriginTrial:
    """Missing description in devtools protocol."""


@dataclass
class Frame:
    """Information about the Frame on the page."""


@dataclass
class FrameResource:
    """Information about the Resource on the page."""


@dataclass
class FrameResourceTree:
    """Information about the Frame hierarchy along with their cached
    resources."""


@dataclass
class FrameTree:
    """Information about the Frame hierarchy."""


@dataclass
class NavigationEntry:
    """Navigation history entry."""


@dataclass
class ScreencastFrameMetadata:
    """Screencast frame metadata."""


@dataclass
class AppManifestError:
    """Error while paring app manifest."""


@dataclass
class AppManifestParsedProperties:
    """Parsed app manifest properties."""


@dataclass
class LayoutViewport:
    """Layout viewport position and dimensions."""


@dataclass
class VisualViewport:
    """Visual viewport position, dimensions, and scale."""


@dataclass
class Viewport:
    """Viewport for capturing screenshot."""


@dataclass
class FontFamilies:
    """Generic font families collection."""


@dataclass
class ScriptFontFamilies:
    """Font families collection for a script."""


@dataclass
class FontSizes:
    """Default font sizes."""


@dataclass
class InstallabilityErrorArgument:
    """Missing description in devtools protocol."""


@dataclass
class InstallabilityError:
    """The installability error."""


@dataclass
class CompilationCacheParams:
    """Per-script compilation cache parameters for
    `Page.produceCompilationCache`"""


@dataclass
class BackForwardCacheNotRestoredExplanation:
    """Missing description in devtools protocol."""


@dataclass
class BackForwardCacheNotRestoredExplanationTree:
    """Missing description in devtools protocol."""
