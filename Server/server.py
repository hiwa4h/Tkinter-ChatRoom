import socket
import datetime

now = datetime.datetime.now()

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6969

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print(f'Server has been Started at {now.strftime("%S:%M:%H %y-%m-%d")}')

present_clients = []
collected_ip = False
ip_address_list = []

while True:
    comms, address = s.accept()
    if not collected_ip:
        ip_address = comms.recv(4096)
        print(ip_address.decode('utf-8'))
        ip_address_list.append(ip_address.decode('utf-8'))
        print(f'{ip_address_list[0]} has connected to the Server!')
        collected_ip = True
    msg = comms.recv(4096)
    print(msg.decode('utf-8'))
