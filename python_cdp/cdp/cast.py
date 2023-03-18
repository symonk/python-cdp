# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Cast`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Cast/

from __future__ import annotations

import typing
from dataclasses import dataclass

from .utils import memoize_event


@dataclass
class Sink:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    id: str
    #: Text describing the current session. Present only if there is an activesession on the sink.# noqa
    session: typing.Optional[str] = None


@memoize_event("Cast.sinksUpdated")
class SinksUpdated:
    """This is fired whenever the list of available sinks changes.

    A sink is a device or a software surface that you can cast to.
    """

    ...


@memoize_event("Cast.issueUpdated")
class IssueUpdated:
    """This is fired whenever the outstanding issue/error message changes.

    |issueMessage| is empty if there is no issue.
    """

    ...


async def enable() -> None:
    """Starts observing for sinks that can be used for tab mirroring, and if
    set, sinks compatible with |presentationUrl| as well. When sinks are found,
    a.

    |sinksUpdated| event is fired. Also starts observing for issue
    messages. When an issue is added or removed, an |issueUpdated| event
    is fired. # noqa
    """
    ...


async def disable() -> None:
    """Stops observing for sinks and issues.

    # noqa
    """
    ...


async def set_sink_to_use() -> None:
    """Sets a sink to be used when the web page requests the browser to choose
    a sink via Presentation API, Remote Playback API, or Cast SDK.

    # noqa
    """
    ...


async def start_desktop_mirroring() -> None:
    """Starts mirroring the desktop to the sink.

    # noqa
    """
    ...


async def start_tab_mirroring() -> None:
    """Starts mirroring the tab to the sink.

    # noqa
    """
    ...


async def stop_casting() -> None:
    """Stops the active Cast session on the sink.

    # noqa
    """
    ...
