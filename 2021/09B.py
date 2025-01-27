import sys

def neighbours(grid,pos):
    n = {(pos[0] + dr, pos[1] + dc) for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]}
    return {p for p in n if p in grid}

def basin(grid,pos,locations):
    locations.add(pos)
    return 1 + sum(basin(grid,pos2,locations) for pos2 in neighbours(grid,pos) if pos2 not in locations and grid[pos2] != 9)

def is_low(grid,pos):
    return all(grid[pos2] > grid[pos] for pos2 in neighbours(grid,pos))

def solve(input):
    grid = {(r,c) : int(v) for r,l in enumerate(input.splitlines()) for c, v in enumerate(l)}
    basins = sorted([basin(grid,p,set()) for p in grid.keys() if is_low(grid,p)])
    return basins[-1] * basins[-2] * basins[-3]
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))