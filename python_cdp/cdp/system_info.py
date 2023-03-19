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


class GPUDevice(None):
    """Describes a single graphics processor (GPU)."""

    def to_json(self) -> GPUDevice:
        return self

    @classmethod
    def from_json(cls, value: None) -> GPUDevice:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Size(None):
    """Describes the width and height dimensions of an entity."""

    def to_json(self) -> Size:
        return self

    @classmethod
    def from_json(cls, value: None) -> Size:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class VideoDecodeAcceleratorCapability(None):
    """Describes a supported video decoding profile with its associated minimum and maximum resolutions."""

    def to_json(self) -> VideoDecodeAcceleratorCapability:
        return self

    @classmethod
    def from_json(cls, value: None) -> VideoDecodeAcceleratorCapability:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class VideoEncodeAcceleratorCapability(None):
    """Describes a supported video encoding profile with its associated maximum resolution and maximum framerate."""

    def to_json(self) -> VideoEncodeAcceleratorCapability:
        return self

    @classmethod
    def from_json(cls, value: None) -> VideoEncodeAcceleratorCapability:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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


class ImageDecodeAcceleratorCapability(None):
    """Describes a supported image decoding profile with its associated minimum and maximum resolutions and
    subsampling."""

    def to_json(self) -> ImageDecodeAcceleratorCapability:
        return self

    @classmethod
    def from_json(cls, value: None) -> ImageDecodeAcceleratorCapability:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class GPUInfo(None):
    """Provides information about the GPU(s) on the system."""

    def to_json(self) -> GPUInfo:
        return self

    @classmethod
    def from_json(cls, value: None) -> GPUInfo:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ProcessInfo(None):
    """Represents process info."""

    def to_json(self) -> ProcessInfo:
        return self

    @classmethod
    def from_json(cls, value: None) -> ProcessInfo:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


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
