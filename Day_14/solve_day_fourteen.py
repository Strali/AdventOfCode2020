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


def get_floating_addresses(mask):
    """Recursively yield floating addresses by replacing 'X':s with 0 and 1"""
    if 'X' in mask:
        for val in ('0', '1'):
            for address in get_floating_addresses(mask.replace('X', val, 1)):
                yield address
    else:
        yield mask

def solve_day_fourteen(is_part_two=False):
    input_data = read_aoc_input_file('Day_14', return_as_string=True)

    memory = {}
    mem_regex = r'\w+\[(\d+)\]'

    for line in input_data:
        instruction, value = line.split(' = ')
        if 'mask' in instruction:
            mask = value
        else:
            mem_address = re.match(mem_regex, instruction).groups()[0]

            if is_part_two:
                mem_address = '{:036b}'.format(int(mem_address))
                val_as_int = int(value)

                output_value = ''.join([adr if m=='0' else m for m, adr in zip(mask, mem_address)])
                for address in get_floating_addresses(output_value):
                    memory[int(address, base=2)] = val_as_int

            else:
                val_as_bytes = '{:036b}'.format(int(value))
                output_value = ''.join([val if mem=='X' else mem for mem, val in zip(mask, val_as_bytes)])
                memory[mem_address] = int(output_value, base=2)

    print(f'Sum of values in memory: {sum(memory.values())}')


if __name__ == '__main__':
    solve_day_fourteen()
    solve_day_fourteen(True)