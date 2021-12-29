from collections import deque
import functools
import re
import sys
import os
import operator
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np
from utils.read_aoc_input_file import read_aoc_input_file
from utils.listprod import listprod


def task_1(earliest_departure, bus_lines):
    previous_departure = [earliest_departure % b for b in bus_lines]
    next_departure = [b-a for b, a in zip(bus_lines, previous_departure)]
    bus_to_catch = bus_lines[next_departure.index(min(next_departure))]
    time_to_wait = min(next_departure)

    print(f'Bus to catch: {bus_to_catch}, leaves in {time_to_wait} minutes. ID*wait time: {time_to_wait*bus_to_catch}')


def task_2(schedule):
    bus_order = [(schedule[i], i) for i in range(len(schedule))]
    busses = [(int(bus), (int(bus) - arrival) % int(bus))
        for bus, arrival in bus_order if not 'x' in bus]

    # Chinese Remainder Theorem, solve the problem for the LCM
    lcm = listprod([bus for bus, _ in busses])
    rem = [lcm//bus for bus, _ in busses]
    x = [pow(rem[i], -1, busses[i][0]) for i in range(len(rem))]
    y = [rem[i] * x[i] * busses[i][1] for i in range(len(rem))]

    print(f'Earliest timestamp after which busses leave in sequence: {functools.reduce(operator.add, y, 0) % lcm}')

def solve_day_thirteen():
    input_data = read_aoc_input_file('Day_13', return_as_string=True, test_input=False)
    earliest_departure = int(input_data[0])
    bus_lines = [int(b) for b in input_data[1].split(',') if b != 'x']
    bus_schedule = input_data[1].split(',')

    task_1(earliest_departure, bus_lines)
    task_2(bus_schedule)


if __name__ == '__main__':
    solve_day_thirteen()