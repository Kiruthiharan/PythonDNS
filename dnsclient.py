import struct
import socket
import random

time_out_count=0

while(time_out_count<3):
    server='127.0.0.1'
    port=8080
    host='host99.student.test'

    serverAddress=(server,port)

    clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.settimeout(1.0)

    mType=1
    rCode=0
    mIden=random.randint(1,101)
    ques=(host+' A IN').encode("utf-8")
    qLen=len(ques)
    aLen=0

    print("Sending Request to ",server,", ",port,":")
    print("Message ID: ", mIden)
    print("Question Length: ", qLen)
    print("Answer Length: ", aLen)
    print("Question: ", (host+' A IN'))

    req=struct.pack("hhihh32s",mType,rCode,mIden,qLen,aLen,ques)

    clientSocket.sendto(req,serverAddress)
    try:
        data,address=clientSocket.recvfrom(1024)
        res=struct.unpack("hhihh32s64s",data)

        print("\n")
        print("Received Response from ",address[0],", ",address[1],":")
        print("Return Code: ", res[1])
        print("Message ID: ", res[2])
        print("Question Length: ", res[3])
        print("Answer Length: ", res[4])
            
        if(res[1]==1):
            print("host-not-exist.student.test A IN")
        else:
            print("Question: ", res[5].decode("utf-8"))
            print("Answer: ", res[6].decode("utf-8"))

        #response success then terminate the loop
        break

    except socket.timeout:
        time_out_count=time_out_count+1
        print('REQUEST TIMED OUT')
        






