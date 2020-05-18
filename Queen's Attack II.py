#!/bin/python

n, k = map(int, raw_input().split(' '))
queen_row, queen_column = map(int, raw_input().split(' '))

top = n - queen_row
bottom = queen_row - 1
right = n - queen_column
left = queen_column - 1

top_left = min(n - queen_row, queen_column - 1)
top_right = n - max(queen_column, queen_row)
bottom_left = min(queen_row, queen_column) - 1
bottom_right = min(queen_row - 1, n - queen_column)

for a0 in xrange(k):
    obstacle_row, obstacle_column = map(int, raw_input().split(' '))
    
    # horizontal
    if obstacle_row == queen_row:
        if obstacle_column > queen_column:
            top = min(top, obstacle_column - queen_column - 1)
        else:
            bottom = min(bottom, queen_column - obstacle_column - 1)
    # vertical
    elif obstacle_column == queen_column:
        if obstacle_row > queen_row:
            right = min(right, obstacle_row - queen_row - 1)
        else:
            left = min(left, queen_row - obstacle_row - 1)
    # diagonals
    elif abs(obstacle_column - queen_column) == abs(obstacle_row - queen_row):
        # top right
        if obstacle_column > queen_column and obstacle_row > queen_row:
            top_right = min(top_right, obstacle_column - queen_column - 1)
        # bottom right
        elif obstacle_column > queen_column and obstacle_row < queen_row:
            bottom_right = min(bottom_right, obstacle_column - queen_column - 1)
        # top left
        elif obstacle_column < queen_column and obstacle_row > queen_row:
            top_left = min(top_left, queen_column - obstacle_column - 1)
        # bottom left
        elif obstacle_column < queen_column and obstacle_row < queen_row:
            bottom_left = min(bottom_left, queen_column - obstacle_column - 1)
    
            
print top + bottom + right + left + top_left + top_right + bottom_left + bottom_right
