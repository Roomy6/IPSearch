#!/bin/python

# Import stuff
import sys
import time
import random
import socket
from datetime import datetime as date

# 127.0.0.1     80
#  1  2 3 4    port

#addr = input("Enter IP: ")
portStart = int(input("Enter Port Start: "))
portEnd = int(input("Enter Port End: "))

# Define the target
if len(sys.argv) == 2: # name.py = 1 argument
    target = socket.gethostbyname(sys.argv[1]) # Convert hostname to IPv4

else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 search.py <IP>")

# Banner
print("~" * 50)
print("Scanning target: " + target)
print("Time Started: " + str(date.now()))
print("~" * 50)

try:
    for port in range(portStart, portEnd + 1): # 80 goes to 79 (whats why the + 1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # Wait 1 second continue
        result = s.connect_ex((target,port))

        print("[*]Checking port: {}".format(port)) #DEBUG

        if result == 0:
            print("[*]Port {} is open".format(port))

            # Save information to a txt in `out/list.txt`
            with open("out/list.txt", "w") as f:
                f.writelines('\n' + str(target) + ":" + str(port))

        s.close()

except KeyboardInterrupt:
    print("\n[!]Exiting...")
    sys.exit()

except socket.gaierror:
    print("[!]Hostname could not be resolved!")
    sys.exit()

except socket.error:
    print("[!]Could not connect to server!")
    sys.exit()