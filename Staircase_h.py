#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    boya=""
    for i in range(n):
        boya=boya+" "
    for i in range(n):
        boya=boya+"#"
        boya=boya[1:]
        print(boya)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
