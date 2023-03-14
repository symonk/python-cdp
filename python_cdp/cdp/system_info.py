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

from dataclasses import dataclass


@dataclass
class GPUDevice:
    """Describes a single graphics processor (GPU)."""

    ...


@dataclass
class Size:
    """Describes the width and height dimensions of an entity."""

    ...


@dataclass
class VideoDecodeAcceleratorCapability:
    """Describes a supported video decoding profile with its associated minimum
    and maximum resolutions."""

    ...


@dataclass
class VideoEncodeAcceleratorCapability:
    """Describes a supported video encoding profile with its associated maximum
    resolution and maximum framerate."""

    ...


class SubsamplingFormat(str):
    """YUV subsampling type of the pixels of a given image.."""

    def to_json(self) -> str:
        return self


class ImageType(str):
    """Image format of a given image.."""

    def to_json(self) -> str:
        return self


@dataclass
class ImageDecodeAcceleratorCapability:
    """Describes a supported image decoding profile with its associated minimum
    and maximum resolutions and subsampling."""

    ...


@dataclass
class GPUInfo:
    """Provides information about the GPU(s) on the system."""

    ...


@dataclass
class ProcessInfo:
    """Represents process info."""

    ...
