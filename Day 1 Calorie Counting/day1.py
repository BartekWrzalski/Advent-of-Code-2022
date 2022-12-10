with open('source', 'r+') as file:
    file = file.read().splitlines()
    calories = [int(calorie) if calorie else 0 for calorie in file]


def first_puzzle():
    max_cal = current_cal = 0

    for calorie in calories:
        if calorie:
            current_cal += calorie
        else:
            if current_cal > max_cal:
                max_cal = current_cal
            current_cal = 0
    print(max_cal)


def second_puzzle():
    sum_calories = []

    elf_calorie = 0
    for calorie in calories:
        if calorie:
            elf_calorie += calorie
        else:
            sum_calories.append(elf_calorie)
            elf_calorie = 0

    print(sum(sorted(sum_calories)[-3::]))


first_puzzle()
second_puzzle()

