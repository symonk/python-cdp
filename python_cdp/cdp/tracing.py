# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Tracing`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Tracing/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass


@dataclass
class MemoryDumpConfig:
    """Configuration for memory dump.

    Used only when "memory-infra" category is enabled.
    """


@dataclass
class TraceConfig:
    """Description is missing from the devtools protocol document."""

    #: Controls how the trace buffer stores data.# noqa
    record_mode: typing.Optional[str] = None
    #: Size of the trace buffer in kilobytes. If not specified or zero ispassed, a default value of 200 MB would be used.# noqa
    trace_buffer_size_in_kb: typing.Optional[float] = None
    #: Turns on JavaScript stack sampling.# noqa
    enable_sampling: typing.Optional[bool] = None
    #: Turns on system tracing.# noqa
    enable_systrace: typing.Optional[bool] = None
    #: Turns on argument filter.# noqa
    enable_argument_filter: typing.Optional[bool] = None
    #: Included category filters.# noqa
    included_categories: typing.Optional[typing.List[str]] = None
    #: Excluded category filters.# noqa
    excluded_categories: typing.Optional[typing.List[str]] = None
    #: Configuration to synthesize the delays in tracing.# noqa
    synthetic_delays: typing.Optional[typing.List[str]] = None
    #: Configuration for memory dump triggers. Used only when "memory-infra"category is enabled.# noqa
    memory_dump_config: typing.Optional[MemoryDumpConfig] = None


class StreamFormat(str, enum.Enum):
    """Data format of a trace.

    Can be either the legacy JSON format or the protocol buffer format.
    Note that the JSON format will be deprecated soon.
    """

    JSON = "json"
    PROTO = "proto"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class StreamCompression(str, enum.Enum):
    """Compression type to use for traces returned via streams."""

    NONE = "none"
    GZIP = "gzip"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class MemoryDumpLevelOfDetail(str, enum.Enum):
    """Details exposed when memory request explicitly declared.

    Keep consistent with memory_dump_request_args.h and
    memory_instrumentation.mojom
    """

    BACKGROUND = "background"
    LIGHT = "light"
    DETAILED = "detailed"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class TracingBackend(str, enum.Enum):
    """Backend type to use for tracing.

    `chrome` uses the Chrome-integrated tracing service and is supported
    on all platforms. `system` is only supported on Chrome OS and uses
    the Perfetto system tracing service. `auto` chooses `system` when
    the perfettoConfig provided to Tracing.start specifies at least one
    non-Chrome data source; otherwise uses `chrome`.
    """

    AUTO = "auto"
    CHROME = "chrome"
    SYSTEM = "system"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)
