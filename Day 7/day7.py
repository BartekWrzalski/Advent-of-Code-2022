with open('source', 'r') as file:
    file = file.read().splitlines()


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent: Dir = parent
        self.size = 0
        self.dirs = {}


root = Dir('/')


def build_tree():
    current: Dir = root
    for line in file:
        if line[0] == '$':
            if line[2] != 'c':
                continue

            dir_name = line.split(' ')[2]
            if dir_name == '/':
                current = root
            elif dir_name == '..':
                current = current.parent
            else:
                current = current.dirs[dir_name]

        elif line[0] == 'd':
            dir_name = line.split(' ')[-1]
            current.dirs[dir_name] = Dir(dir_name, current)

        else:
            size = int(line.split(' ')[0])
            _current = current
            _current.size += size
            while _current.parent:
                _current.parent.size += size
                _current = _current.parent


def first_puzzle():
    sum_of_dirs = 0
    dirs = [root]
    for directory in dirs:
        if directory.size < 100000:
            sum_of_dirs += directory.size

            all_below = list(directory.dirs.values())
            for child_dir in all_below:
                sum_of_dirs += child_dir.size
                all_below.extend(list(child_dir.dirs.values()))

        else:
            dirs.extend(list(directory.dirs.values()))
    print(sum_of_dirs)


def second_puzzle():
    size_to_free = root.size - 40000000

    dirs_to_search = [root]
    dir_del_size = 40000000
    for directory in dirs_to_search:
        if directory.size > size_to_free:
            if directory.size < dir_del_size:
                dir_del_size = directory.size
            dirs_to_search.extend(directory.dirs.values())

    print(dir_del_size)


build_tree()
first_puzzle()
second_puzzle()
