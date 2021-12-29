from collections import deque

import sys
import os
import operator
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

from utils.read_aoc_input_file import read_aoc_input_file


def convert_to_rpn(infix_expression, is_part_two=True):
    output_rpn = ''
    operator_stack = deque()

    # Construct RPN expression using Shunting-Yard algorithm
    for char in infix_expression:
        if char.isnumeric():
            output_rpn += char
        else:
            if char in ['*', '+']:
                if (is_part_two and char == '*') or not is_part_two:
                    while operator_stack and operator_stack[-1] != '(':
                        output_rpn += operator_stack.pop()
                    operator_stack.append(char)
                else:
                    operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            else:
                next_from_stack = operator_stack.pop()
                while next_from_stack != '(':
                    output_rpn += next_from_stack
                    next_from_stack = operator_stack.pop()

    # Add any remaining operators to RPN expression
    while operator_stack:
        output_rpn += operator_stack.pop()

    return output_rpn


def evaluate_rpn(rpn_expression):
    output = deque()
    operands = {'+': operator.add,
                '*': operator.mul}

    for char in rpn_expression:
        if char.isnumeric():
            output.append(int(char))
        elif char in ['+', '*']:
            a = output.pop()
            b = output.pop()

            op_result = operands.get(char)(a, b)
            output.append(op_result)

    return output.pop()


def solve_day_eighteen():
    input_data = read_aoc_input_file('Day_18', return_as_string=True)
    input_data = [expr.replace(' ', '') for expr in input_data]

    for task in [(1, False), (2, True)]:
        results = []
        for expr in input_data:
            rpn = convert_to_rpn(expr, task[1])
            results.append(evaluate_rpn(rpn))

        print(f'Sum of all expression evaluations using precedence in task {task[0]}: {sum(results)}')


if __name__ == '__main__':
    solve_day_eighteen()
