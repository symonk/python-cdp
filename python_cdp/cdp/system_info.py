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
from dataclasses import dataclass


@dataclass
class GPUDevice:
    """Describes a single graphics processor (GPU)."""

    #: PCI ID of the GPU vendor, if available; 0 otherwise.# noqa
    vendorId: str
    #: PCI ID of the GPU device, if available; 0 otherwise.# noqa
    deviceId: str
    #: Sub sys ID of the GPU, only available on Windows.# noqa
    subSysId: str
    #: Revision of the GPU, only available on Windows.# noqa
    revision: str
    #: String description of the GPU vendor, if the PCI ID is not available.# noqa
    vendorString: str
    #: String description of the GPU device, if the PCI ID is not available.# noqa
    deviceString: str
    #: String description of the GPU driver vendor.# noqa
    driverVendor: str
    #: String description of the GPU driver version.# noqa
    driverVersion: str


@dataclass
class Size:
    """Describes the width and height dimensions of an entity."""

    #: Width in pixels.# noqa
    width: str
    #: Height in pixels.# noqa
    height: str


@dataclass
class VideoDecodeAcceleratorCapability:
    """Describes a supported video decoding profile with its associated minimum
    and maximum resolutions."""

    #: Video codec profile that is supported, e.g. VP9 Profile 2.# noqa
    profile: str
    #: Maximum video dimensions in pixels supported for this |profile|.# noqa
    maxResolution: str
    #: Minimum video dimensions in pixels supported for this |profile|.# noqa
    minResolution: str


@dataclass
class VideoEncodeAcceleratorCapability:
    """Describes a supported video encoding profile with its associated maximum
    resolution and maximum framerate."""

    #: Video codec profile that is supported, e.g H264 Main.# noqa
    profile: str
    #: Maximum video dimensions in pixels supported for this |profile|.# noqa
    maxResolution: str
    #: Maximum encoding framerate in frames per second supported for this|profile|, as fraction's numerator and denominator, e.g. 24/1 fps, 24000/1001fps, etc.# noqa
    maxFramerateNumerator: str
    #: Description is missing from the devtools protocol document.# noqa
    maxFramerateDenominator: str


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
    """Describes a supported image decoding profile with its associated minimum
    and maximum resolutions and subsampling."""

    #: Image coded, e.g. Jpeg.# noqa
    imageType: str
    #: Maximum supported dimensions of the image in pixels.# noqa
    maxDimensions: str
    #: Minimum supported dimensions of the image in pixels.# noqa
    minDimensions: str
    #: Optional array of supported subsampling formats, e.g. 4:2:0, if known.# noqa
    subsamplings: str


@dataclass
class GPUInfo:
    """Provides information about the GPU(s) on the system."""

    #: The graphics devices on the system. Element 0 is the primary GPU.# noqa
    devices: str
    #: An optional dictionary of additional GPU related attributes.# noqa
    auxAttributes: str
    #: An optional dictionary of graphics features and their status.# noqa
    featureStatus: str
    #: An optional array of GPU driver bug workarounds.# noqa
    driverBugWorkarounds: str
    #: Supported accelerated video decoding capabilities.# noqa
    videoDecoding: str
    #: Supported accelerated video encoding capabilities.# noqa
    videoEncoding: str
    #: Supported accelerated image decoding capabilities.# noqa
    imageDecoding: str


@dataclass
class ProcessInfo:
    """Represents process info."""

    #: Specifies process type.# noqa
    type: str
    #: Specifies process id.# noqa
    id: str
    #: Specifies cumulative CPU usage in seconds across all threads of theprocess since the process start.# noqa
    cpuTime: str
