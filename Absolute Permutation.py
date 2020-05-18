#!/bin/python3

import sys


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n, k = map(int, input().strip().split(' '))
        permutation = []
        if k == 0:
            print(" ".join([str(number) for number in range(1, n + 1)]))
        else:
            if n % 2 == 0 and n % (2 * k) == 0:
                blocks = n // k
                current_number = k
                for block in range(0, blocks):
                    for i in range(0, k):
                        current_number += 1
                        permutation.append(current_number)
                    current_number = current_number + (2 * k) if block % 2 != 0 else current_number - (2 * k)
                print(" ".join([str(number) for number in permutation]))
            else:
                print(str(-1))
