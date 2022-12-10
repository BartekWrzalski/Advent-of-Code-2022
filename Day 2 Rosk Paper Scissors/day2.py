with open('source', 'r') as file:
    file = file.read().splitlines()
    games = [(game[0], game[2]) for game in file]

points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

tie_against = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

win_against = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

lose_against = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}


def first_puzzle():
    score = 0

    for foe, me in games:
        score += points[me]

        if me == tie_against[foe]:
            score += 3
        elif me == win_against[foe]:
            score += 6
    print(score)


def second_puzzle():
    score = 0

    for foe, result in games:
        if result == 'Z':
            score += 6 + points[win_against[foe]]
        elif result == 'Y':
            score += 3 + points[tie_against[foe]]
        else:
            score += points[lose_against[foe]]

    print(score)


first_puzzle()
second_puzzle()
