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
    """Unique script identifier."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class WebDriverValue:
    """Represents the value serialiazed by the WebDriver BiDi specification
    https://w3c.github.io/webdriver-bidi."""

    #: Description is missing from the devtools protocol document.
    type: str
    #: Description is missing from the devtools protocol document.
    value: str
    #: Description is missing from the devtools protocol document.
    objectId: str


class RemoteObjectId(str):
    """Unique object identifier."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class UnserializableValue(str):
    """Primitive value which cannot be JSON-stringified.

    Includes values `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint
    literals.
    """

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class RemoteObject:
    """Mirror object referencing original JavaScript object."""

    #: Object type.
    type: str
    #: Object subtype hint. Specified for `object` type values only. NOTE: Ifyou change anything here, make sure to also update `subtype` in `ObjectPreview`and `PropertyPreview` below.
    subtype: str
    #: Object class (constructor) name. Specified for `object` type values only.
    className: str
    #: Remote object value in case of primitive values or JSON values (if it wasrequested).
    value: str
    #: Primitive value which can not be JSON-stringified does not have `value`,but gets this property.
    unserializableValue: str
    #: String representation of the object.
    description: str
    #: WebDriver BiDi representation of the value.
    webDriverValue: str
    #: Unique object identifier (for non-primitive values).
    objectId: str
    #: Preview containing abbreviated property values. Specified for `object`type values only.
    preview: str
    #: Description is missing from the devtools protocol document.
    customPreview: str


@dataclass
class CustomPreview:
    """Description is missing from the devtools protocol document."""

    #: The JSON-stringified result of formatter.header(object, config) call. Itcontains json ML array that represents RemoteObject.
    header: str
    #: If formatter returns true as a result of formatter.hasBody call thenbodyGetterId will contain RemoteObjectId for the function that returns result offormatter.body(object, config) call. The result value is json ML array.
    bodyGetterId: str


@dataclass
class ObjectPreview:
    """Object containing abbreviated remote object value."""

    #: Object type.
    type: str
    #: Object subtype hint. Specified for `object` type values only.
    subtype: str
    #: String representation of the object.
    description: str
    #: True iff some of the properties or entries of the original object did notfit.
    overflow: str
    #: List of the properties.
    properties: str
    #: List of the entries. Specified for `map` and `set` subtype values only.
    entries: str


@dataclass
class PropertyPreview:
    """Description is missing from the devtools protocol document."""

    #: Property name.
    name: str
    #: Object type. Accessor means that the property itself is an accessorproperty.
    type: str
    #: User-friendly property value string.
    value: str
    #: Nested value preview.
    valuePreview: str
    #: Object subtype hint. Specified for `object` type values only.
    subtype: str


@dataclass
class EntryPreview:
    """Description is missing from the devtools protocol document."""

    #: Preview of the key. Specified for map-like collection entries.
    key: str
    #: Preview of the value.
    value: str


@dataclass
class PropertyDescriptor:
    """Object property descriptor."""

    #: Property name or symbol description.
    name: str
    #: The value associated with the property.
    value: str
    #: True if the value associated with the property may be changed (datadescriptors only).
    writable: str
    #: A function which serves as a getter for the property, or `undefined` ifthere is no getter (accessor descriptors only).
    get: str
    #: A function which serves as a setter for the property, or `undefined` ifthere is no setter (accessor descriptors only).
    set: str
    #: True if the type of this property descriptor may be changed and if theproperty may be deleted from the corresponding object.
    configurable: str
    #: True if this property shows up during enumeration of the properties onthe corresponding object.
    enumerable: str
    #: True if the result was thrown during the evaluation.
    wasThrown: str
    #: True if the property is owned for the object.
    isOwn: str
    #: Property symbol object, if the property is of the `symbol` type.
    symbol: str


@dataclass
class InternalPropertyDescriptor:
    """Object internal property descriptor.

    This property isn't normally visible in JavaScript code.
    """

    #: Conventional property name.
    name: str
    #: The value associated with the property.
    value: str


@dataclass
class PrivatePropertyDescriptor:
    """Object private field descriptor."""

    #: Private property name.
    name: str
    #: The value associated with the private property.
    value: str
    #: A function which serves as a getter for the private property, or`undefined` if there is no getter (accessor descriptors only).
    get: str
    #: A function which serves as a setter for the private property, or`undefined` if there is no setter (accessor descriptors only).
    set: str


@dataclass
class CallArgument:
    """Represents function call argument.

    Either remote object id `objectId`, primitive `value`,
    unserializable primitive value or neither of (for undefined) them
    should be specified.
    """

    #: Primitive value or serializable javascript object.
    value: str
    #: Primitive value which can not be JSON-stringified.
    unserializableValue: str
    #: Remote object handle.
    objectId: str


@dataclass
class ExecutionContextId:
    """Id of an execution context."""


@dataclass
class ExecutionContextDescription:
    """Description of an isolated world."""

    #: Unique id of the execution context. It can be used to specify in whichexecution context script evaluation should be performed.
    id: str
    #: Execution context origin.
    origin: str
    #: Human readable name describing given context.
    name: str
    #: A system-unique execution context identifier. Unlike the id, this isunique across multiple processes, so can be reliably used to identify specificcontext while backend performs a cross-process navigation.
    uniqueId: str
    #: Embedder-specific auxiliary data.
    auxData: str


@dataclass
class ExceptionDetails:
    """Detailed information about exception (or error) that was thrown during
    script compilation or execution."""

    #: Exception id.
    exceptionId: str
    #: Exception text, which should be used together with exception object whenavailable.
    text: str
    #: Line number of the exception location (0-based).
    lineNumber: str
    #: Column number of the exception location (0-based).
    columnNumber: str
    #: Script ID of the exception location.
    scriptId: str
    #: URL of the exception location, to be used when the script was notreported.
    url: str
    #: JavaScript stack trace if available.
    stackTrace: str
    #: Exception object if available.
    exception: str
    #: Identifier of the context where exception happened.
    executionContextId: str
    #: Dictionary with entries of meta data that the client associated with thisexception, such as information about associated network requests, etc.
    exceptionMetaData: str


class Timestamp(float):
    """Number of milliseconds since epoch."""

    def to_json(self) -> float:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


class TimeDelta(float):
    """Number of milliseconds."""

    def to_json(self) -> float:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class CallFrame:
    """Stack entry for runtime errors and assertions."""

    #: JavaScript function name.
    functionName: str
    #: JavaScript script id.
    scriptId: str
    #: JavaScript script name or url.
    url: str
    #: JavaScript script line number (0-based).
    lineNumber: str
    #: JavaScript script column number (0-based).
    columnNumber: str


@dataclass
class StackTrace:
    """Call frames for assertions or error messages."""

    #: String label of this stack trace. For async traces this may be a name ofthe function that initiated the async call.
    description: str
    #: JavaScript function name.
    callFrames: str
    #: Asynchronous JavaScript stack trace that preceded this stack, ifavailable.
    parent: str
    #: Asynchronous JavaScript stack trace that preceded this stack, ifavailable.
    parentId: str


class UniqueDebuggerId(str):
    """Unique identifier of current debugger."""

    def to_json(self) -> str:
        return self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({super().__repr__()})"


@dataclass
class StackTraceId:
    """If `debuggerId` is set stack trace comes from another debugger and can
    be resolved there.

    This allows to track cross-debugger calls. See `Runtime.StackTrace`
    and `Debugger.paused` for usages.
    """

    #: Description is missing from the devtools protocol document.
    id: str
    #: Description is missing from the devtools protocol document.
    debuggerId: str
