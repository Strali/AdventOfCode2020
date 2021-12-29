import sys
import os
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np
from scipy.ndimage import convolve
from utils.read_aoc_input_file import read_aoc_input_file


def solve_day_seventeen():
    # NB: To solve for task 1, remove first dimension of all arrays and remove loop over "w"
    input_data = read_aoc_input_file('Day_17', return_as_string=True, test_input=False)

    mapping = {'.': 0, '#': 1}
    kernel = np.ones((3, 3, 3, 3))
    kernel[1, 1, 1, 1] = 0

    initial_state = np.array([[mapping.get(c) for c in line] for line in input_data])
    surrounding_states = np.zeros((3, 3,) + initial_state.shape)
    surrounding_states[1, 1, :, :] = initial_state

    current_state = surrounding_states
    previous_state = np.empty(current_state.shape)
    for i in range(0, 6):
        previous_state = current_state
        next_state = np.pad(previous_state, 1)
        surroundings = convolve(next_state, kernel, mode='constant')
        for w in range(next_state.shape[0]):
            for z in range(next_state.shape[1]):
                for x in range(next_state.shape[2]):
                    for y in range(next_state.shape[3]):
                        if next_state[w, z, x, y] == 1 and (surroundings[w, z, x, y] == 2 or surroundings[w, z, x, y] == 3):
                            next_state[w, z, x, y] = 1
                        elif next_state[w, z, x, y] == 0 and surroundings[w, z, x, y] == 3:
                            next_state[w, z, x, y] = 1
                        else:
                            next_state[w, z, x, y] = 0

        current_state = next_state

    num_active_cubes = np.sum(current_state)
    print(f'Number of active cubes after six cycles: {num_active_cubes}')


if __name__ == '__main__':
    solve_day_seventeen()
