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

def run(grid,start,end,dir):
    q = []
    heapq.heappush(q, (0, start, dir))

    visited = set()
    while q:
        points, pos, dir = heapq.heappop(q)
        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))
        if pos == end:
            return points

        for dir2 in DIR.keys():
            pos2 = get_new_pos(pos,dir2)
            if pos2 in grid:
                points2 = points + 1
                if dir != dir2:
                    if dir in 'UD': 
                        points2 += 1000 # 90 deg
                        if dir2 in 'UD':
                            continue
                    elif dir in 'LR':
                        points2 += 1000 # 90 deg
                        if dir2 in 'LR':
                            continue
                heapq.heappush(q, (points2, pos2, dir2))

    return 0

def solve(input):

    grid = []
    start = None
    end = None
    for r, line in enumerate(input.splitlines()):
        for c, val in enumerate(line):
            if val != '#':
                grid.append((r,c))
                if val == 'S':
                    start = (r,c)
                if val == 'E':
                    end = (r,c)

    return run(grid,start,end,'R')
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))