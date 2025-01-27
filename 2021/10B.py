import sys

OPEN  = '([{<'
CLOSE = ')]}>'
POINTS = { ')' :1,']': 2, '}': 3,'>': 4}

def points(line):
    o = []
    for c in line:
        if c in OPEN:
            o.append(c)
        elif CLOSE.index(c) != OPEN.index(o[-1]):
            return 0
        else:
            o.pop()
    score = 0
    for c in reversed(o):
        cl = CLOSE[OPEN.index(c)]
        score = 5 * score + POINTS[cl]
    return score

def solve(input):
    scores = sorted(points(line) for line in input.splitlines())
    scores = [score for score in scores if score > 0]
    return scores[len(scores) // 2]
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))