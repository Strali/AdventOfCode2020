from collections import deque
import re
import sys
import os
import operator
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

from utils.read_aoc_input_file import read_aoc_input_file


ops = {'L': operator.add,
        'R': operator.sub}

def manhattan_distance(state):
    return abs(state.get('N') - state.get('S')) + abs(state.get('W') - state.get('E'))


def task_1(input_data):
    ship_state = {'N': 0, 'W': 0, 'S': 0, 'E': 0, 'H': 'E'}
    h_mapping = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
    current_heading = 'E'
    ship_heading = 0
    regex = r'(\w)(\d+)'

    for line in input_data:
        direction, distance = re.findall(regex, line)[0]
        if direction == 'F':
            ship_state[current_heading] += int(distance)
        elif direction in ['N', 'W', 'S', 'E']:
            ship_state[direction] += int(distance)
        else:
            ship_heading = ops[direction](ship_heading, int(distance))%360
            if ship_heading < 0:
                ship_heading = 360-abs(ship_heading)
            current_heading = h_mapping.get(ship_heading)
            ship_state['H'] = current_heading

    print(f'Distance of ship: {manhattan_distance(ship_state)}')

def task_2(input_data):
    ship_state = {'N': 0, 'W': 0, 'S': 0, 'E': 0, 'H': 'E'}
    waypoint_state = {'N': 1, 'W': 0, 'S': 0, 'E': 10}

    regex = r'(\w)(\d+)'

    for line in input_data:
        direction, distance = re.findall(regex, line)[0]
        if direction == 'F':
            new_ship_state = {k: ship_state[k]+int(distance)*waypoint_state[k] for k in waypoint_state.keys()}
            ship_state = new_ship_state

        elif direction in ['N', 'W', 'S', 'E']:
            waypoint_state[direction] += int(distance)
        else:

            waypoint_shift = (ops[direction](0, int(distance)))//90
            waypoint_values = deque([v for v in waypoint_state.values()])
            waypoint_values.rotate(waypoint_shift)
            waypoint_state = {k: v for k, v in zip(waypoint_state.keys(), waypoint_values)}
        #print(ship_state, waypoint_state)
    print(f'Distance from start location: {manhattan_distance(ship_state)}')


def solve_day_twelve():
    input_data = read_aoc_input_file('Day_12', return_as_string=True, test_input=False)

    task_1(input_data)
    task_2(input_data)


if __name__ == '__main__':
    solve_day_twelve()