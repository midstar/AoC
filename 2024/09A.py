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

    while fs.count(-1) > 0:
        last = fs.pop()
        if last != -1:
            fs[fs.index(-1)] = last

    return sum([i * id for i, id in enumerate(fs)])
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))