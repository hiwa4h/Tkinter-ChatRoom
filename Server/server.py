import socket
import datetime

now = datetime.datetime.now()

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6969

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print(f'Server has been Started at {now.strftime("%S:%M:%H %y-%m-%d")}')

while True:
    comms, address = s.accept()
    msg = comms.recv(4096)
    print(msg.decode('utf-8'))

    
