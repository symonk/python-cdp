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

from . import network
from . import page
from .utils import memoize_event


class RuleSetId(str):
    """Unique id."""

    def to_json(self) -> RuleSetId:
        return self

    @classmethod
    def from_json(cls, value: str) -> RuleSetId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class RuleSet:
    """Corresponds to SpeculationRuleSet."""

    # Description is missing from the devtools protocol document.# noqa
    id: RuleSetId
    # Identifies a document which the rule set is associated with.# noqa
    loader_id: network.LoaderId
    # Source text of JSON representing the rule set. If it comes from <script>tag, it is the textContent of the node. Note that it is a JSON for valid case.See also: - https://wicg.github.io/nav-speculation/speculation-rules.html -https://github.com/WICG/nav-speculation/blob/main/triggers.md# noqa
    source_text: str


class SpeculationAction(str, enum.Enum):
    """The type of preloading attempted.

    It corresponds to mojom::SpeculationAction (although PrefetchWithSubresources is omitted as it isn't being used by
    clients).
    """

    _PREFETCH = "prefetch"
    _PRERENDER = "prerender"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class SpeculationTargetHint(str, enum.Enum):
    """Corresponds to mojom::SpeculationTargetHint.

    See https://github.com/WICG/nav-speculation/blob/main/triggers.md#window-name-targeting-hints
    """

    _BLANK = "blank"
    _SELF = "self"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class PreloadingAttemptKey:
    """A key that identifies a preloading attempt.

    The url used is the url specified by the trigger (i.e. the initial URL), and not the final url that is navigated to.
    For example, prerendering allows same-origin main frame navigations during the attempt, but the attempt is still
    keyed with the initial URL.
    """

    # Description is missing from the devtools protocol document.# noqa
    loader_id: network.LoaderId
    # Description is missing from the devtools protocol document.# noqa
    action: SpeculationAction
    # Description is missing from the devtools protocol document.# noqa
    url: str
    # Description is missing from the devtools protocol document.# noqa
    target_hint: typing.Optional[SpeculationTargetHint]


@dataclass
class PreloadingAttemptSource:
    """Lists sources for a preloading attempt, specifically the ids of rule sets that had a speculation rule that
    triggered the attempt, and the BackendNodeIds of <a href> or <area href> elements that triggered the attempt (in the
    case of attempts triggered by a document rule).

    It is possible for mulitple rule sets and links to trigger a single attempt.
    """

    # Description is missing from the devtools protocol document.# noqa
    key: PreloadingAttemptKey
    # Description is missing from the devtools protocol document.# noqa
    rule_set_ids: RuleSetId
    # Description is missing from the devtools protocol document.# noqa
    node_ids: dom.BackendNodeId


