# Copyright 2023 Jeanette Villanueva jivillan@bu.edu
# Copyright 2023 Tristen Liu tristenl@bu.edu

"""
UDP client - IPv4
"""
import sys
import socket as s
import os
import hashlib

# create client socket 
client_soc = s.socket(s.AF_INET, s.SOCK_DGRAM)
filename = sys.argv[1]
request_msg = "GET {}".format(filename) + "\r\n"

# encode the message before sending it 
bstring = request_msg.encode()

# default IP addr of server & port 
if (len(sys.argv) > 2):
    ip = sys.argv[2]
else:
     ip = "127.0.0.1"

# client_soc.sendto(bstring, (ip,9000))

print(request_msg)
print(ip)
