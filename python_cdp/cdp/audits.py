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

    # The following three properties uniquely identify a cookie # noqa
    name: str
    # Description is missing from the devtools protocol document. # noqa
    path: str
    # Description is missing from the devtools protocol document. # noqa
    domain: str


@dataclass
class AffectedRequest:
    """Information about a request that is affected by an inspector issue."""

    # The unique request id. # noqa
    request_id: network.RequestId
    # Description is missing from the devtools protocol document. # noqa
    url: typing.Optional[str]


@dataclass
class AffectedFrame:
    """Information about the frame affected by an inspector issue."""

    # Description is missing from the devtools protocol document. # noqa
    frame_id: page.FrameId


class CookieExclusionReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    EXCLUDE_SAME_SITE_UNSPECIFIED_TREATED_AS_LAX = "exclude_same_site_unspecified_treated_as_lax"
    EXCLUDE_SAME_SITE_NONE_INSECURE = "exclude_same_site_none_insecure"
    EXCLUDE_SAME_SITE_LAX = "exclude_same_site_lax"
    EXCLUDE_SAME_SITE_STRICT = "exclude_same_site_strict"
    EXCLUDE_INVALID_SAME_PARTY = "exclude_invalid_same_party"
    EXCLUDE_SAME_PARTY_CROSS_PARTY_CONTEXT = "exclude_same_party_cross_party_context"
    EXCLUDE_DOMAIN_NON_A_S_C_I_I = "exclude_domain_non_ascii"
    EXCLUDE_THIRD_PARTY_COOKIE_BLOCKED_IN_FIRST_PARTY_SET = "exclude_third_party_cookie_blocked_in_first_party_set"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookieWarningReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    WARN_SAME_SITE_UNSPECIFIED_CROSS_SITE_CONTEXT = "warn_same_site_unspecified_cross_site_context"
    WARN_SAME_SITE_NONE_INSECURE = "warn_same_site_none_insecure"
    WARN_SAME_SITE_UNSPECIFIED_LAX_ALLOW_UNSAFE = "warn_same_site_unspecified_lax_allow_unsafe"
    WARN_SAME_SITE_STRICT_LAX_DOWNGRADE_STRICT = "warn_same_site_strict_lax_downgrade_strict"
    WARN_SAME_SITE_STRICT_CROSS_DOWNGRADE_STRICT = "warn_same_site_strict_cross_downgrade_strict"
    WARN_SAME_SITE_STRICT_CROSS_DOWNGRADE_LAX = "warn_same_site_strict_cross_downgrade_lax"
    WARN_SAME_SITE_LAX_CROSS_DOWNGRADE_STRICT = "warn_same_site_lax_cross_downgrade_strict"
    WARN_SAME_SITE_LAX_CROSS_DOWNGRADE_LAX = "warn_same_site_lax_cross_downgrade_lax"
    WARN_ATTRIBUTE_VALUE_EXCEEDS_MAX_SIZE = "warn_attribute_value_exceeds_max_size"
    WARN_DOMAIN_NON_A_S_C_I_I = "warn_domain_non_ascii"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class CookieOperation(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    SET_COOKIE = "set_cookie"
    READ_COOKIE = "read_cookie"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class CookieIssueDetails:
    """This information is currently necessary, as the front-end has a difficult time finding a specific cookie.

    With this, we can convey specific error information without the cookie.
    """

    # Description is missing from the devtools protocol document. # noqa
    cookie_warning_reasons: CookieWarningReason
    # Description is missing from the devtools protocol document. # noqa
    cookie_exclusion_reasons: CookieExclusionReason
    # Optionally identifies the site-for-cookies and the cookie url, which maybe used by the front-end as additional context. # noqa
    operation: CookieOperation
    # If AffectedCookie is not set then rawCookieLine contains the raw Set-Cookie header string. This hints at a problem where the cookie line issyntactically or semantically malformed in a way that no valid cookie could becreated. # noqa
    cookie: typing.Optional[AffectedCookie]
    # Description is missing from the devtools protocol document. # noqa
    raw_cookie_line: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    site_for_cookies: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    cookie_url: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    request: typing.Optional[AffectedRequest]


class MixedContentResolutionStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    MIXED_CONTENT_BLOCKED = "mixed_content_blocked"
    MIXED_CONTENT_AUTOMATICALLY_UPGRADED = "mixed_content_automatically_upgraded"
    MIXED_CONTENT_WARNING = "mixed_content_warning"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class MixedContentResourceType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    ATTRIBUTION_SRC = "attribution_src"
    AUDIO = "audio"
    BEACON = "beacon"
    C_S_P_REPORT = "csp_report"
    DOWNLOAD = "download"
    EVENT_SOURCE = "event_source"
    FAVICON = "favicon"
    FONT = "font"
    FORM = "form"
    FRAME = "frame"
    IMAGE = "image"
    IMPORT = "import"
    MANIFEST = "manifest"
    PING = "ping"
    PLUGIN_DATA = "plugin_data"
    PLUGIN_RESOURCE = "plugin_resource"
    PREFETCH = "prefetch"
    RESOURCE = "resource"
    SCRIPT = "script"
    SERVICE_WORKER = "service_worker"
    SHARED_WORKER = "shared_worker"
    STYLESHEET = "stylesheet"
    TRACK = "track"
    VIDEO = "video"
    WORKER = "worker"
    X_M_L_HTTP_REQUEST = "xml_http_request"
    X_S_L_T = "xslt"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class MixedContentIssueDetails:
    """Description is missing from the devtools protocol document."""

    # The way the mixed content issue is being resolved. # noqa
    resolution_status: MixedContentResolutionStatus
    # The unsafe http url causing the mixed content issue. # noqa
    insecure_url: str
    # The url responsible for the call to an unsafe url. # noqa
    main_resource_url: str
    # The type of resource causing the mixed content issue (css, js, iframe,form,...). Marked as optional because it is mapped to fromblink::mojom::RequestContextType, which will be replaced bynetwork::mojom::RequestDestination # noqa
    resource_type: typing.Optional[MixedContentResourceType]
    # The mixed content request. Does not always exist (e.g. for unsafe formsubmission urls). # noqa
    request: typing.Optional[AffectedRequest]
    # Optional because not every mixed content issue is necessarily linked to aframe. # noqa
    frame: typing.Optional[AffectedFrame]


class BlockedByResponseReason(str, enum.Enum):
    """Enum indicating the reason a response has been blocked.

    These reasons are refinements of the net error BLOCKED_BY_RESPONSE.
    """

    COEP_FRAME_RESOURCE_NEEDS_COEP_HEADER = "coep_frame_resource_needs_coep_header"
    COOP_SANDBOXED_I_FRAME_CANNOT_NAVIGATE_TO_COOP_PAGE = "coop_sandboxed_i_frame_cannot_navigate_to_coop_page"
    CORP_NOT_SAME_ORIGIN = "corp_not_same_origin"
    CORP_NOT_SAME_ORIGIN_AFTER_DEFAULTED_TO_SAME_ORIGIN_BY_COEP = (
        "corp_not_same_origin_after_defaulted_to_same_origin_by_coep"
    )
    CORP_NOT_SAME_SITE = "corp_not_same_site"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class BlockedByResponseIssueDetails:
    """Details for a request that has been blocked with the BLOCKED_BY_RESPONSE code.

    Currently only used for COEP/COOP, but may be extended to include some CSP errors in the future.
    """

    # Description is missing from the devtools protocol document. # noqa
    request: AffectedRequest
    # Description is missing from the devtools protocol document. # noqa
    reason: BlockedByResponseReason
    # Description is missing from the devtools protocol document. # noqa
    parent_frame: typing.Optional[AffectedFrame]
    # Description is missing from the devtools protocol document. # noqa
    blocked_frame: typing.Optional[AffectedFrame]


class HeavyAdResolutionStatus(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    HEAVY_AD_BLOCKED = "heavy_ad_blocked"
    HEAVY_AD_WARNING = "heavy_ad_warning"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class HeavyAdReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    NETWORK_TOTAL_LIMIT = "network_total_limit"
    CPU_TOTAL_LIMIT = "cpu_total_limit"
    CPU_PEAK_LIMIT = "cpu_peak_limit"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class HeavyAdIssueDetails:
    """Description is missing from the devtools protocol document."""

    # The resolution status, either blocking the content or warning. # noqa
    resolution: HeavyAdResolutionStatus
    # The reason the ad was blocked, total network or cpu or peak cpu. # noqa
    reason: HeavyAdReason
    # The frame that was blocked. # noqa
    frame: AffectedFrame


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

    # Description is missing from the devtools protocol document. # noqa
    url: str
    # Description is missing from the devtools protocol document. # noqa
    line_number: int
    # Description is missing from the devtools protocol document. # noqa
    column_number: int
    # Description is missing from the devtools protocol document. # noqa
    script_id: typing.Optional[runtime.ScriptId]


@dataclass
class ContentSecurityPolicyIssueDetails:
    """Description is missing from the devtools protocol document."""

    # Specific directive that is violated, causing the CSP issue. # noqa
    violated_directive: str
    # Description is missing from the devtools protocol document. # noqa
    is_report_only: bool
    # Description is missing from the devtools protocol document. # noqa
    content_security_policy_violation_type: ContentSecurityPolicyViolationType
    # The url not included in allowed sources. # noqa
    blocked_url: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    frame_ancestor: typing.Optional[AffectedFrame]
    # Description is missing from the devtools protocol document. # noqa
    source_code_location: typing.Optional[SourceCodeLocation]
    # Description is missing from the devtools protocol document. # noqa
    violating_node_id: typing.Optional[dom.BackendNodeId]


class SharedArrayBufferIssueType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    TRANSFER_ISSUE = "transfer_issue"
    CREATION_ISSUE = "creation_issue"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SharedArrayBufferIssueDetails:
    """Details for a issue arising from an SAB being instantiated in, or transferred to a context that is not cross-
    origin isolated."""

    # Description is missing from the devtools protocol document. # noqa
    source_code_location: SourceCodeLocation
    # Description is missing from the devtools protocol document. # noqa
    is_warning: bool
    # Description is missing from the devtools protocol document. # noqa
    type: SharedArrayBufferIssueType


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

    # The url that triggers the violation. # noqa
    url: str
    # Description is missing from the devtools protocol document. # noqa
    violation_type: TwaQualityEnforcementViolationType
    # Description is missing from the devtools protocol document. # noqa
    http_status_code: typing.Optional[int]
    # The package name of the Trusted Web Activity client app. This field isonly used when violation type is kDigitalAssetLinks. # noqa
    package_name: typing.Optional[str]
    # The signature of the Trusted Web Activity client app. This field is onlyused when violation type is kDigitalAssetLinks. # noqa
    signature: typing.Optional[str]


@dataclass
class LowTextContrastIssueDetails:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document. # noqa
    violating_node_id: dom.BackendNodeId
    # Description is missing from the devtools protocol document. # noqa
    violating_node_selector: str
    # Description is missing from the devtools protocol document. # noqa
    contrast_ratio: float
    # Description is missing from the devtools protocol document. # noqa
    threshold_aa: float
    # Description is missing from the devtools protocol document. # noqa
    threshold_aaa: float
    # Description is missing from the devtools protocol document. # noqa
    font_size: str
    # Description is missing from the devtools protocol document. # noqa
    font_weight: str


@dataclass
class CorsIssueDetails:
    """Details for a CORS related issue, e.g. a warning or error related to CORS RFC1918 enforcement."""

    # Description is missing from the devtools protocol document. # noqa
    cors_error_status: network.CorsErrorStatus
    # Description is missing from the devtools protocol document. # noqa
    is_warning: bool
    # Description is missing from the devtools protocol document. # noqa
    request: AffectedRequest
    # Description is missing from the devtools protocol document. # noqa
    location: typing.Optional[SourceCodeLocation]
    # Description is missing from the devtools protocol document. # noqa
    initiator_origin: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    resource_ip_address_space: typing.Optional[network.IPAddressSpace]
    # Description is missing from the devtools protocol document. # noqa
    client_security_state: typing.Optional[network.ClientSecurityState]


class AttributionReportingIssueType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    PERMISSION_POLICY_DISABLED = "permission_policy_disabled"
    UNTRUSTWORTHY_REPORTING_ORIGIN = "untrustworthy_reporting_origin"
    INSECURE_CONTEXT = "insecure_context"
    INVALID_HEADER = "invalid_header"
    INVALID_REGISTER_TRIGGER_HEADER = "invalid_register_trigger_header"
    INVALID_ELIGIBLE_HEADER = "invalid_eligible_header"
    TOO_MANY_CONCURRENT_REQUESTS = "too_many_concurrent_requests"
    SOURCE_AND_TRIGGER_HEADERS = "source_and_trigger_headers"
    SOURCE_IGNORED = "source_ignored"
    TRIGGER_IGNORED = "trigger_ignored"
    OS_SOURCE_IGNORED = "os_source_ignored"
    OS_TRIGGER_IGNORED = "os_trigger_ignored"
    INVALID_REGISTER_OS_SOURCE_HEADER = "invalid_register_os_source_header"
    INVALID_REGISTER_OS_TRIGGER_HEADER = "invalid_register_os_trigger_header"
    WEB_AND_OS_HEADERS = "web_and_os_headers"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class AttributionReportingIssueDetails:
    """Details for issues around "Attribution Reporting API" usage.

    Explainer: https://github.com/WICG/attribution-reporting-api
    """

    # Description is missing from the devtools protocol document. # noqa
    violation_type: AttributionReportingIssueType
    # Description is missing from the devtools protocol document. # noqa
    request: typing.Optional[AffectedRequest]
    # Description is missing from the devtools protocol document. # noqa
    violating_node_id: typing.Optional[dom.BackendNodeId]
    # Description is missing from the devtools protocol document. # noqa
    invalid_parameter: typing.Optional[str]


@dataclass
class QuirksModeIssueDetails:
    """Details for issues about documents in Quirks Mode or Limited Quirks Mode that affects page layouting."""

    # If false, it means the document's mode is "quirks" instead of "limited-quirks". # noqa
    is_limited_quirks_mode: bool
    # Description is missing from the devtools protocol document. # noqa
    document_node_id: dom.BackendNodeId
    # Description is missing from the devtools protocol document. # noqa
    url: str
    # Description is missing from the devtools protocol document. # noqa
    frame_id: page.FrameId
    # Description is missing from the devtools protocol document. # noqa
    loader_id: network.LoaderId


@dataclass
class NavigatorUserAgentIssueDetails:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document. # noqa
    url: str
    # Description is missing from the devtools protocol document. # noqa
    location: typing.Optional[SourceCodeLocation]


class GenericIssueErrorType(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    CROSS_ORIGIN_PORTAL_POST_MESSAGE_ERROR = "cross_origin_portal_post_message_error"
    FORM_LABEL_FOR_NAME_ERROR = "form_label_for_name_error"
    FORM_DUPLICATE_ID_FOR_INPUT_ERROR = "form_duplicate_id_for_input_error"
    FORM_INPUT_WITH_NO_LABEL_ERROR = "form_input_with_no_label_error"
    FORM_AUTOCOMPLETE_ATTRIBUTE_EMPTY_ERROR = "form_autocomplete_attribute_empty_error"
    FORM_EMPTY_ID_AND_NAME_ATTRIBUTES_FOR_INPUT_ERROR = "form_empty_id_and_name_attributes_for_input_error"
    FORM_ARIA_LABELLED_BY_TO_NON_EXISTING_ID = "form_aria_labelled_by_to_non_existing_id"
    FORM_INPUT_ASSIGNED_AUTOCOMPLETE_VALUE_TO_ID_OR_NAME_ATTRIBUTE_ERROR = (
        "form_input_assigned_autocomplete_value_to_id_or_name_attribute_error"
    )
    FORM_LABEL_HAS_NEITHER_FOR_NOR_NESTED_INPUT = "form_label_has_neither_for_nor_nested_input"
    FORM_LABEL_FOR_MATCHES_NON_EXISTING_ID_ERROR = "form_label_for_matches_non_existing_id_error"
    FORM_INPUT_HAS_WRONG_BUT_WELL_INTENDED_AUTOCOMPLETE_VALUE_ERROR = (
        "form_input_has_wrong_but_well_intended_autocomplete_value_error"
    )

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class GenericIssueDetails:
    """Depending on the concrete errorType, different properties are set."""

    # Issues with the same errorType are aggregated in the frontend. # noqa
    error_type: GenericIssueErrorType
    # Description is missing from the devtools protocol document. # noqa
    frame_id: typing.Optional[page.FrameId]
    # Description is missing from the devtools protocol document. # noqa
    violating_node_id: typing.Optional[dom.BackendNodeId]


@dataclass
class DeprecationIssueDetails:
    """This issue tracks information needed to print a deprecation message.

    https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/core/frame/third_party/blink/renderer/core/frame/deprecation/README.md
    """

    # Description is missing from the devtools protocol document. # noqa
    source_code_location: SourceCodeLocation
    # One of the deprecation names fromthird_party/blink/renderer/core/frame/deprecation/deprecation.json5 # noqa
    type: str
    # Description is missing from the devtools protocol document. # noqa
    affected_frame: typing.Optional[AffectedFrame]


class ClientHintIssueReason(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    META_TAG_ALLOW_LIST_INVALID_ORIGIN = "meta_tag_allow_list_invalid_origin"
    META_TAG_MODIFIED_H_T_M_L = "meta_tag_modified_html"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class FederatedAuthRequestIssueDetails:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document. # noqa
    federated_auth_request_issue_reason: FederatedAuthRequestIssueReason


class FederatedAuthRequestIssueReason(str, enum.Enum):
    """Represents the failure reason when a federated authentication reason fails.

    Should be updated alongside RequestIdTokenStatus in
    third_party/blink/public/mojom/devtools/inspector_issue.mojom to include
    all cases except for success.
    """

    SHOULD_EMBARGO = "should_embargo"
    TOO_MANY_REQUESTS = "too_many_requests"
    WELL_KNOWN_HTTP_NOT_FOUND = "well_known_http_not_found"
    WELL_KNOWN_NO_RESPONSE = "well_known_no_response"
    WELL_KNOWN_INVALID_RESPONSE = "well_known_invalid_response"
    WELL_KNOWN_LIST_EMPTY = "well_known_list_empty"
    CONFIG_NOT_IN_WELL_KNOWN = "config_not_in_well_known"
    WELL_KNOWN_TOO_BIG = "well_known_too_big"
    CONFIG_HTTP_NOT_FOUND = "config_http_not_found"
    CONFIG_NO_RESPONSE = "config_no_response"
    CONFIG_INVALID_RESPONSE = "config_invalid_response"
    CLIENT_METADATA_HTTP_NOT_FOUND = "client_metadata_http_not_found"
    CLIENT_METADATA_NO_RESPONSE = "client_metadata_no_response"
    CLIENT_METADATA_INVALID_RESPONSE = "client_metadata_invalid_response"
    DISABLED_IN_SETTINGS = "disabled_in_settings"
    ERROR_FETCHING_SIGNIN = "error_fetching_signin"
    INVALID_SIGNIN_RESPONSE = "invalid_signin_response"
    ACCOUNTS_HTTP_NOT_FOUND = "accounts_http_not_found"
    ACCOUNTS_NO_RESPONSE = "accounts_no_response"
    ACCOUNTS_INVALID_RESPONSE = "accounts_invalid_response"
    ACCOUNTS_LIST_EMPTY = "accounts_list_empty"
    ID_TOKEN_HTTP_NOT_FOUND = "id_token_http_not_found"
    ID_TOKEN_NO_RESPONSE = "id_token_no_response"
    ID_TOKEN_INVALID_RESPONSE = "id_token_invalid_response"
    ID_TOKEN_INVALID_REQUEST = "id_token_invalid_request"
    ERROR_ID_TOKEN = "error_id_token"
    CANCELED = "canceled"
    RP_PAGE_NOT_VISIBLE = "rp_page_not_visible"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class ClientHintIssueDetails:
    """This issue tracks client hints related issues.

    It's used to deprecate old features, encourage the use of new ones, and provide general guidance.
    """

    # Description is missing from the devtools protocol document. # noqa
    source_code_location: SourceCodeLocation
    # Description is missing from the devtools protocol document. # noqa
    client_hint_issue_reason: ClientHintIssueReason


class InspectorIssueCode(str, enum.Enum):
    """A unique identifier for the type of issue.

    Each type may use one of the optional fields in InspectorIssueDetails to convey more specific information about the
    kind of issue.
    """

    COOKIE_ISSUE = "cookie_issue"
    MIXED_CONTENT_ISSUE = "mixed_content_issue"
    BLOCKED_BY_RESPONSE_ISSUE = "blocked_by_response_issue"
    HEAVY_AD_ISSUE = "heavy_ad_issue"
    CONTENT_SECURITY_POLICY_ISSUE = "content_security_policy_issue"
    SHARED_ARRAY_BUFFER_ISSUE = "shared_array_buffer_issue"
    TRUSTED_WEB_ACTIVITY_ISSUE = "trusted_web_activity_issue"
    LOW_TEXT_CONTRAST_ISSUE = "low_text_contrast_issue"
    CORS_ISSUE = "cors_issue"
    ATTRIBUTION_REPORTING_ISSUE = "attribution_reporting_issue"
    QUIRKS_MODE_ISSUE = "quirks_mode_issue"
    NAVIGATOR_USER_AGENT_ISSUE = "navigator_user_agent_issue"
    GENERIC_ISSUE = "generic_issue"
    DEPRECATION_ISSUE = "deprecation_issue"
    CLIENT_HINT_ISSUE = "client_hint_issue"
    FEDERATED_AUTH_REQUEST_ISSUE = "federated_auth_request_issue"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class InspectorIssueDetails:
    """This struct holds a list of optional fields with additional information specific to the kind of issue.

    When adding a new issue code, please also add a new optional field to this type.
    """

    # Description is missing from the devtools protocol document. # noqa
    cookie_issue_details: typing.Optional[CookieIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    mixed_content_issue_details: typing.Optional[MixedContentIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    blocked_by_response_issue_details: typing.Optional[BlockedByResponseIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    heavy_ad_issue_details: typing.Optional[HeavyAdIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    content_security_policy_issue_details: typing.Optional[ContentSecurityPolicyIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    shared_array_buffer_issue_details: typing.Optional[SharedArrayBufferIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    twa_quality_enforcement_details: typing.Optional[TrustedWebActivityIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    low_text_contrast_issue_details: typing.Optional[LowTextContrastIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    cors_issue_details: typing.Optional[CorsIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    attribution_reporting_issue_details: typing.Optional[AttributionReportingIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    quirks_mode_issue_details: typing.Optional[QuirksModeIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    navigator_user_agent_issue_details: typing.Optional[NavigatorUserAgentIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    generic_issue_details: typing.Optional[GenericIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    deprecation_issue_details: typing.Optional[DeprecationIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    client_hint_issue_details: typing.Optional[ClientHintIssueDetails]
    # Description is missing from the devtools protocol document. # noqa
    federated_auth_request_issue_details: typing.Optional[FederatedAuthRequestIssueDetails]


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

    # Description is missing from the devtools protocol document. # noqa
    code: InspectorIssueCode
    # Description is missing from the devtools protocol document. # noqa
    details: InspectorIssueDetails
    # A unique id for this issue. May be omitted if no other entity (e.g.exception, CDP message, etc.) is referencing this issue. # noqa
    issue_id: typing.Optional[IssueId]


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
