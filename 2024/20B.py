import sys

DIR = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}

def get_new_pos(pos, dir):
    return (pos[0] + DIR[dir][0], pos[1] + DIR[dir][1])

def run(grid,start,end):
    q = [(start,[start])]
    visited = set()
    while q:
        pos, path = q.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        if pos == end:
            return path
        for dir in DIR.keys():
            pos2 = get_new_pos(pos, dir)
            if (pos2 in grid) and (pos2 not in path) and (grid[pos2] == '.'):
                q.append((pos2, path + [pos2]))
    return None

    

def solve(input):
    grid = {}
    start = None
    end = None
    for r, line in enumerate(input.splitlines()):
        for c, val in enumerate(line):
            grid[(r,c)] = val
            if val == 'S':
                start = (r,c)
                grid[(r,c)] = '.'
            if val == 'E':
                end = (r,c)
                grid[(r,c)] = '.'

    orig_path = run(grid,start,end)
    orig_path_l = len(orig_path)

    result = 0
    for i, pos in enumerate(orig_path[:-1]):
        for j, pos2 in enumerate(orig_path[i+1:]):
            r1, c1 = pos
            r2, c2 = pos2
            # Steps between pos and pos2
            steps = abs(r1 - r2) + abs(c1 - c2)
            if steps <= 20:
                new_l = (steps - 1) + (i+1) + len(orig_path[i+1+j:])
                if new_l < orig_path_l:
                    saved = orig_path_l - new_l
                    if saved >= 100:
                        result +=1

    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))