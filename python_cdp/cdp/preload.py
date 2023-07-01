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

    # Description is missing from the devtools protocol document. # noqa
    id: RuleSetId
    # Identifies a document which the rule set is associated with. # noqa
    loader_id: network.LoaderId
    # Source text of JSON representing the rule set. If it comes from <script>tag, it is the textContent of the node. Note that it is a JSON for valid case.See also: - https://wicg.github.io/nav-speculation/speculation-rules.html -https://github.com/WICG/nav-speculation/blob/main/triggers.md # noqa
    source_text: str
    # A speculation rule set is either added through an inline <script> tag orthrough an external resource via the 'Speculation-Rules' HTTP header. For thefirst case, we include the BackendNodeId of the relevant <script> tag. For thesecond case, we include the external URL where the rule set was loaded from, andalso RequestId if Network domain is enabled.  See also: -https://wicg.github.io/nav-speculation/speculation-rules.html#speculation-rules-script - https://wicg.github.io/nav-speculation/speculation-rules.html#speculation-rules-header # noqa
    backend_node_id: typing.Optional[dom.BackendNodeId]
    # Description is missing from the devtools protocol document. # noqa
    url: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    request_id: typing.Optional[network.RequestId]
    # Error information `errorMessage` is null iff `errorType` is null. # noqa
    error_type: typing.Optional[RuleSetErrorType]
    # TODO(https://crbug.com/1425354): Replace this property with structurederror. # noqa
    error_message: typing.Optional[str]


class RuleSetErrorType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    SOURCE_IS_NOT_JSON_OBJECT = "source_is_not_json_object"
    INVALID_RULES_SKIPPED = "invalid_rules_skipped"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class SpeculationAction(str, enum.Enum):
    """The type of preloading attempted.

    It corresponds to
    mojom::SpeculationAction (although PrefetchWithSubresources is omitted as it
    isn't being used by clients).
    """

    PREFETCH = "prefetch"
    PRERENDER = "prerender"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class SpeculationTargetHint(str, enum.Enum):
    """Corresponds to mojom::SpeculationTargetHint.
    See https://github.com/WICG/nav-speculation/blob/main/triggers.md#window-name-targeting-hints"""

    BLANK = "blank"
    SELF = "self"

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

    # Description is missing from the devtools protocol document. # noqa
    loader_id: network.LoaderId
    # Description is missing from the devtools protocol document. # noqa
    action: SpeculationAction
    # Description is missing from the devtools protocol document. # noqa
    url: str
    # Description is missing from the devtools protocol document. # noqa
    target_hint: typing.Optional[SpeculationTargetHint]


@dataclass
class PreloadingAttemptSource:
    """Lists sources for a preloading attempt, specifically the ids of rule sets that had a speculation rule that
    triggered the attempt, and the BackendNodeIds of <a href> or <area href> elements that triggered the attempt (in the
    case of attempts triggered by a document rule).

    It is possible for mulitple rule sets and links to trigger a single attempt.
    """

    # Description is missing from the devtools protocol document. # noqa
    key: PreloadingAttemptKey
    # Description is missing from the devtools protocol document. # noqa
    rule_set_ids: RuleSetId
    # Description is missing from the devtools protocol document. # noqa
    node_ids: dom.BackendNodeId


