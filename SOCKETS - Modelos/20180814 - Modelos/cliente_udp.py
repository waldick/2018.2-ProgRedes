import socket

HOST = '10.20.1.171'
PORT = 50000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print((HOST, PORT))
print('Para sair use CTRL+X\n')

msg = input('Digite a mensagem: ')

while msg != '\x18':
   msg = msg.encode('utf-8')
   udp.sendto(msg, (HOST, PORT))
   msg = input('Digite a mensagem: ')

udp.close()
