import os
import re
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np

from utils.read_aoc_input_file import read_aoc_input_file


def format_input_groups(raw_input):
    input_groups = {}
    input_group_count = 0
    for line in raw_input:
        if input_group_count not in input_groups.keys():
            input_groups[input_group_count] = []
        if line == '':
            input_group_count += 1
            continue
        else:
            input_groups[input_group_count].append(line)

    return input_groups


def solve_day_six():
    input_data = read_aoc_input_file('Day_6', return_as_string=True)

    input_groups = format_input_groups(input_data)

    group_counts = [len(set(''.join(g))) for g in input_groups.values()] # Task 1
    common_answer_count = [(sum([all(v in g for g in group) for v in set(''.join(group))])) for group in input_groups.values()] # Task 2

    print(f'Number of questions where anyone answered yes: {sum(group_counts)}')
    print(f'Number of questions where everyone answered yes: {sum(common_answer_count)}')

if __name__ == '__main__':
    solve_day_six()
