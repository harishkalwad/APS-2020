#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mini=0
    maxi=0
    mini_count=scores[0]
    max_count=scores[0]
    for i in scores:
        if(i>max_count):
            max_count=i
            maxi+=1
        if(i<mini_count):
            mini_count=i
            mini+=1
    return (maxi,mini)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
