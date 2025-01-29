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

def solve(input):
    grid = {(r,c) : int(v) for r,l in enumerate(input.splitlines()) for c, v in enumerate(l)}
    return lowest_risk(grid,min(grid.keys()),max(grid.keys()))
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))