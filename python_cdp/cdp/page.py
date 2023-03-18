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

    PARENTISAD = "ParentIsAd"
    CREATEDBYADSCRIPT = "CreatedByAdScript"
    MATCHEDBLOCKINGRULE = "MatchedBlockingRule"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class AdFrameStatus:
    """Indicates whether a frame has been identified as an ad and why."""

    #: Description is missing from the devtools protocol document.# noqa
    ad_frame_type: AdFrameType
    #: Description is missing from the devtools protocol document.# noqa
    explanations: typing.Optional[typing.List[AdFrameExplanation]] = None


@dataclass
class AdScriptId:
    """Identifies the bottom-most script which caused the frame to be labelled
    as an ad."""

    #: Script Id of the bottom-most script which caused the frame to be labelledas an ad.# noqa
    script_id: runtime.ScriptId
    #: Id of adScriptId's debugger.# noqa
    debugger_id: runtime.UniqueDebuggerId


class SecureContextType(str, enum.Enum):
    """Indicates whether the frame is a secure context and why it is the
    case."""

    SECURE = "Secure"
    SECURELOCALHOST = "SecureLocalhost"
    INSECURESCHEME = "InsecureScheme"
    INSECUREANCESTOR = "InsecureAncestor"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CrossOriginIsolatedContextType(str, enum.Enum):
    """Indicates whether the frame is cross-origin isolated and why it is the
    case."""

    ISOLATED = "Isolated"
    NOTISOLATED = "NotIsolated"
    NOTISOLATEDFEATUREDISABLED = "NotIsolatedFeatureDisabled"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class GatedAPIFeatures(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    SHAREDARRAYBUFFERS = "SharedArrayBuffers"
    SHAREDARRAYBUFFERSTRANSFERALLOWED = "SharedArrayBuffersTransferAllowed"
    PERFORMANCEMEASUREMEMORY = "PerformanceMeasureMemory"
    PERFORMANCEPROFILE = "PerformanceProfile"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PermissionsPolicyFeature(str, enum.Enum):
    """All Permissions Policy features.

    This enum should match the one defined
    in third_party/blink/renderer/core/permissions_policy/permissions_policy_features.json5.
    """

    ACCELEROMETER = "accelerometer"
    AMBIENT_LIGHT_SENSOR = "ambient_light_sensor"
    ATTRIBUTION_REPORTING = "attribution_reporting"
    AUTOPLAY = "autoplay"
    BLUETOOTH = "bluetooth"
    BROWSING_TOPICS = "browsing_topics"
    CAMERA = "camera"
    CH_DPR = "ch_dpr"
    CH_DEVICE_MEMORY = "ch_device_memory"
    CH_DOWNLINK = "ch_downlink"
    CH_ECT = "ch_ect"
    CH_PREFERS_COLOR_SCHEME = "ch_prefers_color_scheme"
    CH_PREFERS_REDUCED_MOTION = "ch_prefers_reduced_motion"
    CH_RTT = "ch_rtt"
    CH_SAVE_DATA = "ch_save_data"
    CH_UA = "ch_ua"
    CH_UA_ARCH = "ch_ua_arch"
    CH_UA_BITNESS = "ch_ua_bitness"
    CH_UA_PLATFORM = "ch_ua_platform"
    CH_UA_MODEL = "ch_ua_model"
    CH_UA_MOBILE = "ch_ua_mobile"
    CH_UA_FULL = "ch_ua_full"
    CH_UA_FULL_VERSION = "ch_ua_full_version"
    CH_UA_FULL_VERSION_LIST = "ch_ua_full_version_list"
    CH_UA_PLATFORM_VERSION = "ch_ua_platform_version"
    CH_UA_REDUCED = "ch_ua_reduced"
    CH_UA_WOW64 = "ch_ua_wow64"
    CH_VIEWPORT_HEIGHT = "ch_viewport_height"
    CH_VIEWPORT_WIDTH = "ch_viewport_width"
    CH_WIDTH = "ch_width"
    CLIPBOARD_READ = "clipboard_read"
    CLIPBOARD_WRITE = "clipboard_write"
    COMPUTE_PRESSURE = "compute_pressure"
    CROSS_ORIGIN_ISOLATED = "cross_origin_isolated"
    DIRECT_SOCKETS = "direct_sockets"
    DISPLAY_CAPTURE = "display_capture"
    DOCUMENT_DOMAIN = "document_domain"
    ENCRYPTED_MEDIA = "encrypted_media"
    EXECUTION_WHILE_OUT_OF_VIEWPORT = "execution_while_out_of_viewport"
    EXECUTION_WHILE_NOT_RENDERED = "execution_while_not_rendered"
    FOCUS_WITHOUT_USER_ACTIVATION = "focus_without_user_activation"
    FULLSCREEN = "fullscreen"
    FROBULATE = "frobulate"
    GAMEPAD = "gamepad"
    GEOLOCATION = "geolocation"
    GYROSCOPE = "gyroscope"
    HID = "hid"
    IDENTITY_CREDENTIALS_GET = "identity_credentials_get"
    IDLE_DETECTION = "idle_detection"
    INTEREST_COHORT = "interest_cohort"
    JOIN_AD_INTEREST_GROUP = "join_ad_interest_group"
    KEYBOARD_MAP = "keyboard_map"
    LOCAL_FONTS = "local_fonts"
    MAGNETOMETER = "magnetometer"
    MICROPHONE = "microphone"
    MIDI = "midi"
    OTP_CREDENTIALS = "otp_credentials"
    PAYMENT = "payment"
    PICTURE_IN_PICTURE = "picture_in_picture"
    PRIVATE_AGGREGATION = "private_aggregation"
    PUBLICKEY_CREDENTIALS_GET = "publickey_credentials_get"
    RUN_AD_AUCTION = "run_ad_auction"
    SCREEN_WAKE_LOCK = "screen_wake_lock"
    SERIAL = "serial"
    SHARED_AUTOFILL = "shared_autofill"
    SHARED_STORAGE = "shared_storage"
    SHARED_STORAGE_SELECT_URL = "shared_storage_select_url"
    SMART_CARD = "smart_card"
    STORAGE_ACCESS = "storage_access"
    SYNC_XHR = "sync_xhr"
    TRUST_TOKEN_REDEMPTION = "trust_token_redemption"
    UNLOAD = "unload"
    USB = "usb"
    VERTICAL_SCROLL = "vertical_scroll"
    WEB_SHARE = "web_share"
    WINDOW_MANAGEMENT = "window_management"
    WINDOW_PLACEMENT = "window_placement"
    XR_SPATIAL_TRACKING = "xr_spatial_tracking"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class PermissionsPolicyBlockReason(str, enum.Enum):
    """Reason for a permissions policy feature to be disabled."""

    HEADER = "Header"
    IFRAMEATTRIBUTE = "IframeAttribute"
    INFENCEDFRAMETREE = "InFencedFrameTree"
    INISOLATEDAPP = "InIsolatedApp"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class PermissionsPolicyBlockLocator:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    frame_id: FrameId
    #: Description is missing from the devtools protocol document.# noqa
    block_reason: PermissionsPolicyBlockReason


@dataclass
class PermissionsPolicyFeatureState:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    feature: PermissionsPolicyFeature
    #: Description is missing from the devtools protocol document.# noqa
    allowed: bool
    #: Description is missing from the devtools protocol document.# noqa
    locator: typing.Optional[PermissionsPolicyBlockLocator] = None


class OriginTrialTokenStatus(str, enum.Enum):
    """Origin Trial(https://www.chromium.org/blink/origin-trials) support.

    Status for an Origin Trial token.
    """

    SUCCESS = "Success"
    NOTSUPPORTED = "NotSupported"
    INSECURE = "Insecure"
    EXPIRED = "Expired"
    WRONGORIGIN = "WrongOrigin"
    INVALIDSIGNATURE = "InvalidSignature"
    MALFORMED = "Malformed"
    WRONGVERSION = "WrongVersion"
    FEATUREDISABLED = "FeatureDisabled"
    TOKENDISABLED = "TokenDisabled"
    FEATUREDISABLEDFORUSER = "FeatureDisabledForUser"
    UNKNOWNTRIAL = "UnknownTrial"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class OriginTrialStatus(str, enum.Enum):
    """Status for an Origin Trial."""

    ENABLED = "Enabled"
    VALIDTOKENNOTPROVIDED = "ValidTokenNotProvided"
    OSNOTSUPPORTED = "OSNotSupported"
    TRIALNOTALLOWED = "TrialNotAllowed"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class OriginTrialUsageRestriction(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    NONE = "None"
    SUBSET = "Subset"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class OriginTrialToken:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    origin: str
    #: Description is missing from the devtools protocol document.# noqa
    match_sub_domains: bool
    #: Description is missing from the devtools protocol document.# noqa
    trial_name: str
    #: Description is missing from the devtools protocol document.# noqa
    expiry_time: network.TimeSinceEpoch
    #: Description is missing from the devtools protocol document.# noqa
    is_third_party: bool
    #: Description is missing from the devtools protocol document.# noqa
    usage_restriction: OriginTrialUsageRestriction


@dataclass
class OriginTrialTokenWithStatus:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    raw_token_text: str
    #: Description is missing from the devtools protocol document.# noqa
    status: OriginTrialTokenStatus
    #: `parsedToken` is present only when the token is extractable and parsable.# noqa
    parsed_token: typing.Optional[OriginTrialToken] = None


@dataclass
class OriginTrial:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    trial_name: str
    #: Description is missing from the devtools protocol document.# noqa
    status: OriginTrialStatus
    #: Description is missing from the devtools protocol document.# noqa
    tokens_with_status: OriginTrialTokenWithStatus


@dataclass
class Frame:
    """Information about the Frame on the page."""

    #: Frame unique identifier.# noqa
    id: FrameId
    #: Identifier of the loader associated with this frame.# noqa
    loader_id: network.LoaderId
    #: Frame document's URL without fragment.# noqa
    url: str
    #: Frame document's registered domain, taking the public suffixes list intoaccount. Extracted from the Frame's url. Example URLs:http://www.google.com/file.html -> "google.com"http://a.b.co.uk/file.html      -> "b.co.uk"# noqa
    domain_and_registry: str
    #: Frame document's security origin.# noqa
    security_origin: str
    #: Frame document's mimeType as determined by the browser.# noqa
    mime_type: str
    #: Indicates whether the main document is a secure context and explains whythat is the case.# noqa
    secure_context_type: SecureContextType
    #: Indicates whether this is a cross origin isolated context.# noqa
    cross_origin_isolated_context_type: CrossOriginIsolatedContextType
    #: Indicated which gated APIs / features are available.# noqa
    gated_api_features: GatedAPIFeatures
    #: Parent frame identifier.# noqa
    parent_id: typing.Optional[FrameId] = None
    #: Frame's name as specified in the tag.# noqa
    name: typing.Optional[str] = None
    #: Frame document's URL fragment including the '#'.# noqa
    url_fragment: typing.Optional[str] = None
    #: If the frame failed to load, this contains the URL that could not beloaded. Note that unlike url above, this URL may contain a fragment.# noqa
    unreachable_url: typing.Optional[str] = None
    #: Indicates whether this frame was tagged as an ad and why.# noqa
    ad_frame_status: typing.Optional[AdFrameStatus] = None


@dataclass
class FrameResource:
    """Information about the Resource on the page."""

    #: Resource URL.# noqa
    url: str
    #: Type of this resource.# noqa
    type: network.ResourceType
    #: Resource mimeType as determined by the browser.# noqa
    mime_type: str
    #: last-modified timestamp as reported by server.# noqa
    last_modified: typing.Optional[network.TimeSinceEpoch] = None
    #: Resource content size.# noqa
    content_size: typing.Optional[float] = None
    #: True if the resource failed to load.# noqa
    failed: typing.Optional[bool] = None
    #: True if the resource was canceled during loading.# noqa
    canceled: typing.Optional[bool] = None


@dataclass
class FrameResourceTree:
    """Information about the Frame hierarchy along with their cached
    resources."""

    #: Frame information for this tree item.# noqa
    frame: Frame
    #: Information about frame resources.# noqa
    resources: FrameResource
    #: Child frames.# noqa
    child_frames: typing.Optional[typing.List[FrameResourceTree]] = None


@dataclass
class FrameTree:
    """Information about the Frame hierarchy."""

    #: Frame information for this tree item.# noqa
    frame: Frame
    #: Child frames.# noqa
    child_frames: typing.Optional[typing.List[FrameTree]] = None


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

    #: Unique id of the navigation history entry.# noqa
    id: int
    #: URL of the navigation history entry.# noqa
    url: str
    #: URL that the user typed in the url bar.# noqa
    user_typed_url: str
    #: Title of the navigation history entry.# noqa
    title: str
    #: Transition type.# noqa
    transition_type: TransitionType


@dataclass
class ScreencastFrameMetadata:
    """Screencast frame metadata."""

    #: Top offset in DIP.# noqa
    offset_top: float
    #: Page scale factor.# noqa
    page_scale_factor: float
    #: Device screen width in DIP.# noqa
    device_width: float
    #: Device screen height in DIP.# noqa
    device_height: float
    #: Position of horizontal scroll in CSS pixels.# noqa
    scroll_offset_x: float
    #: Position of vertical scroll in CSS pixels.# noqa
    scroll_offset_y: float
    #: Frame swap timestamp.# noqa
    timestamp: typing.Optional[network.TimeSinceEpoch] = None


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

    #: Error message.# noqa
    message: str
    #: If criticial, this is a non-recoverable parse error.# noqa
    critical: int
    #: Error line.# noqa
    line: int
    #: Error column.# noqa
    column: int


@dataclass
class AppManifestParsedProperties:
    """Parsed app manifest properties."""

    #: Computed scope value# noqa
    scope: str


@dataclass
class LayoutViewport:
    """Layout viewport position and dimensions."""

    #: Horizontal offset relative to the document (CSS pixels).# noqa
    page_x: int
    #: Vertical offset relative to the document (CSS pixels).# noqa
    page_y: int
    #: Width (CSS pixels), excludes scrollbar if present.# noqa
    client_width: int
    #: Height (CSS pixels), excludes scrollbar if present.# noqa
    client_height: int


@dataclass
class VisualViewport:
    """Visual viewport position, dimensions, and scale."""

    #: Horizontal offset relative to the layout viewport (CSS pixels).# noqa
    offset_x: float
    #: Vertical offset relative to the layout viewport (CSS pixels).# noqa
    offset_y: float
    #: Horizontal offset relative to the document (CSS pixels).# noqa
    page_x: float
    #: Vertical offset relative to the document (CSS pixels).# noqa
    page_y: float
    #: Width (CSS pixels), excludes scrollbar if present.# noqa
    client_width: float
    #: Height (CSS pixels), excludes scrollbar if present.# noqa
    client_height: float
    #: Scale relative to the ideal viewport (size at width=device-width).# noqa
    scale: float
    #: Page zoom factor (CSS to device independent pixels ratio).# noqa
    zoom: typing.Optional[float] = None


@dataclass
class Viewport:
    """Viewport for capturing screenshot."""

    #: X offset in device independent pixels (dip).# noqa
    x: float
    #: Y offset in device independent pixels (dip).# noqa
    y: float
    #: Rectangle width in device independent pixels (dip).# noqa
    width: float
    #: Rectangle height in device independent pixels (dip).# noqa
    height: float
    #: Page scale factor.# noqa
    scale: float


@dataclass
class FontFamilies:
    """Generic font families collection."""

    #: The standard font-family.# noqa
    standard: typing.Optional[str] = None
    #: The fixed font-family.# noqa
    fixed: typing.Optional[str] = None
    #: The serif font-family.# noqa
    serif: typing.Optional[str] = None
    #: The sansSerif font-family.# noqa
    sans_serif: typing.Optional[str] = None
    #: The cursive font-family.# noqa
    cursive: typing.Optional[str] = None
    #: The fantasy font-family.# noqa
    fantasy: typing.Optional[str] = None
    #: The math font-family.# noqa
    math: typing.Optional[str] = None


@dataclass
class ScriptFontFamilies:
    """Font families collection for a script."""

    #: Name of the script which these font families are defined for.# noqa
    script: str
    #: Generic font families collection for the script.# noqa
    font_families: FontFamilies


@dataclass
class FontSizes:
    """Default font sizes."""

    #: Default standard font size.# noqa
    standard: typing.Optional[int] = None
    #: Default fixed font size.# noqa
    fixed: typing.Optional[int] = None


class ClientNavigationReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    FORMSUBMISSIONGET = "formSubmissionGet"
    FORMSUBMISSIONPOST = "formSubmissionPost"
    HTTPHEADERREFRESH = "httpHeaderRefresh"
    SCRIPTINITIATED = "scriptInitiated"
    METATAGREFRESH = "metaTagRefresh"
    PAGEBLOCKINTERSTITIAL = "pageBlockInterstitial"
    RELOAD = "reload"
    ANCHORCLICK = "anchorClick"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ClientNavigationDisposition(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    CURRENTTAB = "currentTab"
    NEWTAB = "newTab"
    NEWWINDOW = "newWindow"
    DOWNLOAD = "download"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class InstallabilityErrorArgument:
    """Description is missing from the devtools protocol document."""

    #: Argument name (e.g. name:'minimum-icon-size-in-pixels').# noqa
    name: str
    #: Argument value (e.g. value:'64').# noqa
    value: str


@dataclass
class InstallabilityError:
    """The installability error."""

    #: The error id (e.g. 'manifest-missing-suitable-icon').# noqa
    error_id: str
    #: The list of error arguments (e.g. {name:'minimum-icon-size-in-pixels',value:'64'}).# noqa
    error_arguments: InstallabilityErrorArgument


class ReferrerPolicy(str, enum.Enum):
    """The referring-policy used for the navigation."""

    NOREFERRER = "noReferrer"
    NOREFERRERWHENDOWNGRADE = "noReferrerWhenDowngrade"
    ORIGIN = "origin"
    ORIGINWHENCROSSORIGIN = "originWhenCrossOrigin"
    SAMEORIGIN = "sameOrigin"
    STRICTORIGIN = "strictOrigin"
    STRICTORIGINWHENCROSSORIGIN = "strictOriginWhenCrossOrigin"
    UNSAFEURL = "unsafeUrl"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class CompilationCacheParams:
    """Per-script compilation cache parameters for
    `Page.produceCompilationCache`"""

    #: The URL of the script to produce a compilation cache entry for.# noqa
    url: str
    #: A hint to the backend whether eager compilation is recommended. (theactual compilation mode used is upon backend discretion).# noqa
    eager: typing.Optional[bool] = None


class AutoResponseMode(str, enum.Enum):
    """Enum of possible auto-reponse for permisison / prompt dialogs."""

    NONE = "none"
    AUTOACCEPT = "autoAccept"
    AUTOREJECT = "autoReject"
    AUTOOPTOUT = "autoOptOut"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class NavigationType(str, enum.Enum):
    """The type of a frameNavigated event."""

    NAVIGATION = "Navigation"
    BACKFORWARDCACHERESTORE = "BackForwardCacheRestore"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class BackForwardCacheNotRestoredReason(str, enum.Enum):
    """List of not restored reasons for back-forward cache."""

    NOTPRIMARYMAINFRAME = "NotPrimaryMainFrame"
    BACKFORWARDCACHEDISABLED = "BackForwardCacheDisabled"
    RELATEDACTIVECONTENTSEXIST = "RelatedActiveContentsExist"
    HTTPSTATUSNOTOK = "HTTPStatusNotOK"
    SCHEMENOTHTTPORHTTPS = "SchemeNotHTTPOrHTTPS"
    LOADING = "Loading"
    WASGRANTEDMEDIAACCESS = "WasGrantedMediaAccess"
    DISABLEFORRENDERFRAMEHOSTCALLED = "DisableForRenderFrameHostCalled"
    DOMAINNOTALLOWED = "DomainNotAllowed"
    HTTPMETHODNOTGET = "HTTPMethodNotGET"
    SUBFRAMEISNAVIGATING = "SubframeIsNavigating"
    TIMEOUT = "Timeout"
    CACHELIMIT = "CacheLimit"
    JAVASCRIPTEXECUTION = "JavaScriptExecution"
    RENDERERPROCESSKILLED = "RendererProcessKilled"
    RENDERERPROCESSCRASHED = "RendererProcessCrashed"
    SCHEDULERTRACKEDFEATUREUSED = "SchedulerTrackedFeatureUsed"
    CONFLICTINGBROWSINGINSTANCE = "ConflictingBrowsingInstance"
    CACHEFLUSHED = "CacheFlushed"
    SERVICEWORKERVERSIONACTIVATION = "ServiceWorkerVersionActivation"
    SESSIONRESTORED = "SessionRestored"
    SERVICEWORKERPOSTMESSAGE = "ServiceWorkerPostMessage"
    ENTEREDBACKFORWARDCACHEBEFORESERVICEWORKERHOSTADDED = "EnteredBackForwardCacheBeforeServiceWorkerHostAdded"
    RENDERFRAMEHOSTREUSED_SAMESITE = "RenderFrameHostReused_SameSite"
    RENDERFRAMEHOSTREUSED_CROSSSITE = "RenderFrameHostReused_CrossSite"
    SERVICEWORKERCLAIM = "ServiceWorkerClaim"
    IGNOREEVENTANDEVICT = "IgnoreEventAndEvict"
    HAVEINNERCONTENTS = "HaveInnerContents"
    TIMEOUTPUTTINGINCACHE = "TimeoutPuttingInCache"
    BACKFORWARDCACHEDISABLEDBYLOWMEMORY = "BackForwardCacheDisabledByLowMemory"
    BACKFORWARDCACHEDISABLEDBYCOMMANDLINE = "BackForwardCacheDisabledByCommandLine"
    NETWORKREQUESTDATAPIPEDRAINEDASBYTESCONSUMER = "NetworkRequestDatapipeDrainedAsBytesConsumer"
    NETWORKREQUESTREDIRECTED = "NetworkRequestRedirected"
    NETWORKREQUESTTIMEOUT = "NetworkRequestTimeout"
    NETWORKEXCEEDSBUFFERLIMIT = "NetworkExceedsBufferLimit"
    NAVIGATIONCANCELLEDWHILERESTORING = "NavigationCancelledWhileRestoring"
    NOTMOSTRECENTNAVIGATIONENTRY = "NotMostRecentNavigationEntry"
    BACKFORWARDCACHEDISABLEDFORPRERENDER = "BackForwardCacheDisabledForPrerender"
    USERAGENTOVERRIDEDIFFERS = "UserAgentOverrideDiffers"
    FOREGROUNDCACHELIMIT = "ForegroundCacheLimit"
    BROWSINGINSTANCENOTSWAPPED = "BrowsingInstanceNotSwapped"
    BACKFORWARDCACHEDISABLEDFORDELEGATE = "BackForwardCacheDisabledForDelegate"
    UNLOADHANDLEREXISTSINMAINFRAME = "UnloadHandlerExistsInMainFrame"
    UNLOADHANDLEREXISTSINSUBFRAME = "UnloadHandlerExistsInSubFrame"
    SERVICEWORKERUNREGISTRATION = "ServiceWorkerUnregistration"
    CACHECONTROLNOSTORE = "CacheControlNoStore"
    CACHECONTROLNOSTORECOOKIEMODIFIED = "CacheControlNoStoreCookieModified"
    CACHECONTROLNOSTOREHTTPONLYCOOKIEMODIFIED = "CacheControlNoStoreHTTPOnlyCookieModified"
    NORESPONSEHEAD = "NoResponseHead"
    UNKNOWN = "Unknown"
    ACTIVATIONNAVIGATIONSDISALLOWEDFORBUG1234857 = "ActivationNavigationsDisallowedForBug1234857"
    ERRORDOCUMENT = "ErrorDocument"
    FENCEDFRAMESEMBEDDER = "FencedFramesEmbedder"
    WEBSOCKET = "WebSocket"
    WEBTRANSPORT = "WebTransport"
    WEBRTC = "WebRTC"
    MAINRESOURCEHASCACHECONTROLNOSTORE = "MainResourceHasCacheControlNoStore"
    MAINRESOURCEHASCACHECONTROLNOCACHE = "MainResourceHasCacheControlNoCache"
    SUBRESOURCEHASCACHECONTROLNOSTORE = "SubresourceHasCacheControlNoStore"
    SUBRESOURCEHASCACHECONTROLNOCACHE = "SubresourceHasCacheControlNoCache"
    CONTAINSPLUGINS = "ContainsPlugins"
    DOCUMENTLOADED = "DocumentLoaded"
    DEDICATEDWORKERORWORKLET = "DedicatedWorkerOrWorklet"
    OUTSTANDINGNETWORKREQUESTOTHERS = "OutstandingNetworkRequestOthers"
    OUTSTANDINGINDEXEDDBTRANSACTION = "OutstandingIndexedDBTransaction"
    REQUESTEDMIDIPERMISSION = "RequestedMIDIPermission"
    REQUESTEDAUDIOCAPTUREPERMISSION = "RequestedAudioCapturePermission"
    REQUESTEDVIDEOCAPTUREPERMISSION = "RequestedVideoCapturePermission"
    REQUESTEDBACKFORWARDCACHEBLOCKEDSENSORS = "RequestedBackForwardCacheBlockedSensors"
    REQUESTEDBACKGROUNDWORKPERMISSION = "RequestedBackgroundWorkPermission"
    BROADCASTCHANNEL = "BroadcastChannel"
    INDEXEDDBCONNECTION = "IndexedDBConnection"
    WEBXR = "WebXR"
    SHAREDWORKER = "SharedWorker"
    WEBLOCKS = "WebLocks"
    WEBHID = "WebHID"
    WEBSHARE = "WebShare"
    REQUESTEDSTORAGEACCESSGRANT = "RequestedStorageAccessGrant"
    WEBNFC = "WebNfc"
    OUTSTANDINGNETWORKREQUESTFETCH = "OutstandingNetworkRequestFetch"
    OUTSTANDINGNETWORKREQUESTXHR = "OutstandingNetworkRequestXHR"
    APPBANNER = "AppBanner"
    PRINTING = "Printing"
    WEBDATABASE = "WebDatabase"
    PICTUREINPICTURE = "PictureInPicture"
    PORTAL = "Portal"
    SPEECHRECOGNIZER = "SpeechRecognizer"
    IDLEMANAGER = "IdleManager"
    PAYMENTMANAGER = "PaymentManager"
    SPEECHSYNTHESIS = "SpeechSynthesis"
    KEYBOARDLOCK = "KeyboardLock"
    WEBOTPSERVICE = "WebOTPService"
    OUTSTANDINGNETWORKREQUESTDIRECTSOCKET = "OutstandingNetworkRequestDirectSocket"
    INJECTEDJAVASCRIPT = "InjectedJavascript"
    INJECTEDSTYLESHEET = "InjectedStyleSheet"
    KEEPALIVEREQUEST = "KeepaliveRequest"
    INDEXEDDBEVENT = "IndexedDBEvent"
    DUMMY = "Dummy"
    AUTHORIZATIONHEADER = "AuthorizationHeader"
    CONTENTSECURITYHANDLER = "ContentSecurityHandler"
    CONTENTWEBAUTHENTICATIONAPI = "ContentWebAuthenticationAPI"
    CONTENTFILECHOOSER = "ContentFileChooser"
    CONTENTSERIAL = "ContentSerial"
    CONTENTFILESYSTEMACCESS = "ContentFileSystemAccess"
    CONTENTMEDIADEVICESDISPATCHERHOST = "ContentMediaDevicesDispatcherHost"
    CONTENTWEBBLUETOOTH = "ContentWebBluetooth"
    CONTENTWEBUSB = "ContentWebUSB"
    CONTENTMEDIASESSIONSERVICE = "ContentMediaSessionService"
    CONTENTSCREENREADER = "ContentScreenReader"
    EMBEDDERPOPUPBLOCKERTABHELPER = "EmbedderPopupBlockerTabHelper"
    EMBEDDERSAFEBROWSINGTRIGGEREDPOPUPBLOCKER = "EmbedderSafeBrowsingTriggeredPopupBlocker"
    EMBEDDERSAFEBROWSINGTHREATDETAILS = "EmbedderSafeBrowsingThreatDetails"
    EMBEDDERAPPBANNERMANAGER = "EmbedderAppBannerManager"
    EMBEDDERDOMDISTILLERVIEWERSOURCE = "EmbedderDomDistillerViewerSource"
    EMBEDDERDOMDISTILLERSELFDELETINGREQUESTDELEGATE = "EmbedderDomDistillerSelfDeletingRequestDelegate"
    EMBEDDEROOMINTERVENTIONTABHELPER = "EmbedderOomInterventionTabHelper"
    EMBEDDEROFFLINEPAGE = "EmbedderOfflinePage"
    EMBEDDERCHROMEPASSWORDMANAGERCLIENTBINDCREDENTIALMANAGER = (
        "EmbedderChromePasswordManagerClientBindCredentialManager"
    )
    EMBEDDERPERMISSIONREQUESTMANAGER = "EmbedderPermissionRequestManager"
    EMBEDDERMODALDIALOG = "EmbedderModalDialog"
    EMBEDDEREXTENSIONS = "EmbedderExtensions"
    EMBEDDEREXTENSIONMESSAGING = "EmbedderExtensionMessaging"
    EMBEDDEREXTENSIONMESSAGINGFOROPENPORT = "EmbedderExtensionMessagingForOpenPort"
    EMBEDDEREXTENSIONSENTMESSAGETOCACHEDFRAME = "EmbedderExtensionSentMessageToCachedFrame"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class BackForwardCacheNotRestoredReasonType(str, enum.Enum):
    """Types of not restored reasons for back-forward cache."""

    SUPPORTPENDING = "SupportPending"
    PAGESUPPORTNEEDED = "PageSupportNeeded"
    CIRCUMSTANTIAL = "Circumstantial"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class BackForwardCacheNotRestoredExplanation:
    """Description is missing from the devtools protocol document."""

    #: Type of the reason# noqa
    type: BackForwardCacheNotRestoredReasonType
    #: Not restored reason# noqa
    reason: BackForwardCacheNotRestoredReason
    #: Context associated with the reason. The meaning of this context isdependent on the reason: - EmbedderExtensionSentMessageToCachedFrame: theextension ID.# noqa
    context: typing.Optional[str] = None


@dataclass
class BackForwardCacheNotRestoredExplanationTree:
    """Description is missing from the devtools protocol document."""

    #: URL of each frame# noqa
    url: str
    #: Not restored reasons of each frame# noqa
    explanations: BackForwardCacheNotRestoredExplanation
    #: Array of children frame# noqa
    children: BackForwardCacheNotRestoredExplanationTree


@dataclass
@memoize_event("Page.domContentEventFired")
class DomContentEventFired:
    """Description is missing from the devtools protocol document."""

    timestamp: typing.Any


@dataclass
@memoize_event("Page.fileChooserOpened")
class FileChooserOpened:
    """Emitted only when `page.interceptFileChooser` is enabled."""

    frameId: typing.Any
    mode: typing.Any
    backendNodeId: typing.Any


@dataclass
@memoize_event("Page.frameAttached")
class FrameAttached:
    """Fired when frame has been attached to its parent."""

    frameId: typing.Any
    parentFrameId: typing.Any
    stack: typing.Any


@dataclass
@memoize_event("Page.frameClearedScheduledNavigation")
class FrameClearedScheduledNavigation:
    """Fired when frame no longer has a scheduled navigation."""

    frameId: typing.Any


@dataclass
@memoize_event("Page.frameDetached")
class FrameDetached:
    """Fired when frame has been detached from its parent."""

    frameId: typing.Any
    reason: typing.Any


@dataclass
@memoize_event("Page.frameNavigated")
class FrameNavigated:
    """Fired once navigation of the frame has completed.

    Frame is now associated with the new loader.
    """

    frame: typing.Any
    type: typing.Any


@dataclass
@memoize_event("Page.documentOpened")
class DocumentOpened:
    """Fired when opening document to write to."""

    frame: typing.Any


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

    frameId: typing.Any
    reason: typing.Any
    url: typing.Any
    disposition: typing.Any


@dataclass
@memoize_event("Page.frameScheduledNavigation")
class FrameScheduledNavigation:
    """Fired when frame schedules a potential navigation."""

    frameId: typing.Any
    delay: typing.Any
    reason: typing.Any
    url: typing.Any


@dataclass
@memoize_event("Page.frameStartedLoading")
class FrameStartedLoading:
    """Fired when frame has started loading."""

    frameId: typing.Any


@dataclass
@memoize_event("Page.frameStoppedLoading")
class FrameStoppedLoading:
    """Fired when frame has stopped loading."""

    frameId: typing.Any


@dataclass
@memoize_event("Page.downloadWillBegin")
class DownloadWillBegin:
    """Fired when page is about to start a download.

    Deprecated. Use Browser.downloadWillBegin instead.
    """

    frameId: typing.Any
    guid: typing.Any
    url: typing.Any
    suggestedFilename: typing.Any


@dataclass
@memoize_event("Page.downloadProgress")
class DownloadProgress:
    """Fired when download makes progress.

    Last call has |done| == true. Deprecated. Use
    Browser.downloadProgress instead.
    """

    guid: typing.Any
    totalBytes: typing.Any
    receivedBytes: typing.Any
    state: typing.Any


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
    """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or
    onbeforeunload) has been closed."""

    result: typing.Any
    userInput: typing.Any


@dataclass
@memoize_event("Page.javascriptDialogOpening")
class JavascriptDialogOpening:
    """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or
    onbeforeunload) is about to open."""

    url: typing.Any
    message: typing.Any
    type: typing.Any
    hasBrowserHandler: typing.Any
    defaultPrompt: typing.Any


@dataclass
@memoize_event("Page.lifecycleEvent")
class LifecycleEvent:
    """Fired for top level page lifecycle events such as navigation, load,
    paint, etc."""

    frameId: typing.Any
    loaderId: typing.Any
    name: typing.Any
    timestamp: typing.Any


@dataclass
@memoize_event("Page.backForwardCacheNotUsed")
class BackForwardCacheNotUsed:
    """Fired for failed bfcache history navigations if BackForwardCache feature
    is enabled.

    Do not assume any ordering with the Page.frameNavigated event. This
    event is fired only for main-frame history navigation where the
    document changes (non-same-document navigations), when bfcache
    navigation fails.
    """

    loaderId: typing.Any
    frameId: typing.Any
    notRestoredExplanations: typing.Any
    notRestoredExplanationsTree: typing.Any


@dataclass
@memoize_event("Page.loadEventFired")
class LoadEventFired:
    """Description is missing from the devtools protocol document."""

    timestamp: typing.Any


@dataclass
@memoize_event("Page.navigatedWithinDocument")
class NavigatedWithinDocument:
    """Fired when same-document navigation happens, e.g. due to history API
    usage or anchor navigation."""

    frameId: typing.Any
    url: typing.Any


@dataclass
@memoize_event("Page.screencastFrame")
class ScreencastFrame:
    """Compressed image data requested by the `startScreencast`."""

    data: typing.Any
    metadata: typing.Any
    sessionId: typing.Any


@dataclass
@memoize_event("Page.screencastVisibilityChanged")
class ScreencastVisibilityChanged:
    """Fired when the page with currently enabled screencast was shown or
    hidden `."""

    visible: typing.Any


@dataclass
@memoize_event("Page.windowOpen")
class WindowOpen:
    """Fired when a new window is going to be opened, via window.open(), link
    click, form submission, etc."""

    url: typing.Any
    windowName: typing.Any
    windowFeatures: typing.Any
    userGesture: typing.Any


@dataclass
@memoize_event("Page.compilationCacheProduced")
class CompilationCacheProduced:
    """Issued for every compilation cache generated.

    Is only available if Page.setGenerateCompilationCache is enabled.
    """

    url: typing.Any
    data: typing.Any


async def add_script_to_evaluate_on_load() -> None:
    """Deprecated, please use addScriptToEvaluateOnNewDocument instead.

    # noqa
    """
    ...


async def add_script_to_evaluate_on_new_document() -> None:
    """Evaluates given script in every frame upon creation (before loading
    frame's scripts).

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

    For MHTML format, the serialization includes iframes, shadow DOM,
    external resources, and element-inline styles. # noqa
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
    """Deprecated because it's not guaranteed that the returned icon is in fact
    the one used for PWA installation.

    # noqa
    """
    ...


async def get_app_id() -> None:
    """Returns the unique (PWA) app id.

    Only returns values if the feature flag 'WebAppEnableManifestId' is
    enabled # noqa
    """
    ...


async def get_ad_script_id() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def get_cookies() -> None:
    """Returns all browser cookies for the page and all of its subframes.

    Depending on the backend support, will return detailed cookie
    information in the `cookies` field. # noqa
    """
    ...


async def get_frame_tree() -> None:
    """Returns present frame tree structure.

    # noqa
    """
    ...


async def get_layout_metrics() -> None:
    """Returns metrics relating to the layouting of the page, such as viewport
    bounds/scale.

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
    """Accepts or dismisses a JavaScript initiated dialog (alert, confirm,
    prompt, or onbeforeunload).

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
    """Overrides the values of device screen dimensions (window.screen.width,
    window.screen.height, window.innerWidth, window.innerHeight, and "device-
    width"/"device-height"-related CSS media query results).

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
    https://github.com/WICG/web-lifecycle/
    # noqa
    """
    ...


async def stop_screencast() -> None:
    """Stops sending each frame in the `screencastFrame`.

    # noqa
    """
    ...


async def produce_compilation_cache() -> None:
    """Requests backend to produce compilation cache for the specified scripts.

    `scripts` are appeneded to the list of scripts for which the cache
    would be produced. The list may be reset during page navigation.
    When script with a matching URL is encountered, the cache is
    optionally produced upon backend discretion, based on internal
    heuristics. See also: `Page.compilationCacheProduced`. # noqa
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

    https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode
    # noqa
    """
    ...


async def set_rph_registration_mode() -> None:
    """Extensions for Custom Handlers API:

    https://html.spec.whatwg.org/multipage/system-state.html#rph-automation
    # noqa
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
    """Intercept file chooser requests and transfer control to protocol
    clients.

    When file chooser interception is enabled, native file chooser
    dialog is not shown. Instead, a protocol event
    `Page.fileChooserOpened` is emitted. # noqa
    """
    ...
