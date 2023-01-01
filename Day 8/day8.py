import numpy as np

with open('source', 'r') as file:
    file = file.read().splitlines()
    _forest = [list(int(tree) for tree in row) for row in file]


def first_puzzle():
    def check_side(forest, visible_trees):
        for i, row in enumerate(forest):
            tallest = row[0]
            visible_trees[i][0] = True
            for j, tree in enumerate(row):
                if tree > tallest:
                    tallest = tree
                    visible_trees[i][j] = True

    forest = np.asarray(a=_forest)
    visibilities = np.zeros(dtype=bool, shape=(len(forest), len(forest[0])))

    check_side(_forest, visibilities)

    forest = np.fliplr(forest)
    visibilities = np.fliplr(visibilities)
    check_side(forest, visibilities)

    forest = np.transpose(forest)
    visibilities = np.transpose(visibilities)
    check_side(forest, visibilities)

    forest = np.fliplr(forest)
    visibilities = np.fliplr(visibilities)
    check_side(forest, visibilities)

    print(np.count_nonzero(visibilities))


def second_puzzle():
    def get_upper_range(i, j):
        for k in range(i - 1, -1, -1):
            if _forest[k][j] >= _forest[i][j]:
                return i - k
        return i

    def get_down_range(i, j):
        for k in range(i + 1, len(_forest)):
            if _forest[k][j] >= _forest[i][j]:
                return k - i
        return len(_forest) - i - 1

    def get_left_range(i, j):
        for k in range(j - 1, -1, -1):
            if _forest[i][k] >= _forest[i][j]:
                return j - k
        return j

    def get_right_range(i, j):
        for k in range(j + 1, len(_forest)):
            if _forest[i][k] >= _forest[i][j]:
                return k - j
        return len(_forest) - j - 1

    best_score = 0
    for i in range(1, len(_forest) - 1):
        for j in range(1, len(_forest[0]) - 1):
            score = get_upper_range(i, j) * get_down_range(i, j) * get_left_range(i, j) * get_right_range(i, j)
            if score > best_score:
                best_score = score
    print(best_score)


first_puzzle()
second_puzzle()
