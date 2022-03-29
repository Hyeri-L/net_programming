import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()

    while True:
        print('connection from', addr)
        data = client.recv(1024)
     
        try:         
            data = data.decode()
        except:
            client.send(b'Try again!')
        else:
          if not data:
             break

        x,y = data.split()
        form = data.split()
        x = int(x)
        y = int(y)

        if form == '+':
            result = x+y
        elif form == '-':
            result = x-y
        elif form == '*' :
            result = x*y
        elif form == '/':
            result = round(x/y, 1)

        client.send(str(result).encode())

    client.close()