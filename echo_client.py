import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    msg = input("Enter message: ")
    s.send(msg.encode())

    if msg.lower() == 'exit':
        break

    data = s.recv(1024).decode()
    print("Server:", data)

s.close()
