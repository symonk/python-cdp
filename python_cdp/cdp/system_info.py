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


@dataclass
class Size:
    """Describes the width and height dimensions of an entity."""


@dataclass
class VideoDecodeAcceleratorCapability:
    """Describes a supported video decoding profile with its associated minimum
    and maximum resolutions."""


@dataclass
class VideoEncodeAcceleratorCapability:
    """Describes a supported video encoding profile with its associated maximum
    resolution and maximum framerate."""


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


@dataclass
class GPUInfo:
    """Provides information about the GPU(s) on the system."""


@dataclass
class ProcessInfo:
    """Represents process info."""
