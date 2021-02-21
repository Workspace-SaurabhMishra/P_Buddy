import socket
import threading as thread
import pickle

#configurations
port = 8091
host = '0.0.0.0'

def listen(server):
    conn,addr = server.accept()
    print(conn)
    client_id = conn.recv(1024)
    client_id = client_id.decode("utf-8")
    print(client_id)
    conn.send(b"done")
    peer = conn.getpeername()
    x = socket.socket().connect(peer)
    print(x)
    # x = socket.socket()
    # y = x.connect(())


s = socket.socket()
s.bind((host,port))
s.listen(5)
listen(s)


