# Copyright 2023 Jeanette Villanueva jivillan@bu.edu
# Copyright 2023 Tristen Liu tristenl@bu.edu

"""
UDP client - IPv4
"""
import sys
import socket as s
import os
import hashlib



def main():
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

    client_soc.sendto(bstring, (ip,9000))

    reply = client_soc.recv(1024).decode()

    if 'NOTFOUND' in reply:
        print(f"{filename} was not found in the server's directory.")
        return
    if 'TOOLARGE' in reply:
        print(f"{filename} was found in the server, but the file size exceeded UDP packet size and could not be sent")
        return 
    if "BADREQUEST" in reply:
        print(f"{filename} includes directory specifications and is not allowed")
        return 

    lines = reply.split('\n')
    print(lines)

if __name__ == "__main__":
    main()