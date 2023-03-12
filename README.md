
[![version](https://img.shields.io/pypi/v/python-cdp?color=green)](https://pypi.org/project/python-cdp/)
[![supports](https://img.shields.io/pypi/pyversions/python-cdp?color=blue&label=supports)](https://pypi.org/project/python-cdp/)
[![test coverage](https://codecov.io/gh/symonk/python-cdp/branch/main/graph/badge.svg)](https://codecov.io/gh/symonk/python-cdp)
[![docs](https://img.shields.io/badge/documentation-online-brightgreen.svg)](https://symonk.github.io/python-cdp/)


# python-cdp (**ALPHA**)

-----

`python-cdp` is a python library that can be used to attach to a remotely running chrome instance for debugging.  In order to
connect to the browser it should be launched with `--remote-debugging-port=X`.  `python-cdp` exposes a simple client for `asyncio`
and various wrappers for the devtools protocol.  This is all event driven and bidirectional via websockets.

`python-cdp` will expose a full interface for all cdp:
    
    * Commands
    * Events
    * Types

-----

Right now the aim for `1.0.0` is to implement the `stable RC 1.3` version of the chrome devtools protocol and include as part of that
a simple asynchronous client based on `asyncio` to support interactions with the browser.