# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Profiler`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Profiler/

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ProfileNode:
    """Profile node.

    Holds callsite information, execution statistics and child nodes.
    """

    ...


@dataclass
class Profile:
    """Profile."""

    ...


@dataclass
class PositionTickInfo:
    """Specifies a number of samples attributed to a certain source
    position."""

    ...


@dataclass
class CoverageRange:
    """Coverage data for a source range."""

    ...


@dataclass
class FunctionCoverage:
    """Coverage data for a JavaScript function."""

    ...


@dataclass
class ScriptCoverage:
    """Coverage data for a JavaScript script."""

    ...
