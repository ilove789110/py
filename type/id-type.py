# -*- coding: utf-8 -*-

aInt = 7

print "aInt id:", id(aInt), \
    "aInt type:", type(aInt)

bFloat = 2.5

print "bFloat id:", id(bFloat), \
    "bFloat type:", type(bFloat)

aInt = bFloat

print "aInt id:", id(aInt), \
    "aInt type:", type(aInt)

cInt = 123456789 * 987654321

print "cInt id:", id(cInt), \
    "cInt type:", type(cInt), \
    "cInt value:", cInt

print 012  # 012为8进制的12

print 0x10  # 0x10为16进制的10

dBool = True

print "dBool id:", id(dBool), \
    "dBool type:", type(dBool), \
    "dBool value:", dBool

eStr = "smap"  # python中只有字符串类型，不分字符和字符串。字符串是一种序列，属于集合类型

print "eStr id:", id(eStr), \
    "eStr type:", type(eStr), \
    "eStr value:", eStr

fList = [4, 5.37, 'abc']

print "fList id:", id(fList), \
    "fList type:", type(fList), \
    "fList value:", fList

gDict = {"Jones": 3471124, "Will": 123456}

print "gDict id:", id(gDict), \
    "gDict type:", type(gDict), \
    "gDict value:", gDict

hSet = set([1, 3, 5])

print "hSet id:", id(hSet), \
    "hSet type:", type(hSet), \
    "hSet value:", hSet
