#!/bin/python3

import sys



if __name__ == '__main__':
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        configuration = input().strip()
        ladybugs = dict()
        there_is_empty_cell = False
        already_happy_ladybugs = True
        for i in range(len(configuration)):
            current_cell = configuration[i]
            if current_cell != '_':
                
                if current_cell in ladybugs:
                    ladybugs[current_cell] = True
                else:
                    ladybugs[current_cell] = False
                if i == 0:
                    if len(configuration) != 1:
                        if configuration[1] != current_cell:
                            already_happy_ladybugs = False
                    else:
                        already_happy_ladybugs = False
                elif i != 0 and i != len(configuration) - 1:
                    if not (configuration[i - 1] == current_cell or configuration[i + 1] == current_cell):
                        already_happy_ladybugs = False
                elif i == len(configuration) - 1:
                    if configuration[len(configuration) - 2] != current_cell:
                        already_happy_ladybugs = False
            else:
                there_is_empty_cell = True

        single_ladybug = False
        for key, value in ladybugs.items():
            if value is False:
                single_ladybug = True
                break
        print("YES" if already_happy_ladybugs or (not single_ladybug and there_is_empty_cell) else "NO")
