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

import enum
import typing
from dataclasses import dataclass

from . import dom
from . import network
from . import runtime
from .utils import memoize_event


class FrameId(str):
    """Unique frame identifier."""

    def to_json(self) -> FrameId:
        return self

    @classmethod
    def from_json(cls, value: str) -> FrameId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class AdFrameType(str, enum.Enum):
    """Indicates whether a frame has been identified as an ad."""

    NONE = "none"
    CHILD = "child"
    ROOT = "root"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class AdFrameExplanation(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _PARENT_IS_AD = "parent_is_ad"
    _CREATED_BY_AD_SCRIPT = "created_by_ad_script"
    _MATCHED_BLOCKING_RULE = "matched_blocking_rule"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class AdFrameStatus:
    """Indicates whether a frame has been identified as an ad and why."""

    # Description is missing from the devtools protocol document.# noqa
    ad_frame_type: AdFrameType
    # Description is missing from the devtools protocol document.# noqa
    explanations: typing.Optional[AdFrameExplanation]


@dataclass
class AdScriptId:
    """Identifies the bottom-most script which caused the frame to be labelled as an ad."""

    # Script Id of the bottom-most script which caused the frame to be labelledas an ad.# noqa
    script_id: runtime.ScriptId
    # Id of adScriptId's debugger.# noqa
    debugger_id: runtime.UniqueDebuggerId


class SecureContextType(str, enum.Enum):
    """Indicates whether the frame is a secure context and why it is the case."""

    _SECURE = "secure"
    _SECURE_LOCALHOST = "secure_localhost"
    _INSECURE_SCHEME = "insecure_scheme"
    _INSECURE_ANCESTOR = "insecure_ancestor"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CrossOriginIsolatedContextType(str, enum.Enum):
    """Indicates whether the frame is cross-origin isolated and why it is the case."""

    _ISOLATED = "isolated"
    _NOT_ISOLATED = "not_isolated"
    _NOT_ISOLATED_FEATURE_DISABLED = "not_isolated_feature_disabled"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class GatedAPIFeatures(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _SHARED_ARRAY_BUFFERS = "shared_array_buffers"
    _SHARED_ARRAY_BUFFERS_TRANSFER_ALLOWED = "shared_array_buffers_transfer_allowed"
    _PERFORMANCE_MEASURE_MEMORY = "performance_measure_memory"
    _PERFORMANCE_PROFILE = "performance_profile"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PermissionsPolicyFeature(str, enum.Enum):
    """All Permissions Policy features.

    This enum should match the one defined
    in third_party/blink/renderer/core/permissions_policy/permissions_policy_features.json5.
    """

    ACCELEROMETER = "accelerometer"
    AMBIENT_LIGHT_SENSOR = "ambient-light-sensor"
    ATTRIBUTION_REPORTING = "attribution-reporting"
    AUTOPLAY = "autoplay"
    BLUETOOTH = "bluetooth"
    BROWSING_TOPICS = "browsing-topics"
    CAMERA = "camera"
    CH_DPR = "ch-dpr"
    CH_DEVICE_MEMORY = "ch-device-memory"
    CH_DOWNLINK = "ch-downlink"
    CH_ECT = "ch-ect"
    CH_PREFERS_COLOR_SCHEME = "ch-prefers-color-scheme"
    CH_PREFERS_REDUCED_MOTION = "ch-prefers-reduced-motion"
    CH_RTT = "ch-rtt"
    CH_SAVE_DATA = "ch-save-data"
    CH_UA = "ch-ua"
    CH_UA_ARCH = "ch-ua-arch"
    CH_UA_BITNESS = "ch-ua-bitness"
    CH_UA_PLATFORM = "ch-ua-platform"
    CH_UA_MODEL = "ch-ua-model"
    CH_UA_MOBILE = "ch-ua-mobile"
    CH_UA_FULL = "ch-ua-full"
    CH_UA_FULL_VERSION = "ch-ua-full-version"
    CH_UA_FULL_VERSION_LIST = "ch-ua-full-version-list"
    CH_UA_PLATFORM_VERSION = "ch-ua-platform-version"
    CH_UA_REDUCED = "ch-ua-reduced"
    CH_UA_WOW64 = "ch-ua-wow64"
    CH_VIEWPORT_HEIGHT = "ch-viewport-height"
    CH_VIEWPORT_WIDTH = "ch-viewport-width"
    CH_WIDTH = "ch-width"
    CLIPBOARD_READ = "clipboard-read"
    CLIPBOARD_WRITE = "clipboard-write"
    COMPUTE_PRESSURE = "compute-pressure"
    CROSS_ORIGIN_ISOLATED = "cross-origin-isolated"
    DIRECT_SOCKETS = "direct-sockets"
    DISPLAY_CAPTURE = "display-capture"
    DOCUMENT_DOMAIN = "document-domain"
    ENCRYPTED_MEDIA = "encrypted-media"
    EXECUTION_WHILE_OUT_OF_VIEWPORT = "execution-while-out-of-viewport"
    EXECUTION_WHILE_NOT_RENDERED = "execution-while-not-rendered"
    FOCUS_WITHOUT_USER_ACTIVATION = "focus-without-user-activation"
    FULLSCREEN = "fullscreen"
    FROBULATE = "frobulate"
    GAMEPAD = "gamepad"
    GEOLOCATION = "geolocation"
    GYROSCOPE = "gyroscope"
    HID = "hid"
    IDENTITY_CREDENTIALS_GET = "identity-credentials-get"
    IDLE_DETECTION = "idle-detection"
    INTEREST_COHORT = "interest-cohort"
    JOIN_AD_INTEREST_GROUP = "join-ad-interest-group"
    KEYBOARD_MAP = "keyboard-map"
    LOCAL_FONTS = "local-fonts"
    MAGNETOMETER = "magnetometer"
    MICROPHONE = "microphone"
    MIDI = "midi"
    OTP_CREDENTIALS = "otp-credentials"
    PAYMENT = "payment"
    PICTURE_IN_PICTURE = "picture-in-picture"
    PRIVATE_AGGREGATION = "private-aggregation"
    PUBLICKEY_CREDENTIALS_GET = "publickey-credentials-get"
    RUN_AD_AUCTION = "run-ad-auction"
    SCREEN_WAKE_LOCK = "screen-wake-lock"
    SERIAL = "serial"
    SHARED_AUTOFILL = "shared-autofill"
    SHARED_STORAGE = "shared-storage"
    SHARED_STORAGE_SELECT_URL = "shared-storage-select-url"
    SMART_CARD = "smart-card"
    STORAGE_ACCESS = "storage-access"
    SYNC_XHR = "sync-xhr"
    TRUST_TOKEN_REDEMPTION = "trust-token-redemption"
    UNLOAD = "unload"
    USB = "usb"
    VERTICAL_SCROLL = "vertical-scroll"
    WEB_SHARE = "web-share"
    WINDOW_MANAGEMENT = "window-management"
    WINDOW_PLACEMENT = "window-placement"
    XR_SPATIAL_TRACKING = "xr-spatial-tracking"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PermissionsPolicyBlockReason(str, enum.Enum):
    """Reason for a permissions policy feature to be disabled."""

    _HEADER = "header"
    _IFRAME_ATTRIBUTE = "iframe_attribute"
    _IN_FENCED_FRAME_TREE = "in_fenced_frame_tree"
    _IN_ISOLATED_APP = "in_isolated_app"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class PermissionsPolicyBlockLocator:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa
    frame_id: FrameId
    # Description is missing from the devtools protocol document.# noqa
    block_reason: PermissionsPolicyBlockReason


@dataclass
class PermissionsPolicyFeatureState:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa
    feature: PermissionsPolicyFeature
    # Description is missing from the devtools protocol document.# noqa
    allowed: bool
    # Description is missing from the devtools protocol document.# noqa
    locator: typing.Optional[PermissionsPolicyBlockLocator]


class OriginTrialTokenStatus(str, enum.Enum):
    """Origin Trial(https://www.chromium.org/blink/origin-trials) support.

    Status for an Origin Trial token.
    """

    _SUCCESS = "success"
    _NOT_SUPPORTED = "not_supported"
    _INSECURE = "insecure"
    _EXPIRED = "expired"
    _WRONG_ORIGIN = "wrong_origin"
    _INVALID_SIGNATURE = "invalid_signature"
    _MALFORMED = "malformed"
    _WRONG_VERSION = "wrong_version"
    _FEATURE_DISABLED = "feature_disabled"
    _TOKEN_DISABLED = "token_disabled"
    _FEATURE_DISABLED_FOR_USER = "feature_disabled_for_user"
    _UNKNOWN_TRIAL = "unknown_trial"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class OriginTrialStatus(str, enum.Enum):
    """Status for an Origin Trial."""

    _ENABLED = "enabled"
    _VALID_TOKEN_NOT_PROVIDED = "valid_token_not_provided"
    _O_S_NOT_SUPPORTED = "os_not_supported"
    _TRIAL_NOT_ALLOWED = "trial_not_allowed"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class OriginTrialUsageRestriction(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _NONE = "none"
    _SUBSET = "subset"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class OriginTrialToken:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa
    origin: str
    # Description is missing from the devtools protocol document.# noqa
    match_sub_domains: bool
    # Description is missing from the devtools protocol document.# noqa
    trial_name: str
    # Description is missing from the devtools protocol document.# noqa
    expiry_time: network.TimeSinceEpoch
    # Description is missing from the devtools protocol document.# noqa
    is_third_party: bool
    # Description is missing from the devtools protocol document.# noqa
    usage_restriction: OriginTrialUsageRestriction


@dataclass
class OriginTrialTokenWithStatus:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa
    raw_token_text: str
    # Description is missing from the devtools protocol document.# noqa
    status: OriginTrialTokenStatus
    # `parsedToken` is present only when the token is extractable and parsable.# noqa
    parsed_token: typing.Optional[OriginTrialToken]


@dataclass
class OriginTrial:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa
    trial_name: str
    # Description is missing from the devtools protocol document.# noqa
    status: OriginTrialStatus
    # Description is missing from the devtools protocol document.# noqa
    tokens_with_status: OriginTrialTokenWithStatus


@dataclass
class Frame:
    """Information about the Frame on the page."""

    # Frame unique identifier.# noqa
    id: FrameId
    # Identifier of the loader associated with this frame.# noqa
    loader_id: network.LoaderId
    # Frame document's URL without fragment.# noqa
    url: str
    # Frame document's registered domain, taking the public suffixes list intoaccount. Extracted from the Frame's url. Example URLs:http://www.google.com/file.html -> "google.com"http://a.b.co.uk/file.html      -> "b.co.uk"# noqa
    domain_and_registry: str
    # Frame document's security origin.# noqa
    security_origin: str
    # Frame document's mimeType as determined by the browser.# noqa
    mime_type: str
    # Indicates whether the main document is a secure context and explains whythat is the case.# noqa
    secure_context_type: SecureContextType
    # Indicates whether this is a cross origin isolated context.# noqa
    cross_origin_isolated_context_type: CrossOriginIsolatedContextType
    # Indicated which gated APIs / features are available.# noqa
    gated_api_features: GatedAPIFeatures
    # Parent frame identifier.# noqa
    parent_id: typing.Optional[FrameId]
    # Frame's name as specified in the tag.# noqa
    name: typing.Optional[str]
    # Frame document's URL fragment including the '#'.# noqa
    url_fragment: typing.Optional[str]
    # If the frame failed to load, this contains the URL that could not beloaded. Note that unlike url above, this URL may contain a fragment.# noqa
    unreachable_url: typing.Optional[str]
    # Indicates whether this frame was tagged as an ad and why.# noqa
    ad_frame_status: typing.Optional[AdFrameStatus]


@dataclass
class FrameResource:
    """Information about the Resource on the page."""

    # Resource URL.# noqa
    url: str
    # Type of this resource.# noqa
    type: network.ResourceType
    # Resource mimeType as determined by the browser.# noqa
    mime_type: str
    # last-modified timestamp as reported by server.# noqa
    last_modified: typing.Optional[network.TimeSinceEpoch]
    # Resource content size.# noqa
    content_size: typing.Optional[float]
    # True if the resource failed to load.# noqa
    failed: typing.Optional[bool]
    # True if the resource was canceled during loading.# noqa
    canceled: typing.Optional[bool]


@dataclass
class FrameResourceTree:
    """Information about the Frame hierarchy along with their cached resources."""

    # Frame information for this tree item.# noqa
    frame: Frame
    # Information about frame resources.# noqa
    resources: FrameResource
    # Child frames.# noqa
    child_frames: typing.Optional[FrameResourceTree]


@dataclass
class FrameTree:
    """Information about the Frame hierarchy."""

    # Frame information for this tree item.# noqa
    frame: Frame
    # Child frames.# noqa
    child_frames: typing.Optional[FrameTree]


class ScriptIdentifier(str):
    """Unique script identifier."""

    def to_json(self) -> ScriptIdentifier:
        return self

    @classmethod
    def from_json(cls, value: str) -> ScriptIdentifier:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class TransitionType(str, enum.Enum):
    """Transition type."""

    LINK = "link"
    TYPED = "typed"
    ADDRESS_BAR = "address_bar"
    AUTO_BOOKMARK = "auto_bookmark"
    AUTO_SUBFRAME = "auto_subframe"
    MANUAL_SUBFRAME = "manual_subframe"
    GENERATED = "generated"
    AUTO_TOPLEVEL = "auto_toplevel"
    FORM_SUBMIT = "form_submit"
    RELOAD = "reload"
    KEYWORD = "keyword"
    KEYWORD_GENERATED = "keyword_generated"
    OTHER = "other"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class NavigationEntry:
    """Navigation history entry."""

    # Unique id of the navigation history entry.# noqa
    id: int
    # URL of the navigation history entry.# noqa
    url: str
    # URL that the user typed in the url bar.# noqa
    user_typed_url: str
    # Title of the navigation history entry.# noqa
    title: str
    # Transition type.# noqa
    transition_type: TransitionType


@dataclass
class ScreencastFrameMetadata:
    """Screencast frame metadata."""

    # Top offset in DIP.# noqa
    offset_top: float
    # Page scale factor.# noqa
    page_scale_factor: float
    # Device screen width in DIP.# noqa
    device_width: float
    # Device screen height in DIP.# noqa
    device_height: float
    # Position of horizontal scroll in CSS pixels.# noqa
    scroll_offset_x: float
    # Position of vertical scroll in CSS pixels.# noqa
    scroll_offset_y: float
    # Frame swap timestamp.# noqa
    timestamp: typing.Optional[network.TimeSinceEpoch]


class DialogType(str, enum.Enum):
    """Javascript dialog type."""

    ALERT = "alert"
    CONFIRM = "confirm"
    PROMPT = "prompt"
    BEFOREUNLOAD = "beforeunload"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class AppManifestError:
    """Error while paring app manifest."""

    # Error message.# noqa
    message: str
    # If criticial, this is a non-recoverable parse error.# noqa
    critical: int
    # Error line.# noqa
    line: int
    # Error column.# noqa
    column: int


@dataclass
class AppManifestParsedProperties:
    """Parsed app manifest properties."""

    # Computed scope value# noqa
    scope: str


@dataclass
class LayoutViewport:
    """Layout viewport position and dimensions."""

    # Horizontal offset relative to the document (CSS pixels).# noqa
    page_x: int
    # Vertical offset relative to the document (CSS pixels).# noqa
    page_y: int
    # Width (CSS pixels), excludes scrollbar if present.# noqa
    client_width: int
    # Height (CSS pixels), excludes scrollbar if present.# noqa
    client_height: int


@dataclass
class VisualViewport:
    """Visual viewport position, dimensions, and scale."""

    # Horizontal offset relative to the layout viewport (CSS pixels).# noqa
    offset_x: float
    # Vertical offset relative to the layout viewport (CSS pixels).# noqa
    offset_y: float
    # Horizontal offset relative to the document (CSS pixels).# noqa
    page_x: float
    # Vertical offset relative to the document (CSS pixels).# noqa
    page_y: float
    # Width (CSS pixels), excludes scrollbar if present.# noqa
    client_width: float
    # Height (CSS pixels), excludes scrollbar if present.# noqa
    client_height: float
    # Scale relative to the ideal viewport (size at width=device-width).# noqa
    scale: float
    # Page zoom factor (CSS to device independent pixels ratio).# noqa
    zoom: typing.Optional[float]


@dataclass
class Viewport:
    """Viewport for capturing screenshot."""

    # X offset in device independent pixels (dip).# noqa
    x: float
    # Y offset in device independent pixels (dip).# noqa
    y: float
    # Rectangle width in device independent pixels (dip).# noqa
    width: float
    # Rectangle height in device independent pixels (dip).# noqa
    height: float
    # Page scale factor.# noqa
    scale: float


@dataclass
class FontFamilies:
    """Generic font families collection."""

    # The standard font-family.# noqa
    standard: typing.Optional[str]
    # The fixed font-family.# noqa
    fixed: typing.Optional[str]
    # The serif font-family.# noqa
    serif: typing.Optional[str]
    # The sansSerif font-family.# noqa
    sans_serif: typing.Optional[str]
    # The cursive font-family.# noqa
    cursive: typing.Optional[str]
    # The fantasy font-family.# noqa
    fantasy: typing.Optional[str]
    # The math font-family.# noqa
    math: typing.Optional[str]


@dataclass
class ScriptFontFamilies:
    """Font families collection for a script."""

    # Name of the script which these font families are defined for.# noqa
    script: str
    # Generic font families collection for the script.# noqa
    font_families: FontFamilies


@dataclass
class FontSizes:
    """Default font sizes."""

    # Default standard font size.# noqa
    standard: typing.Optional[int]
    # Default fixed font size.# noqa
    fixed: typing.Optional[int]


class ClientNavigationReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    FORM_SUBMISSION_GET = "form_submission_get"
    FORM_SUBMISSION_POST = "form_submission_post"
    HTTP_HEADER_REFRESH = "http_header_refresh"
    SCRIPT_INITIATED = "script_initiated"
    META_TAG_REFRESH = "meta_tag_refresh"
    PAGE_BLOCK_INTERSTITIAL = "page_block_interstitial"
    RELOAD = "reload"
    ANCHOR_CLICK = "anchor_click"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ClientNavigationDisposition(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    CURRENT_TAB = "current_tab"
    NEW_TAB = "new_tab"
    NEW_WINDOW = "new_window"
    DOWNLOAD = "download"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class InstallabilityErrorArgument:
    """Description is missing from the devtools protocol document."""

    # Argument name (e.g. name:'minimum-icon-size-in-pixels').# noqa
    name: str
    # Argument value (e.g. value:'64').# noqa
    value: str


@dataclass
class InstallabilityError:
    """The installability error."""

    # The error id (e.g. 'manifest-missing-suitable-icon').# noqa
    error_id: str
    # The list of error arguments (e.g. {name:'minimum-icon-size-in-pixels',value:'64'}).# noqa
    error_arguments: InstallabilityErrorArgument


class ReferrerPolicy(str, enum.Enum):
    """The referring-policy used for the navigation."""

    NO_REFERRER = "no_referrer"
    NO_REFERRER_WHEN_DOWNGRADE = "no_referrer_when_downgrade"
    ORIGIN = "origin"
    ORIGIN_WHEN_CROSS_ORIGIN = "origin_when_cross_origin"
    SAME_ORIGIN = "same_origin"
    STRICT_ORIGIN = "strict_origin"
    STRICT_ORIGIN_WHEN_CROSS_ORIGIN = "strict_origin_when_cross_origin"
    UNSAFE_URL = "unsafe_url"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class CompilationCacheParams:
    """Per-script compilation cache parameters for `Page.produceCompilationCache`"""

    # The URL of the script to produce a compilation cache entry for.# noqa
    url: str
    # A hint to the backend whether eager compilation is recommended. (theactual compilation mode used is upon backend discretion).# noqa
    eager: typing.Optional[bool]


class AutoResponseMode(str, enum.Enum):
    """Enum of possible auto-reponse for permisison / prompt dialogs."""

    NONE = "none"
    AUTO_ACCEPT = "auto_accept"
    AUTO_REJECT = "auto_reject"
    AUTO_OPT_OUT = "auto_opt_out"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class NavigationType(str, enum.Enum):
    """The type of a frameNavigated event."""

    _NAVIGATION = "navigation"
    _BACK_FORWARD_CACHE_RESTORE = "back_forward_cache_restore"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class BackForwardCacheNotRestoredReason(str, enum.Enum):
    """List of not restored reasons for back-forward cache."""

    _NOT_PRIMARY_MAIN_FRAME = "not_primary_main_frame"
    _BACK_FORWARD_CACHE_DISABLED = "back_forward_cache_disabled"
    _RELATED_ACTIVE_CONTENTS_EXIST = "related_active_contents_exist"
    _H_T_T_P_STATUS_NOT_O_K = "http_status_not_ok"
    _SCHEME_NOT_H_T_T_P_OR_H_T_T_P_S = "scheme_not_http_or_https"
    _LOADING = "loading"
    _WAS_GRANTED_MEDIA_ACCESS = "was_granted_media_access"
    _DISABLE_FOR_RENDER_FRAME_HOST_CALLED = "disable_for_render_frame_host_called"
    _DOMAIN_NOT_ALLOWED = "domain_not_allowed"
    _H_T_T_P_METHOD_NOT_G_E_T = "http_method_not_get"
    _SUBFRAME_IS_NAVIGATING = "subframe_is_navigating"
    _TIMEOUT = "timeout"
    _CACHE_LIMIT = "cache_limit"
    _JAVA_SCRIPT_EXECUTION = "java_script_execution"
    _RENDERER_PROCESS_KILLED = "renderer_process_killed"
    _RENDERER_PROCESS_CRASHED = "renderer_process_crashed"
    _SCHEDULER_TRACKED_FEATURE_USED = "scheduler_tracked_feature_used"
    _CONFLICTING_BROWSING_INSTANCE = "conflicting_browsing_instance"
    _CACHE_FLUSHED = "cache_flushed"
    _SERVICE_WORKER_VERSION_ACTIVATION = "service_worker_version_activation"
    _SESSION_RESTORED = "session_restored"
    _SERVICE_WORKER_POST_MESSAGE = "service_worker_post_message"
    _ENTERED_BACK_FORWARD_CACHE_BEFORE_SERVICE_WORKER_HOST_ADDED = (
        "entered_back_forward_cache_before_service_worker_host_added"
    )
    _RENDER_FRAME_HOST_REUSED__SAME_SITE = "render_frame_host_reused__same_site"
    _RENDER_FRAME_HOST_REUSED__CROSS_SITE = "render_frame_host_reused__cross_site"
    _SERVICE_WORKER_CLAIM = "service_worker_claim"
    _IGNORE_EVENT_AND_EVICT = "ignore_event_and_evict"
    _HAVE_INNER_CONTENTS = "have_inner_contents"
    _TIMEOUT_PUTTING_IN_CACHE = "timeout_putting_in_cache"
    _BACK_FORWARD_CACHE_DISABLED_BY_LOW_MEMORY = "back_forward_cache_disabled_by_low_memory"
    _BACK_FORWARD_CACHE_DISABLED_BY_COMMAND_LINE = "back_forward_cache_disabled_by_command_line"
    _NETWORK_REQUEST_DATAPIPE_DRAINED_AS_BYTES_CONSUMER = "network_request_datapipe_drained_as_bytes_consumer"
    _NETWORK_REQUEST_REDIRECTED = "network_request_redirected"
    _NETWORK_REQUEST_TIMEOUT = "network_request_timeout"
    _NETWORK_EXCEEDS_BUFFER_LIMIT = "network_exceeds_buffer_limit"
    _NAVIGATION_CANCELLED_WHILE_RESTORING = "navigation_cancelled_while_restoring"
    _NOT_MOST_RECENT_NAVIGATION_ENTRY = "not_most_recent_navigation_entry"
    _BACK_FORWARD_CACHE_DISABLED_FOR_PRERENDER = "back_forward_cache_disabled_for_prerender"
    _USER_AGENT_OVERRIDE_DIFFERS = "user_agent_override_differs"
    _FOREGROUND_CACHE_LIMIT = "foreground_cache_limit"
    _BROWSING_INSTANCE_NOT_SWAPPED = "browsing_instance_not_swapped"
    _BACK_FORWARD_CACHE_DISABLED_FOR_DELEGATE = "back_forward_cache_disabled_for_delegate"
    _UNLOAD_HANDLER_EXISTS_IN_MAIN_FRAME = "unload_handler_exists_in_main_frame"
    _UNLOAD_HANDLER_EXISTS_IN_SUB_FRAME = "unload_handler_exists_in_sub_frame"
    _SERVICE_WORKER_UNREGISTRATION = "service_worker_unregistration"
    _CACHE_CONTROL_NO_STORE = "cache_control_no_store"
    _CACHE_CONTROL_NO_STORE_COOKIE_MODIFIED = "cache_control_no_store_cookie_modified"
    _CACHE_CONTROL_NO_STORE_H_T_T_P_ONLY_COOKIE_MODIFIED = "cache_control_no_store_http_only_cookie_modified"
    _NO_RESPONSE_HEAD = "no_response_head"
    _UNKNOWN = "unknown"
    _ACTIVATION_NAVIGATIONS_DISALLOWED_FOR_BUG1234857 = "activation_navigations_disallowed_for_bug1234857"
    _ERROR_DOCUMENT = "error_document"
    _FENCED_FRAMES_EMBEDDER = "fenced_frames_embedder"
    _WEB_SOCKET = "web_socket"
    _WEB_TRANSPORT = "web_transport"
    _WEB_R_T_C = "web_rtc"
    _MAIN_RESOURCE_HAS_CACHE_CONTROL_NO_STORE = "main_resource_has_cache_control_no_store"
    _MAIN_RESOURCE_HAS_CACHE_CONTROL_NO_CACHE = "main_resource_has_cache_control_no_cache"
    _SUBRESOURCE_HAS_CACHE_CONTROL_NO_STORE = "subresource_has_cache_control_no_store"
    _SUBRESOURCE_HAS_CACHE_CONTROL_NO_CACHE = "subresource_has_cache_control_no_cache"
    _CONTAINS_PLUGINS = "contains_plugins"
    _DOCUMENT_LOADED = "document_loaded"
    _DEDICATED_WORKER_OR_WORKLET = "dedicated_worker_or_worklet"
    _OUTSTANDING_NETWORK_REQUEST_OTHERS = "outstanding_network_request_others"
    _OUTSTANDING_INDEXED_D_B_TRANSACTION = "outstanding_indexed_db_transaction"
    _REQUESTED_M_I_D_I_PERMISSION = "requested_midi_permission"
    _REQUESTED_AUDIO_CAPTURE_PERMISSION = "requested_audio_capture_permission"
    _REQUESTED_VIDEO_CAPTURE_PERMISSION = "requested_video_capture_permission"
    _REQUESTED_BACK_FORWARD_CACHE_BLOCKED_SENSORS = "requested_back_forward_cache_blocked_sensors"
    _REQUESTED_BACKGROUND_WORK_PERMISSION = "requested_background_work_permission"
    _BROADCAST_CHANNEL = "broadcast_channel"
    _INDEXED_D_B_CONNECTION = "indexed_db_connection"
    _WEB_X_R = "web_xr"
    _SHARED_WORKER = "shared_worker"
    _WEB_LOCKS = "web_locks"
    _WEB_H_I_D = "web_hid"
    _WEB_SHARE = "web_share"
    _REQUESTED_STORAGE_ACCESS_GRANT = "requested_storage_access_grant"
    _WEB_NFC = "web_nfc"
    _OUTSTANDING_NETWORK_REQUEST_FETCH = "outstanding_network_request_fetch"
    _OUTSTANDING_NETWORK_REQUEST_X_H_R = "outstanding_network_request_xhr"
    _APP_BANNER = "app_banner"
    _PRINTING = "printing"
    _WEB_DATABASE = "web_database"
    _PICTURE_IN_PICTURE = "picture_in_picture"
    _PORTAL = "portal"
    _SPEECH_RECOGNIZER = "speech_recognizer"
    _IDLE_MANAGER = "idle_manager"
    _PAYMENT_MANAGER = "payment_manager"
    _SPEECH_SYNTHESIS = "speech_synthesis"
    _KEYBOARD_LOCK = "keyboard_lock"
    _WEB_O_T_P_SERVICE = "web_otp_service"
    _OUTSTANDING_NETWORK_REQUEST_DIRECT_SOCKET = "outstanding_network_request_direct_socket"
    _INJECTED_JAVASCRIPT = "injected_javascript"
    _INJECTED_STYLE_SHEET = "injected_style_sheet"
    _KEEPALIVE_REQUEST = "keepalive_request"
    _INDEXED_D_B_EVENT = "indexed_db_event"
    _DUMMY = "dummy"
    _AUTHORIZATION_HEADER = "authorization_header"
    _CONTENT_SECURITY_HANDLER = "content_security_handler"
    _CONTENT_WEB_AUTHENTICATION_A_P_I = "content_web_authentication_api"
    _CONTENT_FILE_CHOOSER = "content_file_chooser"
    _CONTENT_SERIAL = "content_serial"
    _CONTENT_FILE_SYSTEM_ACCESS = "content_file_system_access"
    _CONTENT_MEDIA_DEVICES_DISPATCHER_HOST = "content_media_devices_dispatcher_host"
    _CONTENT_WEB_BLUETOOTH = "content_web_bluetooth"
    _CONTENT_WEB_U_S_B = "content_web_usb"
    _CONTENT_MEDIA_SESSION_SERVICE = "content_media_session_service"
    _CONTENT_SCREEN_READER = "content_screen_reader"
    _EMBEDDER_POPUP_BLOCKER_TAB_HELPER = "embedder_popup_blocker_tab_helper"
    _EMBEDDER_SAFE_BROWSING_TRIGGERED_POPUP_BLOCKER = "embedder_safe_browsing_triggered_popup_blocker"
    _EMBEDDER_SAFE_BROWSING_THREAT_DETAILS = "embedder_safe_browsing_threat_details"
    _EMBEDDER_APP_BANNER_MANAGER = "embedder_app_banner_manager"
    _EMBEDDER_DOM_DISTILLER_VIEWER_SOURCE = "embedder_dom_distiller_viewer_source"
    _EMBEDDER_DOM_DISTILLER_SELF_DELETING_REQUEST_DELEGATE = "embedder_dom_distiller_self_deleting_request_delegate"
    _EMBEDDER_OOM_INTERVENTION_TAB_HELPER = "embedder_oom_intervention_tab_helper"
    _EMBEDDER_OFFLINE_PAGE = "embedder_offline_page"
    _EMBEDDER_CHROME_PASSWORD_MANAGER_CLIENT_BIND_CREDENTIAL_MANAGER = (
        "embedder_chrome_password_manager_client_bind_credential_manager"
    )
    _EMBEDDER_PERMISSION_REQUEST_MANAGER = "embedder_permission_request_manager"
    _EMBEDDER_MODAL_DIALOG = "embedder_modal_dialog"
    _EMBEDDER_EXTENSIONS = "embedder_extensions"
    _EMBEDDER_EXTENSION_MESSAGING = "embedder_extension_messaging"
    _EMBEDDER_EXTENSION_MESSAGING_FOR_OPEN_PORT = "embedder_extension_messaging_for_open_port"
    _EMBEDDER_EXTENSION_SENT_MESSAGE_TO_CACHED_FRAME = "embedder_extension_sent_message_to_cached_frame"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class BackForwardCacheNotRestoredReasonType(str, enum.Enum):
    """Types of not restored reasons for back-forward cache."""

    _SUPPORT_PENDING = "support_pending"
    _PAGE_SUPPORT_NEEDED = "page_support_needed"
    _CIRCUMSTANTIAL = "circumstantial"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class BackForwardCacheNotRestoredExplanation:
    """Description is missing from the devtools protocol document."""

    # Type of the reason# noqa
    type: BackForwardCacheNotRestoredReasonType
    # Not restored reason# noqa
    reason: BackForwardCacheNotRestoredReason
    # Context associated with the reason. The meaning of this context isdependent on the reason: - EmbedderExtensionSentMessageToCachedFrame: theextension ID.# noqa
    context: typing.Optional[str]


@dataclass
class BackForwardCacheNotRestoredExplanationTree:
    """Description is missing from the devtools protocol document."""

    # URL of each frame# noqa
    url: str
    # Not restored reasons of each frame# noqa
    explanations: BackForwardCacheNotRestoredExplanation
    # Array of children frame# noqa
    children: BackForwardCacheNotRestoredExplanationTree


@dataclass
@memoize_event("Page.domContentEventFired")
class DomContentEventFired:
    """Description is missing from the devtools protocol document."""

    timestamp: network.MonotonicTime


@dataclass
@memoize_event("Page.fileChooserOpened")
class FileChooserOpened:
    """Emitted only when `page.interceptFileChooser` is enabled."""

    frame_id: FrameId
    mode: typing.Literal["select_single", "select_multiple"]
    backend_node_id: typing.Optional[dom.BackendNodeId]


@dataclass
@memoize_event("Page.frameAttached")
class FrameAttached:
    """Fired when frame has been attached to its parent."""

    frame_id: FrameId
    parent_frame_id: FrameId
    stack: typing.Optional[runtime.StackTrace]


@dataclass
@memoize_event("Page.frameClearedScheduledNavigation")
class FrameClearedScheduledNavigation:
    """Fired when frame no longer has a scheduled navigation."""

    frame_id: FrameId


@dataclass
@memoize_event("Page.frameDetached")
class FrameDetached:
    """Fired when frame has been detached from its parent."""

    frame_id: FrameId
    reason: typing.Literal["remove", "swap"]


@dataclass
@memoize_event("Page.frameNavigated")
class FrameNavigated:
    """Fired once navigation of the frame has completed.

    Frame is now associated with the new loader.
    """

    frame: Frame
    type: NavigationType


@dataclass
@memoize_event("Page.documentOpened")
class DocumentOpened:
    """Fired when opening document to write to."""

    frame: Frame


@dataclass
@memoize_event("Page.frameResized")
class FrameResized:
    """Description is missing from the devtools protocol document."""


@dataclass
@memoize_event("Page.frameRequestedNavigation")
class FrameRequestedNavigation:
    """Fired when a renderer-initiated navigation is requested.

    Navigation may still be cancelled after the event is issued.
    """

    frame_id: FrameId
    reason: ClientNavigationReason
    url: str
    disposition: ClientNavigationDisposition


@dataclass
@memoize_event("Page.frameScheduledNavigation")
class FrameScheduledNavigation:
    """Fired when frame schedules a potential navigation."""

    frame_id: FrameId
    delay: float
    reason: ClientNavigationReason
    url: str


@dataclass
@memoize_event("Page.frameStartedLoading")
class FrameStartedLoading:
    """Fired when frame has started loading."""

    frame_id: FrameId


@dataclass
@memoize_event("Page.frameStoppedLoading")
class FrameStoppedLoading:
    """Fired when frame has stopped loading."""

    frame_id: FrameId


@dataclass
@memoize_event("Page.downloadWillBegin")
class DownloadWillBegin:
    """Fired when page is about to start a download.

    Deprecated. Use Browser.downloadWillBegin instead.
    """

    frame_id: FrameId
    guid: str
    url: str
    suggested_filename: str


@dataclass
@memoize_event("Page.downloadProgress")
class DownloadProgress:
    """Fired when download makes progress.

    Last call has |done| == true. Deprecated. Use Browser.downloadProgress instead.
    """

    guid: str
    total_bytes: float
    received_bytes: float
    state: typing.Literal["in_progress", "completed", "canceled"]


@dataclass
@memoize_event("Page.interstitialHidden")
class InterstitialHidden:
    """Fired when interstitial page was hidden."""


@dataclass
@memoize_event("Page.interstitialShown")
class InterstitialShown:
    """Fired when interstitial page was shown."""


@dataclass
@memoize_event("Page.javascriptDialogClosed")
class JavascriptDialogClosed:
    """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been closed."""

    result: bool
    user_input: str


@dataclass
@memoize_event("Page.javascriptDialogOpening")
class JavascriptDialogOpening:
    """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to open."""

    url: str
    message: str
    type: DialogType
    has_browser_handler: bool
    default_prompt: typing.Optional[str]


@dataclass
@memoize_event("Page.lifecycleEvent")
class LifecycleEvent:
    """Fired for top level page lifecycle events such as navigation, load, paint, etc."""

    frame_id: FrameId
    loader_id: network.LoaderId
    name: str
    timestamp: network.MonotonicTime


@dataclass
@memoize_event("Page.backForwardCacheNotUsed")
class BackForwardCacheNotUsed:
    """Fired for failed bfcache history navigations if BackForwardCache feature is enabled.

    Do not assume any ordering with the Page.frameNavigated event. This event is fired only for main-frame history
    navigation where the document changes (non-same-document navigations), when bfcache navigation fails.
    """

    loader_id: network.LoaderId
    frame_id: FrameId
    not_restored_explanations: typing.List[BackForwardCacheNotRestoredExplanation]
    not_restored_explanations_tree: typing.Optional[BackForwardCacheNotRestoredExplanationTree]


@dataclass
@memoize_event("Page.loadEventFired")
class LoadEventFired:
    """Description is missing from the devtools protocol document."""

    timestamp: network.MonotonicTime


@dataclass
@memoize_event("Page.navigatedWithinDocument")
class NavigatedWithinDocument:
    """Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation."""

    frame_id: FrameId
    url: str


@dataclass
@memoize_event("Page.screencastFrame")
class ScreencastFrame:
    """Compressed image data requested by the `startScreencast`."""

    data: str
    metadata: ScreencastFrameMetadata
    session_id: int


@dataclass
@memoize_event("Page.screencastVisibilityChanged")
class ScreencastVisibilityChanged:
    """Fired when the page with currently enabled screencast was shown or hidden `."""

    visible: bool


@dataclass
@memoize_event("Page.windowOpen")
class WindowOpen:
    """Fired when a new window is going to be opened, via window.open(), link click, form submission, etc."""

    url: str
    window_name: str
    window_features: typing.List[str]
    user_gesture: bool


@dataclass
@memoize_event("Page.compilationCacheProduced")
class CompilationCacheProduced:
    """Issued for every compilation cache generated.

    Is only available if Page.setGenerateCompilationCache is enabled.
    """

    url: str
    data: str


async def add_script_to_evaluate_on_load() -> None:
    """Deprecated, please use addScriptToEvaluateOnNewDocument instead.

    # noqa
    """
    ...


async def add_script_to_evaluate_on_new_document() -> None:
    """Evaluates given script in every frame upon creation (before loading frame's scripts).

    # noqa
    """
    ...


async def bring_to_front() -> None:
    """Brings page to front (activates tab).

    # noqa
    """
    ...


async def capture_screenshot() -> None:
    """Capture page screenshot.

    # noqa
    """
    ...


async def capture_snapshot() -> None:
    """Returns a snapshot of the page as a string.

    For MHTML format, the serialization includes iframes, shadow DOM, external resources, and element-inline styles. #
    noqa
    """
    ...


async def clear_device_metrics_override() -> None:
    """Clears the overridden device metrics.

    # noqa
    """
    ...


async def clear_device_orientation_override() -> None:
    """Clears the overridden Device Orientation.

    # noqa
    """
    ...


async def clear_geolocation_override() -> None:
    """Clears the overridden Geolocation Position and Error.

    # noqa
    """
    ...


async def create_isolated_world() -> None:
    """Creates an isolated world for the given frame.

    # noqa
    """
    ...


async def delete_cookie() -> None:
    """Deletes browser cookie with given name, domain and path.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables page domain notifications.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables page domain notifications.

    # noqa
    """
    ...


async def get_app_manifest() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def get_installability_errors() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def get_manifest_icons() -> None:
    """Deprecated because it's not guaranteed that the returned icon is in fact the one used for PWA installation.

    # noqa
    """
    ...


async def get_app_id() -> None:
    """Returns the unique (PWA) app id.

    Only returns values if the feature flag 'WebAppEnableManifestId' is enabled # noqa
    """
    ...


async def get_ad_script_id() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def get_cookies() -> None:
    """Returns all browser cookies for the page and all of its subframes.

    Depending on the backend support, will return detailed cookie information in the `cookies` field. # noqa
    """
    ...


async def get_frame_tree() -> None:
    """Returns present frame tree structure.

    # noqa
    """
    ...


async def get_layout_metrics() -> None:
    """Returns metrics relating to the layouting of the page, such as viewport bounds/scale.

    # noqa
    """
    ...


async def get_navigation_history() -> None:
    """Returns navigation history for the current page.

    # noqa
    """
    ...


async def reset_navigation_history() -> None:
    """Resets navigation history for the current page.

    # noqa
    """
    ...


async def get_resource_content() -> None:
    """Returns content of the given resource.

    # noqa
    """
    ...


async def get_resource_tree() -> None:
    """Returns present frame / resource tree structure.

    # noqa
    """
    ...


async def handle_java_script_dialog() -> None:
    """Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).

    # noqa
    """
    ...


async def navigate() -> None:
    """Navigates current page to the given URL.

    # noqa
    """
    ...


async def navigate_to_history_entry() -> None:
    """Navigates current page to the given history entry.

    # noqa
    """
    ...


async def print_to_pdf() -> None:
    """Print page as PDF.

    # noqa
    """
    ...


async def reload() -> None:
    """Reloads given page optionally ignoring the cache.

    # noqa
    """
    ...


async def remove_script_to_evaluate_on_load() -> None:
    """Deprecated, please use removeScriptToEvaluateOnNewDocument instead.

    # noqa
    """
    ...


async def remove_script_to_evaluate_on_new_document() -> None:
    """Removes given script from the list.

    # noqa
    """
    ...


async def screencast_frame_ack() -> None:
    """Acknowledges that a screencast frame has been received by the frontend.

    # noqa
    """
    ...


async def search_in_resource() -> None:
    """Searches for given string in resource content.

    # noqa
    """
    ...


async def set_ad_blocking_enabled() -> None:
    """Enable Chrome's experimental ad filter on all sites.

    # noqa
    """
    ...


async def set_bypass_csp() -> None:
    """Enable page Content Security Policy by-passing.

    # noqa
    """
    ...


async def get_permissions_policy_state() -> None:
    """Get Permissions Policy state on given frame.

    # noqa
    """
    ...


async def get_origin_trials() -> None:
    """Get Origin Trials on given frame.

    # noqa
    """
    ...


async def set_device_metrics_override() -> None:
    """Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth,
    window.innerHeight, and "device-width"/"device-height"-related CSS media query results).

    # noqa
    """
    ...


async def set_device_orientation_override() -> None:
    """Overrides the Device Orientation.

    # noqa
    """
    ...


async def set_font_families() -> None:
    """Set generic font families.

    # noqa
    """
    ...


async def set_font_sizes() -> None:
    """Set default font sizes.

    # noqa
    """
    ...


async def set_document_content() -> None:
    """Sets given markup as the document's HTML.

    # noqa
    """
    ...


async def set_download_behavior() -> None:
    """Set the behavior when downloading a file.

    # noqa
    """
    ...


async def set_geolocation_override() -> None:
    """Overrides the Geolocation Position or Error.

    Omitting any of the parameters emulates position unavailable. # noqa
    """
    ...


async def set_lifecycle_events_enabled() -> None:
    """Controls whether page will emit lifecycle events.

    # noqa
    """
    ...


async def set_touch_emulation_enabled() -> None:
    """Toggles mouse event-based touch event emulation.

    # noqa
    """
    ...


async def start_screencast() -> None:
    """Starts sending each frame using the `screencastFrame` event.

    # noqa
    """
    ...


async def stop_loading() -> None:
    """Force the page stop all navigations and pending resource fetches.

    # noqa
    """
    ...


async def crash() -> None:
    """Crashes renderer on the IO thread, generates minidumps.

    # noqa
    """
    ...


async def close() -> None:
    """Tries to close page, running its beforeunload hooks, if any.

    # noqa
    """
    ...


async def set_web_lifecycle_state() -> None:
    """Tries to update the web lifecycle state of the page.

    It will transition the page to the given state according to:
    https://github.com/WICG/web-lifecycle/ # noqa
    """
    ...


async def stop_screencast() -> None:
    """Stops sending each frame in the `screencastFrame`.

    # noqa
    """
    ...


async def produce_compilation_cache() -> None:
    """Requests backend to produce compilation cache for the specified scripts.

    `scripts` are appeneded to the list of scripts for which the cache would be produced. The list may be reset during
    page navigation. When script with a matching URL is encountered, the cache is optionally produced upon backend
    discretion, based on internal heuristics. See also: `Page.compilationCacheProduced`. # noqa
    """
    ...


async def add_compilation_cache() -> None:
    """Seeds compilation cache for given url.

    Compilation cache does not survive cross-process navigation. # noqa
    """
    ...


async def clear_compilation_cache() -> None:
    """Clears seeded compilation cache.

    # noqa
    """
    ...


async def set_spc_transaction_mode() -> None:
    """Sets the Secure Payment Confirmation transaction mode.

    https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode # noqa
    """
    ...


async def set_rph_registration_mode() -> None:
    """Extensions for Custom Handlers API:

    https://html.spec.whatwg.org/multipage/system-state.html#rph-automation # noqa
    """
    ...


async def generate_test_report() -> None:
    """Generates a report for testing.

    # noqa
    """
    ...


async def wait_for_debugger() -> None:
    """Pauses page execution.

    Can be resumed using generic Runtime.runIfWaitingForDebugger. # noqa
    """
    ...


async def set_intercept_file_chooser_dialog() -> None:
    """Intercept file chooser requests and transfer control to protocol clients.

    When file chooser interception is enabled, native file chooser dialog is not shown. Instead, a protocol event
    `Page.fileChooserOpened` is emitted. # noqa
    """
    ...
