#!/bin/python


# Import stuff
import sys
import time
import random
import socket
from datetime import datetime as date

# Define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Convert hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Useage: python3 search.py <IP>")

# Banner
print("~" * 50)
print("Scanning target: " + target)
print("Time Started: " + str(date.now()))
print("~" * 50)

try:
    for port in range(1, 81): # 80 goes to 79 (whats why the +1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # Wait 1 second continue
        result = s.connect_ex((target,port))
        print("[*]Checking port: {}".format(port))
        if result == 0:
            print("[*]Port {} is open".format(port))
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