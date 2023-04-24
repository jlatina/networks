# Copyright 2023 Jeanette Villanueva jivillan@bu.edu
# Copyright 2023 Tristen Liu tristenl@bu.edu

"""
UDP server - IPv4
"""

import socket as s
import os
import hashlib


# create server socket 
server_soc = s.socket(s.AF_INET, s.SOCK_DGRAM)
server_soc.bind( ("127.0.0.1",9000))


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
        print(file_size)

        with open(params[1],'rb') as f:
            contents = f.read()

        sendmsg = f"FOUND {params[1]}\r\n"

        h=hashlib.md5()
        h.update(contents)
        md5sum = h.hexdigest()

        sendmsg = sendmsg + f"MD5 {md5sum}\r\n"
        sendmsg = sendmsg + f"LENGTH {file_size}\r\n"
        sendmsg = sendmsg + contents.decode()

        headerlen_bits = len(sendmsg) * 8
        avail_space = 2**16 - headerlen_bits
        if (file_size * 8 > avail_space):
            sendmsg = f"TOOLARGE {params[1]}\r\n"


    except FileNotFoundError:
        sendmsg = "NOTFOUND {}".format(params[1]) + "\r\n"

    except Exception:
        sendmsg = "BADREQUEST\r\n"

    server_soc.sendto(sendmsg.encode(), address)

       
    

   
    
            
            
    
