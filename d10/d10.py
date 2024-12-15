from typing import List

TEST = 'test.txt'
PROD = 'input.txt'


def read_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [list(map(int, line.rstrip('\n'))) for line in f.readlines()]


def trails(data: List) -> (int, int):
    def find_end(y: int, x: int):
        if data[y][x] == 9:
            trails_pt1.add((y, x))
            trails_pt2.append((y, x))
            return
        if y > 0 and data[y][x] + 1 == data[y - 1][x]:
            find_end(y - 1, x)
        if x > 0 and data[y][x] + 1 == data[y][x - 1]:
            find_end(y, x - 1)
        if y < h and data[y][x] + 1 == data[y + 1][x]:
            find_end(y + 1, x)
        if x < w and data[y][x] + 1 == data[y][x + 1]:
            find_end(y, x + 1)
        return

    starts = get_starts(data)
    trails_pt2 = []
    h, w, total_pt1 = len(data) - 1, len(data[0]) - 1, 0

    for start in starts:
        trails_pt1 = set()
        find_end(start[0], start[1])
        total_pt1 += len(list(trails_pt1))

    return total_pt1, len(trails_pt2)


def get_starts(data: List) -> List:
    starts = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                starts.append((y, x))

    return starts


if __name__ == '__main__':
    test_data = read_file(TEST)
    prod_data = read_file(PROD)

    print("---------")
    print("TEST DATA")
    print("part1 = %d \npart2 = %d" % (trails(test_data)))
    print("---------")
    print("PROD DATA")
    print("part1 = %d \npart2 = %d" % (trails(prod_data)))
