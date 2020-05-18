#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mini=0
    maxi=0
    arr1=arr[:]
    for i in range(0,4):
        mini=mini+min(arr)
        arr.remove(min(arr))
    for i in range(0,4):
        maxi=maxi+max(arr1)
        arr1.remove(max(arr1))
    print(mini,maxi)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
