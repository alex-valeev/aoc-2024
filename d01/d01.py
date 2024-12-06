from typing import List
from collections import Counter

TEST = 'test.txt'
PROD = 'input.txt'


def parse_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n').split() for line in f.readlines()]


def get_transpose_data(data: List) -> (List, List):
    first_list, second_list = [], []
    for el in data:
        first_list.append(int(el[0]))
        second_list.append(int(el[1]))

    return sorted(first_list), sorted(second_list)


def part1(data: List) -> int:
    distance = 0
    one, two = get_transpose_data(data)
    for i in range(len(one)):
        distance += abs(one[i] - two[i])

    return distance


def part2(data: List) -> int:
    score = 0
    one, two = get_transpose_data(data)
    freq_two = Counter(two)
    for el in one:
        if el in freq_two:
            score += el * freq_two[el]

    return score


if __name__ == '__main__':
    test_data = parse_file(TEST)
    prod_data = parse_file(PROD)

    print("---------")
    print("TEST DATA")
    print(f"part1 = {part1(test_data)}")
    print(f"part2 = {part2(test_data)}")
    print("---------")
    print("PROD DATA")
    print(f"part1 = {part1(prod_data)}")
    print(f"part2 = {part2(prod_data)}")