class PrerenderFinalStatus(str, enum.Enum):
    """List of FinalStatus reasons for Prerender2."""

    ACTIVATED = "activated"
    DESTROYED = "destroyed"
    LOW_END_DEVICE = "low_end_device"
    INVALID_SCHEME_REDIRECT = "invalid_scheme_redirect"
    INVALID_SCHEME_NAVIGATION = "invalid_scheme_navigation"
    IN_PROGRESS_NAVIGATION = "in_progress_navigation"
    NAVIGATION_REQUEST_BLOCKED_BY_CSP = "navigation_request_blocked_by_csp"
    MAIN_FRAME_NAVIGATION = "main_frame_navigation"
    MOJO_BINDER_POLICY = "mojo_binder_policy"
    RENDERER_PROCESS_CRASHED = "renderer_process_crashed"
    RENDERER_PROCESS_KILLED = "renderer_process_killed"
    DOWNLOAD = "download"
    TRIGGER_DESTROYED = "trigger_destroyed"
    NAVIGATION_NOT_COMMITTED = "navigation_not_committed"
    NAVIGATION_BAD_HTTP_STATUS = "navigation_bad_http_status"
    CLIENT_CERT_REQUESTED = "client_cert_requested"
    NAVIGATION_REQUEST_NETWORK_ERROR = "navigation_request_network_error"
    MAX_NUM_OF_RUNNING_PRERENDERS_EXCEEDED = "max_num_of_running_prerenders_exceeded"
    CANCEL_ALL_HOSTS_FOR_TESTING = "cancel_all_hosts_for_testing"
    DID_FAIL_LOAD = "did_fail_load"
    STOP = "stop"
    SSL_CERTIFICATE_ERROR = "ssl_certificate_error"
    LOGIN_AUTH_REQUESTED = "login_auth_requested"
    UA_CHANGE_REQUIRES_RELOAD = "ua_change_requires_reload"
    BLOCKED_BY_CLIENT = "blocked_by_client"
    AUDIO_OUTPUT_DEVICE_REQUESTED = "audio_output_device_requested"
    MIXED_CONTENT = "mixed_content"
    TRIGGER_BACKGROUNDED = "trigger_backgrounded"
    EMBEDDER_TRIGGERED_AND_CROSS_ORIGIN_REDIRECTED = "embedder_triggered_and_cross_origin_redirected"
    MEMORY_LIMIT_EXCEEDED = "memory_limit_exceeded"
    FAIL_TO_GET_MEMORY_USAGE = "fail_to_get_memory_usage"
    DATA_SAVER_ENABLED = "data_saver_enabled"
    HAS_EFFECTIVE_URL = "has_effective_url"
    ACTIVATED_BEFORE_STARTED = "activated_before_started"
    INACTIVE_PAGE_RESTRICTION = "inactive_page_restriction"
    START_FAILED = "start_failed"
    TIMEOUT_BACKGROUNDED = "timeout_backgrounded"
    CROSS_SITE_REDIRECT_IN_INITIAL_NAVIGATION = "cross_site_redirect_in_initial_navigation"
    CROSS_SITE_NAVIGATION_IN_INITIAL_NAVIGATION = "cross_site_navigation_in_initial_navigation"
    SAME_SITE_CROSS_ORIGIN_REDIRECT_NOT_OPT_IN_IN_INITIAL_NAVIGATION = (
        "same_site_cross_origin_redirect_not_opt_in_in_initial_navigation"
    )
    SAME_SITE_CROSS_ORIGIN_NAVIGATION_NOT_OPT_IN_IN_INITIAL_NAVIGATION = (
        "same_site_cross_origin_navigation_not_opt_in_in_initial_navigation"
    )
    ACTIVATION_NAVIGATION_PARAMETER_MISMATCH = "activation_navigation_parameter_mismatch"
    ACTIVATED_IN_BACKGROUND = "activated_in_background"
    EMBEDDER_HOST_DISALLOWED = "embedder_host_disallowed"
    ACTIVATION_NAVIGATION_DESTROYED_BEFORE_SUCCESS = "activation_navigation_destroyed_before_success"
    TAB_CLOSED_BY_USER_GESTURE = "tab_closed_by_user_gesture"
    TAB_CLOSED_WITHOUT_USER_GESTURE = "tab_closed_without_user_gesture"
    PRIMARY_MAIN_FRAME_RENDERER_PROCESS_CRASHED = "primary_main_frame_renderer_process_crashed"
    PRIMARY_MAIN_FRAME_RENDERER_PROCESS_KILLED = "primary_main_frame_renderer_process_killed"
    ACTIVATION_FRAME_POLICY_NOT_COMPATIBLE = "activation_frame_policy_not_compatible"
    PRELOADING_DISABLED = "preloading_disabled"
    BATTERY_SAVER_ENABLED = "battery_saver_enabled"
    ACTIVATED_DURING_MAIN_FRAME_NAVIGATION = "activated_during_main_frame_navigation"
    PRELOADING_UNSUPPORTED_BY_WEB_CONTENTS = "preloading_unsupported_by_web_contents"
    CROSS_SITE_REDIRECT_IN_MAIN_FRAME_NAVIGATION = "cross_site_redirect_in_main_frame_navigation"
    CROSS_SITE_NAVIGATION_IN_MAIN_FRAME_NAVIGATION = "cross_site_navigation_in_main_frame_navigation"
    SAME_SITE_CROSS_ORIGIN_REDIRECT_NOT_OPT_IN_IN_MAIN_FRAME_NAVIGATION = (
        "same_site_cross_origin_redirect_not_opt_in_in_main_frame_navigation"
    )
    SAME_SITE_CROSS_ORIGIN_NAVIGATION_NOT_OPT_IN_IN_MAIN_FRAME_NAVIGATION = (
        "same_site_cross_origin_navigation_not_opt_in_in_main_frame_navigation"
    )
    MEMORY_PRESSURE_ON_TRIGGER = "memory_pressure_on_trigger"
    MEMORY_PRESSURE_AFTER_TRIGGERED = "memory_pressure_after_triggered"
    PRERENDERING_DISABLED_BY_DEV_TOOLS = "prerendering_disabled_by_dev_tools"
    RESOURCE_LOAD_BLOCKED_BY_CLIENT = "resource_load_blocked_by_client"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PreloadingStatus(str, enum.Enum):
    """Preloading status values, see also PreloadingTriggeringOutcome.

    This status is shared by prefetchStatusUpdated and prerenderStatusUpdated.
    """

    PENDING = "pending"
    RUNNING = "running"
    READY = "ready"
    SUCCESS = "success"
    FAILURE = "failure"
    NOT_SUPPORTED = "not_supported"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PrefetchStatus(str, enum.Enum):
    """TODO(https://crbug.com/1384419): revisit the list of PrefetchStatus and
    filter out the ones that aren't necessary to the developers."""

    PREFETCH_ALLOWED = "prefetch_allowed"
    PREFETCH_FAILED_INELIGIBLE_REDIRECT = "prefetch_failed_ineligible_redirect"
    PREFETCH_FAILED_INVALID_REDIRECT = "prefetch_failed_invalid_redirect"
    PREFETCH_FAILED_M_I_M_E_NOT_SUPPORTED = "prefetch_failed_mime_not_supported"
    PREFETCH_FAILED_NET_ERROR = "prefetch_failed_net_error"
    PREFETCH_FAILED_NON2_X_X = "prefetch_failed_non2_xx"
    PREFETCH_FAILED_PER_PAGE_LIMIT_EXCEEDED = "prefetch_failed_per_page_limit_exceeded"
    PREFETCH_EVICTED = "prefetch_evicted"
    PREFETCH_HELDBACK = "prefetch_heldback"
    PREFETCH_INELIGIBLE_RETRY_AFTER = "prefetch_ineligible_retry_after"
    PREFETCH_IS_PRIVACY_DECOY = "prefetch_is_privacy_decoy"
    PREFETCH_IS_STALE = "prefetch_is_stale"
    PREFETCH_NOT_ELIGIBLE_BROWSER_CONTEXT_OFF_THE_RECORD = "prefetch_not_eligible_browser_context_off_the_record"
    PREFETCH_NOT_ELIGIBLE_DATA_SAVER_ENABLED = "prefetch_not_eligible_data_saver_enabled"
    PREFETCH_NOT_ELIGIBLE_EXISTING_PROXY = "prefetch_not_eligible_existing_proxy"
    PREFETCH_NOT_ELIGIBLE_HOST_IS_NON_UNIQUE = "prefetch_not_eligible_host_is_non_unique"
    PREFETCH_NOT_ELIGIBLE_NON_DEFAULT_STORAGE_PARTITION = "prefetch_not_eligible_non_default_storage_partition"
    PREFETCH_NOT_ELIGIBLE_SAME_SITE_CROSS_ORIGIN_PREFETCH_REQUIRED_PROXY = (
        "prefetch_not_eligible_same_site_cross_origin_prefetch_required_proxy"
    )
    PREFETCH_NOT_ELIGIBLE_SCHEME_IS_NOT_HTTPS = "prefetch_not_eligible_scheme_is_not_https"
    PREFETCH_NOT_ELIGIBLE_USER_HAS_COOKIES = "prefetch_not_eligible_user_has_cookies"
    PREFETCH_NOT_ELIGIBLE_USER_HAS_SERVICE_WORKER = "prefetch_not_eligible_user_has_service_worker"
    PREFETCH_NOT_ELIGIBLE_BATTERY_SAVER_ENABLED = "prefetch_not_eligible_battery_saver_enabled"
    PREFETCH_NOT_ELIGIBLE_PRELOADING_DISABLED = "prefetch_not_eligible_preloading_disabled"
    PREFETCH_NOT_FINISHED_IN_TIME = "prefetch_not_finished_in_time"
    PREFETCH_NOT_STARTED = "prefetch_not_started"
    PREFETCH_NOT_USED_COOKIES_CHANGED = "prefetch_not_used_cookies_changed"
    PREFETCH_PROXY_NOT_AVAILABLE = "prefetch_proxy_not_available"
    PREFETCH_RESPONSE_USED = "prefetch_response_used"
    PREFETCH_SUCCESSFUL_BUT_NOT_USED = "prefetch_successful_but_not_used"
    PREFETCH_NOT_USED_PROBE_FAILED = "prefetch_not_used_probe_failed"

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

    key: PreloadingAttemptKey
    initiating_frame_id: page.FrameId
    prerendering_url: str
    final_status: PrerenderFinalStatus
    disallowed_api_method: typing.Optional[str]


