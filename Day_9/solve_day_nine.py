import os
import re
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

from itertools import combinations

from utils.read_aoc_input_file import read_aoc_input_file

def chunks(lst, chunk_size):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


def solve_day_nine():
    input_data = read_aoc_input_file('Day_9', return_as_string=False, test_input=False)

    preamble_length = 25
    for (i, num) in enumerate(input_data):
        if i < preamble_length:
            continue
        current_preamble = input_data[i-preamble_length:i]
        preamble_sums = [sum(g) for g in combinations(current_preamble, 2)]
        if num not in preamble_sums:
            print(f'{num} not in preamble at position {i}')
            break


    for chunk_size in range(2, 150):
        for start_idx in range(0, i-chunk_size):
            relevant_input = input_data[start_idx:i]
            sublists = list(chunks(relevant_input, chunk_size))
            sublist_sums = [sum(l) for l in sublists]
            if num in sublist_sums:
                key_list = sublists[sublist_sums.index(num)]
                break

    print(f'List of numbers that sum to input: {key_list}. Sum of min an max: {min(key_list) + max(key_list)}')

if __name__ == '__main__':
    solve_day_nine()