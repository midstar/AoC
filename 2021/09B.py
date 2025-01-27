import sys

def basin(grid,pos,locations):
    locations.add(pos)
    r, c = pos
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        pos2 = (r + dr, c + dc)
        if pos2 in grid and pos2 not in locations and grid[pos2] != 9:
            basin(grid,pos2,locations)
    return len(locations)

def is_low(grid,pos):
    r, c = pos
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        pos2 = (r + dr, c + dc)
        if pos2 in grid and grid[pos2] <= grid[pos]:
            return False
    return True

def solve(input):
    grid = {(r,c) : int(v) for r,l in enumerate(input.splitlines()) for c, v in enumerate(l)}
    basins = sorted([basin(grid,p,set()) for p in grid.keys() if is_low(grid,p)])
    return basins[-1] * basins[-2] * basins[-3]
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))