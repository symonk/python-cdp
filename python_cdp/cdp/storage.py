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

from dataclasses import dataclass


class SerializedStorageKey(str):
    """Description is missing from the devtools protocol document.."""

    def to_json(self) -> str:
        return self


class StorageType(str):
    """Enum of possible storage types.."""

    def to_json(self) -> str:
        return self


@dataclass
class UsageForType:
    """Usage for a storage type."""

    ...


@dataclass
class TrustTokens:
    """Pair of issuer origin and number of available (signed, but not used)
    Trust Tokens from that issuer."""

    ...


class InterestGroupAccessType(str):
    """Enum of interest group access types.."""

    def to_json(self) -> str:
        return self


@dataclass
class InterestGroupAd:
    """Ad advertising element inside an interest group."""

    ...


@dataclass
class InterestGroupDetails:
    """The full details of an interest group."""

    ...


class SharedStorageAccessType(str):
    """Enum of shared storage access types.."""

    def to_json(self) -> str:
        return self


@dataclass
class SharedStorageEntry:
    """Struct for a single key-value pair in an origin's shared storage."""

    ...


@dataclass
class SharedStorageMetadata:
    """Details for an origin's shared storage."""

    ...


@dataclass
class SharedStorageReportingMetadata:
    """Pair of reporting metadata details for a candidate URL for
    `selectURL()`."""

    ...


@dataclass
class SharedStorageUrlWithMetadata:
    """Bundles a candidate URL with its reporting metadata."""

    ...


@dataclass
class SharedStorageAccessParams:
    """Bundles the parameters for shared storage access events whose
    presence/absence can vary according to SharedStorageAccessType."""

    ...
