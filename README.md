
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


 -----

 ## Contributing 

 This project takes the devtools protocol json files and based on those generates python source code.  It is not currently building
 AST trees to unparse but it may do so in future, for now it is generating relatively complex source code (largely in the form of
 python dataclasses).  In order to generate the files again do the following:


 ```shell
 poetry shell
 poetry install
 python -m python_cdp.generate
 tox -e linting  # format the generated source code (will unstage)
 # inspect the `python_cdp/cdp/*` directory.
 ```

The CDP protocol repository is a submodule within this repository and will be automatically updated when google releases changes on
the upstream repository.

The power of keeping the repository auto generated is that it requires minimmal maintenance work when the `tip-of-the-tree` for the
protocol is updated which is pretty much every day, the target is forever moving.

-----

## Useful utilities

The below examples use the power `jq` tool to generate output that can be useful for debugging or checking things that should be
generated etc.

### Generating all the possible properties that an `Event` class may need:

