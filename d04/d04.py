from typing import List

TEST = 'test.txt'
PROD = 'input.txt'


def parse_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]


def check_xmas(mas: str) -> bool:
    if mas == 'XMAS' or mas == 'SAMX':
        return True
    return False


def check_mas(mas: str) -> bool:
    if mas == 'MAS' or mas == 'SAM':
        return True
    return False


def search_xmas_line(i: int, j: int, data: list) -> int:
    xmas = 0
    down = True if i <= len(data) - 4 else False
    left = True if j >= 3 else False
    right = True if j <= len(data) - 4 else False

    if right and check_xmas(data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i][j + 3]):
        xmas += 1

    if down and check_xmas(data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 3][j]):
        xmas += 1

    if right and down and check_xmas(
            data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2] + data[i + 3][j + 3]):
        xmas += 1

    if left and down and check_xmas(
            data[i][j] + data[i + 1][j - 1] + data[i + 2][j - 2] + data[i + 3][j - 3]):
        xmas += 1

    return xmas


def search_xmas_cross(i: int, j: int, data: list) -> int:
    xmas = 0

    if check_mas(data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2]) \
            and check_mas(data[i + 2][j] + data[i + 1][j + 1] + data[i][j + 2]):
        xmas += 1

    return xmas


def part1(data: List) -> int:
    words = 0

    for i in range(len(data)):
        for j in range(len((data[0]))):
            if data[i][j] == 'X' or data[i][j] == 'S':
                words += search_xmas_line(i, j, data)

    return words


def part2(data: List) -> int:
    words = 0

    for i in range(len(data) - 2):
        for j in range(len((data[0])) - 2):
            if data[i][j] == 'M' or data[i][j] == 'S':
                words += search_xmas_cross(i, j, data)

    return words


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
