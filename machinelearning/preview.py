# -*- coding: utf-8 -*-

from numpy import *

print "-----------randArray--------------"

randArray = random.rand(4, 4)

print randArray

print "-----------randMat--------------"

randMat = mat(randArray)

print randMat

print "-----------invRandMat--------------"

invRandMat = randMat.I

print invRandMat

print "-----------myEye--------------"

myEye = randMat * invRandMat

print myEye

print "-----------deviation--------------"

deviation = myEye - eye(4)

print deviation

print "-----------eye(4)--------------"

print eye(4)
