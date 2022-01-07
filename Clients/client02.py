import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 6969

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(HOST.encode('utf=8'))

username = input('Enter a Username : ')

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))


    def send_to_server():
        s.send(full_message.encode('utf-8'))


    msg = input('Enter Your Message Here : ')
    full_message = f'[  {username}  ] -->  {msg}'
    send_to_server()
