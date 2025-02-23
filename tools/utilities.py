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

# Print matrix, i.e. a set with tuple values (row,col)
def print_matrix(matrix, filled='#', empty='.',min_row=None,min_col=None,max_row=None,max_col=None):
    rows = {r for r,_ in matrix}
    cols = {c for _,c in matrix}
    min_r,min_c,max_r,max_c = min(rows),min(cols),max(rows),max(cols)
    if min_row != None: min_r = min(min_r,min_row)
    if min_col != None: min_c = min(min_c,min_col)
    if max_row != None: max_r = max(max_r,max_row)
    if max_col != None: max_c = max(max_c,max_col)
    for r in range(min_r,max_r + 1):
        for c in range(min_c,max_c + 1):
            val = empty
            if((r,c) in matrix): val = filled
            print(val,end='')
        print()

# BFS example.
def bfs(grid, start, stop):
    q = [(0, start)]
    visited = set()
    while q:
        steps, pos = q.pop(0)
        if pos == stop: return steps
        if pos in visited: continue
        visited.add(pos)
        for pos2 in neighbours(grid,pos):
            q.append((steps + 1, pos2))

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

# Figures out value at index (index may be larger than len(values)). The values
# list needs to increase or decrease in a repeating pattern for this function to work
def value_at(values,index,min_pattern_length=5):
    steps = []
    for i, v in enumerate(values[:-1]):
        steps.append(values[i+1]-v)
    start_i, p = pattern(steps,min_pattern_length)
    l = index - start_i
    return values[start_i] + sum(p) * (l // len(p)) + sum(p[:l % len(p)])

# Find repeating pattern in list, returns index just before pattern and pattern
def pattern(values, min_length):
    values_rev = list(reversed(values))
    pattern = values_rev[:min_length]
    values_rev = values_rev[min_length:]
    while not values_equal(pattern,values_rev[:len(pattern)]):
        if len(values_rev) == 0: return None # No pattern found
        pattern.append(values_rev.pop(0))
    pattern.reverse()
    for i in range(len(values)):
        if values_equal(pattern, values[i:i+len(pattern)]):
            return i, pattern

# Check if to lists of values are equal
def values_equal(values1, values2):
    return all(v1 == v2 for v1, v2 in zip(values1, values2))