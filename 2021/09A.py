import sys

def is_low(grid,pos):
    r, c = pos
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        pos2 = (r + dr, c + dc)
        if pos2 in grid and grid[pos2] <= grid[pos]:
            return False
    return True

def solve(input):
    grid = {(r,c) : int(v) for r,l in enumerate(input.splitlines()) for c, v in enumerate(l)}
    return sum(v + 1 for p,v in grid.items() if is_low(grid,p))
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))