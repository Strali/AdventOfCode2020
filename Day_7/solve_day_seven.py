import os
import re
import sys
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np

from utils.read_aoc_input_file import read_aoc_input_file


def recursive_contents(bag_color, bag_dict):
    containing_bags = [bag for bag in bag_dict if bag_color in bag_dict[bag]]
    return [bag_color, *[contents for bag in containing_bags for contents in recursive_contents(bag, bag_dict)]]


def count_bags(bag_color, bag_dict):
    return sum(bag_dict[bag_color][content_color]*(1+count_bags(content_color, bag_dict)) for content_color in bag_dict[bag_color])


def solve_day_seven():
    input_data = read_aoc_input_file('Day_7', return_as_string=True)

    base_bag = 'shiny gold'

    bag_matcher = r'(\d+) (\w* \w*)'
    bag_dict = {}
    for line in input_data:
        top_bag = re.match(r'(\w* \w*)', line)[0]
        bag_contents = {bag: int(count) for count, bag in re.findall(bag_matcher, line)}
        bag_dict[top_bag] = bag_contents

    can_hold_gold_bag = len(set(recursive_contents(base_bag, bag_dict))) - 1 # Remove gold bag itself
    bag_content_count = count_bags(base_bag, bag_dict)

    print(f'Contains {base_bag} bag: {can_hold_gold_bag}')
    print(f'Bag contents of {base_bag} bag: {bag_content_count}')

if __name__ == '__main__':
    solve_day_seven()
