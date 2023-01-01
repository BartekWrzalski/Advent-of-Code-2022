from itertools import chain
from collections import Counter

with open('source', 'r') as file:
    file = file.read().splitlines()
    moves = [(row[0], int(row[2::])) for row in file]


def first_puzzle():
    head = [0, 0]
    tail = [0, 0]
    tail_positions = [tuple(tail)]

    for direction, steps in moves:
        while steps > 0:
            head[0 if direction in 'RL' else 1] += 1 if direction in 'RU' else -1

            if not (-1 <= head[0] - tail[0] <= 1):
                tail[0] += 1 if head[0] > tail[0] else -1
                if head[1] != tail[1]:
                    tail[1] = head[1]

                tail_positions.append(tuple(tail))

            elif not (-1 <= head[1] - tail[1] <= 1):
                tail[1] += 1 if head[1] > tail[1] else -1
                if head[0] != tail[0]:
                    tail[0] = head[0]

                tail_positions.append(tuple(tail))
            steps -= 1

    print(len(Counter(chain(tail_positions))))


def second_puzzle():
    pos = [[0, 0] for _ in range(10)]
    tail_positions = [tuple(pos[9])]

    for direction, steps in moves:
        while steps > 0:
            pos[0][0 if direction in 'RL' else 1] += 1 if direction in 'RU' else -1

            for x in range(1, 10):
                if not (-1 <= pos[x - 1][0] - pos[x][0] <= 1):
                    pos[x][0] += 1 if pos[x - 1][0] > pos[x][0] else -1
                    if pos[x - 1][1] != pos[x][1]:
                        pos[x][1] += 1 if pos[x - 1][1] > pos[x][1] else -1  # always at 2 diagonal dist

                elif not (-1 <= pos[x - 1][1] - pos[x][1] <= 1):
                    pos[x][1] += 1 if pos[x - 1][1] > pos[x][1] else -1
                    if pos[x - 1][0] != pos[x][0]:
                        pos[x][0] += 1 if pos[x - 1][0] > pos[x][0] else -1  # always at 2 diagonal dist

                else:
                    break
            else:
                tail_positions.append(tuple(pos[9]))

            steps -= 1

    print(len(Counter(chain(tail_positions))))


first_puzzle()
second_puzzle()
