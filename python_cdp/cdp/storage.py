# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Storage`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Storage/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass

from . import network


class SerializedStorageKey(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> SerializedStorageKey:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class StorageType(str, enum.Enum):
    """Enum of possible storage types."""

    APPCACHE = "appcache"
    COOKIES = "cookies"
    FILE_SYSTEMS = "file_systems"
    INDEXEDDB = "indexeddb"
    LOCAL_STORAGE = "local_storage"
    SHADER_CACHE = "shader_cache"
    WEBSQL = "websql"
    SERVICE_WORKERS = "service_workers"
    CACHE_STORAGE = "cache_storage"
    INTEREST_GROUPS = "interest_groups"
    SHARED_STORAGE = "shared_storage"
    ALL = "all"
    OTHER = "other"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class UsageForType:
    """Usage for a storage type."""

    #: Name of storage type.# noqa
    storage_type: StorageType
    #: Storage usage (bytes).# noqa
    usage: float


@dataclass
class TrustTokens:
    """Pair of issuer origin and number of available (signed, but not used)
    Trust Tokens from that issuer."""

    #: Description is missing from the devtools protocol document.# noqa
    issuer_origin: str
    #: Description is missing from the devtools protocol document.# noqa
    count: float


class InterestGroupAccessType(str, enum.Enum):
    """Enum of interest group access types."""

    JOIN = "join"
    LEAVE = "leave"
    UPDATE = "update"
    LOADED = "loaded"
    BID = "bid"
    WIN = "win"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class InterestGroupAd:
    """Ad advertising element inside an interest group."""

    #: Description is missing from the devtools protocol document.# noqa
    render_url: str
    #: Description is missing from the devtools protocol document.# noqa
    metadata: typing.Optional[str] = None


@dataclass
class InterestGroupDetails:
    """The full details of an interest group."""

    #: Description is missing from the devtools protocol document.# noqa
    owner_origin: str
    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    expiration_time: network.TimeSinceEpoch
    #: Description is missing from the devtools protocol document.# noqa
    joining_origin: str
    #: Description is missing from the devtools protocol document.# noqa
    trusted_bidding_signals_keys: str
    #: Description is missing from the devtools protocol document.# noqa
    ads: InterestGroupAd
    #: Description is missing from the devtools protocol document.# noqa
    ad_components: InterestGroupAd
    #: Description is missing from the devtools protocol document.# noqa
    bidding_url: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    bidding_wasm_helper_url: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    update_url: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    trusted_bidding_signals_url: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    user_bidding_signals: typing.Optional[str] = None


class SharedStorageAccessType(str, enum.Enum):
    """Enum of shared storage access types."""

    DOCUMENTADDMODULE = "documentAddModule"
    DOCUMENTSELECTURL = "documentSelectURL"
    DOCUMENTRUN = "documentRun"
    DOCUMENTSET = "documentSet"
    DOCUMENTAPPEND = "documentAppend"
    DOCUMENTDELETE = "documentDelete"
    DOCUMENTCLEAR = "documentClear"
    WORKLETSET = "workletSet"
    WORKLETAPPEND = "workletAppend"
    WORKLETDELETE = "workletDelete"
    WORKLETCLEAR = "workletClear"
    WORKLETGET = "workletGet"
    WORKLETKEYS = "workletKeys"
    WORKLETENTRIES = "workletEntries"
    WORKLETLENGTH = "workletLength"
    WORKLETREMAININGBUDGET = "workletRemainingBudget"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SharedStorageEntry:
    """Struct for a single key-value pair in an origin's shared storage."""

    #: Description is missing from the devtools protocol document.# noqa
    key: str
    #: Description is missing from the devtools protocol document.# noqa
    value: str


@dataclass
class SharedStorageMetadata:
    """Details for an origin's shared storage."""

    #: Description is missing from the devtools protocol document.# noqa
    creation_time: network.TimeSinceEpoch
    #: Description is missing from the devtools protocol document.# noqa
    length: int
    #: Description is missing from the devtools protocol document.# noqa
    remaining_budget: float


@dataclass
class SharedStorageReportingMetadata:
    """Pair of reporting metadata details for a candidate URL for
    `selectURL()`."""

    #: Description is missing from the devtools protocol document.# noqa
    event_type: str
    #: Description is missing from the devtools protocol document.# noqa
    reporting_url: str


@dataclass
class SharedStorageUrlWithMetadata:
    """Bundles a candidate URL with its reporting metadata."""

    #: Spec of candidate URL.# noqa
    url: str
    #: Any associated reporting metadata.# noqa
    reporting_metadata: SharedStorageReportingMetadata


@dataclass
class SharedStorageAccessParams:
    """Bundles the parameters for shared storage access events whose
    presence/absence can vary according to SharedStorageAccessType."""

    #: Spec of the module script URL. Present only forSharedStorageAccessType.documentAddModule.# noqa
    script_source_url: typing.Optional[str] = None
    #: Name of the registered operation to be run. Present only forSharedStorageAccessType.documentRun andSharedStorageAccessType.documentSelectURL.# noqa
    operation_name: typing.Optional[str] = None
    #: The operation's serialized data in bytes (converted to a string). Presentonly for SharedStorageAccessType.documentRun andSharedStorageAccessType.documentSelectURL.# noqa
    serialized_data: typing.Optional[str] = None
    #: Array of candidate URLs' specs, along with any associated metadata.Present only for SharedStorageAccessType.documentSelectURL.# noqa
    urls_with_metadata: typing.Optional[typing.List[SharedStorageUrlWithMetadata]] = None
    #: Key for a specific entry in an origin's shared storage. Present only forSharedStorageAccessType.documentSet, SharedStorageAccessType.documentAppend,SharedStorageAccessType.documentDelete, SharedStorageAccessType.workletSet,SharedStorageAccessType.workletAppend, SharedStorageAccessType.workletDelete,and SharedStorageAccessType.workletGet.# noqa
    key: typing.Optional[str] = None
    #: Value for a specific entry in an origin's shared storage. Present onlyfor SharedStorageAccessType.documentSet, SharedStorageAccessType.documentAppend,SharedStorageAccessType.workletSet, and SharedStorageAccessType.workletAppend.# noqa
    value: typing.Optional[str] = None
    #: Whether or not to set an entry for a key if that key is already present.Present only for SharedStorageAccessType.documentSet andSharedStorageAccessType.workletSet.# noqa
    ignore_if_present: typing.Optional[bool] = None
