import os

def read_aoc_input_file(input_path: str, return_as_string: bool = False):

    input_data = []
    with open(input_path) as f:
        for line in f:
            if return_as_string:
                input_data.append(line.strip('\n'))
            else:
                input_data.append(int(line.strip('\n')))

    return input_data
