import sys

def solve(input):
    fs = []
    id = 0
    for i, c in enumerate(input.strip()):
        l = int(c)
        val = -1
        if i % 2 == 0: # File
            val = id
            id += 1 
        if l > 0:
            fs.append((val,l))

    for i in reversed(range(id)):
        ni = -1
        nl = 0
        for j, (id_, l_) in enumerate(fs):
            if id_ == i:
                ni = j
                nl = l_
                break

        # Find free space
        for j, (id_, l_) in enumerate(fs):
            if j > ni:
                break # No Free space
            if id_ == -1 and l_ >= nl:
                fs[ni] = (-1, nl)
                if l_ == nl:
                    fs[j] = (i, nl)
                else:
                    fs[j] = (-1, l_ - nl)
                    fs.insert(j, (i, nl))
                break

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