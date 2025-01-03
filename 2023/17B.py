import sys
import heapq

DIRECTION = {
    'Up'    : (-1,  0 ),
    'Down'  : ( 1,  0 ),
    'Left'  : ( 0, -1 ),
    'Right' : ( 0,  1 ) 
}

def goto_node(node, dir):
    return tuple(map(lambda i, j: i + j, node, DIRECTION[dir]))

def dijkstra(grid, min_steps, max_steps):
    # Queue items (total heat in path, (row, col), direction, number of "straight" steps , path)
    queue = []
    heapq.heappush(queue, (grid[(0,1)], (0,1), 'Right', 1, ((0,0),)))
    heapq.heappush(queue, (grid[(1,0)], (1,0), 'Down', 1,  ((0,0),)))

    end_node = max(grid)
    visited = set()

    while queue:
        node_metadata = heapq.heappop(queue)
        #print(*node_metadata)
        heat, node, dir, steps, path = node_metadata
        if node == end_node and steps >= (min_steps - 1):
            return heat, path

        if (node, dir, steps) in visited:
            continue
        visited.add((node, dir, steps))
        directions = []
        if steps < (max_steps - 1):
            directions.append(dir)
        if steps >= (min_steps - 1):
            if dir in ['Up', 'Down']:
                directions.append('Left')
                directions.append('Right')
            if dir in ['Left', 'Right']:
                directions.append('Up')
                directions.append('Down')
        for direction in directions:
            next_node = goto_node(node, direction)
            if next_node in grid:
                next_step = 0 if direction != dir else steps + 1
                next_path = path + (node,)
                heapq.heappush(queue, (heat + grid[next_node], next_node, direction, next_step, next_path))


def solve(input):
    grid = {}
    for row, lines in enumerate(input.splitlines()):
        for col, heat in enumerate(lines):
            grid[(row, col)] = int(heat)

    result, path = dijkstra(grid, 4, 10)

    '''
    print(path)
    for row, lines in enumerate(input.splitlines()):
        line = []
        for col, heat in enumerate(lines):
            if (row, col) in path:
                line.append('#')
            else: 
                line.append(str(heat))
        print(''.join(line))
    '''
    return result 

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))