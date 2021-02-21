import socket
import threading as thread
from json import JSONEncoder,JSONDecoder
connected = []
host = ""
port = 8080

def server_starter(host,port):
    s = socket.socket()
    s.bind((str(host),port))
    s.listen()
    return s

def listener():
    while  True:
        # print("l")
        conn, addr = s.accept()
        print("connected to", addr)
        connected.append(conn)
        conn.send(b"You are connected")

def broadcaster(client_id):
    while True:
        client_id.send(input("Enter message"))


s = server_starter(host,port)
# thread.start_new_thread(listener,(s,))
# thread.start_new_thread(broadcaster,(connected,))
thread.Thread(target=broadcaster,args=(client_id,)).start()
thread.Thread(target=listener).start()