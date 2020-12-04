import os
import re
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

from itertools import combinations
from utils.read_aoc_input_file import read_aoc_input_file


def solve_day_two():
    input_path = os.path.join ('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode', 'Day_2', 'input.txt')
    input_data = read_aoc_input_file('Day_2', return_as_string=True)

    valid_password_count_policy_1 = 0
    valid_password_count_policy_2 = 0

    for password_line in input_data:
        policy, letter, password = password_line.split(' ')
        min_letter_count = int(re.search(r'^\d{1,2}', policy).group(0))
        max_letter_count = int(re.search(r'\d{1,2}$', policy).group(0))
        letter = letter.strip(':')

        # Task 1
        if password.count(letter) in range(min_letter_count, max_letter_count+1):
            valid_password_count_policy_1 += 1

        # Task 2
        first_letter_idx = min_letter_count - 1
        second_letter_idx = max_letter_count - 1
        if (password[first_letter_idx] == letter) != (password[second_letter_idx] == letter): # XOR
            valid_password_count_policy_2 += 1

    print(f'Valid password count using policy 1: {valid_password_count_policy_1}')
    print(f'Valid password count using policy 2: {valid_password_count_policy_2}')

if __name__ == '__main__':
    solve_day_two()