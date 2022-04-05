from socket import *
import random

BUFF_SIZE = 1024

d2_s = socket()
d2_s.bind(('',2222))
d2_s.listen(10)

while True:
     c, addr = d2_s.accept()
     msg_d2 = c.recv(BUFF_SIZE).decode()

     if msg_d2 == 'Request':
          heartbeat = random.randint(40,140)
          steps = random.randint(2000,6000)
          cal = random.randint(1000,4000)
          res = "Heartbeat="+str(heartbeat)+", "+"Steps="+str(steps)+", "+"Cal="+str(cal)+"\n\r"
          c.send(res.encode())

     elif msg_d2 == 'quit':
          c.close()
          break

     