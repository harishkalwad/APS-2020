#!/bin/python3

import sys

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    sorted_list = []
    unsorted_list = []
    for number in arr:
        sorted_list.append(number)
        unsorted_list.append(number)
    sorted_list.sort()

    number_of_differences = 0
    start_swap_index = 0
    end_swap_index = 0
    for i in range(n):
        if(unsorted_list[i] != sorted_list[i]):
            number_of_differences += 1
            if number_of_differences == 1:
                start_swap_index = i
            if number_of_differences >= 2:
                end_swap_index = i
    if number_of_differences == 0:
        print("yes")
    elif number_of_differences == 2:
        print("yes\nswap {} {}".format(start_swap_index + 1, end_swap_index + 1))

       else:
        can_be_ordered = True
        sub_array = unsorted_list[start_swap_index:end_swap_index + 1]
        for i in range(1, len(sub_array)):
            if sub_array[i] > sub_array[i - 1]:
                can_be_ordered = False
                break
        if can_be_ordered:
            print("yes\nreverse {} {}".format(start_swap_index + 1, end_swap_index + 1))
        else:
            print("no")
