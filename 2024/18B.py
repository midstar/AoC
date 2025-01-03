import sys

DIR = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}

def get_new_pos(pos, dir):
    return (pos[0] + DIR[dir][0], pos[1] + DIR[dir][1])

def run(grid, max):
    end = (max,max)
    q = [((0,0), [(0,0)])]
    visited = set()
    while q:
        pos, path = q.pop(0)
        if pos == end:
            return path
        if pos in visited:
            continue
        visited.add(pos)
        for dir in DIR.keys():
            pos2 = get_new_pos(pos,dir)
            if pos2 not in grid:
                x, y = pos2
                if x >= 0 and y >= 0 and x <= max and y <= max:
                    q.append((pos2,path + [pos2]))
    return None

def solve(input):
    grid = [(int(l.split(',')[0]),int(l.split(',')[1])) for l in input.splitlines()]

    max = 70
    fallen_bytes = 1024

    #Example
    #max = 6
    #fallen_bytes = 12
    path = None
    for f in range(fallen_bytes, len(grid)):
        if path != None:
            if not any(v in grid[:f] for v in path):
                continue
        path = run(grid[:f], max)
        if path == None:
            x, y = grid[f - 1]
            return f'{x},{y}'
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))