# -*- coding: utf-8 -*-

import socket
import struct

port=8080
ip='127.0.0.1'

serverSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((ip,port))
hosts={}

def readHost():
    datafile = open("dns-master.txt",'r')

    if datafile:
        print("open")
        for line in datafile:
            if line[0]!='#':
                print(line)
                data=line.split(" ")
                hosts[data[0]]=data[4]
        print(hosts)        
    else :
        print("Error! cannot open dns_master.txt")
        
readHost()

def buildResponse(data):
    question=data[5].decode("utf-8").split(" ") 
    print (question[0])
    
    mType=2
    mIdent=data[2]
    qLen=data[3]
    
    qSelect=str(question[0])
    Answer=''
    
    if (qSelect in hosts.keys()):
        Answer=(qSelect+" A IN "+hosts[qSelect]).encode("utf-8")
        print(Answer)
        rCode=0
        aLen=len(Answer)
    else:
        rCode=1
        Answer=b''
        aLen=len(Answer)

    qSelect=str(question[0]).encode("utf-8")
    res=struct.pack("hhihh32s64s",mType,rCode,mIdent,qLen,aLen,qSelect,Answer)
    return res
    


while 1:
    data,address=serverSocket.recvfrom(512)
    #print(len(data))
    msg=struct.unpack("hhihh32s",data)
    #print(len(msg))
    print(msg)
    res=buildResponse(msg)
    serverSocket.sendto(res,address)
    
    
