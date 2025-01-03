import sys

DIR = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}

def get_new_pos(pos, dir):
    return (pos[0] + DIR[dir][0], pos[1] + DIR[dir][1])

def head_score(grid, head):
    zero_pos = set()
    q = [head]
    while q:
        pos = q.pop(0)
        if grid[pos] == 0:
            zero_pos.add(pos)
            continue
        for dir in DIR.keys():
            pos2 = get_new_pos(pos,dir)
            if pos2 in grid and grid[pos2] == (grid[pos] - 1):
                q.append(pos2)
    return len(zero_pos)

def solve(input):
    grid = {}
    heads = []
    for r, line in enumerate(input.splitlines()):
        for c, val in enumerate(line):
            if val == '.': continue
            grid[(r,c)] = int(val)
            if int(val) == 9: heads.append((r,c))

    return sum([head_score(grid, head) for head in heads])
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))