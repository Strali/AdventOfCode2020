from collections import deque, Counter, defaultdict
import functools
import re
import sys
import os
import operator
sys.path.insert(0, os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode'))

import numpy as np
from utils.read_aoc_input_file import read_aoc_input_file
from utils.get_input_path import get_input_path


def solve_day_sixteen():
    input_data = read_aoc_input_file('Day_16', return_as_string=True)
    regex = r'([\d-]*) or ([\d-]*)'

    valid_ranges = {}
    rules = input_data[:20]
    tickets = [int(t) for r in input_data[25:] for t in r.split(',')]

    for rule in rules:
        ranges = re.findall(regex, rule)
        for interval in ranges[0]:
            limits = interval.split('-')
            valid_ranges([int(limits[0]), int(limits[1])])

    tser = 0
    for ticket_value in tickets:
        if not any([ticket_value in range(r[0], r[1]) for r in valid_ranges]):
            tser += ticket_value

    print(tser)


def parse_field(field):
    name, valid = field.split(':')
    valid = [tuple(map(int, r)) for r in
             (r.split('-') for r in valid.split(' or '))]
    return name, valid

def read_ticket(ticket):
    return [int(v) for v in ticket.split(',')]

def valid_value(fields, value):
    return any(value in range(r[0], r[1]+1) for val in fields.values() for r in val)


def part_two():
    with open(get_input_path('Day_16', False)) as f:
        fields, ticket, nearby = f.read().split('\n\n')

    own_ticket = read_ticket(ticket.splitlines()[1])
    nearby_tickets = [read_ticket(t) for t in nearby.splitlines()[1:]]
    fields = {p[0]: p[1] for p in (parse_field(f) for f in fields.splitlines())}

    valid_tickets = [t for t in nearby_tickets if all(valid_value(fields, n) for n in t)]

    candidates = {}
    for i in range(len(own_ticket)):
        candidates[i] = set()
        for f, v in fields.items():
            if all(any(r[0] <= t[i] <= r[1] for r in v) for t in valid_tickets):
                candidates[i].add(f)

if __name__ == '__main__':
    solve_day_sixteen()
