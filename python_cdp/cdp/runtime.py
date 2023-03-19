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

import typing
from dataclasses import dataclass

from .utils import memoize_event


class ScriptId(str):
    """Unique script identifier."""

    def to_json(self) -> ScriptId:
        return self

    @classmethod
    def from_json(cls, value: str) -> ScriptId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class WebDriverValue(None):
    """Represents the value serialiazed by the WebDriver BiDi specification https://w3c.github.io/webdriver-bidi."""

    def to_json(self) -> WebDriverValue:
        return self

    @classmethod
    def from_json(cls, value: None) -> WebDriverValue:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class RemoteObjectId(str):
    """Unique object identifier."""

    def to_json(self) -> RemoteObjectId:
        return self

    @classmethod
    def from_json(cls, value: str) -> RemoteObjectId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class UnserializableValue(str):
    """Primitive value which cannot be JSON-stringified.

    Includes values `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint literals.
    """

    def to_json(self) -> UnserializableValue:
        return self

    @classmethod
    def from_json(cls, value: str) -> UnserializableValue:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class RemoteObject(None):
    """Mirror object referencing original JavaScript object."""

    def to_json(self) -> RemoteObject:
        return self

    @classmethod
    def from_json(cls, value: None) -> RemoteObject:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CustomPreview(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> CustomPreview:
        return self

    @classmethod
    def from_json(cls, value: None) -> CustomPreview:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ObjectPreview(None):
    """Object containing abbreviated remote object value."""

    def to_json(self) -> ObjectPreview:
        return self

    @classmethod
    def from_json(cls, value: None) -> ObjectPreview:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class PropertyPreview(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> PropertyPreview:
        return self

    @classmethod
    def from_json(cls, value: None) -> PropertyPreview:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class EntryPreview(None):
    """Description is missing from the devtools protocol document."""

    def to_json(self) -> EntryPreview:
        return self

    @classmethod
    def from_json(cls, value: None) -> EntryPreview:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class PropertyDescriptor(None):
    """Object property descriptor."""

    def to_json(self) -> PropertyDescriptor:
        return self

    @classmethod
    def from_json(cls, value: None) -> PropertyDescriptor:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class InternalPropertyDescriptor(None):
    """Object internal property descriptor.

    This property isn't normally visible in JavaScript code.
    """

    def to_json(self) -> InternalPropertyDescriptor:
        return self

    @classmethod
    def from_json(cls, value: None) -> InternalPropertyDescriptor:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class PrivatePropertyDescriptor(None):
    """Object private field descriptor."""

    def to_json(self) -> PrivatePropertyDescriptor:
        return self

    @classmethod
    def from_json(cls, value: None) -> PrivatePropertyDescriptor:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CallArgument(None):
    """Represents function call argument.

    Either remote object id `objectId`, primitive `value`, unserializable primitive value or neither of (for undefined)
    them should be specified.
    """

    def to_json(self) -> CallArgument:
        return self

    @classmethod
    def from_json(cls, value: None) -> CallArgument:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ExecutionContextId(int):
    """Id of an execution context."""

    def to_json(self) -> ExecutionContextId:
        return self

    @classmethod
    def from_json(cls, value: int) -> ExecutionContextId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ExecutionContextDescription(None):
    """Description of an isolated world."""

    def to_json(self) -> ExecutionContextDescription:
        return self

    @classmethod
    def from_json(cls, value: None) -> ExecutionContextDescription:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class ExceptionDetails(None):
    """Detailed information about exception (or error) that was thrown during script compilation or execution."""

    def to_json(self) -> ExceptionDetails:
        return self

    @classmethod
    def from_json(cls, value: None) -> ExceptionDetails:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class Timestamp(float):
    """Number of milliseconds since epoch."""

    def to_json(self) -> Timestamp:
        return self

    @classmethod
    def from_json(cls, value: float) -> Timestamp:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class TimeDelta(float):
    """Number of milliseconds."""

    def to_json(self) -> TimeDelta:
        return self

    @classmethod
    def from_json(cls, value: float) -> TimeDelta:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class CallFrame(None):
    """Stack entry for runtime errors and assertions."""

    def to_json(self) -> CallFrame:
        return self

    @classmethod
    def from_json(cls, value: None) -> CallFrame:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class StackTrace(None):
    """Call frames for assertions or error messages."""

    def to_json(self) -> StackTrace:
        return self

    @classmethod
    def from_json(cls, value: None) -> StackTrace:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class UniqueDebuggerId(str):
    """Unique identifier of current debugger."""

    def to_json(self) -> UniqueDebuggerId:
        return self

    @classmethod
    def from_json(cls, value: str) -> UniqueDebuggerId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class StackTraceId(None):
    """If `debuggerId` is set stack trace comes from another debugger and can be resolved there.

    This allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.
    """

    def to_json(self) -> StackTraceId:
        return self

    @classmethod
    def from_json(cls, value: None) -> StackTraceId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
@memoize_event("Runtime.bindingCalled")
class BindingCalled:
    """Notification is issued every time when binding is called."""

    name: str
    payload: str
    execution_context_id: ExecutionContextId


@dataclass
@memoize_event("Runtime.consoleAPICalled")
class ConsoleAPICalled:
    """Issued when console API was called."""

    type: typing.Literal[
        "log",
        "debug",
        "info",
        "error",
        "warning",
        "dir",
        "dirxml",
        "table",
        "trace",
        "clear",
        "start_group",
        "start_group_collapsed",
        "end_group",
        "assert",
        "profile",
        "profile_end",
        "count",
        "time_end",
    ]
    args: typing.List[RemoteObject]
    execution_context_id: ExecutionContextId
    timestamp: Timestamp
    stack_trace: StackTrace
    context: typing.Optional[str]


@dataclass
@memoize_event("Runtime.exceptionRevoked")
class ExceptionRevoked:
    """Issued when unhandled exception was revoked."""

    reason: str
    exception_id: int


@dataclass
@memoize_event("Runtime.exceptionThrown")
class ExceptionThrown:
    """Issued when exception was thrown and unhandled."""

    timestamp: Timestamp
    exception_details: ExceptionDetails


@dataclass
@memoize_event("Runtime.executionContextCreated")
class ExecutionContextCreated:
    """Issued when new execution context is created."""

    context: ExecutionContextDescription


@dataclass
@memoize_event("Runtime.executionContextDestroyed")
class ExecutionContextDestroyed:
    """Issued when execution context is destroyed."""

    execution_context_id: ExecutionContextId
    execution_context_unique_id: str


@dataclass
@memoize_event("Runtime.executionContextsCleared")
class ExecutionContextsCleared:
    """Issued when all executionContexts were cleared in browser."""


@dataclass
@memoize_event("Runtime.inspectRequested")
class InspectRequested:
    """Issued when object should be inspected (for example, as a result of inspect() command line API call)."""

    object: RemoteObject
    hints: typing.Any
    execution_context_id: ExecutionContextId


async def await_promise() -> None:
    """Add handler to promise with given promise object id.

    # noqa
    """
    ...


async def call_function_on() -> None:
    """Calls function with given declaration on the given object.

    Object group of the result is inherited from the target object. # noqa
    """
    ...


async def compile_script() -> None:
    """Compiles expression.

    # noqa
    """
    ...


async def disable() -> None:
    """Disables reporting of execution contexts creation.

    # noqa
    """
    ...


async def discard_console_entries() -> None:
    """Discards collected exceptions and console API calls.

    # noqa
    """
    ...


async def enable() -> None:
    """Enables reporting of execution contexts creation by means of `executionContextCreated` event.

    When the reporting gets enabled the event will be sent immediately for each existing execution context. # noqa
    """
    ...


async def evaluate() -> None:
    """Evaluates expression on global object.

    # noqa
    """
    ...


async def get_isolate_id() -> None:
    """Returns the isolate id.

    # noqa
    """
    ...


async def get_heap_usage() -> None:
    """Returns the JavaScript heap usage.

    It is the total usage of the corresponding isolate not scoped to a particular Runtime. # noqa
    """
    ...


async def get_properties() -> None:
    """Returns properties of a given object.

    Object group of the result is inherited from the target object. # noqa
    """
    ...


async def global_lexical_scope_names() -> None:
    """Returns all let, const and class variables from global scope.

    # noqa
    """
    ...


async def query_objects() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def release_object() -> None:
    """Releases remote object with given id.

    # noqa
    """
    ...


async def release_object_group() -> None:
    """Releases all remote objects that belong to a given group.

    # noqa
    """
    ...


async def run_if_waiting_for_debugger() -> None:
    """Tells inspected instance to run if it was waiting for debugger to attach.

    # noqa
    """
    ...


async def run_script() -> None:
    """Runs script with given id in a given context.

    # noqa
    """
    ...


async def set_async_call_stack_depth() -> None:
    """Enables or disables async call stacks tracking.

    # noqa
    """
    ...


async def set_custom_object_formatter_enabled() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def set_max_call_stack_size_to_capture() -> None:
    """Description is missing from the devtools protocol document.

    # noqa
    """
    ...


async def terminate_execution() -> None:
    """Terminate current or next JavaScript execution.

    Will cancel the termination when the outer-most script execution ends. # noqa
    """
    ...


async def add_binding() -> None:
    """If executionContextId is empty, adds binding with the given name on the global objects of all inspected contexts,
    including those created later, bindings survive reloads.

    Binding function takes exactly one argument, this argument should be string, in case of any other input, function
    throws an exception. Each binding function call produces Runtime.bindingCalled notification. # noqa
    """
    ...


async def remove_binding() -> None:
    """This method does not remove binding function from global object but unsubscribes current runtime agent from
    Runtime.bindingCalled notifications.

    # noqa
    """
    ...


async def get_exception_details() -> None:
    """This method tries to lookup and populate exception details for a JavaScript Error object.

    Note that the stackTrace portion of the resulting exceptionDetails will only be populated if the Runtime domain was
    enabled at the time when the Error was thrown. # noqa
    """
    ...
