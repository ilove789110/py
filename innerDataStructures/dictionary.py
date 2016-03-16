# -*- coding: utf-8 -*-

d = {'A': 10, 'B': 20, 'C': 30}

print type(d)

print "A's score is ", d['A']

del d['A']

for name, score in d.items():
    print '{0} is {1}'.format(name, score)

d['D'] = 40

if 'D' in d:
    print "D's score is ", d['D']
