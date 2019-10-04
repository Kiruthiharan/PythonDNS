import time
import struct
import socket

serverAddress=('localhost',8080)
message='host1.student.test A IN'

clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)




message=b"hello"
clientSocket.sendto(message,serverAddress)
    

