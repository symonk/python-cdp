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
    storageType: StorageType
    #: Storage usage (bytes).# noqa
    usage: float


@dataclass
class TrustTokens:
    """Pair of issuer origin and number of available (signed, but not used)
    Trust Tokens from that issuer."""

    #: Description is missing from the devtools protocol document.# noqa
    issuerOrigin: str
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
    renderUrl: str
    #: Description is missing from the devtools protocol document.# noqa
    metadata: typing.Optional[str] = None


@dataclass
class InterestGroupDetails:
    """The full details of an interest group."""

    #: Description is missing from the devtools protocol document.# noqa
    ownerOrigin: str
    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    expirationTime: network.TimeSinceEpoch
    #: Description is missing from the devtools protocol document.# noqa
    joiningOrigin: str
    #: Description is missing from the devtools protocol document.# noqa
    trustedBiddingSignalsKeys: str
    #: Description is missing from the devtools protocol document.# noqa
    ads: InterestGroupAd
    #: Description is missing from the devtools protocol document.# noqa
    adComponents: InterestGroupAd
    #: Description is missing from the devtools protocol document.# noqa
    biddingUrl: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    biddingWasmHelperUrl: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    updateUrl: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    trustedBiddingSignalsUrl: typing.Optional[str] = None
    #: Description is missing from the devtools protocol document.# noqa
    userBiddingSignals: typing.Optional[str] = None


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
    creationTime: network.TimeSinceEpoch
    #: Description is missing from the devtools protocol document.# noqa
    length: int
    #: Description is missing from the devtools protocol document.# noqa
    remainingBudget: float


@dataclass
class SharedStorageReportingMetadata:
    """Pair of reporting metadata details for a candidate URL for
    `selectURL()`."""

    #: Description is missing from the devtools protocol document.# noqa
    eventType: str
    #: Description is missing from the devtools protocol document.# noqa
    reportingUrl: str


@dataclass
class SharedStorageUrlWithMetadata:
    """Bundles a candidate URL with its reporting metadata."""

    #: Spec of candidate URL.# noqa
    url: str
    #: Any associated reporting metadata.# noqa
    reportingMetadata: SharedStorageReportingMetadata


@dataclass
class SharedStorageAccessParams:
    """Bundles the parameters for shared storage access events whose
    presence/absence can vary according to SharedStorageAccessType."""

    #: Spec of the module script URL. Present only forSharedStorageAccessType.documentAddModule.# noqa
    scriptSourceUrl: typing.Optional[str] = None
    #: Name of the registered operation to be run. Present only forSharedStorageAccessType.documentRun andSharedStorageAccessType.documentSelectURL.# noqa
    operationName: typing.Optional[str] = None
    #: The operation's serialized data in bytes (converted to a string). Presentonly for SharedStorageAccessType.documentRun andSharedStorageAccessType.documentSelectURL.# noqa
    serializedData: typing.Optional[str] = None
    #: Array of candidate URLs' specs, along with any associated metadata.Present only for SharedStorageAccessType.documentSelectURL.# noqa
    urlsWithMetadata: typing.Optional[typing.List[SharedStorageUrlWithMetadata]] = None
    #: Key for a specific entry in an origin's shared storage. Present only forSharedStorageAccessType.documentSet, SharedStorageAccessType.documentAppend,SharedStorageAccessType.documentDelete, SharedStorageAccessType.workletSet,SharedStorageAccessType.workletAppend, SharedStorageAccessType.workletDelete,and SharedStorageAccessType.workletGet.# noqa
    key: typing.Optional[str] = None
    #: Value for a specific entry in an origin's shared storage. Present onlyfor SharedStorageAccessType.documentSet, SharedStorageAccessType.documentAppend,SharedStorageAccessType.workletSet, and SharedStorageAccessType.workletAppend.# noqa
    value: typing.Optional[str] = None
    #: Whether or not to set an entry for a key if that key is already present.Present only for SharedStorageAccessType.documentSet andSharedStorageAccessType.workletSet.# noqa
    ignoreIfPresent: typing.Optional[bool] = None
