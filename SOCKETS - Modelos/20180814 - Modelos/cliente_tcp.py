import socket

HOST = '10.20.1.171'
PORT = 50000

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect((HOST, PORT))

print('Para sair use CTRL+X\n')

msg = input('Digite a mensagem: ')

while msg != '\x18':
   msg = msg.encode('utf-8')
   print(msg)
   tcp_socket.send(msg)
   msg = input('Digite a mensagem: ')

tcp_socket.close()
