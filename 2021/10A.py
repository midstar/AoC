import sys

OPEN  = '([{<'
CLOSE = ')]}>'
POINTS = { ')' :3,']': 57, '}': 1197,'>': 25137}

def points(line):
    o = []
    for c in line:
        if c in OPEN:
            o.append(c)
        elif CLOSE.index(c) != OPEN.index(o[-1]):
            return POINTS[c]
        else:
            o.pop()
    return 0

def solve(input):
    return sum(points(line) for line in input.splitlines())
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))