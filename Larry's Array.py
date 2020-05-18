#!/bin/python3

import sys

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        numbers = list(map(int, input().strip().split(' ')))
        number_of_inversions = 0
        
        for i in range(0, n):
            for j in range(i + 1, n):
                if numbers[i] > numbers[j]:
                    number_of_inversions += 1
        print("YES" if number_of_inversions % 2 == 0 else "NO")
