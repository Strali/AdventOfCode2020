import os
import operator
import re
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np

from utils.read_aoc_input_file import read_aoc_input_file


ops = {'+': operator.add,
       '-': operator.sub}


def execute_code(instruction_set):
    acc = 0
    pointer = 0
    visited_instructions = []

    while True:
        if pointer in visited_instructions or pointer >= len(instruction_set):
            break
        visited_instructions.append(pointer)
        next_instruction = instruction_set[pointer]
        op = next_instruction[0]
        sign = next_instruction[1]
        step = next_instruction[2]

        if op == 'jmp':
            pointer = ops[sign](pointer, int(step))
        elif op == 'acc':
            acc = ops[sign](acc, int(step))

        if op in ['acc', 'nop']:
            pointer += 1

    return acc, pointer == len(instruction_set)


def solve_day_eight():
    input_data = read_aoc_input_file('Day_8', return_as_string=True)

    instruction_regex = r'(\w{3}) ([\+-])(\d+)'
    instruction_set = []
    for line in input_data:
        line_instruction = re.findall(instruction_regex, line)
        instruction_set.append(list(line_instruction[0]))

    part_one_answer, _ = execute_code(instruction_set)

    for line_num, (instruction, _, _) in enumerate(instruction_set):
        if instruction in ['jmp', 'nop']:
            instruction_set[line_num][0] = 'jmp' if instruction == 'nop' else 'nop'
            accumulator, no_loop = execute_code(instruction_set)
            instruction_set[line_num][0] = instruction
            if no_loop:
                part_two_answer = accumulator
                break

    print(f'Accumulator output before loop with original code: {part_one_answer}')
    print(f'Accumulator output after changing line {line_num}: {part_two_answer}')

if __name__ == '__main__':
    solve_day_eight()
