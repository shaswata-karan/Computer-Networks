#Write a program to implement simple client-server application using UDP.
#Server side code:
import socket
localIP= "127.0.0.1"
localPort= 20001
bufferSize= 1024
msg_From_Server= "Hello"
bytes_To_Send = str.encode(msg_From_Server)
Server_Socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
Server_Socket.bind((localIP, localPort))
print("Server listening...")
while(True):
    bytes_Address_Pair =Server_Socket.recvfrom(bufferSize)
    message = bytes_Address_Pair[0]
    address = bytes_Address_Pair[1]
    client_Msg = "Message from Client:{}".format(message)
    client_IP  = "Client IP Address:{}".format(address)
    print(client_Msg)
    print(client_IP)
    Server_Socket.sendto(bytes_To_Send, address)
