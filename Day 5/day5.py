from collections import deque
from copy import deepcopy

with open('source', 'r') as file:
    file = file.read().splitlines()

list_row = file.index([line for line in file if line.startswith(' ')][0])
list_num = int(file[list_row][-1])

_dequeues: [deque] = [deque() for _ in range(list_num)]
for i in range(list_num):
    for line in file[list_row - 1:: -1]:
        if 1 + i * 4 > len(line) or line[1 + i * 4] == ' ':
            break
        _dequeues[i].append(line[1 + i * 4])

moves = []
for line in file[list_row + 2::]:
    moves.append(tuple(map(int, line.split(' ')[1::2])))


def first_puzzle(lists):
    for amount, src, dest in moves:
        lists[dest - 1].extend(
            [lists[src - 1].pop() for _ in range(amount)]
        )
    print(''.join(deq.pop() for deq in lists))


def second_puzzle(lists):
    for amount, src, dest in moves:
        lists[dest - 1].extend(
            reversed([lists[src - 1].pop() for _ in range(amount)])
        )
    print(''.join(deq.pop() for deq in lists))


first_puzzle(deepcopy(_dequeues))
second_puzzle(deepcopy(_dequeues))
