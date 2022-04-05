from socket import *


BUFF_SIZE = 1024
port = 1234

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))

mboxID_msg = {} 

while True:    
    data, addr = s_sock.recvfrom(BUFF_SIZE)

    cmd, mboxID, *msg = data.decode().split(maxsplit=2) 
    msg = " ".join(msg) 

    if cmd == 'send': 
        if mboxID not in mboxID_msg: 
            mboxID_msg[mboxID] = []  
        mboxID_msg[mboxID].append(msg) 
        s_sock.sendto("OK".encode(), addr) 

    elif cmd == 'receive': 
        if (mboxID not in mboxID_msg) or (not(mboxID_msg[mboxID])):
            s_sock.sendto("No messages".encode(), addr) 
        else: 
            s_sock.sendto(mboxID_msg[mboxID].pop(0).encode(), addr) 

    elif data.decode() == "quit": 
        break

s_sock.close() 