# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Page`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Page/

from __future__ import annotations

from dataclasses import dataclass


class FrameId(str):
    """Unique frame identifier."""

    def to_json(self) -> str:
        return self


class AdFrameType(str):
    """Indicates whether a frame has been identified as an ad."""

    def to_json(self) -> str:
        return self


class AdFrameExplanation(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


@dataclass
class AdFrameStatus:
    """Indicates whether a frame has been identified as an ad and why."""


@dataclass
class AdScriptId:
    """Identifies the bottom-most script which caused the frame to be labelled
    as an ad."""


class SecureContextType(str):
    """Indicates whether the frame is a secure context and why it is the
    case."""

    def to_json(self) -> str:
        return self


class CrossOriginIsolatedContextType(str):
    """Indicates whether the frame is cross-origin isolated and why it is the
    case."""

    def to_json(self) -> str:
        return self


class GatedAPIFeatures(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


class PermissionsPolicyFeature(str):
    """All Permissions Policy features.

    This enum should match the one defined
    in third_party/blink/renderer/core/permissions_policy/permissions_policy_features.json5.
    """

    def to_json(self) -> str:
        return self


class PermissionsPolicyBlockReason(str):
    """Reason for a permissions policy feature to be disabled."""

    def to_json(self) -> str:
        return self


@dataclass
class PermissionsPolicyBlockLocator:
    """Description is missing from the devtools protocol document."""


@dataclass
class PermissionsPolicyFeatureState:
    """Description is missing from the devtools protocol document."""


class OriginTrialTokenStatus(str):
    """Origin Trial(https://www.chromium.org/blink/origin-trials) support.

    Status for an Origin Trial token.
    """

    def to_json(self) -> str:
        return self


class OriginTrialStatus(str):
    """Status for an Origin Trial."""

    def to_json(self) -> str:
        return self


class OriginTrialUsageRestriction(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


@dataclass
class OriginTrialToken:
    """Description is missing from the devtools protocol document."""


@dataclass
class OriginTrialTokenWithStatus:
    """Description is missing from the devtools protocol document."""


@dataclass
class OriginTrial:
    """Description is missing from the devtools protocol document."""


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


class ScriptIdentifier(str):
    """Unique script identifier."""

    def to_json(self) -> str:
        return self


class TransitionType(str):
    """Transition type."""

    def to_json(self) -> str:
        return self


@dataclass
class NavigationEntry:
    """Navigation history entry."""


@dataclass
class ScreencastFrameMetadata:
    """Screencast frame metadata."""


class DialogType(str):
    """Javascript dialog type."""

    def to_json(self) -> str:
        return self


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


class ClientNavigationReason(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


class ClientNavigationDisposition(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self


@dataclass
class InstallabilityErrorArgument:
    """Description is missing from the devtools protocol document."""


@dataclass
class InstallabilityError:
    """The installability error."""


class ReferrerPolicy(str):
    """The referring-policy used for the navigation."""

    def to_json(self) -> str:
        return self


@dataclass
class CompilationCacheParams:
    """Per-script compilation cache parameters for
    `Page.produceCompilationCache`"""


class AutoResponseMode(str):
    """Enum of possible auto-reponse for permisison / prompt dialogs."""

    def to_json(self) -> str:
        return self


class NavigationType(str):
    """The type of a frameNavigated event."""

    def to_json(self) -> str:
        return self


class BackForwardCacheNotRestoredReason(str):
    """List of not restored reasons for back-forward cache."""

    def to_json(self) -> str:
        return self


class BackForwardCacheNotRestoredReasonType(str):
    """Types of not restored reasons for back-forward cache."""

    def to_json(self) -> str:
        return self


@dataclass
class BackForwardCacheNotRestoredExplanation:
    """Description is missing from the devtools protocol document."""


@dataclass
class BackForwardCacheNotRestoredExplanationTree:
    """Description is missing from the devtools protocol document."""
