#Write a program to implement simple client-server application using UDP.
#Client side code:
import socket
msg_From_Client= "Hi"
bytes_To_Send= str.encode(msg_From_Client)
server_Address_Port= ("127.0.0.1", 20001)
bufferSize= 1024
Client_Socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
Client_Socket.sendto(bytes_To_Send, server_Address_Port)
msg_From_Server = Client_Socket.recvfrom(bufferSize)
msg = "Messagefrom Server {}".format(msg_From_Server[0])
print(msg)
