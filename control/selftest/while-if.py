# -*- coding: utf-8 -*-

userVal = raw_input("Please enter a positive integer:")

myInt = int(userVal)

count = 0

while myInt > 0:
    if myInt % 2 == 1:
        myInt /= 2
    else:
        myInt += 1
    count += 1

print count

print myInt
