import sys

def get_file(fs, id, start_i):
    for j in range(start_i, len(fs)):
        id_, l_ = fs[j]
        if id_ == id:
            return j, l_

def get_free_space(fs, min_size, max_i, start_i = 0):
    first_free = -1
    for j in range(start_i, len(fs)):
        id_, l_ = fs[j]
        if j > max_i:
            return -1, -1, first_free
        if id_ == -1:
            if first_free == -1: 
                first_free = j
            if l_ >= min_size:
                return j, l_, first_free
    return -1, -1, first_free

def solve(input):
    fs = []
    files = {}
    id = 0
    for i, c in enumerate(input.strip()):
        l = int(c)
        val = -1
        if i % 2 == 0: # File
            files[id] = (len(fs),l)
            val = id
            id += 1 
        if l > 0:
            fs.append((val,l))

    first_free = 0
    for i in reversed(range(id)):
        ni, nl = get_file(fs, i, files[i][0])
        free_i, l, first_free = get_free_space(fs,nl,ni, first_free)
        if free_i >= 0:
            fs[ni] = (-1, nl)
            if l == nl:
                fs[free_i] = (i, nl)
            else:
                fs[free_i] = (-1, l - nl)
                fs.insert(free_i, (i, nl))


    checksum = 0
    multiplier = 0
    for i, (id, l) in enumerate(fs):
        for j in range(l):
            if id > 0:
                checksum += multiplier * id
            multiplier += 1

    return checksum
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))