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

from dataclasses import dataclass


@dataclass
class RuleSetId:
    """Unique id."""

    ...


@dataclass
class RuleSet:
    """Corresponds to SpeculationRuleSet."""

    ...


@dataclass
class SpeculationAction:
    """The type of preloading attempted.

    It corresponds to mojom::SpeculationAction (although
    PrefetchWithSubresources is omitted as it isn't being used by
    clients).
    """

    ...


@dataclass
class SpeculationTargetHint:
    """Corresponds to mojom::SpeculationTargetHint.

    See
    https://github.com/WICG/nav-speculation/blob/main/triggers.md#window-name-targeting-hints
    """

    ...


@dataclass
class PreloadingAttemptKey:
    """A key that identifies a preloading attempt.

    The url used is the url specified by the trigger (i.e. the initial
    URL), and not the final url that is navigated to. For example,
    prerendering allows same-origin main frame navigations during the
    attempt, but the attempt is still keyed with the initial URL.
    """

    ...


@dataclass
class PreloadingAttemptSource:
    """Lists sources for a preloading attempt, specifically the ids of rule
    sets that had a speculation rule that triggered the attempt, and the
    BackendNodeIds of <a href> or <area href> elements that triggered the
    attempt (in the case of attempts triggered by a document rule).

    It is possible for mulitple rule sets and links to trigger a single
    attempt.
    """

    ...


@dataclass
class PrerenderFinalStatus:
    """List of FinalStatus reasons for Prerender2."""

    ...


@dataclass
class PreloadingStatus:
    """Preloading status values, see also PreloadingTriggeringOutcome.

    This status is shared by prefetchStatusUpdated and
    prerenderStatusUpdated.
    """

    ...
