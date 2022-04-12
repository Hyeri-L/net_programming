from socket import *
import random

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
     sock.settimeout(None)
     
     while True:
          data, addr = sock.recvfrom(BUFF_SIZE)
          
          if random.random() <= 0.5: # 50%의 확률로 손실 발생시
               continue
          else:
               sock.sendto(b'ack', addr)   
               print('<-', data.decode())    
               break

     msg = input('->')
     reTx = 0
     while reTx <=3:
          resp = str(reTx) + ' ' + msg
          sock.sendto(resp.encode(), addr)
          sock.settimeout(2)     # timeout 시간 2초로 설정. 2초 내 메시지 미 수신시 timeout 예외 발생.
          
          try:
               data, addr = sock.recvfrom(BUFF_SIZE)
          except timeout:
               reTx += 1      # timeout 발생 시 재전송 횟수 1 증가시키고, 재전송
               continue
          else:
               break 