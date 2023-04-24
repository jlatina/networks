# Copyright 2023 Jeanette Villanueva jivillan@bu.edu
# Copyright 2023 Tristen Liu tristenl@bu.edu

"""
UDP server - IPv4
"""
import sys
import socket as s
import os
import hashlib
# from get_file_sftp import bstring, filename


# create server socket 
server_soc = s.socket(s.AF_INET, s.SOCK_DGRAM)
server_soc.bind( ("127.0.0.1",9000))

# list to store responses of server 
messages = ['FOUND', 'BADREQUEST', 'TOOLARGE', 'NOTFOUND']


while True:

    try:
        message, address = server_soc.recvfrom(1024)
        print(f"speaking to {address}")
        params = message.decode().split()
        print(message.decode())

        if params[0] != "GET":
           print("BADREQUEST {}".format(params[1]) + "\r\n")
        
        file_size = os.stat(params[1]).st_size

        with open(params[1],'rb') as f:
            contents = f.read()

    except FileNotFoundError:
        print("NOTFOUND {}".format(params[1]) + "\r\n")
       
        # check if it's in the directory
        files = os.listdir()

        h=hashlib.md5()
        h.update(contents)
        md5sum = h.hexdigest()

   
    
            
            
    