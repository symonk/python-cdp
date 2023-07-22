# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `IO`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/IO/

from __future__ import annotations


class StreamHandle(str):
    """This is either obtained from another method or specified as `blob:<uuid>` where `<uuid>` is an UUID of a Blob."""

    def to_json(self) -> StreamHandle:
        return self

    @classmethod
    def from_json(cls, value: str) -> StreamHandle:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


async def close() -> None:
    """Close the stream, discard any temporary backing storage.

    # noqa
    """
    ...


async def read() -> None:
    """Read a chunk of the stream # noqa."""
    ...


async def resolve_blob() -> None:
    """Return UUID of Blob object specified by a remote object id.

    # noqa
    """
    ...
