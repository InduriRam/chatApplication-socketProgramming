import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5050))

full_message = ''

while True:
    full_message = ''
    new_msg = True
    while True:
        msg = s.recv(10)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            messagelen = int(msg[:HEADERSIZE])
            new_msg = False
        full_message += msg.decode("utf-8")
        if len(full_message)-HEADERSIZE == messagelen:
            print("Entire message recieved")
            print(full_message[HEADERSIZE:])
            new_msg = True
            full_message = ''

    print(full_message )

