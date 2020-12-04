import os
import re
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np

from itertools import combinations
from utils.read_aoc_input_file import read_aoc_input_file


def check_fields(passport_entry):

    hgt_regex = r'(\d{2,3})([cmin]{2})'
    hcl_regex = r'(#)([a-f1-9]{6})'
    pid_regex = r'(\d{9})'

    if len(set(passport_entry.keys())) != len(passport_entry.keys()):
        return False

    for field, value in passport_entry.items():
        if field == 'byr':
            valid = len(value) == 4 and int(value) >= 1920 and int(value) <= 2002
        elif field == 'iyr':
            valid = len(value) == 4 and int(value) >= 2010 and int(value) <= 2020
        elif field == 'eyr':
            valid = len(value) == 4 and int(value) >= 2020 and int(value) <= 2030
        elif field == 'hgt':
            match = re.search(hgt_regex, value)
            if match:
                height_value = match.group(1)
                height_unit = match.group(2)
                if height_unit == 'cm':
                    valid = int(height_value) >= 150 and int(height_value) <= 193
                elif height_unit == 'in':
                    valid = int(height_value) >= 59 and int(height_value) <= 76
        elif field == 'hcl':
            valid = re.search(hcl_regex, value) is not None
        elif field == 'ecl':
            valid = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and len(value)==1
        elif field == 'pid':
            valid = re.search(pid_regex, value) is not None

    return valid


def format_passport_inputs(raw_input):
    passport_entries = {}
    entry_count = 0
    for line in raw_input:
        if entry_count not in passport_entries.keys():
            passport_entries[entry_count] = {}
        if line == '':
            entry_count += 1
            continue
        line_entries = line.split(' ')
        for entry in line_entries:
            key, value = entry.split(':')
            passport_entries[entry_count][key] = value

    return passport_entries


def solve_day_four():
    input_data = read_aoc_input_file('Day_4', return_as_string=True)

    passport_entries = format_passport_inputs(input_data)

    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passport_count_task_1 = 0
    valid_passport_count_task_2 = 0
    invalid_passport_count_task_1 = 0
    invalid_passport_count_task_2 = 0

    for entry in passport_entries.values():
        if all([k in entry.keys() for k in mandatory_fields]):

            valid_passport_count_task_1 += 1
            # Additional checks for task 2.
            valid_passport_task_2 = check_fields(entry)
            if valid_passport_task_2:
                valid_passport_count_task_2 += 1
            else:
                invalid_passport_count_task_2 += 1
        else:
            invalid_passport_count_task_1 += 1
            invalid_passport_count_task_2 += 1

    print(f'Total number of passports checked: {len(passport_entries)}')
    print('-'*50)
    print(f'Passports with complete data for task 1: {valid_passport_count_task_1}')
    print(f'Passports with missing data for task 1: {invalid_passport_count_task_1}')
    print('-'*50)
    print(f'Passports with complete data for task 2: {valid_passport_count_task_2}')
    print(f'Passports with missing data for task 2: {invalid_passport_count_task_2}')

if __name__ == '__main__':
    solve_day_four()