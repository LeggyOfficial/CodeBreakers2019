#!/usr/bin/env python3
from itertools import cycle
from math import sqrt, floor
from textwrap import wrap
import operator
import copy

key='FLEISNRGA'

inputText = "DNFOAV ENLAEI RSITCR HEISCS ATNIBH EREODE PESRSG HESRBO IELARA DONAPR LEDSDT CIHWIE MEDARI ATBNYT GNTWAR ARMHXE HEGGYX ERDRUX"
def printMatrix(matrix):
    for line in matrix:
        print(line)

def rotateRight(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def rotateLeft(matrix):
     return list(reversed([list((col)) for col in zip(*matrix)]))


keySort = "".join(sorted(key))

keyN =[]
for i in key:
    keyN.append(keySort.find(i)+1)
N = int(sqrt(len(keyN)))

inputText = ''.join([i for i in inputText if i.isalpha()]).upper()

matrix = [[i+j*N+1 for i in range(N)] for j in range(N)]

keyIt=iter(keyN)
#this will need some huge refactor..........
windows = floor(len(keyN)/4)
matrixes = []
for i in range(4):
    toBeMarked = [];
    for j in range(windows):
        toBeMarked.append(next(keyIt))
    if i == 3 and windows*4<len(keyN):
        toBeMarked.append(next(keyIt))
    matrixCp = [[0 if k in toBeMarked else k for k in l] for l in matrix]
    matrixes.append(matrixCp)

half1 = matrixes[0]+rotateLeft(matrixes[3])
half2 = rotateRight(matrixes[1]) +rotateRight(rotateRight(matrixes[2]))

full = [half1, half2]
grill = list(map(lambda x: x[0]+x[1], zip(*full)))


inputText = wrap(inputText,4*N*N)

outputText =""
for text in inputText:
    code=wrap(text,2*N)
    thisGrill=copy.deepcopy(grill)

   # thisGrill = rotateRight(thisGrill)
    for i in range(4):
        for j in range(2*N):                
            for k in range(2*N):
                if thisGrill[j][k] == 0:
                    outputText += code[j][k]
       # thisGrill = rotateLeft(thisGrill)
        thisGrill = rotateRight(thisGrill)
print(outputText)
