import os
import re
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np

from itertools import compress
from utils.read_aoc_input_file import read_aoc_input_file


def binary_seat_search(boarding_code):

    seat_range = [0, 127] if len(boarding_code) > 3 else [0, 7]

    for letter in boarding_code:
        if letter in ['F', 'L']:
            new_top_range = seat_range[1]-(seat_range[1]-seat_range[0])//2 - 1
            seat_range = [seat_range[0], new_top_range]
        elif letter in ['B', 'R']:
            new_bottom_range = seat_range[0] + (seat_range[1]-seat_range[0] + 1)//2
            seat_range = [new_bottom_range, seat_range[1]]

    return sum(seat_range)/2


def solve_day_five():
    input_data = read_aoc_input_file('Day_5', return_as_string=True)
    seat_ids = {}
    for boarding_code in input_data:

        row_code = boarding_code[0:7]
        col_code = boarding_code[7:]

        seat_row = binary_seat_search(row_code)
        seat_col = binary_seat_search(col_code)
        seat_ids[boarding_code] = seat_row*8 + seat_col

    sorted_ids = sorted([v for v in seat_ids.values()])
    id_diff = np.diff(sorted_ids)
    skipped_id_idx = id_diff > 1
    skipped_id = list(compress(sorted_ids, skipped_id_idx))[0] + 1

    print(f'Maximum seat ID: {int(sorted_ids[-1])}')
    print(f'Own seat location: {int(skipped_id)}')


if __name__ == '__main__':
    solve_day_five()
