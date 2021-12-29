import os
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np
from utils.read_aoc_input_file import read_aoc_input_file


def solve_day_10():
    input_data = read_aoc_input_file('Day_10', return_as_string=False, test_input=False)

    # Task 1
    input_data = sorted(input_data)
    all_jolts = [0] +  input_data + [max(input_data)+3]
    rating_diffs = np.diff(all_jolts)
    one_diff = len(rating_diffs[rating_diffs==1])
    three_diff = len(rating_diffs[rating_diffs==3])
    print(f'Product of the count of "one-diff" and "three-diff" adapters: {one_diff*three_diff}')

    # Task 2
    group_splits = [0] + [idx+1 for idx, val in enumerate(rating_diffs) if val==3] # Find where the jump between adapter is the maximum 3 jolts
    adapter_groups = [all_jolts[i:j] for i, j in zip(group_splits, group_splits[1:])] # Split adapters into groups where we can "reach" the next group

    # From each group we can choose to include a subset of the adapters according to a tribonacci sequence.
    tribonacci_mapping = {1: 1, 2: 1, 3: 2, 4: 4, 5: 7}
    possibilities = 1
    for group in adapter_groups:
        possibilities *= tribonacci_mapping.get(len(group))

    print(f'Number of possible adapter configurations: {possibilities}')


if __name__ == '__main__':
    solve_day_10()
