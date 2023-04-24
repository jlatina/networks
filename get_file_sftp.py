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
    if 'FOUND' in reply:
        lines = reply.split('\r\n')
        server_md5 = lines[1].split()[1]
        server_filelen = lines[2].split()[1]
        file_contents = lines[3]
        
        h=hashlib.md5()
        h.update(file_contents.encode())
        md5sum = h.hexdigest()

        if server_md5 != md5sum:
            print("The md5 check failed! Exiting without storing.")
            return
        elif server_filelen != str(len(file_contents)):
            print(f"The file length check failed! {server_filelen} != {len(file_contents)}")
            return
        else: 
            print("Proceeding!")
            with open(filename,'w') as f:
                f.write(file_contents)

if __name__ == "__main__":
    main()