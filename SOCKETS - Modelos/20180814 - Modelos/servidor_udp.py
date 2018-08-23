import socket

HOST = ''
PORT = 50000


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.bind((HOST, PORT))

while True:
   msg, cliente = udp.recvfrom(512)
   print(cliente, msg.decode('utf-8'))

udp.close()
