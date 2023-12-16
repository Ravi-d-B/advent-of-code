import re

import numpy as np


def check_lines_cols(lines):
    # find number of lines and columns in file
    num_lines = len(lines)
    num_columns = len(lines[0])

    return num_lines, num_columns


# fill the matrix with the data from the file
with open('data/day3.txt') as f:
    lines = f.read().splitlines()
    num_rows, num_cols = check_lines_cols(lines)
    # create a matrix of zeros with the size of the file
    matrix = [[0] * num_cols for i in range(num_rows)]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            matrix[i][j] = lines[i][j]

matrix = np.array(matrix)


def check_left(matrix, i, j):
    if j == 0:
        return []
    if matrix[i][j - 1].isdigit():
        return [find_num(matrix, i, j - 1)]
    else:
        return []


def check_right(matrix, i, j):
    if j == len(matrix[i]) - 1:
        return []
    if matrix[i][j + 1].isdigit():
        return [find_num(matrix, i, j + 1)]
    else:
        return []


def check_down(matrix, i, j):
    max_j = len(matrix[i]) - 1

    if i == len(matrix) - 1:
        return []
    if matrix[i + 1][j].isdigit():
        return [find_num(matrix, i + 1, j)]
    elif j != 0 and j != max_j and matrix[i + 1][j - 1].isdigit() and matrix[i + 1][j + 1].isdigit():
        return [find_num(matrix, i + 1, j - 1), find_num(matrix, i + 1, j + 1)]
    elif j != 0 and matrix[i + 1][j - 1].isdigit():
        return [find_num(matrix, i + 1, j - 1)]
    elif j != max_j and matrix[i + 1][j + 1].isdigit():
        return [find_num(matrix, i + 1, j + 1)]
    else:
        return []

def check_up(matrix, i, j):
    max_j = len(matrix[i]) - 1

    if i == 0:
        return []
    if matrix[i - 1][j].isdigit():
        return [find_num(matrix, i - 1, j)]
    elif j != 0 and j != max_j and matrix[i - 1][j - 1].isdigit() and matrix[i - 1][j + 1].isdigit():
        return [find_num(matrix, i - 1, j - 1), find_num(matrix, i - 1, j + 1)]
    elif j != 0 and matrix[i - 1][j - 1].isdigit():
        return [find_num(matrix, i - 1, j - 1)]
    elif j != max_j and matrix[i - 1][j + 1].isdigit():
        return [find_num(matrix, i - 1, j + 1)]
    else:
        return []

def find_num(matrix, i, start_j):
    number = matrix[i][start_j]
    max_j = len(matrix[i]) - 1

    j = start_j
    while j - 1 >= 0 and matrix[i][j - 1].isdigit():
        j -= 1
        number = matrix[i][j] + number

    j = start_j
    while j + 1 <= max_j and matrix[i][j + 1].isdigit():
        j += 1
        number = number + matrix[i][j]

    return int(number)

count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '*':
            adj_nums = []
            adj_nums += check_left(matrix, i, j)
            adj_nums += check_right(matrix, i, j)
            adj_nums += check_up(matrix, i, j)
            adj_nums += check_down(matrix, i, j)
            if len(adj_nums) == 2:
                count += adj_nums[0] * adj_nums[1]

print(count)
