import os
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

from itertools import combinations
from utils.read_aoc_input_file import read_aoc_input_file
from utils.listprod import listprod


def solve_day_one(target_sum: int=2020, group_size:int=2):
    input_data = read_aoc_input_file('Day_1', return_as_string=False)

    groups = combinations(input_data, group_size)
    target_group = [g for g in groups if sum(g)==target_sum]
    prod = listprod(target_group[0])

    print(f'Found addends: {target_group}')
    print(f'Product of addends for group size {group_size}: {prod}')

if __name__ == '__main__':
    group_sizes = [2, 3]
    for group_size in group_sizes:
        solve_day_one(2020, group_size)
