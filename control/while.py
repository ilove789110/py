# -*- coding: utf-8 -*-

x = 0

# 循环
while x < 10:
    print x
    x += 1

print "end"

while 1 < 2:
    print "while"

    break  # break跳过循环和else子句
else:
    print "else"
