#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    s1=0
    s2=0
    j=0
    for i in range(len(arr)):
        s1=s1+arr[i][j]
        j+=1
    j-=1
    for i in range(len(arr)):
        s2=s2+arr[i][j]
        j-=1
    return abs(s1-s2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
