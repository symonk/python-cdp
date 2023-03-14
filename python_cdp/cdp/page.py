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
from dataclasses import dataclass


class FrameId(str):
    """Unique frame identifier."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


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


@dataclass
class AdScriptId:
    """Identifies the bottom-most script which caused the frame to be labelled
    as an ad."""


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


@dataclass
class PermissionsPolicyFeatureState:
    """Description is missing from the devtools protocol document."""


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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


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


@dataclass
class ScreencastFrameMetadata:
    """Screencast frame metadata."""


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


@dataclass
class InstallabilityError:
    """The installability error."""


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


@dataclass
class BackForwardCacheNotRestoredExplanationTree:
    """Description is missing from the devtools protocol document."""
