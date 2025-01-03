import sys

DIR = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}

def get_new_pos(pos, dir):
    return (pos[0] + DIR[dir][0], pos[1] + DIR[dir][1])

DIR_ORDER = ['U', 'R', 'D', 'L']
def get_new_dir(dir):
    return DIR_ORDER[(DIR_ORDER.index(dir) + 1) % len(DIR_ORDER)]

def run(grid,dir,pos):
    visited = {(pos, dir)}
    while True:
        next = get_new_pos(pos, dir)
        if next not in grid:
            return set([pos for pos, _ in visited])
        if grid[next] == '#':
            dir = get_new_dir(dir)
        else:
            pos = next
            if (pos,dir) in visited:
                return None # In forewer loop
            visited.add((pos, dir))

def solve(input):
    grid = {}
    start = None
    for r, line in enumerate(input.splitlines()):
        for c, val in enumerate(line):
            grid[(r,c)] = val
            if val == "^":
                start = (r,c)
    
    return len(run(grid,'U',start))
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))