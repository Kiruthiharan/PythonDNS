import struct
import socket

serverAddress=('localhost',8080)

clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)




message=b"hello"
clientSocket.sendto(msg,serverAddress)
    