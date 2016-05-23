# -*- coding: utf-8 -*-
from numpy import *

import kNN
import operator

group, labels = kNN.createDataSet()

print group

# shape 返回数组或者矩阵的行列数 shape[0] 行数 shape[1] 列数
print group.shape[0]

print group.shape[1]

print labels


def classify0(inX, inY, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]

    mat = tile((inX, inY), (dataSetSize, 1))

    diffMat = mat - dataSet

    sqDiffMatt = diffMat ** 2

    sqDistances = sqDiffMatt.sum(axis=1)

    distances = sqDistances ** 0.5

    sortedDistIndicies = distances.argsort()

    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)

        print mat

        print diffMat

        print sqDiffMatt

        print sqDistances

        print distances

        print sortedDistIndicies

        print classCount
        return sortedClassCount[0][0]


print classify0(1, 1, group, labels, 3)

