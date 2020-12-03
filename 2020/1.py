from itertools import permutations
import math

data = [int(x) for x in open('data/1.in').readlines()]


def n_sum(l, n, e):
    for x in list(permutations(l, n)):
        if sum(x) == e:
            return math.prod(x)


def part_1():
    return n_sum(data, 2, 2020)


def part_2():
    return n_sum(data, 3, 2020)


print(f'{part_1()} - {part_2()}')
