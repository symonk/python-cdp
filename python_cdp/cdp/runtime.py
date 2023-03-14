# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.
# CHANGES TO THIS FILE ARE FUTILE AS IT WILL BE OVERWRITTEN
# WHEN THE DEVTOOLS PROTOCOL CHANGES.  IF THERE ANY BUGS
# OR YOU WISH TO CHANGE HOW THE FILES ARE GENERATED PLEASE
# REFER TO: https://github.com/symonk/python-cdp OR YOUR
# OWN FORK.  REFERENCE THE `generate.py` FILE FOR CONTEXT
# AND INSTRUCTIONS.
# Chrome Devtools Protocol Domain Mapped to: `Runtime`.
# Url for domain: https://chromedevtools.github.io/devtools-protocol/tot/Runtime/

from __future__ import annotations

from dataclasses import dataclass


class ScriptId(str):
    """Unique script identifier.."""

    def to_json(self) -> str:
        return self


@dataclass
class WebDriverValue:
    """Represents the value serialiazed by the WebDriver BiDi specification
    https://w3c.github.io/webdriver-bidi."""

    ...


class RemoteObjectId(str):
    """Unique object identifier.."""

    def to_json(self) -> str:
        return self


class UnserializableValue(str):
    """Primitive value which cannot be JSON-stringified.

    Includes values `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint
    literals..
    """

    def to_json(self) -> str:
        return self


@dataclass
class RemoteObject:
    """Mirror object referencing original JavaScript object."""

    ...


@dataclass
class CustomPreview:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class ObjectPreview:
    """Object containing abbreviated remote object value."""

    ...


@dataclass
class PropertyPreview:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class EntryPreview:
    """Description is missing from the devtools protocol document."""

    ...


@dataclass
class PropertyDescriptor:
    """Object property descriptor."""

    ...


@dataclass
class InternalPropertyDescriptor:
    """Object internal property descriptor.

    This property isn't normally visible in JavaScript code.
    """

    ...


@dataclass
class PrivatePropertyDescriptor:
    """Object private field descriptor."""

    ...


@dataclass
class CallArgument:
    """Represents function call argument.

    Either remote object id `objectId`, primitive `value`,
    unserializable primitive value or neither of (for undefined) them
    should be specified.
    """

    ...


@dataclass
class ExecutionContextId:
    """Id of an execution context."""

    ...


@dataclass
class ExecutionContextDescription:
    """Description of an isolated world."""

    ...


@dataclass
class ExceptionDetails:
    """Detailed information about exception (or error) that was thrown during
    script compilation or execution."""

    ...


class Timestamp(float):
    """Number of milliseconds since epoch.."""

    def to_json(self) -> float:
        return self


class TimeDelta(float):
    """Number of milliseconds.."""

    def to_json(self) -> float:
        return self


@dataclass
class CallFrame:
    """Stack entry for runtime errors and assertions."""

    ...


@dataclass
class StackTrace:
    """Call frames for assertions or error messages."""

    ...


class UniqueDebuggerId(str):
    """Unique identifier of current debugger.."""

    def to_json(self) -> str:
        return self


@dataclass
class StackTraceId:
    """If `debuggerId` is set stack trace comes from another debugger and can
    be resolved there.

    This allows to track cross-debugger calls. See `Runtime.StackTrace`
    and `Debugger.paused` for usages.
    """

    ...
