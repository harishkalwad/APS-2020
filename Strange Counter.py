#!/bin/python3

import sys


if __name__ == "__main__":
    t = int(input().strip())
    lower_limit = 1
    upper_limit = 3
    while not(t >= lower_limit and t <= upper_limit):
        lower_limit = upper_limit + 1
        upper_limit = (upper_limit * 2) + 3
    print(1 + upper_limit - t)
