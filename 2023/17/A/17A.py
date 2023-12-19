import argparse, time
import heapq

DIRECTION = {
    'Up'    : (-1,  0 ),
    'Down'  : ( 1,  0 ),
    'Left'  : ( 0, -1 ),
    'Right' : ( 0,  1 ) 
}

def goto_node(node, dir):
    return tuple(map(lambda i, j: i + j, node, DIRECTION[dir]))

def dijkstra(grid, max_steps):
    # Queue items (total heat in path, (row, col), direction, number of "straight" steps)
    queue = []
    heapq.heappush(queue, (grid[(0,1)], (0,1), 'Right', 1, ((0,0),)))
    heapq.heappush(queue, (grid[(1,0)], (1,0), 'Down', 1,  ((0,0),)))

    end_node = max(grid)
    visited = set()

    while queue:
        node_metadata = heapq.heappop(queue)
        #print(*node_metadata)
        heat, node, dir, steps, path = node_metadata
        if node == end_node:
            return heat, path


        if (heat, node, dir, steps) in visited:
            continue
        visited.add((heat, node, dir, steps))
        '''
        if node_metadata in visited:
            continue
        visited.add(node_metadata)
        '''
        directions = []
        if steps < max_steps:
            directions.append(dir)
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

    result, path = dijkstra(grid, 3)
    print(path)
    return result 

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        start_time = time.time()
        result = solve(f.read())
        print('Result: %s  (excution time %0.4f s)' % (result, time.time() - start_time))

if __name__ == '__main__':
    main()    