from __future__ import annotations
import operator
operators = {'+': operator.add, '*': operator.mul}


class Monkey:
    monkeys: list[Monkey] = []
    monkey_mod = 1  # least common multiple

    def __init__(
            self,
            _items: list[int],
            sign,
            divisible,
            throw_true: int,
            throw_false: int
    ):
        self.items = _items
        self.sign = sign
        self.divisible = divisible
        self.throw_true = throw_true
        self.throw_false = throw_false

        self.business = 0
        self.monkeys.append(self)

    def inspect(self, element, is_1_puzzle):
        for i in range(len(self.items)):
            self.items[i] = operators[self.sign](self.items[i], self.items[i] if element == 'old' else int(element))
            if is_1_puzzle:
                self.items[i] //= 3
            else:
                self.items[i] %= self.monkey_mod

            self.business += 1

    def throw(self):
        for item in self.items:
            self.monkeys[
                self.throw_true if item % self.divisible == 0 else self.throw_false
            ].items.append(item)
        self.items = []


def get_monkeys():
    Monkey.monkeys = []
    Monkey.monkey_mod = 1
    with open('source', 'r') as file:
        file = file.read().split('Monkey')
        monkeys = {}
        for monkey_data in file[1::]:
            data = monkey_data.splitlines()

            monkeys[Monkey(
                list(int(item) for item in data[1].split(':')[1].strip().split(',')),
                sign=data[2].split(' ')[-2],
                divisible=int(data[3].split(' ')[-1]),
                throw_true=int(data[4].split(' ')[-1]),
                throw_false=int(data[5].split(' ')[-1]),
            )] = data[2].split(' ')[-1]
            Monkey.monkey_mod *= int(data[3].split(' ')[-1])
        return monkeys


def first_puzzle():
    monkeys = get_monkeys()
    for i in range(20):
        for monkey, element in monkeys.items():
            monkey.inspect(element, True)
            monkey.throw()
    businesses = sorted([monkey.business for monkey in monkeys], reverse=True)
    print(businesses[0] * businesses[1])


def second_puzzle():
    monkeys = get_monkeys()
    for i in range(10000):
        for monkey, element in monkeys.items():
            monkey.inspect(element, False)
            monkey.throw()
    businesses = sorted([monkey.business for monkey in monkeys], reverse=True)
    print(businesses[0] * businesses[1])


first_puzzle()
second_puzzle()
