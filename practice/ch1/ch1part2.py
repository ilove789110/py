# -*- coding: utf-8 -*-

# No.10 problem

myVar1 = 10.3
myVar2 = 5.1

print myVar1 % myVar2

# No.13 problem

print 30 - 3 ** 2 + 8 / 3 ** 2 * 10

# # No.17 problem
#
# inputStr = raw_input("input int: ")
#
# inputInt = int(inputStr)
#
# print inputInt % 2

# No.19

print 100000000 * 1 / 1000

# # No.24
#
# a = "1"
# b = "2"
# c = "3"
#
# print (a + b) * c  # TypeError: can't multiply sequence by non-int of type 'str'

# # No.25
#
# inputStr = raw_input("input seconds: ")
#
# inputInt = int(inputStr)
#
# hour = inputInt / (60 * 60)
#
# minute = (inputInt - hour * 60 ** 2) / 60
#
# second = inputInt - hour * 60 ** 2 - minute * 60
#
# print hour, "时", minute, "分", second, "秒"

# No.27

print "trapezoid area formula: (a+c)*h/2.0"  # use 2.0 convert to float

# No.30

import datetime

print "Today's date is: ", datetime.date.today()
