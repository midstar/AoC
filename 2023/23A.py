import sys

def paths(lines, pos):
    p = []
    row, col = pos
    if row > 0:
        o = lines[row-1][col]
        if o == '.' or o == '^':
            steps = 1
            r = row - 1
            if o == '^':
                steps += 1
                r -= 1
            p.append((steps, (r,col)))
    if row < (len(lines) - 1):
        o = lines[row+1][col]
        if o == '.' or o == 'v':
            steps = 1
            r = row + 1
            if o == 'v':
                steps += 1
                r += 1
            p.append((steps, (r,col)))
    if col > 0:
        o = lines[row][col-1]
        if o == '.' or o == '<':
            steps = 1
            c = col - 1
            if o == '<':
                steps += 1
                c -= 1
            p.append((steps, (row,c)))
    if col < (len(lines[0]) - 1):
        o = lines[row][col+1]
        if o == '.' or o == '>':
            steps = 1
            c = col + 1
            if o == '>':
                steps += 1
                c += 1
            p.append((steps, (row,c)))
    return p


def bfs(lines, start, stop):
    # (steps, pos, path)
    q = [(0, start,[start])]
    max_steps = 0
    max_path = []
    while q:
        (steps, pos, path) = q.pop()
        for (step, pos2) in paths(lines, pos):
            if pos2 not in path:
                path2 = path.copy()
                path2.append(pos2)
                steps2 = step + steps
                if pos2 == stop:
                    if steps2 > max_steps:
                         max_steps = steps2
                         max_path = path2
                else:
                    q.append((steps2, pos2, path2))
    return max_steps, max_path




def solve(input):
    lines = input.splitlines()

    start = (0, lines[0].index('.'))
    last_row = len(lines) - 1
    stop = (last_row, lines[last_row].index('.'))

    max_steps, max_path = bfs(lines, start, stop)
    #print(max_path)
    result = max_steps

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))