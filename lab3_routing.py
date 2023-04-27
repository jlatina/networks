# Copyright 2023 Jeanette Villanueva jivillan@bu.edu
# Copyright 2023 Tristen Liu tristenl@bu.edu

import ipaddress as ip
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
  """return the index of the network that matches addr using longest-prefix matching"""
  
# Convert the address to an IPv4Address object
  ip_addr_obj = ip.IPv4Address(addr)

# Convert each network to an IPv4Network object
  network_objs = [ip.IPv4Network(net) for net in nets]

  
  longest_prefix_match = None 
  index = -1

  # how enumerate works, prints: index value
  for i, network in enumerate(network_objs):
    print(i,network)

    # iterate over the networks to perform longest-prefix matching between IPv4 objs
  #for i, network in enumerate(network_objs):
    # check if the given ip_addr is within ONE of the networks   
   # if ip_addr_obj in network: 
        #print (f"Yes the address {addr} exists in the IPv4 networks")
  
  return None


def main():
  # should print 2
  print(get_route("128.197.128.9",["10.0.0.0/8","128.0.0.0/8","128.197.0.0/16"]))

if __name__ == '__main__':
  main()

