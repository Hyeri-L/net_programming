import socket
import time

BUFF_SIZE = 1024
f = open('data.txt','w')

d1_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
d1_addr = ('localhost', 1111)
d1_s.connect(d1_addr)

d2_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
d2_addr = ('localhost', 2222)
d2_s.connect(d2_addr)

while True:
     msg = input("Press 1 or 2: ")
     
     if msg == '1':
          d1_s.send("Request".encode())
          data = d1_s.recv(BUFF_SIZE).decode()
          f.write(str(time.strftime('%c', time.localtime(time.time()))) + ": Device" + msg + ":" + data + "\n")
     elif msg == '2':
          d2_s.send("Request".encode())
          data = d2_s.recv(BUFF_SIZE).decode()
          f.write(str(time.strftime('%c', time.localtime(time.time()))) + ": Device" + msg + ":" + data + "\n")
     elif msg == 'quit':
          d1_s.send('quit'.encode())
          d2_s.send('quit'.encode())
          break

d1_s.close()
d2_s.close()
f.close()

          