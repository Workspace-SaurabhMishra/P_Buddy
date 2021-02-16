import websockets
import asyncio

def starter_func():
    try:
        asyncio.get_event_loop().run_until_complete(start())
    except:
        start()

async def start():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as ws:
        await ws.send(input("<<"))
        print(await ws.recv())
        try:
            while True:
                await ws.send(input("<<"))
                print(">>", await ws.recv())
        except:
            starter_func()

#Initiating Client
starter_func()

































#!/usr/bin/env python3
#
# import socket
#
# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)
#
# print('Received', repr(data))