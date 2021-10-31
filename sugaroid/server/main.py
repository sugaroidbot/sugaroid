

import asyncio
import uuid
import gc
import copy
from typing import Optional

import websockets
from sugaroid.sugaroid import Sugaroid

connected_users: dict = {}
sg: Sugaroid = Sugaroid()
default_globals = copy.copy(sg.chatbot.globals)


async def brain(websocket, path):

    u_raw: str = path.lstrip("/")
    u: Optional[uuid.UUID] = None
    try:
        u = uuid.UUID(u_raw)
    except ValueError:
        print("Invalid request uuid", u_raw)
        websocket.close()
    connected_users[u] = copy.deepcopy(default_globals)

    try:

        async for message in websocket:
            print(f"[RECV][{u}]", message)
            try:
                sg.chatbot.globals = connected_users[u]
                bot_response = str(sg.parse(message))
                await websocket.send(bot_response)
                print(f"[SEND][{u}]", bot_response)
                connected_users[u] = sg.chatbot.globals
                sg.chatbot.globals = default_globals
            except websockets.WebSocketException:
                print("Connection to user closed unexpectedly")
                await websocket.close()
                del connected_users[u]
                gc.collect(2)
            except Exception as e:
                print(f"[SEND][{u}]", e)
                await websocket.send(e)
    except websockets.WebSocketException:
        pass
    finally:
        await websocket.close()
        del connected_users[u]
        gc.collect(2)


async def ws():
    async with websockets.serve(brain, "localhost", 19671):
        await asyncio.Future()


def main():
    asyncio.run(ws())
