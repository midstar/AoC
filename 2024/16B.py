import sys
import heapq

DIR = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}

def get_new_pos(pos, dir):
    return (pos[0] + DIR[dir][0], pos[1] + DIR[dir][1])


NEXT = {
    'U' : [('U',1),('L',1001),('R',1001)],
    'D' : [('D',1),('L',1001),('R',1001)],
    'L' : [('L',1),('U',1001),('D',1001)],
    'R' : [('R',1),('U',1001),('D',1001)]
}

def full_path(path, visited):
    result = path.copy()
    for p_d in path:
        if p_d in visited:
            result |= visited[p_d]['path']
    new_paths = result - path
    if new_paths:
        result |= full_path(new_paths, visited)
    return result

def run(grid,start,end,dir):
    q = []
    heapq.heappush(q, (0, start, dir, {(start,dir)}))

    visited = {}
    best_pos = set()
    best_path_points = 10000000000000

    while q:
        points, pos, dir, path = heapq.heappop(q)

        if points > best_path_points: break

        if pos == end:
            best_path_points = points
            best_pos |= {pos for pos, _ in full_path(path, visited)}
            continue

        if (pos, dir) not in visited:
            visited[(pos, dir)] = {'points':points,'path':path}
        else:
            if points <= visited[(pos, dir)]['points']:
                visited[(pos, dir)]['path'] |= path
            continue

        for dir2, points2 in NEXT[dir]:
            pos2 = get_new_pos(pos,dir2)
            if pos2 in grid:
                heapq.heappush(q, (points + points2, pos2, dir2, path | {(pos2,dir2)}))

    return len(best_pos)

def solve(input):
    grid = set()
    start = None
    end = None
    for r, line in enumerate(input.splitlines()):
        for c, val in enumerate(line):
            if val != '#':
                grid.add((r,c))
                if val == 'S':
                    start = (r,c)
                if val == 'E':
                    end = (r,c)

    return run(grid,start,end,'R')
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))