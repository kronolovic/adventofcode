import math

data = [x.strip() for x in open('data/3.in')]


def count_trees_path(map, right, down):
    column, row, trees = 0, 0, 0

    while row + 1 < len(map):
        column += right
        row += down

        if map[row][column % len(map[row])] == '#':
            trees += 1

    return trees


def part_1():
    return count_trees_path(data, 3, 1)


def part_2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod(count_trees_path(data, x[0], x[1]) for x in slopes)


print(f'{part_1()} - {part_2()}')
