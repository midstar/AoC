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
        for _ in range(l):
            fs.append(val)

    ei = len(fs) - 1
    for i in range(len(fs)):
        if i >= ei:
            fs = fs[:ei + 1]
            break
        if fs[i] == -1:
            while fs[ei] == -1 and ei > i:
                ei -= 1
            if ei > i:
                fs[i] = fs[ei]
                ei -= 1

    return sum([i * id for i, id in enumerate(fs)])
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))