from typing import List

TEST = 'test.txt'
PROD = 'input.txt'


def read_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def dp(i: int, op: list, cur_val: int, ans: int) -> bool:
    if i == len(op):
        return True if cur_val == ans else False

    return any([dp(i + 1, op, cur_val + op[i], ans),
                dp(i + 1, op, cur_val * op[i], ans)])


def dp_advanced(i: int, op: list, cur_val: int, ans: int) -> bool:
    if i == len(op):
        return True if cur_val == ans else False

    return any([dp_advanced(i + 1, op, cur_val + op[i], ans),
                dp_advanced(i + 1, op, cur_val * op[i], ans),
                dp_advanced(i + 1, op, int(str(cur_val) + str(op[i])), ans)])


def calibration(data: List) -> (int, int):
    total_pt1, total_pt2 = 0, 0
    for i, equation in enumerate(data):
        answer, operators = equation.split(':')
        answer, operators = int(answer), list(map(int, operators.split()))

        if dp(0, operators, 0, answer):
            total_pt1 += answer

        if dp_advanced(0, operators, 0, answer):
            total_pt2 += answer

    return total_pt1, total_pt2


if __name__ == '__main__':
    test_data = read_file(TEST)
    prod_data = read_file(PROD)

    print("---------")
    print("TEST DATA")
    print("part1 = %d \npart2 = %d" % (calibration(test_data)))
    print("---------")
    print("PROD DATA")
    print("part1 = %d \npart2 = %d" % (calibration(prod_data)))
