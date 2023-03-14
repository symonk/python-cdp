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


class SerializedStorageKey(str):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


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

    #: Name of storage type.
    storageType: str
    #: Storage usage (bytes).
    usage: str


@dataclass
class TrustTokens:
    """Pair of issuer origin and number of available (signed, but not used)
    Trust Tokens from that issuer."""

    #: Description is missing from the devtools protocol document.
    issuerOrigin: str
    #: Description is missing from the devtools protocol document.
    count: str


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

    #: Description is missing from the devtools protocol document.
    renderUrl: str
    #: Description is missing from the devtools protocol document.
    metadata: str


@dataclass
class InterestGroupDetails:
    """The full details of an interest group."""

    #: Description is missing from the devtools protocol document.
    ownerOrigin: str
    #: Description is missing from the devtools protocol document.
    name: str
    #: Description is missing from the devtools protocol document.
    expirationTime: str
    #: Description is missing from the devtools protocol document.
    joiningOrigin: str
    #: Description is missing from the devtools protocol document.
    biddingUrl: str
    #: Description is missing from the devtools protocol document.
    biddingWasmHelperUrl: str
    #: Description is missing from the devtools protocol document.
    updateUrl: str
    #: Description is missing from the devtools protocol document.
    trustedBiddingSignalsUrl: str
    #: Description is missing from the devtools protocol document.
    trustedBiddingSignalsKeys: str
    #: Description is missing from the devtools protocol document.
    userBiddingSignals: str
    #: Description is missing from the devtools protocol document.
    ads: str
    #: Description is missing from the devtools protocol document.
    adComponents: str


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

    #: Description is missing from the devtools protocol document.
    key: str
    #: Description is missing from the devtools protocol document.
    value: str


@dataclass
class SharedStorageMetadata:
    """Details for an origin's shared storage."""

    #: Description is missing from the devtools protocol document.
    creationTime: str
    #: Description is missing from the devtools protocol document.
    length: str
    #: Description is missing from the devtools protocol document.
    remainingBudget: str


@dataclass
class SharedStorageReportingMetadata:
    """Pair of reporting metadata details for a candidate URL for
    `selectURL()`."""

    #: Description is missing from the devtools protocol document.
    eventType: str
    #: Description is missing from the devtools protocol document.
    reportingUrl: str


@dataclass
class SharedStorageUrlWithMetadata:
    """Bundles a candidate URL with its reporting metadata."""

    #: Spec of candidate URL.
    url: str
    #: Any associated reporting metadata.
    reportingMetadata: str


@dataclass
class SharedStorageAccessParams:
    """Bundles the parameters for shared storage access events whose
    presence/absence can vary according to SharedStorageAccessType."""

    #: Spec of the module script URL. Present only forSharedStorageAccessType.documentAddModule.
    scriptSourceUrl: str
    #: Name of the registered operation to be run. Present only forSharedStorageAccessType.documentRun andSharedStorageAccessType.documentSelectURL.
    operationName: str
    #: The operation's serialized data in bytes (converted to a string). Presentonly for SharedStorageAccessType.documentRun andSharedStorageAccessType.documentSelectURL.
    serializedData: str
    #: Array of candidate URLs' specs, along with any associated metadata.Present only for SharedStorageAccessType.documentSelectURL.
    urlsWithMetadata: str
    #: Key for a specific entry in an origin's shared storage. Present only forSharedStorageAccessType.documentSet, SharedStorageAccessType.documentAppend,SharedStorageAccessType.documentDelete, SharedStorageAccessType.workletSet,SharedStorageAccessType.workletAppend, SharedStorageAccessType.workletDelete,and SharedStorageAccessType.workletGet.
    key: str
    #: Value for a specific entry in an origin's shared storage. Present onlyfor SharedStorageAccessType.documentSet, SharedStorageAccessType.documentAppend,SharedStorageAccessType.workletSet, and SharedStorageAccessType.workletAppend.
    value: str
    #: Whether or not to set an entry for a key if that key is already present.Present only for SharedStorageAccessType.documentSet andSharedStorageAccessType.workletSet.
    ignoreIfPresent: str
