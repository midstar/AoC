# Nice to have fuctions to use in AoC puzzles

# Create a dict keyed with (row,col) tuples with value from matrix
def grid_from_matrix(input):
    return {(r,c) : int(v) for r,l in enumerate(input.splitlines()) for c, v in enumerate(l)}

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

# Dijkstra example. In this example each position has a weight (grid value)
# and the function will find the path with total lowest weight.
import heapq
def dijkstra(grid, start, stop):
    q = []
    heapq.heappush(q, (0,start)) # Assumes weight 0 for start pos. Could be (grid[start], start)
    visited = set()
    while q:
        weight, pos = heapq.heappop(q) 
        if pos == stop:
            return weight
        if pos in visited:
            continue
        visited.add(pos)
        for pos2 in neighbours(grid,pos):
            heapq.heappush(q, (weight + grid[pos2], pos2))

import re
# Following expression finds all patterson of mul(a,b) in a text
# string and multiplies each a*b and summarize all products.
def regular_expression(input):
    return sum([int(a) * int(b) for (a,b) in re.findall(r'mul\((\d+),(\d+)\)', input)])