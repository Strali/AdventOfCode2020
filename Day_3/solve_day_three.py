import os
import re
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np

from itertools import combinations
from utils.read_aoc_input_file import read_aoc_input_file
from utils.listprod import listprod


def solve_day_three(row_steps, col_steps):
    input_data = read_aoc_input_file('Day_3', return_as_string=True)

    row_length = len(input_data[0])

    step_count = 0
    num_trees = [0]*len(row_steps)

    for i, (row_step, col_step) in enumerate(zip(row_steps, col_steps)):
        row_idx = 0
        col_idx = 0
        while row_idx < len(input_data)-1:
            col_idx = (col_idx + col_step)%row_length
            row_idx += row_step

            if input_data[row_idx][col_idx] == '#':
                num_trees[i] += 1
    prod = listprod(num_trees)

    print(f'Number of trees encountered on different slopes: {num_trees}')
    print(f'Solution task 1: {num_trees[1]}')
    print(f'Solution task 2: {prod}')

if __name__ == '__main__':
    row_steps = [1, 1, 1, 1, 2]
    col_steps = [1, 3, 5, 7, 1]
    solve_day_three(row_steps, col_steps)
