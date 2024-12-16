from functools import cache
from math import floor, pow, log10
from typing import List

TEST = 'test.txt'
PROD = 'input.txt'


def read_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return list(map(int, f.read().strip('\n').split()))


def part1(stones: List) -> int:
    return sum(calc_stones(stone, 25) for stone in stones)


def part2(stones: List) -> int:
    return sum(calc_stones(stone, 75) for stone in stones)


def calc_stones(stone: int, level_cap: int) -> int:
    return dp(stone, 0, level_cap)


@cache
def dp(stone: int, level: int, level_cap: int) -> int:
    if level == level_cap:
        return 1

    if stone == 0:
        return dp(1, level + 1, level_cap)
    elif floor(log10(stone)) % 2 == 1:
        mid = int(pow(10, (floor(log10(stone)) + 1) // 2))
        return sum((
            dp(stone // mid, level + 1, level_cap),
            dp(stone % mid, level + 1, level_cap)
        ))
    else:
        return dp(stone * 2024, level + 1, level_cap)


if __name__ == '__main__':
    test_data = read_file(TEST)
    prod_data = read_file(PROD)

    print("---------")
    print("TEST DATA")
    print(f"part1 = {part1(test_data)}")
    print(f"part2 = {part2(test_data)}")
    print("---------")
    print("PROD DATA")
    print(f"part1 = {part1(prod_data)}")
    print(f"part2 = {part2(prod_data)}")
