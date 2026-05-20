import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(1)

print("Waiting for connection...")
conn, addr = s.accept()
print("Connected to", addr)

while True:
    data = conn.recv(1024).decode()

    if not data or data.lower() == 'exit':
        print("Connection closed")
        break

    print("Client:", data)
    conn.send(data.encode())

conn.close()
s.close()
