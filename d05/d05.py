from typing import List, Dict
from collections import defaultdict

TEST = 'test.txt'
PROD = 'input.txt'


def parse_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def prepare_data(data: List) -> (Dict, List):
    rules = defaultdict(list)
    ind = data.index('')

    for rule in sorted(data[:ind]):
        first, last = list(map(int, rule.split('|')))
        rules[first].append(last)

    return [rules, [list(map(int, manual.split(','))) for manual in data[ind + 1:]]]


def print_manual(data: List) -> (int, int):
    rules, manuals = prepare_data(data)
    total_mid_page_num, total_mid_page_num_incorrect = 0, 0
    for manual in manuals:
        if check_pages(rules, manual):
            total_mid_page_num += manual[len(manual) // 2]
        else:
            new_manual = build_manual(rules, manual)
            total_mid_page_num_incorrect += new_manual[len(new_manual) // 2]

    return total_mid_page_num, total_mid_page_num_incorrect


def check_pages(rules: Dict, pages: List) -> bool:
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if pages[j] not in rules[pages[i]]:
                return False
    return True


def build_manual(rules: Dict, pages: List) -> List:
    manual = {}.fromkeys(pages, 0)
    for i in range(len(pages)):
        for j in range(len(pages)):
            if pages[j] in rules[pages[i]]:
                manual[pages[i]] += 1
    return [el[0] for el in sorted(manual.items(), key=lambda x: x[1], reverse=True)]


if __name__ == '__main__':
    test_data = parse_file(TEST)
    prod_data = parse_file(PROD)

    print("---------")
    print("TEST DATA")
    print("part1 = %d \npart2 = %d" % (print_manual(test_data)))
    print("---------")
    print("PROD DATA")
    print("part1 = %d \npart2 = %d" % (print_manual(prod_data)))
