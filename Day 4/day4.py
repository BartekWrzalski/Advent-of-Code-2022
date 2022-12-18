import re

with open('source', 'r') as file:
    file = file.read().splitlines()
    sections = [list(map(int, re.split('[,-]', row))) for row in file]


def first_puzzle():
    overlapping = 0
    for section in sections:
        if (
            section[0] <= section[2] and section[1] >= section[3]
            or section[0] >= section[2] and section[1] <= section[3]
        ):
            overlapping += 1
    print(overlapping)


def second_puzzle():
    overlapping = 0
    for section in sections:
        if not (
            section[0] <= section[1] < section[2]
            or section[3] < section[0] <= section[1]
        ):
            overlapping += 1
    print(overlapping)


first_puzzle()
second_puzzle()
