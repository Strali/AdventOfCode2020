import os
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np
from functools import lru_cache, partial
from itertools import product, count
from scipy.ndimage import convolve
from utils.read_aoc_input_file import read_aoc_input_file


def solve_day_eleven():
    input_data = read_aoc_input_file('Day_11', return_as_string=True, test_input=False)

    mapping = {'.': -1, 'L': 0, '#': 1}
    kernel = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]

    current_seating = np.array([[mapping.get(c) for c in line] for line in input_data])

    previous_seating = np.empty(current_seating.shape)
    while not np.array_equal(current_seating, previous_seating):
        previous_seating = current_seating
        neighbourhood = convolve(np.where(current_seating==-1, 0, current_seating), kernel, mode='constant')
        current_seating = np.where(current_seating==-1, mapping.get('.'), np.where(neighbourhood>= 4, mapping.get('L'), np.where(neighbourhood==0, mapping.get('#'), current_seating)))

    occupied_at_equillibrium = sum(sum(current_seating==mapping.get('#')))
    print(f'Numper of occupied seats at equilibrium: {occupied_at_equillibrium}')


def parse_raw(raw):
    trans = {".": FLOOR, "L": EMPTY}
    return np.array([[trans[char] for char in line] for line in raw])


FLOOR, EMPTY, OCCUPIED = -1, 0, 1
input_data = read_aoc_input_file('Day_11', return_as_string=True, test_input=False)
data = parse_raw(input_data)
floor, no_floor = data == FLOOR, data != FLOOR
h, w = data.shape

@lru_cache(maxsize=None)
def neighborhood(y, x):
    ys, xs = [], []
    for y_step, x_step in product((-1, 0, 1), repeat=2):
        if y_step == x_step == 0:
            continue
        for i in count(1):
            cell_y, cell_x = y + i * y_step, x + i * x_step
            if cell_y not in range(0, h) or cell_x not in range(0, w):
                break
            if no_floor[cell_y, cell_x]:
                ys.append(cell_y)
                xs.append(cell_x)
                break
    return tuple(ys), tuple(xs)

@partial(np.vectorize, excluded=[2])
def seen(y, x, seats):
    h, w = seats.shape
    return seats[neighborhood(y, x)].sum()



def part_two():
    input_data = read_aoc_input_file('Day_11', return_as_string=True, test_input=False)
    data = parse_raw(input_data)
    floor, no_floor = data == FLOOR, data != FLOOR
    h, w = data.shape

    last = None
    seats = neighbors = data.copy()
    ys, xs = np.mgrid[:h, :w]
    ys, xs = ys[no_floor], xs[no_floor]
    while seats.tobytes() != last:
        last = seats.tobytes()
        neighbors[no_floor] = seen(ys, xs, seats)
        seats = np.where(neighbors >= 5, EMPTY, np.where(neighbors == 0, OCCUPIED, seats))

    print(f'{(seats == OCCUPIED).sum()}')


if __name__ == '__main__':
    solve_day_eleven()
    part_two()