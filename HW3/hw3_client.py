import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost',9000)
s.connect(addr)

while True:
    msg = input('Enter two integers to calculate:')

    if msg == 'q':
        break

    s.send(msg.encode())
    print('Received message:', s.recv(1024).decode())

    s.close() 