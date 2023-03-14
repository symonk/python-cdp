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


class ScriptId(str):
    """Unique script identifier."""

    def to_json(self) -> ScriptId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class WebDriverValue:
    """Represents the value serialiazed by the WebDriver BiDi specification
    https://w3c.github.io/webdriver-bidi."""

    #: Description is missing from the devtools protocol document.# noqa
    type: str
    #: Description is missing from the devtools protocol document.# noqa
    value: typing.Optional[typing.Any] = None
    #: Description is missing from the devtools protocol document.# noqa
    objectId: typing.Optional[str] = None


class RemoteObjectId(str):
    """Unique object identifier."""

    def to_json(self) -> RemoteObjectId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class UnserializableValue(str):
    """Primitive value which cannot be JSON-stringified.

    Includes values `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint
    literals.
    """

    def to_json(self) -> UnserializableValue:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class RemoteObject:
    """Mirror object referencing original JavaScript object."""

    #: Object type.# noqa
    type: str
    #: Object subtype hint. Specified for `object` type values only. NOTE: Ifyou change anything here, make sure to also update `subtype` in `ObjectPreview`and `PropertyPreview` below.# noqa
    subtype: typing.Optional[str] = None
    #: Object class (constructor) name. Specified for `object` type values only.# noqa
    className: typing.Optional[str] = None
    #: Remote object value in case of primitive values or JSON values (if it wasrequested).# noqa
    value: typing.Optional[typing.Any] = None
    #: Primitive value which can not be JSON-stringified does not have `value`,but gets this property.# noqa
    unserializableValue: typing.Optional[UnserializableValue] = None
    #: String representation of the object.# noqa
    description: typing.Optional[str] = None
    #: WebDriver BiDi representation of the value.# noqa
    webDriverValue: typing.Optional[WebDriverValue] = None
    #: Unique object identifier (for non-primitive values).# noqa
    objectId: typing.Optional[RemoteObjectId] = None
    #: Preview containing abbreviated property values. Specified for `object`type values only.# noqa
    preview: typing.Optional[ObjectPreview] = None
    #: Description is missing from the devtools protocol document.# noqa
    customPreview: typing.Optional[CustomPreview] = None


@dataclass
class CustomPreview:
    """Description is missing from the devtools protocol document."""

    #: The JSON-stringified result of formatter.header(object, config) call. Itcontains json ML array that represents RemoteObject.# noqa
    header: str
    #: If formatter returns true as a result of formatter.hasBody call thenbodyGetterId will contain RemoteObjectId for the function that returns result offormatter.body(object, config) call. The result value is json ML array.# noqa
    bodyGetterId: typing.Optional[RemoteObjectId] = None


@dataclass
class ObjectPreview:
    """Object containing abbreviated remote object value."""

    #: Object type.# noqa
    type: str
    #: True iff some of the properties or entries of the original object did notfit.# noqa
    overflow: bool
    #: List of the properties.# noqa
    properties: PropertyPreview
    #: Object subtype hint. Specified for `object` type values only.# noqa
    subtype: typing.Optional[str] = None
    #: String representation of the object.# noqa
    description: typing.Optional[str] = None
    #: List of the entries. Specified for `map` and `set` subtype values only.# noqa
    entries: typing.Optional[EntryPreview] = None


@dataclass
class PropertyPreview:
    """Description is missing from the devtools protocol document."""

    #: Property name.# noqa
    name: str
    #: Object type. Accessor means that the property itself is an accessorproperty.# noqa
    type: str
    #: User-friendly property value string.# noqa
    value: typing.Optional[str] = None
    #: Nested value preview.# noqa
    valuePreview: typing.Optional[ObjectPreview] = None
    #: Object subtype hint. Specified for `object` type values only.# noqa
    subtype: typing.Optional[str] = None


@dataclass
class EntryPreview:
    """Description is missing from the devtools protocol document."""

    #: Preview of the value.# noqa
    value: ObjectPreview
    #: Preview of the key. Specified for map-like collection entries.# noqa
    key: typing.Optional[ObjectPreview] = None


@dataclass
class PropertyDescriptor:
    """Object property descriptor."""

    #: Property name or symbol description.# noqa
    name: str
    #: True if the type of this property descriptor may be changed and if theproperty may be deleted from the corresponding object.# noqa
    configurable: bool
    #: True if this property shows up during enumeration of the properties onthe corresponding object.# noqa
    enumerable: bool
    #: The value associated with the property.# noqa
    value: typing.Optional[RemoteObject] = None
    #: True if the value associated with the property may be changed (datadescriptors only).# noqa
    writable: typing.Optional[bool] = None
    #: A function which serves as a getter for the property, or `undefined` ifthere is no getter (accessor descriptors only).# noqa
    get: typing.Optional[RemoteObject] = None
    #: A function which serves as a setter for the property, or `undefined` ifthere is no setter (accessor descriptors only).# noqa
    set: typing.Optional[RemoteObject] = None
    #: True if the result was thrown during the evaluation.# noqa
    wasThrown: typing.Optional[bool] = None
    #: True if the property is owned for the object.# noqa
    isOwn: typing.Optional[bool] = None
    #: Property symbol object, if the property is of the `symbol` type.# noqa
    symbol: typing.Optional[RemoteObject] = None


