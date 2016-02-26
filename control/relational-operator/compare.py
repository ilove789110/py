# -*- coding: utf-8 -*-

import math

print "1" < 2  # 不同类型比较时，python指定各类型的级别。String不管内容都大于数字

float1 = 2.5

float2 = 2.5

float3 = float2

print id(float1)

print id(float2)

print id(float3)

print float3 == float1

print float3 is float1

print float3 is float2

u = 11111113

v = -11111111

w = 7.51111111

x = (u + v) + w

y = u + (v + w)

print x, y

print x == y  # 对于浮点数这种方式不合适，因为浮点数的存储方式中有2进制转10进制的误差

print math.fabs(x - y) < 0.0000001  # 对于浮点数应使用这种方式

intA = 5

print 0 <= intA <= 5

print 0 <= intA <= 2  # 关系运算符链
