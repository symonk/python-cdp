# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Preload`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Preload/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import dom
from . import network


class RuleSetId(str):
    """Unique id."""

    def to_json(self) -> RuleSetId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class RuleSet:
    """Corresponds to SpeculationRuleSet."""

    #: Description is missing from the devtools protocol document.# noqa
    id: RuleSetId
    #: Identifies a document which the rule set is associated with.# noqa
    loaderId: network.LoaderId
    #: Source text of JSON representing the rule set. If it comes from <script>tag, it is the textContent of the node. Note that it is a JSON for valid case.See also: - https://wicg.github.io/nav-speculation/speculation-rules.html -https://github.com/WICG/nav-speculation/blob/main/triggers.md# noqa
    sourceText: str


class SpeculationAction(str, enum.Enum):
    """The type of preloading attempted.

    It corresponds to mojom::SpeculationAction (although
    PrefetchWithSubresources is omitted as it isn't being used by
    clients).
    """

    PREFETCH = "Prefetch"
    PRERENDER = "Prerender"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class SpeculationTargetHint(str, enum.Enum):
    """Corresponds to mojom::SpeculationTargetHint.

    See
    https://github.com/WICG/nav-speculation/blob/main/triggers.md#window-name-targeting-hints
    """

    BLANK = "Blank"
    SELF = "Self"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class PreloadingAttemptKey:
    """A key that identifies a preloading attempt.

    The url used is the url specified by the trigger (i.e. the initial
    URL), and not the final url that is navigated to. For example,
    prerendering allows same-origin main frame navigations during the
    attempt, but the attempt is still keyed with the initial URL.
    """

    #: Description is missing from the devtools protocol document.# noqa
    loaderId: network.LoaderId
    #: Description is missing from the devtools protocol document.# noqa
    action: SpeculationAction
    #: Description is missing from the devtools protocol document.# noqa
    url: str
    #: Description is missing from the devtools protocol document.# noqa
    targetHint: typing.Optional[SpeculationTargetHint] = None


@dataclass
class PreloadingAttemptSource:
    """Lists sources for a preloading attempt, specifically the ids of rule
    sets that had a speculation rule that triggered the attempt, and the
    BackendNodeIds of <a href> or <area href> elements that triggered the
    attempt (in the case of attempts triggered by a document rule).

    It is possible for mulitple rule sets and links to trigger a single
    attempt.
    """

    #: Description is missing from the devtools protocol document.# noqa
    key: PreloadingAttemptKey
    #: Description is missing from the devtools protocol document.# noqa
    ruleSetIds: RuleSetId
    #: Description is missing from the devtools protocol document.# noqa
    nodeIds: dom.BackendNodeId


