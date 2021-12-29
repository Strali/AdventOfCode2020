from collections import deque, Counter, defaultdict
import functools
import re
import sys
import os
import operator
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np
from utils.read_aoc_input_file import read_aoc_input_file

"""
def solve_day_fifteen(target_turn):
    input_data = [2, 0, 1, 9, 5, 19]

    spoken_numbers = input_data
    number_ages = {k: deque([v], maxlen=2) for k, v in zip(spoken_numbers, [i for i in range(len(spoken_numbers), 0, -1)])}
    #number_ages = {0: deque([3], maxlen=2), 3: deque([2], maxlen=2), 6: deque([1], maxlen=2)}

    last_number = input_data[-1]
    turn_counter = 4

    while len(spoken_numbers) < target_turn:
        c = Counter(spoken_numbers)
        if last_number in c.elements() and c[last_number] == 1:
            next_number = 0
            if 0 not in number_ages.keys():
                number_ages[next_number] = deque([0], maxlen=2)
            else:
                number_ages[0].append(0)
        else:
            next_number = abs(np.diff(number_ages.get(last_number))[0])
            if next_number not in number_ages.keys():
                number_ages[next_number] = deque([0], maxlen=2)
            else:
                number_ages[next_number].append(0)

        number_ages = {k: deque([c+1 for c in v], maxlen=2) for k, v in number_ages.items() for c in v}
        spoken_numbers.append(next_number)
        last_number = next_number
        turn_counter += 1

    print(list(spoken_numbers)[-1])
"""
"""
def solve_day_fifteen(start_sequence, target_turns):
    last_seen = [0]*target_turns
    last_number = start_sequence[-1]

    for turn, val in enumerate(start_sequence[:-1], 1):
        last_seen[val] = turn

    for previous_turn in range(len(start_sequence), target_turns):
        current_num = previous_turn - last_seen[last_number]

        if current_num == previous_turn:
            current_num = 0

        last_seen[last_number] = previous_turn
        last_number = current_num

    return current_num
"""
def solve_day_fifteen(start_sequence, num_turns):
    last_seen = defaultdict(lambda: i, {n:i for i,n in enumerate(start_sequence[:-1])})
    previous_number = start_sequence[-1]

    """
    for turn in range(len(start_sequence)-1, num_turns-1):
        last_seen[previous_number] = turn
        previous_number = turn - last_seen[previous_number]
    """
    previous_number = start_sequence[-1]
    for turn in range(len(start_sequence) - 1, num_turns - 1):
        last_seen[previous_number], previous_number = turn, turn - last_seen[previous_number]

    return previous_number

if __name__ == '__main__':
    input_data = [0, 3, 6] #[2, 0, 1, 9, 5, 19]

    print(solve_day_fifteen(input_data, 2020))
    #print(solve_day_fifteen(input_data, 30000000))