class PrerenderFinalStatus(str, enum.Enum):
    """List of FinalStatus reasons for Prerender2."""

    _ACTIVATED = "activated"
    _DESTROYED = "destroyed"
    _LOW_END_DEVICE = "low_end_device"
    _INVALID_SCHEME_REDIRECT = "invalid_scheme_redirect"
    _INVALID_SCHEME_NAVIGATION = "invalid_scheme_navigation"
    _IN_PROGRESS_NAVIGATION = "in_progress_navigation"
    _NAVIGATION_REQUEST_BLOCKED_BY_CSP = "navigation_request_blocked_by_csp"
    _MAIN_FRAME_NAVIGATION = "main_frame_navigation"
    _MOJO_BINDER_POLICY = "mojo_binder_policy"
    _RENDERER_PROCESS_CRASHED = "renderer_process_crashed"
    _RENDERER_PROCESS_KILLED = "renderer_process_killed"
    _DOWNLOAD = "download"
    _TRIGGER_DESTROYED = "trigger_destroyed"
    _NAVIGATION_NOT_COMMITTED = "navigation_not_committed"
    _NAVIGATION_BAD_HTTP_STATUS = "navigation_bad_http_status"
    _CLIENT_CERT_REQUESTED = "client_cert_requested"
    _NAVIGATION_REQUEST_NETWORK_ERROR = "navigation_request_network_error"
    _MAX_NUM_OF_RUNNING_PRERENDERS_EXCEEDED = "max_num_of_running_prerenders_exceeded"
    _CANCEL_ALL_HOSTS_FOR_TESTING = "cancel_all_hosts_for_testing"
    _DID_FAIL_LOAD = "did_fail_load"
    _STOP = "stop"
    _SSL_CERTIFICATE_ERROR = "ssl_certificate_error"
    _LOGIN_AUTH_REQUESTED = "login_auth_requested"
    _UA_CHANGE_REQUIRES_RELOAD = "ua_change_requires_reload"
    _BLOCKED_BY_CLIENT = "blocked_by_client"
    _AUDIO_OUTPUT_DEVICE_REQUESTED = "audio_output_device_requested"
    _MIXED_CONTENT = "mixed_content"
    _TRIGGER_BACKGROUNDED = "trigger_backgrounded"
    _EMBEDDER_TRIGGERED_AND_CROSS_ORIGIN_REDIRECTED = "embedder_triggered_and_cross_origin_redirected"
    _MEMORY_LIMIT_EXCEEDED = "memory_limit_exceeded"
    _FAIL_TO_GET_MEMORY_USAGE = "fail_to_get_memory_usage"
    _DATA_SAVER_ENABLED = "data_saver_enabled"
    _HAS_EFFECTIVE_URL = "has_effective_url"
    _ACTIVATED_BEFORE_STARTED = "activated_before_started"
    _INACTIVE_PAGE_RESTRICTION = "inactive_page_restriction"
    _START_FAILED = "start_failed"
    _TIMEOUT_BACKGROUNDED = "timeout_backgrounded"
    _CROSS_SITE_REDIRECT = "cross_site_redirect"
    _CROSS_SITE_NAVIGATION = "cross_site_navigation"
    _SAME_SITE_CROSS_ORIGIN_REDIRECT = "same_site_cross_origin_redirect"
    _SAME_SITE_CROSS_ORIGIN_REDIRECT_NOT_OPT_IN = "same_site_cross_origin_redirect_not_opt_in"
    _SAME_SITE_CROSS_ORIGIN_NAVIGATION_NOT_OPT_IN = "same_site_cross_origin_navigation_not_opt_in"
    _ACTIVATION_NAVIGATION_PARAMETER_MISMATCH = "activation_navigation_parameter_mismatch"
    _ACTIVATED_IN_BACKGROUND = "activated_in_background"
    _EMBEDDER_HOST_DISALLOWED = "embedder_host_disallowed"
    _ACTIVATION_NAVIGATION_DESTROYED_BEFORE_SUCCESS = "activation_navigation_destroyed_before_success"
    _TAB_CLOSED_BY_USER_GESTURE = "tab_closed_by_user_gesture"
    _TAB_CLOSED_WITHOUT_USER_GESTURE = "tab_closed_without_user_gesture"
    _PRIMARY_MAIN_FRAME_RENDERER_PROCESS_CRASHED = "primary_main_frame_renderer_process_crashed"
    _PRIMARY_MAIN_FRAME_RENDERER_PROCESS_KILLED = "primary_main_frame_renderer_process_killed"
    _ACTIVATION_FRAME_POLICY_NOT_COMPATIBLE = "activation_frame_policy_not_compatible"
    _PRELOADING_DISABLED = "preloading_disabled"
    _BATTERY_SAVER_ENABLED = "battery_saver_enabled"
    _ACTIVATED_DURING_MAIN_FRAME_NAVIGATION = "activated_during_main_frame_navigation"
    _PRELOADING_UNSUPPORTED_BY_WEB_CONTENTS = "preloading_unsupported_by_web_contents"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PreloadingStatus(str, enum.Enum):
    """Preloading status values, see also PreloadingTriggeringOutcome.

    This status is shared by prefetchStatusUpdated and prerenderStatusUpdated.
    """

    _PENDING = "pending"
    _RUNNING = "running"
    _READY = "ready"
    _SUCCESS = "success"
    _FAILURE = "failure"
    _NOT_SUPPORTED = "not_supported"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
@memoize_event("Preload.ruleSetUpdated")
class RuleSetUpdated:
    """Upsert.

    Currently, it is only emitted when a rule set added.
    """

    rule_set: RuleSet


@dataclass
@memoize_event("Preload.ruleSetRemoved")
class RuleSetRemoved:
    """Description is missing from the devtools protocol document."""

    id: RuleSetId


@dataclass
@memoize_event("Preload.prerenderAttemptCompleted")
class PrerenderAttemptCompleted:
    """Fired when a prerender attempt is completed."""

    initiating_frame_id: page.FrameId
    prerendering_url: str
    final_status: PrerenderFinalStatus
    disallowed_api_method: typing.Optional[str]


@dataclass
@memoize_event("Preload.prefetchStatusUpdated")
class PrefetchStatusUpdated:
    """Fired when a prefetch attempt is updated."""

    initiating_frame_id: page.FrameId
    prefetch_url: str
    status: PreloadingStatus


@dataclass
@memoize_event("Preload.prerenderStatusUpdated")
class PrerenderStatusUpdated:
    """Fired when a prerender attempt is updated."""

    initiating_frame_id: page.FrameId
    prerendering_url: str
    status: PreloadingStatus


@dataclass
@memoize_event("Preload.preloadingAttemptSourcesUpdated")
class PreloadingAttemptSourcesUpdated:
    """Send a list of sources for all preloading attempts."""

    preloading_attempt_sources: typing.List[PreloadingAttemptSource]


async def enable() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def disable() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...
