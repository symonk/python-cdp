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
from . import page
from .utils import memoize_event


class SerializedStorageKey(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> SerializedStorageKey:
        return self

    @classmethod
    def from_json(cls, value: str) -> SerializedStorageKey:
        return cls(value)

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
    STORAGE_BUCKETS = "storage_buckets"
    ALL = "all"
    OTHER = "other"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class UsageForType:
    """Usage for a storage type."""

    # Name of storage type. # noqa
    storage_type: StorageType
    # Storage usage (bytes). # noqa
    usage: float


@dataclass
class TrustTokens:
    """Pair of issuer origin and number of available (signed, but not used) Trust Tokens from that issuer."""

    # Description is missing from the devtools protocol document. # noqa
    issuer_origin: str
    # Description is missing from the devtools protocol document. # noqa
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

    # Description is missing from the devtools protocol document. # noqa
    render_url: str
    # Description is missing from the devtools protocol document. # noqa
    metadata: typing.Optional[str]


@dataclass
class InterestGroupDetails:
    """The full details of an interest group."""

    # Description is missing from the devtools protocol document. # noqa
    owner_origin: str
    # Description is missing from the devtools protocol document. # noqa
    name: str
    # Description is missing from the devtools protocol document. # noqa
    expiration_time: network.TimeSinceEpoch
    # Description is missing from the devtools protocol document. # noqa
    joining_origin: str
    # Description is missing from the devtools protocol document. # noqa
    trusted_bidding_signals_keys: str
    # Description is missing from the devtools protocol document. # noqa
    ads: InterestGroupAd
    # Description is missing from the devtools protocol document. # noqa
    ad_components: InterestGroupAd
    # Description is missing from the devtools protocol document. # noqa
    bidding_url: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    bidding_wasm_helper_url: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    update_url: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    trusted_bidding_signals_url: typing.Optional[str]
    # Description is missing from the devtools protocol document. # noqa
    user_bidding_signals: typing.Optional[str]


class SharedStorageAccessType(str, enum.Enum):
    """Enum of shared storage access types."""

    DOCUMENT_ADD_MODULE = "document_add_module"
    DOCUMENT_SELECT_U_R_L = "document_select_url"
    DOCUMENT_RUN = "document_run"
    DOCUMENT_SET = "document_set"
    DOCUMENT_APPEND = "document_append"
    DOCUMENT_DELETE = "document_delete"
    DOCUMENT_CLEAR = "document_clear"
    WORKLET_SET = "worklet_set"
    WORKLET_APPEND = "worklet_append"
    WORKLET_DELETE = "worklet_delete"
    WORKLET_CLEAR = "worklet_clear"
    WORKLET_GET = "worklet_get"
    WORKLET_KEYS = "worklet_keys"
    WORKLET_ENTRIES = "worklet_entries"
    WORKLET_LENGTH = "worklet_length"
    WORKLET_REMAINING_BUDGET = "worklet_remaining_budget"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class SharedStorageEntry:
    """Struct for a single key-value pair in an origin's shared storage."""

    # Description is missing from the devtools protocol document. # noqa
    key: str
    # Description is missing from the devtools protocol document. # noqa
    value: str


@dataclass
class SharedStorageMetadata:
    """Details for an origin's shared storage."""

    # Description is missing from the devtools protocol document. # noqa
    creation_time: network.TimeSinceEpoch
    # Description is missing from the devtools protocol document. # noqa
    length: int
    # Description is missing from the devtools protocol document. # noqa
    remaining_budget: float


@dataclass
class SharedStorageReportingMetadata:
    """Pair of reporting metadata details for a candidate URL for `selectURL()`."""

    # Description is missing from the devtools protocol document. # noqa
    event_type: str
    # Description is missing from the devtools protocol document. # noqa
    reporting_url: str


@dataclass
class SharedStorageUrlWithMetadata:
    """Bundles a candidate URL with its reporting metadata."""

    # Spec of candidate URL. # noqa
    url: str
    # Any associated reporting metadata. # noqa
    reporting_metadata: SharedStorageReportingMetadata


@dataclass
class SharedStorageAccessParams:
    """Bundles the parameters for shared storage access events whose presence/absence can vary according to
    SharedStorageAccessType."""

    # Spec of the module script URL. Present only forSharedStorageAccessType.documentAddModule. # noqa
    script_source_url: typing.Optional[str]
    # Name of the registered operation to be run. Present only forSharedStorageAccessType.documentRun andSharedStorageAccessType.documentSelectURL. # noqa
    operation_name: typing.Optional[str]
    # The operation's serialized data in bytes (converted to a string). Presentonly for SharedStorageAccessType.documentRun andSharedStorageAccessType.documentSelectURL. # noqa
    serialized_data: typing.Optional[str]
    # Array of candidate URLs' specs, along with any associated metadata.Present only for SharedStorageAccessType.documentSelectURL. # noqa
    urls_with_metadata: typing.Optional[SharedStorageUrlWithMetadata]
    # Key for a specific entry in an origin's shared storage. Present only forSharedStorageAccessType.documentSet, SharedStorageAccessType.documentAppend,SharedStorageAccessType.documentDelete, SharedStorageAccessType.workletSet,SharedStorageAccessType.workletAppend, SharedStorageAccessType.workletDelete,and SharedStorageAccessType.workletGet. # noqa
    key: typing.Optional[str]
    # Value for a specific entry in an origin's shared storage. Present only forSharedStorageAccessType.documentSet, SharedStorageAccessType.documentAppend,SharedStorageAccessType.workletSet, and SharedStorageAccessType.workletAppend. # noqa
    value: typing.Optional[str]
    # Whether or not to set an entry for a key if that key is already present.Present only for SharedStorageAccessType.documentSet andSharedStorageAccessType.workletSet. # noqa
    ignore_if_present: typing.Optional[bool]


class StorageBucketsDurability(str, enum.Enum):
    """Description is missing from the devtools protocol document."""

    RELAXED = "relaxed"
    STRICT = "strict"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class StorageBucketInfo:
    """Description is missing from the devtools protocol document."""

    # Description is missing from the devtools protocol document. # noqa
    storage_key: SerializedStorageKey
    # Description is missing from the devtools protocol document. # noqa
    id: str
    # Description is missing from the devtools protocol document. # noqa
    name: str
    # Description is missing from the devtools protocol document. # noqa
    is_default: bool
    # Description is missing from the devtools protocol document. # noqa
    expiration: network.TimeSinceEpoch
    # Storage quota (bytes). # noqa
    quota: float
    # Description is missing from the devtools protocol document. # noqa
    persistent: bool
    # Description is missing from the devtools protocol document. # noqa
    durability: StorageBucketsDurability


@dataclass
@memoize_event("Storage.cacheStorageContentUpdated")
class CacheStorageContentUpdated:
    """A cache's contents have been modified."""

    origin: str
    storage_key: str
    cache_name: str


@dataclass
@memoize_event("Storage.cacheStorageListUpdated")
class CacheStorageListUpdated:
    """A cache has been added/deleted."""

    origin: str
    storage_key: str


@dataclass
@memoize_event("Storage.indexedDBContentUpdated")
class IndexedDBContentUpdated:
    """The origin's IndexedDB object store has been modified."""

    origin: str
    storage_key: str
    database_name: str
    object_store_name: str


@dataclass
@memoize_event("Storage.indexedDBListUpdated")
class IndexedDBListUpdated:
    """The origin's IndexedDB database list has been modified."""

    origin: str
    storage_key: str


@dataclass
@memoize_event("Storage.interestGroupAccessed")
class InterestGroupAccessed:
    """One of the interest groups was accessed by the associated page."""

    access_time: network.TimeSinceEpoch
    type: InterestGroupAccessType
    owner_origin: str
    name: str


@dataclass
@memoize_event("Storage.sharedStorageAccessed")
class SharedStorageAccessed:
    """Shared storage was accessed by the associated page.

    The following parameters are included in all events.
    """

    access_time: network.TimeSinceEpoch
    type: SharedStorageAccessType
    main_frame_id: page.FrameId
    owner_origin: str
    params: SharedStorageAccessParams


@dataclass
@memoize_event("Storage.storageBucketCreatedOrUpdated")
class StorageBucketCreatedOrUpdated:
    """Description is missing from the devtools protocol document."""

    bucket: StorageBucketInfo


@dataclass
@memoize_event("Storage.storageBucketDeleted")
class StorageBucketDeleted:
    """Description is missing from the devtools protocol document."""

    bucket_id: str


async def get_storage_key_for_frame() -> None:
    """Returns a storage key given a frame id.

    # noqa
    """
    ...


async def clear_data_for_origin() -> None:
    """Clears storage for origin.

    # noqa
    """
    ...


async def clear_data_for_storage_key() -> None:
    """Clears storage for storage key.

    # noqa
    """
    ...


async def get_cookies() -> None:
    """Returns all browser cookies.

    # noqa
    """
    ...


async def set_cookies() -> None:
    """Sets given cookies.

    # noqa
    """
    ...


async def clear_cookies() -> None:
    """Clears cookies.

    # noqa
    """
    ...


async def get_usage_and_quota() -> None:
    """Returns usage and quota in bytes.

    # noqa
    """
    ...


async def override_quota_for_origin() -> None:
    """Override quota for the specified origin # noqa."""
    ...


async def track_cache_storage_for_origin() -> None:
    """Registers origin to be notified when an update occurs to its cache storage list.

    # noqa
    """
    ...


async def track_cache_storage_for_storage_key() -> None:
    """Registers storage key to be notified when an update occurs to its cache storage list.

    # noqa
    """
    ...


async def track_indexed_db_for_origin() -> None:
    """Registers origin to be notified when an update occurs to its IndexedDB.

    # noqa
    """
    ...


async def track_indexed_db_for_storage_key() -> None:
    """Registers storage key to be notified when an update occurs to its IndexedDB.

    # noqa
    """
    ...


async def untrack_cache_storage_for_origin() -> None:
    """Unregisters origin from receiving notifications for cache storage.

    # noqa
    """
    ...


async def untrack_cache_storage_for_storage_key() -> None:
    """Unregisters storage key from receiving notifications for cache storage.

    # noqa
    """
    ...


async def untrack_indexed_db_for_origin() -> None:
    """Unregisters origin from receiving notifications for IndexedDB.

    # noqa
    """
    ...


async def untrack_indexed_db_for_storage_key() -> None:
    """Unregisters storage key from receiving notifications for IndexedDB.

    # noqa
    """
    ...


async def get_trust_tokens() -> None:
    """Returns the number of stored Trust Tokens per issuer for the current browsing context.

    # noqa
    """
    ...


async def clear_trust_tokens() -> None:
    """Removes all Trust Tokens issued by the provided issuerOrigin.

    Leaves other stored data, including the issuer's Redemption Records, intact. # noqa
    """
    ...


async def get_interest_group_details() -> None:
    """Gets details for a named interest group.

    # noqa
    """
    ...


async def set_interest_group_tracking() -> None:
    """Enables/Disables issuing of interestGroupAccessed events.

    # noqa
    """
    ...


async def get_shared_storage_metadata() -> None:
    """Gets metadata for an origin's shared storage.

    # noqa
    """
    ...


async def get_shared_storage_entries() -> None:
    """Gets the entries in an given origin's shared storage.

    # noqa
    """
    ...


async def set_shared_storage_entry() -> None:
    """Sets entry with `key` and `value` for a given origin's shared storage.

    # noqa
    """
    ...


async def delete_shared_storage_entry() -> None:
    """Deletes entry for `key` (if it exists) for a given origin's shared storage.

    # noqa
    """
    ...


async def clear_shared_storage_entries() -> None:
    """Clears all entries for a given origin's shared storage.

    # noqa
    """
    ...


async def reset_shared_storage_budget() -> None:
    """Resets the budget for `ownerOrigin` by clearing all budget withdrawals.

    # noqa
    """
    ...


async def set_shared_storage_tracking() -> None:
    """Enables/disables issuing of sharedStorageAccessed events.

    # noqa
    """
    ...


async def set_storage_bucket_tracking() -> None:
    """Set tracking for a storage key's buckets.

    # noqa
    """
    ...


async def delete_storage_bucket() -> None:
    """Deletes the Storage Bucket with the given storage key and bucket name.

    # noqa
    """
    ...
