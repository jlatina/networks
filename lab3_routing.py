# Copyright 2023 Jeanette Villanueva jivillan@bu.edu
# Copyright 2023 Tristen Liu tristenl@bu.edu

import ipaddress as ip
import numpy as np
#https://realpython.com/python-enumerate/ for enumerate()
"""
EC441 Spring 2023
Lab 3 : Routing


Write a function "get_route(addr,nets)" that is passed two arguments

- a string "addr" representing an IPv4 address in dotted decimal format
- a list of strings "nets" representing IPv4 networks, in a.b.c.d/x format

The function should return the index of the IPv4 network that 
the address should be routed to, based on longest-prefix matching.

If the address does not match any of the networks, then the value 
returned should be None

Groups
------

You may complete the lab in groups of up to three. All authors should
appear on a separate copyright line. Submit only once for the group.

Due Date
--------

The lab is due April 28.

Submission
----------

Submit here: https://curl.bu.edu:9999/ec441/spring2023/submit_assignment/lab3


Extra Credit
------------

Write a function get_route_hard(addr,nets) that does not use the facilities
of the ipaddress module.

"""

def get_route(addr, nets):
    """Return the index of the network that matches addr using longest-prefix matching"""
    
    # Convert the address to an IPv4Address object
    ip_addr_obj = ip.IPv4Address(addr)

    # Convert each network to an IPv4Network object
    network_objs = [ip.IPv4Network(net) for net in nets]

    longest_prefix_match = None 
    prefix_len = -1

    # Iterate over the networks to perform longest-prefix matching between IPv4 objects
    for i, network in enumerate(network_objs):
        # Check if the given ip_addr is within ONE of the networks
        # If the network.prefixlen is better than the current prefix_len then set it to the better one   
        if ip_addr_obj in network and network.prefixlen > prefix_len:
            longest_prefix_match = i
            prefix_len = network.prefixlen
    
    if longest_prefix_match is not None:
        return longest_prefix_match
    else:
        return None
    
def get_route_hard(addr, nets):
  addr_split = addr.split('.')
  longest_pref = None
  best_net = None
  address = np.array([int(item) for sublist in addr_split for item in '{0:08b}'.format(int(sublist))])
  for enum, net in enumerate(nets):
    network, size = net.split('/')
    net_mask = np.array([1]*int(size) + [0]*(32-int(size)))
    network = network.split('.')
    for i, segment in enumerate(network):
       network[i] = '{0:08b}'.format(int(segment))
    
    subnet = np.array([int(item) for sublist in network for item in sublist])

    masked_addr = address * net_mask
    if (masked_addr == subnet).all():
      if longest_pref == None:
        longest_pref = int(size)
        best_net = enum
      if int(size) > longest_pref:
        longest_pref = int(size)
        best_net = enum

  return best_net
   


def main():
  # should print 2
  print(get_route("128.197.128.9",["10.0.0.0/8","128.0.0.0/8","128.197.0.0/16"]))

if __name__ == '__main__':
  main()

