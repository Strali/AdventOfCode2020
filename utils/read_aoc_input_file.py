import os

from utils.get_input_path import get_input_path

def read_aoc_input_file(puzzle_day: str, return_as_string: bool = False, test_input: bool = False):

    input_path = get_input_path(puzzle_day, test_input)
    input_data = []
    with open(input_path) as f:
        for line in f:
            if return_as_string:
                input_data.append(line.strip('\n'))
            else:
                input_data.append(int(line.strip('\n')))

    return input_data
