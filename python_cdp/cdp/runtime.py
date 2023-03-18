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


@dataclass
class WebDriverValue:
    """Represents the value serialiazed by the WebDriver BiDi specification
    https://w3c.github.io/webdriver-bidi."""

    # Description is missing from the devtools protocol document.# noqa
    type: str
    # Description is missing from the devtools protocol document.# noqa
    value: typing.Optional[typing.Any] = None
    # Description is missing from the devtools protocol document.# noqa
    object_id: typing.Optional[str] = None


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

    Includes values `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint
    literals.
    """

    def to_json(self) -> UnserializableValue:
        return self

    @classmethod
    def from_json(cls, value: str) -> UnserializableValue:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class RemoteObject:
    """Mirror object referencing original JavaScript object."""

    # Object type.# noqa
    type: str
    # Object subtype hint. Specified for `object` type values only. NOTE: If youchange anything here, make sure to also update `subtype` in `ObjectPreview` and`PropertyPreview` below.# noqa
    subtype: typing.Optional[str] = None
    # Object class (constructor) name. Specified for `object` type values only.# noqa
    class_name: typing.Optional[str] = None
    # Remote object value in case of primitive values or JSON values (if it wasrequested).# noqa
    value: typing.Optional[typing.Any] = None
    # Primitive value which can not be JSON-stringified does not have `value`,but gets this property.# noqa
    unserializable_value: typing.Optional[UnserializableValue] = None
    # String representation of the object.# noqa
    description: typing.Optional[str] = None
    # WebDriver BiDi representation of the value.# noqa
    web_driver_value: typing.Optional[WebDriverValue] = None
    # Unique object identifier (for non-primitive values).# noqa
    object_id: typing.Optional[RemoteObjectId] = None
    # Preview containing abbreviated property values. Specified for `object`type values only.# noqa
    preview: typing.Optional[ObjectPreview] = None
    # Description is missing from the devtools protocol document.# noqa
    custom_preview: typing.Optional[CustomPreview] = None


@dataclass
class CustomPreview:
    """Description is missing from the devtools protocol document."""

    # The JSON-stringified result of formatter.header(object, config) call. Itcontains json ML array that represents RemoteObject.# noqa
    header: str
    # If formatter returns true as a result of formatter.hasBody call thenbodyGetterId will contain RemoteObjectId for the function that returns result offormatter.body(object, config) call. The result value is json ML array.# noqa
    body_getter_id: typing.Optional[RemoteObjectId] = None


@dataclass
class ObjectPreview:
    """Object containing abbreviated remote object value."""

    # Object type.# noqa
    type: str
    # True iff some of the properties or entries of the original object did notfit.# noqa
    overflow: bool
    # List of the properties.# noqa
    properties: PropertyPreview
    # Object subtype hint. Specified for `object` type values only.# noqa
    subtype: typing.Optional[str] = None
    # String representation of the object.# noqa
    description: typing.Optional[str] = None
    # List of the entries. Specified for `map` and `set` subtype values only.# noqa
    entries: typing.Optional[typing.List[EntryPreview]] = None


@dataclass
class PropertyPreview:
    """Description is missing from the devtools protocol document."""

    # Property name.# noqa
    name: str
    # Object type. Accessor means that the property itself is an accessorproperty.# noqa
    type: str
    # User-friendly property value string.# noqa
    value: typing.Optional[str] = None
    # Nested value preview.# noqa
    value_preview: typing.Optional[ObjectPreview] = None
    # Object subtype hint. Specified for `object` type values only.# noqa
    subtype: typing.Optional[str] = None


@dataclass
class EntryPreview:
    """Description is missing from the devtools protocol document."""

    # Preview of the value.# noqa
    value: ObjectPreview
    # Preview of the key. Specified for map-like collection entries.# noqa
    key: typing.Optional[ObjectPreview] = None


@dataclass
class PropertyDescriptor:
    """Object property descriptor."""

    # Property name or symbol description.# noqa
    name: str
    # True if the type of this property descriptor may be changed and if theproperty may be deleted from the corresponding object.# noqa
    configurable: bool
    # True if this property shows up during enumeration of the properties on thecorresponding object.# noqa
    enumerable: bool
    # The value associated with the property.# noqa
    value: typing.Optional[RemoteObject] = None
    # True if the value associated with the property may be changed (datadescriptors only).# noqa
    writable: typing.Optional[bool] = None
    # A function which serves as a getter for the property, or `undefined` ifthere is no getter (accessor descriptors only).# noqa
    get: typing.Optional[RemoteObject] = None
    # A function which serves as a setter for the property, or `undefined` ifthere is no setter (accessor descriptors only).# noqa
    set: typing.Optional[RemoteObject] = None
    # True if the result was thrown during the evaluation.# noqa
    was_thrown: typing.Optional[bool] = None
    # True if the property is owned for the object.# noqa
    is_own: typing.Optional[bool] = None
    # Property symbol object, if the property is of the `symbol` type.# noqa
    symbol: typing.Optional[RemoteObject] = None


@dataclass
class InternalPropertyDescriptor:
    """Object internal property descriptor.

    This property isn't normally visible in JavaScript code.
    """

    # Conventional property name.# noqa
    name: str
    # The value associated with the property.# noqa
    value: typing.Optional[RemoteObject] = None


@dataclass
class PrivatePropertyDescriptor:
    """Object private field descriptor."""

    # Private property name.# noqa
    name: str
    # The value associated with the private property.# noqa
    value: typing.Optional[RemoteObject] = None
    # A function which serves as a getter for the private property, or`undefined` if there is no getter (accessor descriptors only).# noqa
    get: typing.Optional[RemoteObject] = None
    # A function which serves as a setter for the private property, or`undefined` if there is no setter (accessor descriptors only).# noqa
    set: typing.Optional[RemoteObject] = None


@dataclass
class CallArgument:
    """Represents function call argument.

    Either remote object id `objectId`, primitive `value`,
    unserializable primitive value or neither of (for undefined) them
    should be specified.
    """

    # Primitive value or serializable javascript object.# noqa
    value: typing.Optional[typing.Any] = None
    # Primitive value which can not be JSON-stringified.# noqa
    unserializable_value: typing.Optional[UnserializableValue] = None
    # Remote object handle.# noqa
    object_id: typing.Optional[RemoteObjectId] = None


@dataclass
class ExecutionContextId:
    """Id of an execution context."""


@dataclass
class ExecutionContextDescription:
    """Description of an isolated world."""

    # Unique id of the execution context. It can be used to specify in whichexecution context script evaluation should be performed.# noqa
    id: ExecutionContextId
    # Execution context origin.# noqa
    origin: str
    # Human readable name describing given context.# noqa
    name: str
    # A system-unique execution context identifier. Unlike the id, this isunique across multiple processes, so can be reliably used to identify specificcontext while backend performs a cross-process navigation.# noqa
    unique_id: str
    # Embedder-specific auxiliary data.# noqa
    aux_data: typing.Optional[object] = None


@dataclass
class ExceptionDetails:
    """Detailed information about exception (or error) that was thrown during
    script compilation or execution."""

    # Exception id.# noqa
    exception_id: int
    # Exception text, which should be used together with exception object whenavailable.# noqa
    text: str
    # Line number of the exception location (0-based).# noqa
    line_number: int
    # Column number of the exception location (0-based).# noqa
    column_number: int
    # Script ID of the exception location.# noqa
    script_id: typing.Optional[ScriptId] = None
    # URL of the exception location, to be used when the script was notreported.# noqa
    url: typing.Optional[str] = None
    # JavaScript stack trace if available.# noqa
    stack_trace: typing.Optional[StackTrace] = None
    # Exception object if available.# noqa
    exception: typing.Optional[RemoteObject] = None
    # Identifier of the context where exception happened.# noqa
    execution_context_id: typing.Optional[ExecutionContextId] = None
    # Dictionary with entries of meta data that the client associated with thisexception, such as information about associated network requests, etc.# noqa
    exception_meta_data: typing.Optional[object] = None


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


@dataclass
class CallFrame:
    """Stack entry for runtime errors and assertions."""

    # JavaScript function name.# noqa
    function_name: str
    # JavaScript script id.# noqa
    script_id: ScriptId
    # JavaScript script name or url.# noqa
    url: str
    # JavaScript script line number (0-based).# noqa
    line_number: int
    # JavaScript script column number (0-based).# noqa
    column_number: int


@dataclass
class StackTrace:
    """Call frames for assertions or error messages."""

    # JavaScript function name.# noqa
    call_frames: CallFrame
    # String label of this stack trace. For async traces this may be a name ofthe function that initiated the async call.# noqa
    description: typing.Optional[str] = None
    # Asynchronous JavaScript stack trace that preceded this stack, ifavailable.# noqa
    parent: typing.Optional[StackTrace] = None
    # Asynchronous JavaScript stack trace that preceded this stack, ifavailable.# noqa
    parent_id: typing.Optional[StackTraceId] = None


class UniqueDebuggerId(str):
    """Unique identifier of current debugger."""

    def to_json(self) -> UniqueDebuggerId:
        return self

    @classmethod
    def from_json(cls, value: str) -> UniqueDebuggerId:
        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class StackTraceId:
    """If `debuggerId` is set stack trace comes from another debugger and can
    be resolved there.

    This allows to track cross-debugger calls. See `Runtime.StackTrace`
    and `Debugger.paused` for usages.
    """

    # Description is missing from the devtools protocol document.# noqa
    id: str
    # Description is missing from the devtools protocol document.# noqa
    debugger_id: typing.Optional[UniqueDebuggerId] = None


@dataclass
@memoize_event("Runtime.bindingCalled")
class BindingCalled:
    """Notification is issued every time when binding is called."""

    name: typing.Any
    payload: typing.Any
    executionContextId: typing.Any


@dataclass
@memoize_event("Runtime.consoleAPICalled")
class ConsoleAPICalled:
    """Issued when console API was called."""

    type: typing.Any
    args: typing.Any
    executionContextId: typing.Any
    timestamp: typing.Any
    stackTrace: typing.Any
    context: typing.Any


@dataclass
@memoize_event("Runtime.exceptionRevoked")
class ExceptionRevoked:
    """Issued when unhandled exception was revoked."""

    reason: typing.Any
    exceptionId: typing.Any


@dataclass
@memoize_event("Runtime.exceptionThrown")
class ExceptionThrown:
    """Issued when exception was thrown and unhandled."""

    timestamp: typing.Any
    exceptionDetails: typing.Any


@dataclass
@memoize_event("Runtime.executionContextCreated")
class ExecutionContextCreated:
    """Issued when new execution context is created."""

    context: typing.Any


@dataclass
@memoize_event("Runtime.executionContextDestroyed")
class ExecutionContextDestroyed:
    """Issued when execution context is destroyed."""

    executionContextId: typing.Any
    executionContextUniqueId: typing.Any


@dataclass
@memoize_event("Runtime.executionContextsCleared")
class ExecutionContextsCleared:
    """Issued when all executionContexts were cleared in browser."""


@dataclass
@memoize_event("Runtime.inspectRequested")
class InspectRequested:
    """Issued when object should be inspected (for example, as a result of
    inspect() command line API call)."""

    object: typing.Any
    hints: typing.Any
    executionContextId: typing.Any


async def await_promise() -> None:
    """Add handler to promise with given promise object id.

    # noqa
    """
    ...


async def call_function_on() -> None:
    """Calls function with given declaration on the given object.

    Object group of the result is inherited from the target object. #
    noqa
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
    """Enables reporting of execution contexts creation by means of
    `executionContextCreated` event.

    When the reporting gets enabled the event will be sent immediately
    for each existing execution context. # noqa
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

    It is the total usage of the corresponding isolate not scoped to a
    particular Runtime. # noqa
    """
    ...


async def get_properties() -> None:
    """Returns properties of a given object.

    Object group of the result is inherited from the target object. #
    noqa
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
    """Tells inspected instance to run if it was waiting for debugger to
    attach.

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

    Will cancel the termination when the outer-most script execution
    ends. # noqa
    """
    ...


async def add_binding() -> None:
    """If executionContextId is empty, adds binding with the given name on the
    global objects of all inspected contexts, including those created later,
    bindings survive reloads.

    Binding function takes exactly one argument, this argument should be
    string, in case of any other input, function throws an exception.
    Each binding function call produces Runtime.bindingCalled
    notification. # noqa
    """
    ...


async def remove_binding() -> None:
    """This method does not remove binding function from global object but
    unsubscribes current runtime agent from Runtime.bindingCalled
    notifications.

    # noqa
    """
    ...


async def get_exception_details() -> None:
    """This method tries to lookup and populate exception details for a
    JavaScript Error object.

    Note that the stackTrace portion of the resulting exceptionDetails
    will only be populated if the Runtime domain was enabled at the time
    when the Error was thrown. # noqa
    """
    ...
