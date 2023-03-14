
[![version](https://img.shields.io/pypi/v/python-cdp?color=green)](https://pypi.org/project/python-cdp/)
[![supports](https://img.shields.io/pypi/pyversions/python-cdp?color=blue&label=supports)](https://pypi.org/project/python-cdp/)
[![test coverage](https://codecov.io/gh/symonk/python-cdp/branch/main/graph/badge.svg)](https://codecov.io/gh/symonk/python-cdp)
[![docs](https://img.shields.io/badge/documentation-online-brightgreen.svg)](https://symonk.github.io/python-cdp/)


# python-cdp (**ALPHA**)

-----

`python-cdp` is a python library that can be used to attach to a remotely running chrome instance for debugging.  In order to
connect to the browser it should be launched with `--remote-debugging-port=X`.  `python-cdp` exposes a simple client for `asyncio`
and various wrappers for the devtools protocol.  This is all event driven and bidirectional via websockets.

The protocol itself at the tip of tree is moving fast, this library aims to support all domains that are not currently deprecated.


-----

#### Low Level Details

Chrome devtools protocol is built on the concept of `Domains`.  These domains typically expose an API
in the form of:

    * Commands
    * Types
    * Events

Each `Domain` advertised by the CDP will have its own module file written in `python_cdp/cdp/{domain}.py` and have fully
type hinted classes for (de)serialisation.

-----
### Goals for Future

`python-cdp` aims to implement a typed API for the protocol (and maintain) that fully going forward.  Eventually
it hopes to expose a websocket connection/API for actually interacting with the protocol but that is a way
off yet.

 - Full marshalling capabilities for all non deprecated domains.
 - An `asyncio` client for interacting and connecting to chrome in debug mode.
 - Useful utilities for making interactions that little bit easier.
 - 100% type hinted code base
 - Completely auto generated client to make changes and releases as pain free as possible.
 - Auto detection of upstream protocol rollups and auto releases triggered.