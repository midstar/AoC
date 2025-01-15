import sys
import heapq

DIRECTION = {
    '^' : (-1,  0 ),
    'v' : ( 1,  0 ),
    '<' : ( 0, -1 ),
    '>' : ( 0,  1 ) 
}

NEXT_DIR = {
    '^' : ['^', '<', '>'],
    'v' : ['v', '<', '>'],
    '<' : ['<', '^', 'v'],
    '>' : ['>', '^', 'v']     
}

def goto_node(node, dir):
    return tuple(map(lambda i, j: i + j, node, DIRECTION[dir]))

def dijkstra(grid, max_steps):
    # Queue items (total heat in path, (row, col), direction, number of "straight" steps , path)
    queue = []
    heapq.heappush(queue, (grid[(0,1)], (0,1), '>', 1))
    heapq.heappush(queue, (grid[(1,0)], (1,0), 'v', 1))

    end_node = max(grid)
    visited = set()

    while queue:
        node_metadata = heapq.heappop(queue)
        heat, node, dir, steps= node_metadata
        if node == end_node:
            return heat
        if (node, dir, steps) in visited:
            continue
        visited.add((node, dir, steps))
        for direction in NEXT_DIR[dir]:
            if steps >= (max_steps - 1) and direction == dir: continue
            next_node = goto_node(node, direction)
            if next_node in grid:
                next_step = 0 if direction != dir else steps + 1
                heapq.heappush(queue, (heat + grid[next_node], next_node, direction, next_step))

def solve(input):
    grid = {}
    for row, lines in enumerate(input.splitlines()):
        for col, heat in enumerate(lines):
            grid[(row, col)] = int(heat)

    return dijkstra(grid, 3)

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))