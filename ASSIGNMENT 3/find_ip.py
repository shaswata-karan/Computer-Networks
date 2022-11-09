#Write a program to find the IP address of the system
import socket
print("Host Name:", socket.gethostname(), 
      "\nIp Address:", socket.gethostbyname(socket.gethostname()))
