from typing import List
from re import findall

TEST = 'test.txt'
PROD = 'input.txt'
REGEX_PT1 = r'mul\(\d{1,3}\,\d{1,3}\)'
REGEX_PT2 = r'mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)'


def parse_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def calc(mul: str) -> int:
    one, two = map(int, str(mul[4:len(mul) - 1]).split(","))
    return one * two


def part1(data: List) -> int:
    results = 0
    for instruction in data:
        multiplication = findall(REGEX_PT1, instruction)
        for multi in multiplication:
            results += calc(multi)

    return results


def part2(data: List) -> int:
    results = 0
    doit = True
    for instruction in data:
        multiplication = findall(REGEX_PT2, instruction)
        for multi in multiplication:
            match multi:
                case 'do()':
                    doit = True
                case 'don\'t()':
                    doit = False
                case _:
                    if doit:
                        results += calc(multi)

    return results


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
