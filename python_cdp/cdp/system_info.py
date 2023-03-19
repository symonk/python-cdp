# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `SystemInfo`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/SystemInfo/

from __future__ import annotations

import enum
import typing
from dataclasses import dataclass


@dataclass
class GPUDevice:
    """Describes a single graphics processor (GPU)."""

    # PCI ID of the GPU vendor, if available; 0 otherwise.# noqa


float
# PCI ID of the GPU device, if available; 0 otherwise.# noqa
float
# String description of the GPU vendor, if the PCI ID is not available.# noqa
str
# String description of the GPU device, if the PCI ID is not available.# noqa
str
# String description of the GPU driver vendor.# noqa
str
# String description of the GPU driver version.# noqa
str
# Sub sys ID of the GPU, only available on Windows.# noqa
typing.Optional[float]
# Revision of the GPU, only available on Windows.# noqa
typing.Optional[float]


@dataclass
class Size:
    """Describes the width and height dimensions of an entity."""

    # Width in pixels.# noqa


int
# Height in pixels.# noqa
int


@dataclass
class VideoDecodeAcceleratorCapability:
    """Describes a supported video decoding profile with its associated minimum and maximum resolutions."""

    # Video codec profile that is supported, e.g. VP9 Profile 2.# noqa


str
# Maximum video dimensions in pixels supported for this |profile|.# noqa
Size
# Minimum video dimensions in pixels supported for this |profile|.# noqa
Size


@dataclass
class VideoEncodeAcceleratorCapability:
    """Describes a supported video encoding profile with its associated maximum resolution and maximum framerate."""

    # Video codec profile that is supported, e.g H264 Main.# noqa


str
# Maximum video dimensions in pixels supported for this |profile|.# noqa
Size
# Maximum encoding framerate in frames per second supported for this|profile|, as fraction's numerator and denominator, e.g. 24/1 fps, 24000/1001fps, etc.# noqa
int
# Description is missing from the devtools protocol document.# noqa
int


class SubsamplingFormat(str, enum.Enum):
    """YUV subsampling type of the pixels of a given image."""

    YUV420 = "yuv420"
    YUV422 = "yuv422"
    YUV444 = "yuv444"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


class ImageType(str, enum.Enum):
    """Image format of a given image."""

    JPEG = "jpeg"
    WEBP = "webp"
    UNKNOWN = "unknown"

    @classmethod
    def from_json(cls, value: str) -> str:
        return cls(value)


@dataclass
class ImageDecodeAcceleratorCapability:
    """Describes a supported image decoding profile with its associated minimum and maximum resolutions and
    subsampling."""

    # Image coded, e.g. Jpeg.# noqa


ImageType
# Maximum supported dimensions of the image in pixels.# noqa
Size
# Minimum supported dimensions of the image in pixels.# noqa
Size
# Optional array of supported subsampling formats, e.g. 4:2:0, if known.# noqa
typing.List[SubsamplingFormat]


@dataclass
class GPUInfo:
    """Provides information about the GPU(s) on the system."""

    # The graphics devices on the system. Element 0 is the primary GPU.# noqa


typing.List[GPUDevice]
# An optional array of GPU driver bug workarounds.# noqa
typing.List[str]
# Supported accelerated video decoding capabilities.# noqa
typing.List[VideoDecodeAcceleratorCapability]
# Supported accelerated video encoding capabilities.# noqa
typing.List[VideoEncodeAcceleratorCapability]
# Supported accelerated image decoding capabilities.# noqa
typing.List[ImageDecodeAcceleratorCapability]
# An optional dictionary of additional GPU related attributes.# noqa
typing.Optional[object]
# An optional dictionary of graphics features and their status.# noqa
typing.Optional[object]


@dataclass
class ProcessInfo:
    """Represents process info."""

    # Specifies process type.# noqa


str
# Specifies process id.# noqa
int
# Specifies cumulative CPU usage in seconds across all threads of theprocess since the process start.# noqa
float


async def get_info() -> None:
    """Returns information about the system.

    # noqa
    """
    ...


async def get_feature_state() -> None:
    """Returns information about the feature state.

    # noqa
    """
    ...


async def get_process_info() -> None:
    """Returns information about all running processes.

    # noqa
    """
    ...
