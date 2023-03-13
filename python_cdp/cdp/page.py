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


@dataclass
class FrameId:
    """Unique frame identifier."""

    ...


@dataclass
class AdFrameType:
    """Indicates whether a frame has been identified as an ad."""

    ...


@dataclass
class AdFrameExplanation:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class AdFrameStatus:
    """Indicates whether a frame has been identified as an ad and why."""

    ...


@dataclass
class AdScriptId:
    """Identifies the bottom-most script which caused the frame to be labelled
    as an ad."""

    ...


@dataclass
class SecureContextType:
    """Indicates whether the frame is a secure context and why it is the
    case."""

    ...


@dataclass
class CrossOriginIsolatedContextType:
    """Indicates whether the frame is cross-origin isolated and why it is the
    case."""

    ...


@dataclass
class GatedAPIFeatures:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class PermissionsPolicyFeature:
    """All Permissions Policy features.

    This enum should match the one defined
    in third_party/blink/renderer/core/permissions_policy/permissions_policy_features.json5.
    """

    ...


@dataclass
class PermissionsPolicyBlockReason:
    """Reason for a permissions policy feature to be disabled."""

    ...


@dataclass
class PermissionsPolicyBlockLocator:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class PermissionsPolicyFeatureState:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class OriginTrialTokenStatus:
    """Origin Trial(https://www.chromium.org/blink/origin-trials) support.

    Status for an Origin Trial token.
    """

    ...


@dataclass
class OriginTrialStatus:
    """Status for an Origin Trial."""

    ...


@dataclass
class OriginTrialUsageRestriction:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class OriginTrialToken:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class OriginTrialTokenWithStatus:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class OriginTrial:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class Frame:
    """Information about the Frame on the page."""

    ...


@dataclass
class FrameResource:
    """Information about the Resource on the page."""

    ...


@dataclass
class FrameResourceTree:
    """Information about the Frame hierarchy along with their cached
    resources."""

    ...


@dataclass
class FrameTree:
    """Information about the Frame hierarchy."""

    ...


@dataclass
class ScriptIdentifier:
    """Unique script identifier."""

    ...


@dataclass
class TransitionType:
    """Transition type."""

    ...


@dataclass
class NavigationEntry:
    """Navigation history entry."""

    ...


@dataclass
class ScreencastFrameMetadata:
    """Screencast frame metadata."""

    ...


@dataclass
class DialogType:
    """Javascript dialog type."""

    ...


@dataclass
class AppManifestError:
    """Error while paring app manifest."""

    ...


@dataclass
class AppManifestParsedProperties:
    """Parsed app manifest properties."""

    ...


@dataclass
class LayoutViewport:
    """Layout viewport position and dimensions."""

    ...


@dataclass
class VisualViewport:
    """Visual viewport position, dimensions, and scale."""

    ...


@dataclass
class Viewport:
    """Viewport for capturing screenshot."""

    ...


@dataclass
class FontFamilies:
    """Generic font families collection."""

    ...


@dataclass
class ScriptFontFamilies:
    """Font families collection for a script."""

    ...


@dataclass
class FontSizes:
    """Default font sizes."""

    ...


@dataclass
class ClientNavigationReason:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ClientNavigationDisposition:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class InstallabilityErrorArgument:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class InstallabilityError:
    """The installability error."""

    ...


@dataclass
class ReferrerPolicy:
    """The referring-policy used for the navigation."""

    ...


@dataclass
class CompilationCacheParams:
    """Per-script compilation cache parameters for
    `Page.produceCompilationCache`"""

    ...


@dataclass
class AutoResponseMode:
    """Enum of possible auto-reponse for permisison / prompt dialogs."""

    ...


@dataclass
class NavigationType:
    """The type of a frameNavigated event."""

    ...


@dataclass
class BackForwardCacheNotRestoredReason:
    """List of not restored reasons for back-forward cache."""

    ...


@dataclass
class BackForwardCacheNotRestoredReasonType:
    """Types of not restored reasons for back-forward cache."""

    ...


@dataclass
class BackForwardCacheNotRestoredExplanation:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class BackForwardCacheNotRestoredExplanationTree:
    """Description is missing from the devtools protocol document."""

    ...
