#!/bin/python

# Import stuff
from cgitb import reset
import sys
import time
import socket
import colorama
from datetime import datetime as date
from colorama import Fore, Back, Style
from random import randint

# 127.0.0.1     80
#  1  2 3 4    port

#addr = input("Enter IP: ")
portStart = int(input(Fore.BLUE + "Enter Port Start: "))
portEnd = int(input(Fore.BLUE + "Enter Port End: "))

def ip_gen():
    num = randint(0, 256)
    return num

# Define the target
if len(sys.argv) == 2: # name.py = 1 argument
    #target = socket.gethostbyname(sys.argv[1]) # Convert hostname to IPv4
    print('ye')

else:
    print(Fore.RED + "[!] Invalid amount of arguments.")
    print(Fore.RED + "[!] Syntax: python3 search.py <IP>")

target = "{}.{}.{}.{}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))

# Banner
print(Fore.CYAN + "~" * 20)
print("Scanning target: " + target)
print("~" * 20 + Fore.RESET)

try:
    for port in range(portStart, portEnd + 1): # 80 goes to 79 (whats why the + 1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # Wait 1 second, continue
        result = s.connect_ex((target, port))

        print("[" + Fore.RED + "DBG" + Fore.RESET + "] " + "Checking port: {}".format(port)) #DEBUG
        print(target)

        if result == 0:
            print(Fore.GREEN + "[*] Port {} is open".format(port))

            # Save information to a txt in `out/list.txt`
            with open("out/list.txt", "a") as a:
                a.write(str(target) + ":" + str(port) + '\n')

        s.close()

except KeyboardInterrupt:
    print(Fore.YELLOW + "\n[!] Exiting...")
    sys.exit()

except socket.gaierror:
    print(Fore.RED + "[!] {} Hostname could not be resolved!".format(target))
    sys.exit()

except socket.error:
    print(Fore.RED + "[!] Could not connect to server!")
    sys.exit()