@dataclass
class InternalPropertyDescriptor:
    """Object internal property descriptor.

    This property isn't normally visible in JavaScript code.
    """

    #: Conventional property name.# noqa
    name: str
    #: The value associated with the property.# noqa
    value: typing.Optional[RemoteObject] = None


@dataclass
class PrivatePropertyDescriptor:
    """Object private field descriptor."""

    #: Private property name.# noqa
    name: str
    #: The value associated with the private property.# noqa
    value: typing.Optional[RemoteObject] = None
    #: A function which serves as a getter for the private property, or`undefined` if there is no getter (accessor descriptors only).# noqa
    get: typing.Optional[RemoteObject] = None
    #: A function which serves as a setter for the private property, or`undefined` if there is no setter (accessor descriptors only).# noqa
    set: typing.Optional[RemoteObject] = None


@dataclass
class CallArgument:
    """Represents function call argument.

    Either remote object id `objectId`, primitive `value`,
    unserializable primitive value or neither of (for undefined) them
    should be specified.
    """

    #: Primitive value or serializable javascript object.# noqa
    value: typing.Optional[typing.Any] = None
    #: Primitive value which can not be JSON-stringified.# noqa
    unserializableValue: typing.Optional[UnserializableValue] = None
    #: Remote object handle.# noqa
    objectId: typing.Optional[RemoteObjectId] = None


@dataclass
class ExecutionContextId:
    """Id of an execution context."""


@dataclass
class ExecutionContextDescription:
    """Description of an isolated world."""

    #: Unique id of the execution context. It can be used to specify in whichexecution context script evaluation should be performed.# noqa
    id: ExecutionContextId
    #: Execution context origin.# noqa
    origin: str
    #: Human readable name describing given context.# noqa
    name: str
    #: A system-unique execution context identifier. Unlike the id, this isunique across multiple processes, so can be reliably used to identify specificcontext while backend performs a cross-process navigation.# noqa
    uniqueId: str
    #: Embedder-specific auxiliary data.# noqa
    auxData: typing.Optional[object] = None


@dataclass
class ExceptionDetails:
    """Detailed information about exception (or error) that was thrown during
    script compilation or execution."""

    #: Exception id.# noqa
    exceptionId: int
    #: Exception text, which should be used together with exception object whenavailable.# noqa
    text: str
    #: Line number of the exception location (0-based).# noqa
    lineNumber: int
    #: Column number of the exception location (0-based).# noqa
    columnNumber: int
    #: Script ID of the exception location.# noqa
    scriptId: typing.Optional[ScriptId] = None
    #: URL of the exception location, to be used when the script was notreported.# noqa
    url: typing.Optional[str] = None
    #: JavaScript stack trace if available.# noqa
    stackTrace: typing.Optional[StackTrace] = None
    #: Exception object if available.# noqa
    exception: typing.Optional[RemoteObject] = None
    #: Identifier of the context where exception happened.# noqa
    executionContextId: typing.Optional[ExecutionContextId] = None
    #: Dictionary with entries of meta data that the client associated with thisexception, such as information about associated network requests, etc.# noqa
    exceptionMetaData: typing.Optional[object] = None


class Timestamp(float):
    """Number of milliseconds since epoch."""

    def to_json(self) -> Timestamp:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


class TimeDelta(float):
    """Number of milliseconds."""

    def to_json(self) -> TimeDelta:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class CallFrame:
    """Stack entry for runtime errors and assertions."""

    #: JavaScript function name.# noqa
    functionName: str
    #: JavaScript script id.# noqa
    scriptId: ScriptId
    #: JavaScript script name or url.# noqa
    url: str
    #: JavaScript script line number (0-based).# noqa
    lineNumber: int
    #: JavaScript script column number (0-based).# noqa
    columnNumber: int


@dataclass
class StackTrace:
    """Call frames for assertions or error messages."""

    #: JavaScript function name.# noqa
    callFrames: CallFrame
    #: String label of this stack trace. For async traces this may be a name ofthe function that initiated the async call.# noqa
    description: typing.Optional[str] = None
    #: Asynchronous JavaScript stack trace that preceded this stack, ifavailable.# noqa
    parent: typing.Optional[StackTrace] = None
    #: Asynchronous JavaScript stack trace that preceded this stack, ifavailable.# noqa
    parentId: typing.Optional[StackTraceId] = None


class UniqueDebuggerId(str):
    """Unique identifier of current debugger."""

    def to_json(self) -> UniqueDebuggerId:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({super().__repr__()}))"


@dataclass
class StackTraceId:
    """If `debuggerId` is set stack trace comes from another debugger and can
    be resolved there.

    This allows to track cross-debugger calls. See `Runtime.StackTrace`
    and `Debugger.paused` for usages.
    """

    #: Description is missing from the devtools protocol document.# noqa
    id: str
    #: Description is missing from the devtools protocol document.# noqa
    debuggerId: typing.Optional[UniqueDebuggerId] = None
