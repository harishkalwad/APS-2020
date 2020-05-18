#!/bin/python3

import sys


if __name__ == '__main__':

    n, k, q = map(int, input().strip().split(" "))

    array = list(map(int, input().strip().split(" ")))

    shifted_array = [0] * n


    for i in range(n):
        shifted_array[(i + k) % n] = array[i]


    for _ in range(q):
        print(shifted_array[int(input().strip())])
