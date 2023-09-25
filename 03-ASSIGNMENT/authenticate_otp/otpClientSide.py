#Write a program using client server socket programming: Client needs to authenticate itself by entering a server defined string as a password (like OTP) and then to say Hi to server. Server replies with a Hello. Press any key to exit.
#Client side code:
import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 9090))
data = c.recv(1024).decode()
print(data, end=" ")
otp = input()
c.send(otp.encode())
data = c.recv(1024).decode()
print(data)
if data == "You are Authenticated":
    data = input("Enter Text: ")
    c.send(data.encode())
    data = c.recv(1024).decode()
    print("Server:",data)
else:
    c.close()
