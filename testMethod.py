
from numpy import *
import operator

# def createDataSet():
#     group = array([[1,2],[3,4],[5,6],[7,8]])
#     labels = ['A','A','B','B']
#     return group, labels

group = array([[1,1],[1,2],[9,8],[8,9]])
label = ['a','a','b','b']
diffMat = tile([0,0], (4,1)) - group
sqDiffMat = diffMat**2
sqDistence = sqDiffMat.sum(axis=1)
distence = sqDistence ** 0.5

# print(diffMat)
print(diffMat**2)
print((diffMat**2).sum(axis=1))
distance = ((diffMat ** 2).sum(axis=1))**0.5
print(distance)