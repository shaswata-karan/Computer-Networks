# Write a program using client server socket programming: Client needs to authenticate itself by entering a server defined string as a password (like OTP) and then to say Hi to server. Server replies with a Hello. Press any key to exit.
#Server side code
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 9090))
s.listen()
(c, cip) = s.accept()
c.send("Enter OTP:".encode())
otp = c.recv(1024).decode()
if otp == '8894':
    c.send("You are Authenticated".encode())
    data = c.recv(1024).decode()
    print("Client:",data)
    data = input("Enter Text: ")
    c.send(data.encode())
else:
    c.send("You are Not Authenticated".encode())
s.close()
