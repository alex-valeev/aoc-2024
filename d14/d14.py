from collections import defaultdict
from typing import List, Dict
from math import prod

TEST = 'test.txt'
PROD = 'input.txt'
TEST_SPACE = {'w': 11, 'h': 7}
PROD_SPACE = {'w': 101, 'h': 103}
OUTPUT = 'output.txt'


def read_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def parse_data(raw_data: List) -> List:
    parsed_data = []
    for row in raw_data:
        pos, dim = row.split()
        parsed_data.append(
            [
                tuple(map(int, pos[2:].split(','))),
                tuple(map(int, dim[2:].split(',')))
            ]
        )

    return parsed_data


def part1(robots: List, space_dim: Dict) -> int:
    w, h = space_dim['w'], space_dim['h']
    half_w, half_h = w // 2, h // 2
    positions = defaultdict(int)

    for robot in robots:
        pos_x, pos_y = robot[0]
        vel_x, vel_y = robot[1]
        pos_x = (pos_x + vel_x * 100) % w
        pos_y = (pos_y + vel_y * 100) % h
        positions[get_q(pos_x, pos_y, half_w, half_h)] += 1
    positions[''] = 1

    return prod(positions.values())


def part2(robots: List, space_dim: Dict, file: str, loops: int) -> str:
    w, h = space_dim['w'], space_dim['h']

    with open(file, 'w') as f:
        for i in range(loops):
            output = [[' '] * w for _ in range(h)]
            for robot in robots:
                pos_x, pos_y = robot[0]
                vel_x, vel_y = robot[1]
                pos_x = (pos_x + vel_x * i) % w
                pos_y = (pos_y + vel_y * i) % h
                output[pos_y][pos_x] = '#'

            f.write(f'==== {i} ====\n')
            f.write('┌' + '─' * w + '┐\n')
            for row in output:
                f.write('|' + ''.join(row) + '|\n')
            f.write('└' + '─' * w + '┘\n')
            f.write('\n\n')

    return f'see in file "{file}"'


def get_q(pos_x: int, pos_y: int, mid_x: int, mid_y: int) -> str:
    if pos_x == mid_x or pos_y == mid_y:
        return ''
    if pos_x < mid_x:
        if pos_y < mid_y:
            return 'q4'
        else:
            return 'q1'
    else:
        if pos_y < mid_y:
            return 'q3'
        else:
            return 'q2'


if __name__ == '__main__':
    test_data = parse_data(read_file(TEST))
    prod_data = parse_data(read_file(PROD))

    print("---------")
    print("TEST DATA")
    print(f"part1 = {part1(test_data, TEST_SPACE)}")
    print("---------")
    print("PROD DATA")
    print(f"part1 = {part1(prod_data, PROD_SPACE)}")
    print(f"part2 = {part2(prod_data, PROD_SPACE, OUTPUT, 10000)}")
