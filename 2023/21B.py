import sys
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

DIRECTION = {
    'R' : ( 0,  1 ), 
    'D' : ( 1,  0 ), 
    'L' : ( 0, -1 ), 
    'U' : (-1,  0 )  
}

def get_node(grid, h, w, node, dir):
    dr, dc = DIRECTION[dir]
    row = node[0] + dr
    col = node[1] + dc
    if (abs(row % h), abs(col % w)) in grid:
        return (row, col)
    return None

def is_even(node):
    r, c = node
    return (r + c) % 2 == 0

def bfs(grid, h, w, start, steps):
    q = [(start, 0)]
    even_0 = is_even(start)
    visited = set()
    result = [0 for _ in steps]
    next_step = 1
    last_step = steps[-1]
    while next_step <= last_step:
        info = q.pop(0)
        node, step = info
        if step > next_step:
            # Count number of nodes from visited
            if next_step in steps:
                index = steps.index(next_step)
                for n in visited:
                    even = is_even(n)
                    if even and (next_step % 2 == 0 and even_0) or \
                               ((next_step % 2 != 0 and not even_0)):
                        result[index] += 1
                    elif not even and (next_step % 2 != 0 and even_0) or \
                                     ((next_step % 2 == 0 and not even_0)):
                        result[index] += 1
                #print(next_step, result[index])
            next_step = step
        if node in visited:
            continue
        visited.add(node)
        for dir in DIRECTION.keys():
            next = get_node(grid, h, w, node, dir)
            if next:
                q.append((next, step + 1))
    return result

def func(x, a, b, c):
    return a*x**2 + b * x + c

def solve(input):
    grid = []
    start = None
    lines = input.splitlines()
    height = len(lines)
    width = len(lines[0])
    #print('Height:',height,'  Width:', width)
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == '#':
                continue
            node = (row, col)
            grid.append(node)
            if c == 'S':
                start = node

    # Nodes are growing exponetionally. Assume that it is a second
    # degree equation. For that we need three points. Take the 
    # points when the step reach the edge of the grid. We will
    # reach the edge after width / 2 steps since there is no
    # obstacle in the way from start (S) point vertically or
    # horizontally
    input = [int(width / 2) + i * width for i in range(0,3)]
    nodes = bfs(grid, height, width, start, input)
    #for i in range(0, len(nodes)):
    #    print(input[i],nodes[i])

    count = [cl for cl in nodes]

    params, covs = curve_fit(func, input, count)
    #print('params', params)
    #print('covs', covs)
    a, b, c = params
    for i in range(0, len(nodes)):
        x = input[i]
        calc_y = func(input[i], a, b, c)
        #print('x:', input[i], '  y meas:', nodes[i], '  y calc:', calc_y) 

    #plt.plot(input, count)  # Plot the chart 
    #plt.show()  # display 
    x = 26501365
    result = func(x, a, b, c)
    return round(result)

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))