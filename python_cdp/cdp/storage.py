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


@dataclass
class UsageForType:
    """Usage for a storage type."""


@dataclass
class TrustTokens:
    """Pair of issuer origin and number of available (signed, but not used)
    Trust Tokens from that issuer."""


class InterestGroupAccessType(str, enum.Enum):
    """Enum of interest group access types."""

    JOIN = "join"
    LEAVE = "leave"
    UPDATE = "update"
    LOADED = "loaded"
    BID = "bid"
    WIN = "win"


@dataclass
class InterestGroupAd:
    """Ad advertising element inside an interest group."""


@dataclass
class InterestGroupDetails:
    """The full details of an interest group."""


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


@dataclass
class SharedStorageEntry:
    """Struct for a single key-value pair in an origin's shared storage."""


@dataclass
class SharedStorageMetadata:
    """Details for an origin's shared storage."""


@dataclass
class SharedStorageReportingMetadata:
    """Pair of reporting metadata details for a candidate URL for
    `selectURL()`."""


@dataclass
class SharedStorageUrlWithMetadata:
    """Bundles a candidate URL with its reporting metadata."""


@dataclass
class SharedStorageAccessParams:
    """Bundles the parameters for shared storage access events whose
    presence/absence can vary according to SharedStorageAccessType."""
