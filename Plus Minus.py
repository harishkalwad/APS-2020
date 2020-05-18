#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p=0
    z=0
    n=0
    for i in arr:
        if(i>0):
            p+=1
        if(i==0):
            z+=1
        if(i<0):
            n+=1
    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
