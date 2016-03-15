# -*- coding: utf-8 -*-

class_list = ['A', 1, 'B']

print class_list

print 'class have', len(class_list), 'students'

class_list.append("E")

print class_list

class_list.sort()

print class_list

del class_list[0]

print class_list

print 'These students are :',
for student in class_list: print student,
