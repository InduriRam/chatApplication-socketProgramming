import socket
import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1729)) #1729 is port number
s.listen(5)  #5 is size of the queue

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established")
    msg = "welcome to the server human!"
    msg = f'{len(msg):<{HEADERSIZE}}'+ msg
    clientsocket.send(bytes(msg,"utf-8"))
    while True:
        time.sleep(4)
        msg = f"the time is {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}'+msg
        clientsocket.send(bytes(msg,"utf-8"))

