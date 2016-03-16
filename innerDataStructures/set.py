# -*- coding: utf-8 -*-

# s = set('A', 'B', 'C')

# print type(s)

s = set(['A', 'B', 'C'])

print type(s)

print s

if 'A' in s:
    print "A is in ?", 'A' in s

sc = s.copy()

sc.add('D')

sc.remove('A')

print s & sc
