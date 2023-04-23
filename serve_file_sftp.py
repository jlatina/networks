# Copyright 2023 Jeanette Villanueva jivillan@bu.edu
# Copyright 2023 Tristen Liu tristenl@bu.edu

"""
UDP server - IPv4
"""
import sys
import socket as s
import os
import hashlib
from get_file_sftp import bstring, filename


# create server socket 
server_soc = s.socket(s.AF_INET, s.SOCK_DGRAM)

# list to store responses of server 
messages = ['FOUND', 'BADREQUEST', 'TOOLARGE', 'NOTFOUND']


while True:
    message, address = server_soc.recvfrom(1024)
    normalstr = bstring.decode()
    
    # try & catch for opening the file 

    file_size = os.stat(filename).st_size

    with open(filename,'rb') as f:
        contents = f.read()

    # check if it's in the directory
    files = os.listdir()

    h=hashlib.md5()
    h.update(contents)
    md5sum = h.hexdigest()
