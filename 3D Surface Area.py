#!/bin/python3

import sys

if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
       A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
       A.append(A_t)
    result = 2 * H * W
    for i in range(H):
        for j in range(W):
            result += A[i][j] * 4
            if i != 0:
                result -= 2 * min(A[i - 1][j], A[i][j])
            if j != 0:
                result -= 2 * min(A[i][j], A[i][j - 1])
    print(result)
