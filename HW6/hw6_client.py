from socket import *

BUFF_SIZE = 1024
port = 1234

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port))

while True:
    msg = input("Enter a message:(\"send mboxId message\") or (\"receive mboxId\") : ")
    
    c_sock.sendto(msg.encode(), ('localhost', port))
    if msg == 'quit':    
        break
    else:  
        msg, addr = c_sock.recvfrom(BUFF_SIZE) 
        print(msg.decode())
c_sock.close() 