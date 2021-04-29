import ipaddress

red_ipv4 =ipaddress.ip_network('123.45.67.64/27')
print(red_ipv4)
print(red_ipv4.num_addresses)

d = ipaddress.ip_address('123.45.67.69')
print(d in red_ipv4)
d = ipaddress.ip_address('123.45.67.124')
print(d in red_ipv4)

for d in red_ipv4:
  print(d)


