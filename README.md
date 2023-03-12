
[![version](https://img.shields.io/pypi/v/python-cdp?color=green)](https://pypi.org/project/python-cdp/)
[![supports](https://img.shields.io/pypi/pyversions/python-cdp?color=blue&label=supports)](https://pypi.org/project/python-cdp/)
[![test coverage](https://codecov.io/gh/symonk/python-cdp/branch/main/graph/badge.svg)](https://codecov.io/gh/symonk/python-cdp)
[![docs](https://img.shields.io/badge/documentation-online-brightgreen.svg)](https://symonk.github.io/python-cdp/)


# python-cdp (**ALPHA**)

-----

`python-cdp` is a python library that can be used to attach to a remotely running chrome instance for debugging.  In order to
connect to the browser it should be launched with `--remote-debugging-port=X`.  `python-cdp` exposes a simple client for `asyncio`
and various wrappers for the devtools protocol.  This is all event driven and bidirectional via websockets.

-----

#### Low Level Details

Chrome devtools protocol is built on the concept of `Domains`.  These domains typically expose an API
in the form of:

    * Commands
    * Types
    * Events

`python-cdp` generates a per domain python module in idiomatic python syntax, fully typed hinted
for autocompletion assistance.

Types exposed by the protocol fall in to a few categories:

    * Primitive (tho not technically in python) types
        * string
        * integer
        * boolean
        * array
        * number
        * object
        * any
    * Enum types
    * Plain old python objects

*Primitive* Types (again to use the term loosely) end up in simple subclasses of their primitive types
and all `object` types generate a fully type hinted idiomatic python class

-----
### Goals for Future

`python-cdp` aims to implement a typed API for the protocol (and maintain) that fully going forward.  Eventually
it hopes to expose a websocket connection/API for actually interacting with the protocol but that is a way
off yet.