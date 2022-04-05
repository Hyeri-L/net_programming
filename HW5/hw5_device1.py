from socket import *
import random

BUFF_SIZE = 1024

d1_s = socket()
d1_s.bind(('',1111))
d1_s.listen(10)

while True:
     c, addr = d1_s.accept()
     msg_d1 = c.recv(BUFF_SIZE).decode()

     if msg_d1 == 'Request':
          temp = random.randint(0,40)
          humid = random.randint(0,100)
          lilum = random.randint(70,150)
          res = "Temp="+str(temp)+", "+"Humid="+str(humid)+", "+"lilum="+str(lilum)+"\n\r"
          c.send(res.encode())

     elif msg_d1 == 'quit':
          c.close()
          break

     