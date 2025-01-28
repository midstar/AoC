# Nice to have fuctions to use in AoC puzzles

# Get all neighbour positions that exists in grid
# grid: a set or a dictionary keyed with tuple or list (row, col)
# pos:  tuple or list (row, col)
def neighbours(grid,pos):
    n = {(pos[0] + dr, pos[1] + dc) for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]}
    return {p for p in n if p in grid}

# As neighbours but also including diagonal neighbours
def neighbours_diag(grid,pos):
    n = {(pos[0] + dr, pos[1] + dc) for dr, dc in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]}
    return {p for p in n if p in grid}

# Print grid, i.e. a dict with tuple key (row,col) and value max 1 char long
def print_grid(grid):
    max_row = max(r for r,_ in grid.keys())
    max_col = max(c for _,c in grid.keys())
    for r in range(max_row + 1):
        for c in range(max_col + 1):
            print(grid[(r,c)],end='')
        print()