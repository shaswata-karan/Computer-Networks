# Write a client-server application for chat using TCP. (Client side code)
import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 9090))
while True:
    data = input("Enter Text: ")
    c.send(data.encode())
    data = c.recv(1024).decode()
    print("Server:",data)
