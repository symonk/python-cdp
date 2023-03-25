"""This module is just a place holder for now to experiment with websockets etc."""

import asyncio
import json
from pprint import pprint as print

import websockets


class CdpClient:
    """An asynchronous client that can dispatch commands to a remote debuggable instance of any CDP enabled browser."""


async def hello():
    # This is a dummy implementation for messing around with the CDP.
    async with websockets.connect(
        "ws://127.0.0.1:9222/devtools/browser/d456053b-d450-4b42-89dd-d8d5ed5a5898",
    ) as socket:
        await socket.send(json.dumps({"id": 1, "method": "Target.getTargets", "params": {}}))
        targets = json.loads(await socket.recv())
        page_target = [t for t in targets["result"]["targetInfos"] if t["type"] == "page"][0]["targetId"]
        await socket.send(
            json.dumps(
                {"id": 2, "method": "Target.attachToTarget", "params": {"targetId": page_target, "flatten": True}},
            ),
        )
        session_id = json.loads(await socket.recv())["params"]["sessionId"]
        await socket.send(json.dumps({"sessionId": session_id, "id": 3, "method": "Network.enable", "params": {}}))
        while True:
            print(json.loads(await socket.recv()))


asyncio.run(hello())
