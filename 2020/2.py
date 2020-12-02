data = [x for x in open('data/2.in').read().split('\n')]

def valid_password(x):
    count_part, letter_part, password = x.split(' ')
    min_count, max_count = [int(x) for x in count_part.split('-')]
    letter = letter_part[0]

    return min_count <= password.count(letter) <= max_count


def actually_valid_password(x):
    pos_part, letter_part, password = x.split(' ')
    first_pos, second_pos = [int(x) - 1 for x in pos_part.split('-')]
    letter = letter_part[0]

    return (letter == password[first_pos]) is not (letter == password[second_pos])

def part_1():
    return sum([valid_password(x) for x in data])


def part_2():
    return sum([actually_valid_password(x) for x in data])


print(f'{part_1()} - {part_2()}')