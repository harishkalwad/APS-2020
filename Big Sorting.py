#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
for i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)
    #unsorted = sorted(unsorted,key=int)
for i in sorted(unsorted,key=int):
    print(i)
