import sys

DIR = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}

def get_new_pos(pos, dir):
    return (pos[0] + DIR[dir][0], pos[1] + DIR[dir][1])

def run(grid,start,end, start_path=[], orig_path=[]):
    q = [(start,start_path)]
    visited = set(start_path[:-1])
    while q:
        pos, path = q.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        if pos not in start_path and pos in orig_path:
            return path + orig_path[orig_path.index(pos) + 1:]
        if pos == end:
            return path
        for dir in DIR.keys():
            pos2 = get_new_pos(pos, dir)
            if (pos2 in grid) and (grid[pos2] == '.'):
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

    orig_path = run(grid,start,end,[start])
    
    cheat_stones = set()
    result = 0
    for i, pos in enumerate(orig_path):
        for dir in DIR.keys():
            pos2 = get_new_pos(pos, dir)
            if pos2 in grid and grid[pos2] == '#' and grid[pos2] not in cheat_stones:
                cheat_stones.add(pos2)
                grid[pos2] = '.'
                cheat_path = run(grid,pos2,end,orig_path[:i+1] + [pos2], orig_path)
                grid[pos2] = '#'
                if cheat_path != None and (len(orig_path) - len(cheat_path)) >= 100 :
                    result += 1
                    #print(pos2, len(cheat_path), len(orig_path) - len(cheat_path))



    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))