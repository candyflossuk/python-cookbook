"""
This script shows how to generate a list of all IPs
that a CIDR represents

The ipaddress module can be used to do this
"""
import ipaddress

net = ipaddress.ip_network("123.45.67.64/27")
for a in net:
    print(a)

net6 = ipaddress.ip_network("12:3456:78:90ab:cd:ef01:23:30/125")
for a in net6:
    print(a)

# Check for presence in block
a = ipaddress.ip_address("123.45.67.69")
