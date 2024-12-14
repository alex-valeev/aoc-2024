from collections import defaultdict
from typing import List, Dict
from itertools import permutations

TEST = 'test.txt'
PROD = 'input.txt'


def read_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]


def parse_file(data: List) -> Dict:
    antennas = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != '.':
                antennas[data[y][x]].append((y, x))

    return antennas


def part1(field: List, antennas: Dict) -> int:
    return calc_antinodes(field, antennas, single=True)


def part2(field: List, antennas: Dict) -> int:
    return calc_antinodes(field, antennas, single=False)


def calc_antinodes(field: List, antennas: Dict, single: bool) -> int:
    antinodes = set()
    h, w = len(field), len(field[0])
    steps = 1 if single else max(h, w)

    for code in antennas.keys():
        nodes = antennas[code]
        if not single:
            antinodes.update(nodes)

        for pair in permutations(nodes, 2):
            node1, node2 = pair

            for s in range(steps):
                ok = False

                y, x = build_antinode(node1, node2, s)
                if 0 <= y < h and 0 <= x < w:
                    antinodes.add((y, x))
                    ok = True

                y, x = build_antinode(node2, node1, s)
                if 0 <= y < h and 0 <= x < w:
                    antinodes.add((y, x))
                    ok = True

                if not ok:
                    break

    return len(list(antinodes))


def build_antinode(node1: list, node2: list, kf: int) -> (int, int):
    y = node1[0] + (node1[0] - node2[0]) * (kf + 1)
    x = node1[1] + (node1[1] - node2[1]) * (kf + 1)

    return y, x


if __name__ == '__main__':
    test_field = read_file(TEST)
    prod_field = read_file(PROD)
    test_antennas = parse_file(test_field)
    prod_antennas = parse_file(prod_field)

    print("---------")
    print("TEST DATA")
    print(f"part1 = {part1(test_field, test_antennas)}")
    print(f"part2 = {part2(test_field, test_antennas)}")
    print("---------")
    print("PROD DATA")
    print(f"part1 = {part1(prod_field, prod_antennas)}")
    print(f"part2 = {part2(prod_field, prod_antennas)}")
