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

def get_dirs_with_min_size(directory, min_size):
    dirs = []
    if directory.size() >= min_size:
        dirs.append(directory)
    for subdir in directory.children.values():
        dirs += get_dirs_with_min_size(subdir, min_size)

    return dirs

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
    
    to_be_removed = fs.size() - (70000000 - 30000000)
    dirs = get_dirs_with_min_size(fs, to_be_removed)
    dirs.sort(key=lambda x: x.size())
    
    return dirs[0].size()
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))