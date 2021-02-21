import socket
s = socket.socket(family=socket.AF_INET,type = socket.SOCK_STREAM)
port = 8091
s.connect(('0.0.0.0', port))
s.send(b"12345")
conn_tuple = s.getsockname()
s.detach()
s = socket.socket()
s.bind(conn_tuple)

while True:
    s.accept()
    x = s.recv(1024)
    if x.decode("utf-8") == b"":
        print(x)
