from itertools import permutations
import math

data = [int(x) for x in open('data/1.in').readlines()]


def part_1():
    for x in list(permutations(data, 2)):
        if sum(x) == 2020:
            return math.prod(x)


def part_2():
    for x in list(permutations(data, 3)):
        if sum(x) == 2020:
            return math.prod(x)


print(f'{part_1()} - {part_2()}')
