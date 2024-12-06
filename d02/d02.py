from typing import List

TEST = 'test.txt'
PROD = 'input.txt'


def parse_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [list(map(int, line.rstrip('\n').split())) for line in f.readlines()]


def diff(num1: int, num2: int) -> int:
    return abs(num2 - num1)


def sign(num1: int, num2: int) -> int:
    return num2 > num1


def check_report(report: list) -> bool:
    inc = sign(report[0], report[1])
    for i in range(1, len(report)):
        if not (inc == sign(report[i - 1], report[i]) and 0 < diff(report[i - 1], report[i]) < 4):
            return False

    return True


def part1(data: List) -> int:
    good_reports = 0
    for report in data:
        if check_report(report):
            good_reports += 1

    return good_reports


def part2(data: List) -> int:
    good_reports = 0
    for report in data:
        if check_report(report) or check_report(report[1:]) or check_report(report[:len(report) - 1]):
            good_reports += 1
        else:
            for i in range(1, len(report) - 1):
                if check_report(report[:i] + report[i + 1:]):
                    good_reports += 1
                    break

    return good_reports


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
