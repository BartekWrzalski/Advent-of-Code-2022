with open('source', 'r') as file:
    msg = file.read()


def first_puzzle():
    for i in range(len(msg)):
        marker = set(msg[i:i + 4])

        if len(marker) == 4:
            print(i + 4)
            break


def second_puzzle():
    for i in range(len(msg)):
        marker = set(msg[i:i + 14])

        if len(marker) == 14:
            print(i + 14)
            break


first_puzzle()
second_puzzle()
