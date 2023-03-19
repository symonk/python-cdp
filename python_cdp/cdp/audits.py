# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Audits`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Audits/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import dom
from . import network
from . import page
from . import runtime
from .utils import memoize_event


@dataclass
class AffectedCookie:
    """Information about a cookie that is affected by an inspector issue."""

    # The following three properties uniquely identify a cookie# noqa


str
# Description is missing from the devtools protocol document.# noqa
str
# Description is missing from the devtools protocol document.# noqa
str


@dataclass
class AffectedRequest:
    """Information about a request that is affected by an inspector issue."""

    # The unique request id.# noqa


network.RequestId
# Description is missing from the devtools protocol document.# noqa
typing.Optional[str]


@dataclass
class AffectedFrame:
    """Information about the frame affected by an inspector issue."""

    # Description is missing from the devtools protocol document.# noqa


page.FrameId


class CookieExclusionReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _EXCLUDE_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX = "exclude_same_site_unspecified_treated_as_lax"
    _EXCLUDE_SAME_SITE_NONE_INSECURE = "exclude_same_site_none_insecure"
    _EXCLUDE_SAME_SITE_LAX = "exclude_same_site_lax"
    _EXCLUDE_SAME_SITE_STRICT = "exclude_same_site_strict"
    _EXCLUDE_INVALID_SAME_PARTY = "exclude_invalid_same_party"
    _EXCLUDE_SAME_PARTY_CROSS_PARTY_CONTEXT = "exclude_same_party_cross_party_context"
    _EXCLUDE_DOMAIN_NON_A_S_C_I_I = "exclude_domain_non_ascii"
    _EXCLUDE_THIRD_PARTY_COOKIE_BLOCKED_IN_FIRST_PARTY_SET = "exclude_third_party_cookie_blocked_in_first_party_set"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookieWarningReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _WARN_SAME_SITE_UNSPECIFIED_CROSS_SITE_CONTEXT = "warn_same_site_unspecified_cross_site_context"
    _WARN_SAME_SITE_NONE_INSECURE = "warn_same_site_none_insecure"
    _WARN_SAME_SITE_UNSPECIFIED_LAX_ALLOW_UNSAFE = "warn_same_site_unspecified_lax_allow_unsafe"
    _WARN_SAME_SITE_STRICT_LAX_DOWNGRADE_STRICT = "warn_same_site_strict_lax_downgrade_strict"
    _WARN_SAME_SITE_STRICT_CROSS_DOWNGRADE_STRICT = "warn_same_site_strict_cross_downgrade_strict"
    _WARN_SAME_SITE_STRICT_CROSS_DOWNGRADE_LAX = "warn_same_site_strict_cross_downgrade_lax"
    _WARN_SAME_SITE_LAX_CROSS_DOWNGRADE_STRICT = "warn_same_site_lax_cross_downgrade_strict"
    _WARN_SAME_SITE_LAX_CROSS_DOWNGRADE_LAX = "warn_same_site_lax_cross_downgrade_lax"
    _WARN_ATTRIBUTE_VALUE_EXCEEDS_MAX_SIZE = "warn_attribute_value_exceeds_max_size"
    _WARN_DOMAIN_NON_A_S_C_I_I = "warn_domain_non_ascii"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookieOperation(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _SET_COOKIE = "set_cookie"
    _READ_COOKIE = "read_cookie"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class CookieIssueDetails:
    """This information is currently necessary, as the front-end has a difficult time finding a specific cookie.

    With this, we can convey specific error information without the cookie.
    """

    # Description is missing from the devtools protocol document.# noqa


typing.List[CookieWarningReason]
# Description is missing from the devtools protocol document.# noqa
typing.List[CookieExclusionReason]
# Optionally identifies the site-for-cookies and the cookie url, which maybe used by the front-end as additional context.# noqa
CookieOperation
# If AffectedCookie is not set then rawCookieLine contains the raw Set-Cookie header string. This hints at a problem where the cookie line issyntactically or semantically malformed in a way that no valid cookie could becreated.# noqa
AffectedCookie
# Description is missing from the devtools protocol document.# noqa
typing.Optional[str]
# Description is missing from the devtools protocol document.# noqa
typing.Optional[str]
# Description is missing from the devtools protocol document.# noqa
typing.Optional[str]
# Description is missing from the devtools protocol document.# noqa
AffectedRequest


class MixedContentResolutionStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _MIXED_CONTENT_BLOCKED = "mixed_content_blocked"
    _MIXED_CONTENT_AUTOMATICALLY_UPGRADED = "mixed_content_automatically_upgraded"
    _MIXED_CONTENT_WARNING = "mixed_content_warning"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class MixedContentResourceType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _ATTRIBUTION_SRC = "attribution_src"
    _AUDIO = "audio"
    _BEACON = "beacon"
    _C_S_P_REPORT = "csp_report"
    _DOWNLOAD = "download"
    _EVENT_SOURCE = "event_source"
    _FAVICON = "favicon"
    _FONT = "font"
    _FORM = "form"
    _FRAME = "frame"
    _IMAGE = "image"
    _IMPORT = "import"
    _MANIFEST = "manifest"
    _PING = "ping"
    _PLUGIN_DATA = "plugin_data"
    _PLUGIN_RESOURCE = "plugin_resource"
    _PREFETCH = "prefetch"
    _RESOURCE = "resource"
    _SCRIPT = "script"
    _SERVICE_WORKER = "service_worker"
    _SHARED_WORKER = "shared_worker"
    _STYLESHEET = "stylesheet"
    _TRACK = "track"
    _VIDEO = "video"
    _WORKER = "worker"
    _X_M_L_HTTP_REQUEST = "xml_http_request"
    _X_S_L_T = "xslt"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class MixedContentIssueDetails:
    """Description is missing from the devtools protocol document."""

    # The way the mixed content issue is being resolved.# noqa


MixedContentResolutionStatus
# The unsafe http url causing the mixed content issue.# noqa
str
# The url responsible for the call to an unsafe url.# noqa
str
# The type of resource causing the mixed content issue (css, js, iframe,form,...). Marked as optional because it is mapped to fromblink::mojom::RequestContextType, which will be replaced bynetwork::mojom::RequestDestination# noqa
MixedContentResourceType
# The mixed content request. Does not always exist (e.g. for unsafe formsubmission urls).# noqa
AffectedRequest
# Optional because not every mixed content issue is necessarily linked to aframe.# noqa
AffectedFrame


class BlockedByResponseReason(str, enum.Enum):
    """Enum indicating the reason a response has been blocked.

    These reasons are refinements of the net error BLOCKED_BY_RESPONSE.
    """

    _COEP_FRAME_RESOURCE_NEEDS_COEP_HEADER = "coep_frame_resource_needs_coep_header"
    _COOP_SANDBOXED_I_FRAME_CANNOT_NAVIGATE_TO_COOP_PAGE = "coop_sandboxed_i_frame_cannot_navigate_to_coop_page"
    _CORP_NOT_SAME_ORIGIN = "corp_not_same_origin"
    _CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP = (
        "corp_not_same_origin_after_defaulted_to_same_origin_by_coep"
    )
    _CORP_NOT_SAME_SITE = "corp_not_same_site"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class BlockedByResponseIssueDetails:
    """Details for a request that has been blocked with the BLOCKED_BY_RESPONSE code.

    Currently only used for COEP/COOP, but may be extended to include some CSP errors in the future.
    """

    # Description is missing from the devtools protocol document.# noqa


AffectedRequest
# Description is missing from the devtools protocol document.# noqa
BlockedByResponseReason
# Description is missing from the devtools protocol document.# noqa
AffectedFrame
# Description is missing from the devtools protocol document.# noqa
AffectedFrame


class HeavyAdResolutionStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _HEAVY_AD_BLOCKED = "heavy_ad_blocked"
    _HEAVY_AD_WARNING = "heavy_ad_warning"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class HeavyAdReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _NETWORK_TOTAL_LIMIT = "network_total_limit"
    _CPU_TOTAL_LIMIT = "cpu_total_limit"
    _CPU_PEAK_LIMIT = "cpu_peak_limit"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class HeavyAdIssueDetails:
    """Description is missing from the devtools protocol document."""

    # The resolution status, either blocking the content or warning.# noqa


HeavyAdResolutionStatus
# The reason the ad was blocked, total network or cpu or peak cpu.# noqa
HeavyAdReason
# The frame that was blocked.# noqa
AffectedFrame


class ContentSecurityPolicyViolationType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    K_INLINE_VIOLATION = "k_inline_violation"
    K_EVAL_VIOLATION = "k_eval_violation"
    K_U_R_L_VIOLATION = "k_url_violation"
    K_TRUSTED_TYPES_SINK_VIOLATION = "k_trusted_types_sink_violation"
    K_TRUSTED_TYPES_POLICY_VIOLATION = "k_trusted_types_policy_violation"
    K_WASM_EVAL_VIOLATION = "k_wasm_eval_violation"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SourceCodeLocation:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa


str
# Description is missing from the devtools protocol document.# noqa
int
# Description is missing from the devtools protocol document.# noqa
int
# Description is missing from the devtools protocol document.# noqa
typing.Optional[runtime.ScriptId]


@dataclass
class ContentSecurityPolicyIssueDetails:
    """Description is missing from the devtools protocol document."""

    # Specific directive that is violated, causing the CSP issue.# noqa


str
# Description is missing from the devtools protocol document.# noqa
bool
# Description is missing from the devtools protocol document.# noqa
ContentSecurityPolicyViolationType
# The url not included in allowed sources.# noqa
typing.Optional[str]
# Description is missing from the devtools protocol document.# noqa
AffectedFrame
# Description is missing from the devtools protocol document.# noqa
SourceCodeLocation
# Description is missing from the devtools protocol document.# noqa
typing.Optional[dom.BackendNodeId]


class SharedArrayBufferIssueType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _TRANSFER_ISSUE = "transfer_issue"
    _CREATION_ISSUE = "creation_issue"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SharedArrayBufferIssueDetails:
    """Details for a issue arising from an SAB being instantiated in, or transferred to a context that is not cross-
    origin isolated."""

    # Description is missing from the devtools protocol document.# noqa


SourceCodeLocation
# Description is missing from the devtools protocol document.# noqa
bool
# Description is missing from the devtools protocol document.# noqa
SharedArrayBufferIssueType


class TwaQualityEnforcementViolationType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    K_HTTP_ERROR = "k_http_error"
    K_UNAVAILABLE_OFFLINE = "k_unavailable_offline"
    K_DIGITAL_ASSET_LINKS = "k_digital_asset_links"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class TrustedWebActivityIssueDetails:
    """Description is missing from the devtools protocol document."""

    # The url that triggers the violation.# noqa


str
# Description is missing from the devtools protocol document.# noqa
TwaQualityEnforcementViolationType
# Description is missing from the devtools protocol document.# noqa
typing.Optional[int]
# The package name of the Trusted Web Activity client app. This field isonly used when violation type is kDigitalAssetLinks.# noqa
typing.Optional[str]
# The signature of the Trusted Web Activity client app. This field is onlyused when violation type is kDigitalAssetLinks.# noqa
typing.Optional[str]


@dataclass
class LowTextContrastIssueDetails:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa


dom.BackendNodeId
# Description is missing from the devtools protocol document.# noqa
str
# Description is missing from the devtools protocol document.# noqa
float
# Description is missing from the devtools protocol document.# noqa
float
# Description is missing from the devtools protocol document.# noqa
float
# Description is missing from the devtools protocol document.# noqa
str
# Description is missing from the devtools protocol document.# noqa
str


@dataclass
class CorsIssueDetails:
    """Details for a CORS related issue, e.g. a warning or error related to CORS RFC1918 enforcement."""

    # Description is missing from the devtools protocol document.# noqa


network.CorsErrorStatus
# Description is missing from the devtools protocol document.# noqa
bool
# Description is missing from the devtools protocol document.# noqa
AffectedRequest
# Description is missing from the devtools protocol document.# noqa
SourceCodeLocation
# Description is missing from the devtools protocol document.# noqa
typing.Optional[str]
# Description is missing from the devtools protocol document.# noqa
typing.Optional[network.IPAddressSpace]
# Description is missing from the devtools protocol document.# noqa
typing.Optional[network.ClientSecurityState]


class AttributionReportingIssueType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _PERMISSION_POLICY_DISABLED = "permission_policy_disabled"
    _UNTRUSTWORTHY_REPORTING_ORIGIN = "untrustworthy_reporting_origin"
    _INSECURE_CONTEXT = "insecure_context"
    _INVALID_HEADER = "invalid_header"
    _INVALID_REGISTER_TRIGGER_HEADER = "invalid_register_trigger_header"
    _INVALID_ELIGIBLE_HEADER = "invalid_eligible_header"
    _TOO_MANY_CONCURRENT_REQUESTS = "too_many_concurrent_requests"
    _SOURCE_AND_TRIGGER_HEADERS = "source_and_trigger_headers"
    _SOURCE_IGNORED = "source_ignored"
    _TRIGGER_IGNORED = "trigger_ignored"
    _OS_SOURCE_IGNORED = "os_source_ignored"
    _OS_TRIGGER_IGNORED = "os_trigger_ignored"
    _INVALID_REGISTER_OS_SOURCE_HEADER = "invalid_register_os_source_header"
    _INVALID_REGISTER_OS_TRIGGER_HEADER = "invalid_register_os_trigger_header"
    _WEB_AND_OS_HEADERS = "web_and_os_headers"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class AttributionReportingIssueDetails:
    """Details for issues around "Attribution Reporting API" usage.

    Explainer: https://github.com/WICG/attribution-reporting-api
    """

    # Description is missing from the devtools protocol document.# noqa


AttributionReportingIssueType
# Description is missing from the devtools protocol document.# noqa
AffectedRequest
# Description is missing from the devtools protocol document.# noqa
typing.Optional[dom.BackendNodeId]
# Description is missing from the devtools protocol document.# noqa
typing.Optional[str]


@dataclass
class QuirksModeIssueDetails:
    """Details for issues about documents in Quirks Mode or Limited Quirks Mode that affects page layouting."""

    # If false, it means the document's mode is "quirks" instead of "limited-quirks".# noqa


bool
# Description is missing from the devtools protocol document.# noqa
dom.BackendNodeId
# Description is missing from the devtools protocol document.# noqa
str
# Description is missing from the devtools protocol document.# noqa
page.FrameId
# Description is missing from the devtools protocol document.# noqa
network.LoaderId


@dataclass
class NavigatorUserAgentIssueDetails:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa


str
# Description is missing from the devtools protocol document.# noqa
SourceCodeLocation


class GenericIssueErrorType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _CROSS_ORIGIN_PORTAL_POST_MESSAGE_ERROR = "cross_origin_portal_post_message_error"
    _FORM_LABEL_FOR_NAME_ERROR = "form_label_for_name_error"
    _FORM_DUPLICATE_ID_FOR_INPUT_ERROR = "form_duplicate_id_for_input_error"
    _FORM_INPUT_WITH_NO_LABEL_ERROR = "form_input_with_no_label_error"
    _FORM_AUTOCOMPLETE_ATTRIBUTE_EMPTY_ERROR = "form_autocomplete_attribute_empty_error"
    _FORM_EMPTY_ID_AND_NAME_ATTRIBUTES_FOR_INPUT_ERROR = "form_empty_id_and_name_attributes_for_input_error"
    _FORM_ARIA_LABELLED_BY_TO_NON_EXISTING_ID = "form_aria_labelled_by_to_non_existing_id"
    _FORM_INPUT_ASSIGNED_AUTOCOMPLETE_VALUE_TO_ID_OR_NAME_ATTRIBUTE_ERROR = (
        "form_input_assigned_autocomplete_value_to_id_or_name_attribute_error"
    )
    _FORM_LABEL_HAS_NEITHER_FOR_NOR_NESTED_INPUT = "form_label_has_neither_for_nor_nested_input"
    _FORM_LABEL_FOR_MATCHES_NON_EXISTING_ID_ERROR = "form_label_for_matches_non_existing_id_error"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class GenericIssueDetails:
    """Depending on the concrete errorType, different properties are set."""

    # Issues with the same errorType are aggregated in the frontend.# noqa


GenericIssueErrorType
# Description is missing from the devtools protocol document.# noqa
typing.Optional[page.FrameId]
# Description is missing from the devtools protocol document.# noqa
typing.Optional[dom.BackendNodeId]


@dataclass
class DeprecationIssueDetails:
    """This issue tracks information needed to print a deprecation message.

    https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md
    """

    # Description is missing from the devtools protocol document.# noqa


SourceCodeLocation
# One of the deprecation names fromthird_party/blink/renderer/core/frame/deprecation/deprecation.json5# noqa
str
# Description is missing from the devtools protocol document.# noqa
AffectedFrame


class ClientHintIssueReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    _META_TAG_ALLOW_LIST_INVALID_ORIGIN = "meta_tag_allow_list_invalid_origin"
    _META_TAG_MODIFIED_H_T_M_L = "meta_tag_modified_html"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class FederatedAuthRequestIssueDetails:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document.# noqa


FederatedAuthRequestIssueReason


class FederatedAuthRequestIssueReason(str, enum.Enum):
    """Represents the failure reason when a federated authentication reason fails.

    Should be updated alongside RequestIdTokenStatus in
    third_party/blink/public/mojom/devtools/inspector_issue.mojom to include
    all cases except for success.
    """

    _SHOULD_EMBARGO = "should_embargo"
    _TOO_MANY_REQUESTS = "too_many_requests"
    _WELL_KNOWN_HTTP_NOT_FOUND = "well_known_http_not_found"
    _WELL_KNOWN_NO_RESPONSE = "well_known_no_response"
    _WELL_KNOWN_INVALID_RESPONSE = "well_known_invalid_response"
    _WELL_KNOWN_LIST_EMPTY = "well_known_list_empty"
    _CONFIG_NOT_IN_WELL_KNOWN = "config_not_in_well_known"
    _WELL_KNOWN_TOO_BIG = "well_known_too_big"
    _CONFIG_HTTP_NOT_FOUND = "config_http_not_found"
    _CONFIG_NO_RESPONSE = "config_no_response"
    _CONFIG_INVALID_RESPONSE = "config_invalid_response"
    _CLIENT_METADATA_HTTP_NOT_FOUND = "client_metadata_http_not_found"
    _CLIENT_METADATA_NO_RESPONSE = "client_metadata_no_response"
    _CLIENT_METADATA_INVALID_RESPONSE = "client_metadata_invalid_response"
    _DISABLED_IN_SETTINGS = "disabled_in_settings"
    _ERROR_FETCHING_SIGNIN = "error_fetching_signin"
    _INVALID_SIGNIN_RESPONSE = "invalid_signin_response"
    _ACCOUNTS_HTTP_NOT_FOUND = "accounts_http_not_found"
    _ACCOUNTS_NO_RESPONSE = "accounts_no_response"
    _ACCOUNTS_INVALID_RESPONSE = "accounts_invalid_response"
    _ACCOUNTS_LIST_EMPTY = "accounts_list_empty"
    _ID_TOKEN_HTTP_NOT_FOUND = "id_token_http_not_found"
    _ID_TOKEN_NO_RESPONSE = "id_token_no_response"
    _ID_TOKEN_INVALID_RESPONSE = "id_token_invalid_response"
    _ID_TOKEN_INVALID_REQUEST = "id_token_invalid_request"
    _ERROR_ID_TOKEN = "error_id_token"
    _CANCELED = "canceled"
    _RP_PAGE_NOT_VISIBLE = "rp_page_not_visible"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class ClientHintIssueDetails:
    """This issue tracks client hints related issues.

    It's used to deprecate old features, encourage the use of new ones, and provide general guidance.
    """

    # Description is missing from the devtools protocol document.# noqa


SourceCodeLocation
# Description is missing from the devtools protocol document.# noqa
ClientHintIssueReason


class InspectorIssueCode(str, enum.Enum):
    """A unique identifier for the type of issue.

    Each type may use one of the optional fields in InspectorIssueDetails to convey more specific information about the
    kind of issue.
    """

    _COOKIE_ISSUE = "cookie_issue"
    _MIXED_CONTENT_ISSUE = "mixed_content_issue"
    _BLOCKED_BY_RESPONSE_ISSUE = "blocked_by_response_issue"
    _HEAVY_AD_ISSUE = "heavy_ad_issue"
    _CONTENT_SECURITY_POLICY_ISSUE = "content_security_policy_issue"
    _SHARED_ARRAY_BUFFER_ISSUE = "shared_array_buffer_issue"
    _TRUSTED_WEB_ACTIVITY_ISSUE = "trusted_web_activity_issue"
    _LOW_TEXT_CONTRAST_ISSUE = "low_text_contrast_issue"
    _CORS_ISSUE = "cors_issue"
    _ATTRIBUTION_REPORTING_ISSUE = "attribution_reporting_issue"
    _QUIRKS_MODE_ISSUE = "quirks_mode_issue"
    _NAVIGATOR_USER_AGENT_ISSUE = "navigator_user_agent_issue"
    _GENERIC_ISSUE = "generic_issue"
    _DEPRECATION_ISSUE = "deprecation_issue"
    _CLIENT_HINT_ISSUE = "client_hint_issue"
    _FEDERATED_AUTH_REQUEST_ISSUE = "federated_auth_request_issue"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class InspectorIssueDetails:
    """This struct holds a list of optional fields with additional information specific to the kind of issue.

    When adding a new issue code, please also add a new optional field to this type.
    """

    # Description is missing from the devtools protocol document.# noqa


CookieIssueDetails
# Description is missing from the devtools protocol document.# noqa
MixedContentIssueDetails
# Description is missing from the devtools protocol document.# noqa
BlockedByResponseIssueDetails
# Description is missing from the devtools protocol document.# noqa
HeavyAdIssueDetails
# Description is missing from the devtools protocol document.# noqa
ContentSecurityPolicyIssueDetails
# Description is missing from the devtools protocol document.# noqa
SharedArrayBufferIssueDetails
# Description is missing from the devtools protocol document.# noqa
TrustedWebActivityIssueDetails
# Description is missing from the devtools protocol document.# noqa
LowTextContrastIssueDetails
# Description is missing from the devtools protocol document.# noqa
CorsIssueDetails
# Description is missing from the devtools protocol document.# noqa
AttributionReportingIssueDetails
# Description is missing from the devtools protocol document.# noqa
QuirksModeIssueDetails
# Description is missing from the devtools protocol document.# noqa
NavigatorUserAgentIssueDetails
# Description is missing from the devtools protocol document.# noqa
GenericIssueDetails
# Description is missing from the devtools protocol document.# noqa
DeprecationIssueDetails
# Description is missing from the devtools protocol document.# noqa
ClientHintIssueDetails
# Description is missing from the devtools protocol document.# noqa
FederatedAuthRequestIssueDetails


class IssueId(str):
    """A unique id for a DevTools inspector issue.

    Allows other entities (e.g. exceptions, CDP message, console messages, etc.) to reference an issue.
    """

    def to_json(self) -> IssueId:
        return self

    @classmethod
    def from_json(cls, value: str) -> IssueId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class InspectorIssue:
    """An inspector issue reported from the back-end."""

    # Description is missing from the devtools protocol document.# noqa


InspectorIssueCode
# Description is missing from the devtools protocol document.# noqa
InspectorIssueDetails
# A unique id for this issue. May be omitted if no other entity (e.g.exception, CDP message, etc.) is referencing this issue.# noqa
IssueId


@dataclass
@memoize_event("Audits.issueAdded")
class IssueAdded:
    """Description is missing from the devtools protocol document."""

    issue: InspectorIssue


async def get_encoded_response() -> None:
    """Returns the response body and size if it were re-encoded with the specified settings.

    Only applies to images. # noqa
    """
    ...


async def disable() -> None:
    """Disables issues domain, prevents further issues from being reported to the client.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables issues domain, sends the issues collected so far to the client by means of the `issueAdded` event.

    # noqa
    """
    ...


async def check_contrast() -> None:
    """Runs the contrast check for the target page.

    Found issues are reported using Audits.issueAdded event. # noqa
    """
    ...
