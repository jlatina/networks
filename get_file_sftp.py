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
request_msg = "GET {}".format(filename) + " "

# encode the message before sending it 
bstring = request_msg.encode()

# default IP addr of server & port 
client_soc.sendto(bstring, ("127.0.0.1",9000))
