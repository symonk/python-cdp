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


@dataclass
class Sink:
    """Description is missing from the devtools protocol document."""

    #: Description is missing from the devtools protocol document.# noqa
    name: str
    #: Description is missing from the devtools protocol document.# noqa
    id: str
    #: Text describing the current session. Present only if there is an activesession on the sink.# noqa
    session: typing.Optional[str] = None


def enable() -> None:
    """Starts observing for sinks that can be used for tab mirroring, and if
    set, sinks compatible with |presentationUrl| as well. When sinks are found,
    a.

    |sinksUpdated| event is fired. Also starts observing for issue
    messages. When an issue is added or removed, an |issueUpdated| event
    is fired. # noqa
    """
    ...


def disable() -> None:
    """Stops observing for sinks and issues.

    # noqa
    """
    ...


def set_sink_to_use() -> None:
    """Sets a sink to be used when the web page requests the browser to choose
    a sink via Presentation API, Remote Playback API, or Cast SDK.

    # noqa
    """
    ...


def start_desktop_mirroring() -> None:
    """Starts mirroring the desktop to the sink.

    # noqa
    """
    ...


def start_tab_mirroring() -> None:
    """Starts mirroring the tab to the sink.

    # noqa
    """
    ...


def stop_casting() -> None:
    """Stops the active Cast session on the sink.

    # noqa
    """
    ...
