import asyncio
import websockets
async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as ws:
        greeting = await ws.recv()
        print(f"< {greeting}")

async def reg_req():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as ws:
        await ws.send("Admin")
        mssg = await ws.recv()
        print(mssg)

asyncio.get_event_loop().run_until_complete(reg_req())
asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()