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

from . import io
from .utils import memoize_event


@dataclass
class MemoryDumpConfig:
    """Configuration for memory dump.

    Used only when "memory-infra" category is enabled.
    """


@dataclass
class TraceConfig:
    """Description is missing from the devtools protocol document."""

    # Controls how the trace buffer stores data. # noqa
    record_mode: typing.Optional[
        typing.List[typing.Literal["recordUntilFull", "recordContinuously", "recordAsMuchAsPossible", "echoToConsole"]]
    ]
    # Size of the trace buffer in kilobytes. If not specified or zero is passed,a default value of 200 MB would be used. # noqa
    trace_buffer_size_in_kb: typing.Optional[float]
    # Turns on JavaScript stack sampling. # noqa
    enable_sampling: typing.Optional[bool]
    # Turns on system tracing. # noqa
    enable_systrace: typing.Optional[bool]
    # Turns on argument filter. # noqa
    enable_argument_filter: typing.Optional[bool]
    # Included category filters. # noqa
    included_categories: typing.Optional[str]
    # Excluded category filters. # noqa
    excluded_categories: typing.Optional[str]
    # Configuration to synthesize the delays in tracing. # noqa
    synthetic_delays: typing.Optional[str]
    # Configuration for memory dump triggers. Used only when "memory-infra"category is enabled. # noqa
    memory_dump_config: typing.Optional[MemoryDumpConfig]


class StreamFormat(str, enum.Enum):
    """Data format of a trace.

    Can be either the legacy JSON format or the protocol buffer format. Note that the JSON format will be deprecated
    soon.
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

    Keep consistent with memory_dump_request_args.h and memory_instrumentation.mojom
    """

    BACKGROUND = "background"
    LIGHT = "light"
    DETAILED = "detailed"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class TracingBackend(str, enum.Enum):
    """Backend type to use for tracing.

    `chrome` uses the Chrome-integrated
    tracing service and is supported on all platforms. `system` is only
    supported on Chrome OS and uses the Perfetto system tracing service.
    `auto` chooses `system` when the perfettoConfig provided to Tracing.start
    specifies at least one non-Chrome data source; otherwise uses `chrome`.
    """

    AUTO = "auto"
    CHROME = "chrome"
    SYSTEM = "system"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
@memoize_event("Tracing.bufferUsage")
class BufferUsage:
    """Description is missing from the devtools protocol document."""

    percent_full: typing.Optional[float]
    event_count: typing.Optional[float]
    value: typing.Optional[float]


@dataclass
@memoize_event("Tracing.dataCollected")
class DataCollected:
    """Contains a bucket of collected trace events.

    When tracing is stopped collected events will be sent as a sequence of dataCollected events followed by
    tracingComplete event.
    """

    value: typing.List[typing.Any]


@dataclass
@memoize_event("Tracing.tracingComplete")
class TracingComplete:
    """Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via
    dataCollected events."""

    data_loss_occurred: bool
    stream: typing.Optional[io.StreamHandle]
    trace_format: typing.Optional[StreamFormat]
    stream_compression: typing.Optional[StreamCompression]


async def end() -> None:
    """Stop trace events collection.

    # noqa
    """
    ...


async def get_categories() -> None:
    """Gets supported tracing categories.

    # noqa
    """
    ...


async def record_clock_sync_marker() -> None:
    """Record a clock sync marker in the trace.

    # noqa
    """
    ...


async def request_memory_dump() -> None:
    """Request a global memory dump.

    # noqa
    """
    ...


async def start() -> None:
    """Start trace events collection.

    # noqa
    """
    ...
