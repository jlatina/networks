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
    sendmsg = ""
    try:
        message, address = server_soc.recvfrom(1024)
        print(f"speaking to {address}")
        params = message.decode().split()
        print(message.decode())
        if params[1].upper() == 'EXIT':
            break

        if '/' in params[1]:
           raise Exception
        
        file_size = os.stat(params[1]).st_size

        with open(params[1],'rb') as f:
            contents = f.read()

        sendmsg = f"FOUND {params[1]}\r\n"

        h=hashlib.md5()
        h.update(contents)
        md5sum = h.hexdigest()

        sendmsg = sendmsg + f"MD5 {md5sum}\r\n"
        sendmsg = sendmsg + f"LENGTH {len(contents)}\r\n"
        sendmsg = sendmsg + contents.decode()

        print(sendmsg)
        headerlen_bits = len(sendmsg) * 8
        avail_space = 2**16 - headerlen_bits
        if (len(contents) * 8 > avail_space):
            sendmsg = f"TOO LARGE {params}\r\n"


    except FileNotFoundError:
        sendmsg = "NOTFOUND {}".format(params[1]) + "\r\n"

    except Exception:
        sendmsg = "BADREQUEST {}".format(params[1]) + "\r\n"

    print(sendmsg)

       
    

   
    
            
            
    
