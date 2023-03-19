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
from dataclasses import dataclass

from . import network
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
    ALL = "all"
    OTHER = "other"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class UsageForType(None):
    """Usage for a storage type."""

    def to_json(self) -> UsageForType:
        return self

    @classmethod
    def from_json(cls, value: None) -> UsageForType:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class TrustTokens(None):
    """Pair of issuer origin and number of available (signed, but not used) Trust Tokens from that issuer."""

    def to_json(self) -> TrustTokens:
        return self

    @classmethod
    def from_json(cls, value: None) -> TrustTokens:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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


class InterestGroupAd(None):
    """Ad advertising element inside an interest group."""

    def to_json(self) -> InterestGroupAd:
        return self

    @classmethod
    def from_json(cls, value: None) -> InterestGroupAd:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class InterestGroupDetails(None):
    """The full details of an interest group."""

    def to_json(self) -> InterestGroupDetails:
        return self

    @classmethod
    def from_json(cls, value: None) -> InterestGroupDetails:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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


class SharedStorageEntry(None):
    """Struct for a single key-value pair in an origin's shared storage."""

    def to_json(self) -> SharedStorageEntry:
        return self

    @classmethod
    def from_json(cls, value: None) -> SharedStorageEntry:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SharedStorageMetadata(None):
    """Details for an origin's shared storage."""

    def to_json(self) -> SharedStorageMetadata:
        return self

    @classmethod
    def from_json(cls, value: None) -> SharedStorageMetadata:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SharedStorageReportingMetadata(None):
    """Pair of reporting metadata details for a candidate URL for `selectURL()`."""

    def to_json(self) -> SharedStorageReportingMetadata:
        return self

    @classmethod
    def from_json(cls, value: None) -> SharedStorageReportingMetadata:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SharedStorageUrlWithMetadata(None):
    """Bundles a candidate URL with its reporting metadata."""

    def to_json(self) -> SharedStorageUrlWithMetadata:
        return self

    @classmethod
    def from_json(cls, value: None) -> SharedStorageUrlWithMetadata:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class SharedStorageAccessParams(None):
    """Bundles the parameters for shared storage access events whose presence/absence can vary according to
    SharedStorageAccessType."""

    def to_json(self) -> SharedStorageAccessParams:
        return self

    @classmethod
    def from_json(cls, value: None) -> SharedStorageAccessParams:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
