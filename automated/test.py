#!/usr/bin/env python
# Author:rogue


# set
s1 = set([1, 2, 3, 5, 6, 3, 2, 1])
s2 = {1, 3, 5, 6, 5, 4, 3}
print(type(s1))
print(type(s2))
print(s1)
print(s2)
print()

# 数组

l1 = list([1, 2, 3, 3, 2, 1])
l2 = [3, 4, 5, 6, 5, 4, 3, 2]
print(type(l1))
print(type(l2))
print(l1)
print(l2)

# 字典
dict1 = {"key1": "rogue", "key2": "andy", "key3": "confon"}
print(type(dict1))
print(len(dict1))
print(str(dict1))

dict2 = {'nmap': {'scaninfo': {'tcp': {'method': 'connect', 'services': '21-22,80'}},
                  'scanstats': {'elapsed': '1.86', 'totalhosts': '1', 'uphosts': '1', 'downhosts': '0',
                                'timestr': 'Sat Sep  3 14:54:17 2016'},
                  'command_line': 'nmap -oX - -p 21,22,80 -sV 192.168.1.5'}, 'scan': {
    '192.168.1.5': {'hostnames': [{'type': 'PTR', 'name': 'ROGUE-HOME'}],
                    'status': {'state': 'up', 'reason': 'syn-ack'}, 'vendor': {}, 'addresses': {'ipv4': '192.168.1.5'},
                    'tcp': {80: {'cpe': '', 'version': '', 'name': 'http', 'state': 'filtered', 'extrainfo': '',
                                 'reason': 'no-response', 'product': '', 'conf': '3'},
                            21: {'cpe': 'cpe:/o:microsoft:windows', 'version': '', 'name': 'ftp', 'state': 'open',
                                 'extrainfo': '', 'reason': 'syn-ack', 'product': 'Microsoft ftpd', 'conf': '10'},
                            22: {'cpe': '', 'version': '', 'name': 'ssh', 'state': 'filtered', 'extrainfo': '',
                                 'reason': 'no-response', 'product': '', 'conf': '3'}}}}}

print(type(dict2))
print(len(dict2))
print(dict2.get("nmap"))
for k,v in enumerate(dict2):
    print(k,v,dict2.get(k))