@dataclass
@memoize_event("Preload.preloadEnabledStateUpdated")
class PreloadEnabledStateUpdated:
    """Fired when a preload enabled state is updated."""

    disabled_by_preference: bool
    disabled_by_data_saver: bool
    disabled_by_battery_saver: bool
    disabled_by_holdback_prefetch_speculation_rules: bool
    disabled_by_holdback_prerender_speculation_rules: bool


@dataclass
@memoize_event("Preload.prefetchStatusUpdated")
class PrefetchStatusUpdated:
    """Fired when a prefetch attempt is updated."""

    key: PreloadingAttemptKey
    initiating_frame_id: page.FrameId
    prefetch_url: str
    status: PreloadingStatus
    prefetch_status: PrefetchStatus
    request_id: network.RequestId


@dataclass
@memoize_event("Preload.prerenderStatusUpdated")
class PrerenderStatusUpdated:
    """Fired when a prerender attempt is updated."""

    key: PreloadingAttemptKey
    status: PreloadingStatus
    prerender_status: typing.Optional[PrerenderFinalStatus]
    disallowed_mojo_interface: typing.Optional[str]


@dataclass
@memoize_event("Preload.preloadingAttemptSourcesUpdated")
class PreloadingAttemptSourcesUpdated:
    """Send a list of sources for all preloading attempts in a document."""

    loader_id: network.LoaderId
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
