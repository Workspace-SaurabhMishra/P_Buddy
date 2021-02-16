import  websockets
import asyncio

def starter_func():
    start_server = websockets.serve(start, "localhost", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

async def start(ws,path):
    while True:
        mssg = await ws.recv()
        print("<<{0}".format(mssg))
        send_mssg = ">>You are {0}".format(mssg)
        await ws.send(send_mssg)

#initiating server
starter_func()














































#!/usr/bin/env python3
#
# import socket
#
# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)