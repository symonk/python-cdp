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
    vendor_id: float
    # PCI ID of the GPU device, if available; 0 otherwise.# noqa
    device_id: float
    # String description of the GPU vendor, if the PCI ID is not available.# noqa
    vendor_string: str
    # String description of the GPU device, if the PCI ID is not available.# noqa
    device_string: str
    # String description of the GPU driver vendor.# noqa
    driver_vendor: str
    # String description of the GPU driver version.# noqa
    driver_version: str
    # Sub sys ID of the GPU, only available on Windows.# noqa
    sub_sys_id: typing.Optional[float] = None
    # Revision of the GPU, only available on Windows.# noqa
    revision: typing.Optional[float] = None


@dataclass
class Size:
    """Describes the width and height dimensions of an entity."""

    # Width in pixels.# noqa
    width: int
    # Height in pixels.# noqa
    height: int


@dataclass
class VideoDecodeAcceleratorCapability:
    """Describes a supported video decoding profile with its associated minimum and maximum resolutions."""

    # Video codec profile that is supported, e.g. VP9 Profile 2.# noqa
    profile: str
    # Maximum video dimensions in pixels supported for this |profile|.# noqa
    max_resolution: Size
    # Minimum video dimensions in pixels supported for this |profile|.# noqa
    min_resolution: Size


@dataclass
class VideoEncodeAcceleratorCapability:
    """Describes a supported video encoding profile with its associated maximum resolution and maximum framerate."""

    # Video codec profile that is supported, e.g H264 Main.# noqa
    profile: str
    # Maximum video dimensions in pixels supported for this |profile|.# noqa
    max_resolution: Size
    # Maximum encoding framerate in frames per second supported for this|profile|, as fraction's numerator and denominator, e.g. 24/1 fps, 24000/1001fps, etc.# noqa
    max_framerate_numerator: int
    # Description is missing from the devtools protocol document.# noqa
    max_framerate_denominator: int


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
    image_type: ImageType
    # Maximum supported dimensions of the image in pixels.# noqa
    max_dimensions: Size
    # Minimum supported dimensions of the image in pixels.# noqa
    min_dimensions: Size
    # Optional array of supported subsampling formats, e.g. 4:2:0, if known.# noqa
    subsamplings: SubsamplingFormat


@dataclass
class GPUInfo:
    """Provides information about the GPU(s) on the system."""

    # The graphics devices on the system. Element 0 is the primary GPU.# noqa
    devices: GPUDevice
    # An optional array of GPU driver bug workarounds.# noqa
    driver_bug_workarounds: str
    # Supported accelerated video decoding capabilities.# noqa
    video_decoding: VideoDecodeAcceleratorCapability
    # Supported accelerated video encoding capabilities.# noqa
    video_encoding: VideoEncodeAcceleratorCapability
    # Supported accelerated image decoding capabilities.# noqa
    image_decoding: ImageDecodeAcceleratorCapability
    # An optional dictionary of additional GPU related attributes.# noqa
    aux_attributes: typing.Optional[object] = None
    # An optional dictionary of graphics features and their status.# noqa
    feature_status: typing.Optional[object] = None


@dataclass
class ProcessInfo:
    """Represents process info."""

    # Specifies process type.# noqa
    type: str
    # Specifies process id.# noqa
    id: int
    # Specifies cumulative CPU usage in seconds across all threads of theprocess since the process start.# noqa
    cpu_time: float


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
