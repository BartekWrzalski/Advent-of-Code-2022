from textwrap import wrap
with open('source', 'r') as file:
    file = file.read().splitlines()
    signals = [line if line[0] == 'n' else int(line.split(' ')[-1]) for line in file]


def first_puzzle():
    sum_value = 0
    current_val = 1
    check_cycle = 20
    cycle = 0

    def next_cycle():
        nonlocal cycle, check_cycle, sum_value
        cycle += 1
        if cycle == check_cycle:
            sum_value += current_val * check_cycle
            check_cycle += 40

    for signal in signals:
        if isinstance(signal, str):
            next_cycle()

        else:
            next_cycle()
            next_cycle()
            current_val += signal

    print(sum_value)


def second_puzzle():
    current_val = 1
    cycle = 0
    drawing = ''

    def next_cycle():
        nonlocal cycle, current_val
        pixel = '#' if -1 <= current_val - cycle <= 1 else '.'
        cycle += 1
        if cycle == 40:
            cycle = 0

        return pixel

    for signal in signals:
        if isinstance(signal, str):
            drawing += next_cycle()

        else:
            drawing += next_cycle()
            drawing += next_cycle()
            current_val += signal

    print('\n'.join(wrap(drawing, 40)))


first_puzzle()
second_puzzle()
