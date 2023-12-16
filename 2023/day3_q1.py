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


def check_adjoining_symbol(matrix, i, j, len_num):
    # check if the symbol is in the matrix
    start_i = max(i - 1, 0)
    start_j = max(j - 1, 0)
    end_i = min(i + 1, len(matrix))
    end_j = min(j + len_num + 1, len(matrix[0]))

    for elem in matrix[start_i:end_i+1, start_j:end_j].flatten():
        if elem != '.' and not elem.isdigit():
            print(elem)
            print(matrix[start_i:end_i, start_j:end_j])
            print(i,j)
            return True
    return False


count = 0

for i in range(len(matrix)):
    j = 0
    while j < len(matrix[i]):

        if matrix[i][j].isdigit():
            # restore the line by adding all elements
            line = ''.join(matrix[i][j:])
            # find the first number
            number = re.findall(r'\d+', line)[0]

            # check if the number is in the matrix
            if check_adjoining_symbol(matrix, i, j, len(number)):
                print(number)
                count += int(number)
            j += len(number)

        else:
            j += 1
print(count)
