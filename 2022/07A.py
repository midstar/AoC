import sys

class Directory(object):
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = set()
    def size(self):
        s = sum([size for (size, _) in self.files])
        s += sum([child.size() for child in self.children.values()])
        return s

def sum_directory_size(directory, max_size):
    size = 0
    if directory.size() < max_size:
        size += directory.size()
    for subdir in directory.children.values():
        size += sum_directory_size(subdir, max_size)

    return size

def solve(input):
    fs = Directory('/')
    cd = fs
    lines = input.splitlines()
    while lines:
        line = lines.pop(0)
        if line.startswith('$ cd'):
            d = line.split()[2]
            if d == '/':
                cd = fs
            elif d == '..':
                cd = cd.parent
            else:
                if d not in cd.children:
                    cd.children[d] = Directory(d, cd)
                cd = cd.children[d]
        if line == '$ ls':
            while lines and lines[0][0] != '$':
                line = lines.pop(0)
                if not line.startswith('dir'):
                    (size, file_name) = tuple(line.split())
                    cd.files.add((int(size), file_name))
    
    return sum_directory_size(fs, 100000)
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))