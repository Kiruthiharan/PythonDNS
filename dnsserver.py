# -*- coding: utf-8 -*-

import socket

port=8080
ip='127.0.0.1'

serverSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((ip,port))

def buildResponse(data):
    TransactionID=data[0:2]
    TID=''
    print(TransactionID)
    for byte in TransactionID:
        TID += hex(byte)[2:]
    print(TID)
    MType=''
    RCode=''
    Mident=''
    Qlength=''
    ALength=''
    QSelect=''
    Answer=''

while 1:
    data,address=serverSocket.recvfrom(512)
    print (data)
   
    #res=buildResponse(data)
    #serverSocket.sendto(res,address)