class PrerenderFinalStatus(str, enum.Enum):
    """List of FinalStatus reasons for Prerender2."""

    ACTIVATED = "Activated"
    DESTROYED = "Destroyed"
    LOWENDDEVICE = "LowEndDevice"
    INVALIDSCHEMEREDIRECT = "InvalidSchemeRedirect"
    INVALIDSCHEMENAVIGATION = "InvalidSchemeNavigation"
    INPROGRESSNAVIGATION = "InProgressNavigation"
    NAVIGATIONREQUESTBLOCKEDBYCSP = "NavigationRequestBlockedByCsp"
    MAINFRAMENAVIGATION = "MainFrameNavigation"
    MOJOBINDERPOLICY = "MojoBinderPolicy"
    RENDERERPROCESSCRASHED = "RendererProcessCrashed"
    RENDERERPROCESSKILLED = "RendererProcessKilled"
    DOWNLOAD = "Download"
    TRIGGERDESTROYED = "TriggerDestroyed"
    NAVIGATIONNOTCOMMITTED = "NavigationNotCommitted"
    NAVIGATIONBADHTTPSTATUS = "NavigationBadHttpStatus"
    CLIENTCERTREQUESTED = "ClientCertRequested"
    NAVIGATIONREQUESTNETWORKERROR = "NavigationRequestNetworkError"
    MAXNUMOFRUNNINGPRERENDERSEXCEEDED = "MaxNumOfRunningPrerendersExceeded"
    CANCELALLHOSTSFORTESTING = "CancelAllHostsForTesting"
    DIDFAILLOAD = "DidFailLoad"
    STOP = "Stop"
    SSLCERTIFICATEERROR = "SslCertificateError"
    LOGINAUTHREQUESTED = "LoginAuthRequested"
    UACHANGEREQUIRESRELOAD = "UaChangeRequiresReload"
    BLOCKEDBYCLIENT = "BlockedByClient"
    AUDIOOUTPUTDEVICEREQUESTED = "AudioOutputDeviceRequested"
    MIXEDCONTENT = "MixedContent"
    TRIGGERBACKGROUNDED = "TriggerBackgrounded"
    EMBEDDERTRIGGEREDANDCROSSORIGINREDIRECTED = "EmbedderTriggeredAndCrossOriginRedirected"
    MEMORYLIMITEXCEEDED = "MemoryLimitExceeded"
    FAILTOGETMEMORYUSAGE = "FailToGetMemoryUsage"
    DATASAVERENABLED = "DataSaverEnabled"
    HASEFFECTIVEURL = "HasEffectiveUrl"
    ACTIVATEDBEFORESTARTED = "ActivatedBeforeStarted"
    INACTIVEPAGERESTRICTION = "InactivePageRestriction"
    STARTFAILED = "StartFailed"
    TIMEOUTBACKGROUNDED = "TimeoutBackgrounded"
    CROSSSITEREDIRECT = "CrossSiteRedirect"
    CROSSSITENAVIGATION = "CrossSiteNavigation"
    SAMESITECROSSORIGINREDIRECT = "SameSiteCrossOriginRedirect"
    SAMESITECROSSORIGINREDIRECTNOTOPTIN = "SameSiteCrossOriginRedirectNotOptIn"
    SAMESITECROSSORIGINNAVIGATIONNOTOPTIN = "SameSiteCrossOriginNavigationNotOptIn"
    ACTIVATIONNAVIGATIONPARAMETERMISMATCH = "ActivationNavigationParameterMismatch"
    ACTIVATEDINBACKGROUND = "ActivatedInBackground"
    EMBEDDERHOSTDISALLOWED = "EmbedderHostDisallowed"
    ACTIVATIONNAVIGATIONDESTROYEDBEFORESUCCESS = "ActivationNavigationDestroyedBeforeSuccess"
    TABCLOSEDBYUSERGESTURE = "TabClosedByUserGesture"
    TABCLOSEDWITHOUTUSERGESTURE = "TabClosedWithoutUserGesture"
    PRIMARYMAINFRAMERENDERERPROCESSCRASHED = "PrimaryMainFrameRendererProcessCrashed"
    PRIMARYMAINFRAMERENDERERPROCESSKILLED = "PrimaryMainFrameRendererProcessKilled"
    ACTIVATIONFRAMEPOLICYNOTCOMPATIBLE = "ActivationFramePolicyNotCompatible"
    PRELOADINGDISABLED = "PreloadingDisabled"
    BATTERYSAVERENABLED = "BatterySaverEnabled"
    ACTIVATEDDURINGMAINFRAMENAVIGATION = "ActivatedDuringMainFrameNavigation"
    PRELOADINGUNSUPPORTEDBYWEBCONTENTS = "PreloadingUnsupportedByWebContents"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PreloadingStatus(str, enum.Enum):
    """Preloading status values, see also PreloadingTriggeringOutcome.

    This status is shared by prefetchStatusUpdated and
    prerenderStatusUpdated.
    """

    PENDING = "Pending"
    RUNNING = "Running"
    READY = "Ready"
    SUCCESS = "Success"
    FAILURE = "Failure"
    NOTSUPPORTED = "NotSupported"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)
