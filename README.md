# 3a.CREATION FOR ECHO CLIENT AND ECHO SERVER USING TCP SOCKETS

# AIM
To write a python program for creating Echo Client and Echo Server using TCP Socket Links.

## ALGORITHM
1. Import the socket module.
2. Create socket connection using TCP.
3. Bind the server with localhost and port number.
4. Establish connection between client and server.
5. Client sends message to server.
6. Server receives the message and echoes it back to client.
7. Display the received message.
8. Stop the program.

## PROGRAM

### echo_server.py
```python
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
```

### echo_client.py
```python
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
```

## OUTPUT

### Server Side
```text
Waiting for connection...
Connected to ('127.0.0.1', 52314)
Client: Hello
Client: TCP Socket
Connection closed
```

### Client Side
```text
Enter message: Hello
Server: Hello
Enter message: TCP Socket
Server: TCP Socket
Enter message: exit
```

## RESULT
Thus, the python program for creating Echo Client and Echo Server using TCP Socket Links was successfully created and executed.
