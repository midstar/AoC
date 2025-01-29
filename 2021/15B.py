import sys
import heapq

def neighbours(grid,pos):
    n = {(pos[0] + dr, pos[1] + dc) for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]}
    return {p for p in n if p in grid}

# Dijkstra
def lowest_risk(grid, start, stop):
    q = []
    heapq.heappush(q, (0,start))
    visited = set()
    while q:
        risk, node = heapq.heappop(q)
        if node == stop:
            return risk
        if node in visited:
            continue
        visited.add(node)
        for node2 in neighbours(grid,node):
            heapq.heappush(q, (risk + grid[node2], node2))

def next_val(prev, inc):
    new = prev + inc
    if new > 9:
        new = new - 9
    return new

def solve(input):
    grid = {(r,c) : int(v) for r,l in enumerate(input.splitlines()) for c, v in enumerate(l)}
    height = max(grid.keys())[0] + 1
    width = max(grid.keys())[1] + 1
    # Expand 4 times down
    grid2 = {}
    for tile in range(1,5):
        for (r,c),val in grid.items():
            grid2[(r + height * tile,c)] = next_val(val,tile)
    grid |= grid2
    # Expand 4 times right
    grid2 = {}
    for tile in range(1,5):
        for (r,c),val in grid.items():
            grid2[(r,c + width * tile)] = next_val(val,tile)
    grid |= grid2

    return lowest_risk(grid,min(grid.keys()),max(grid.keys()))
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))