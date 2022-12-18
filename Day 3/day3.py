import string

with open('source', 'r') as file:
    rucksacks = file.read().splitlines()


def first_puzzle():
    value = 0
    for rucksack in rucksacks:
        half = len(rucksack) // 2
        left_part = rucksack[:half]
        right_part = rucksack[half:]

        item = set(left_part).intersection(set(right_part)).pop()

        if item in string.ascii_lowercase:
            value += ord(item) - 96
        else:
            value += ord(item) - 38
    print(value)


def second_puzzle():
    value = 0
    for i in range(0, len(rucksacks), 3):
        first_elf = rucksacks[i]
        second_elf = rucksacks[i + 1]
        third_elf = rucksacks[i + 2]

        badge = set(first_elf).intersection(second_elf).intersection(third_elf).pop()

        if badge in string.ascii_lowercase:
            value += ord(badge) - 96
        else:
            value += ord(badge) - 38
    print(value)


first_puzzle()
second_puzzle()
