import sys

def neighbours(grid,pos):
    n = {(pos[0] + dr, pos[1] + dc) for dr, dc in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]}
    return {p for p in n if p in grid}

def increase_all(grid):
    for p, v in grid.items():
        grid[p] = (v + 1) % 10

def flash(grid, pos, flashed):
    if grid[pos] > 0:
        grid[pos] = (grid[pos] + 1) % 10
    if grid[pos] == 0 and pos not in flashed:
        flashed.add(pos)
        for p in neighbours(grid, pos):
            flash(grid,p,flashed)

def flash_all(grid):
    all0 = {p for p,v in grid.items() if v == 0}
    flashed = set()
    for p in all0:
        flash(grid,p,flashed)
    return len({p for p,v in grid.items() if v == 0})

def increase_and_flash(grid):
    increase_all(grid)
    return flash_all(grid)

def solve(input):
    grid = {(r,c) : int(v) for r,l in enumerate(input.splitlines()) for c, v in enumerate(l)}
    return sum(increase_and_flash(grid) for _ in range(100))
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))