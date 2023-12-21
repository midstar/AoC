import argparse, time

DIRECTION = {
    'R' : ( 0,  1 ), 
    'D' : ( 1,  0 ), 
    'L' : ( 0, -1 ), 
    'U' : (-1,  0 )  
}

def get_node(node, dir, steps):
    dr, dc = DIRECTION[dir]
    return (node[0] + dr * steps, node[1] + dc * steps)

def bfs(grid, start, steps):
    q = [(start, 0)]
    visited = set()
    result = set()
    while q:
        info = q.pop(0)
        node, step = info
        if info in visited:
            continue
        visited.add(info)
        if step == steps:
            result.add(node)
            continue
        for dir in DIRECTION.keys():
            next = get_node(node, dir, 1)
            if next in grid:
                q.append((next, step + 1))
    return result


def solve(input):
    grid = []
    start = None
    for row, line in enumerate(input.splitlines()):
        for col, c in enumerate(line):
            if c == '#':
                continue
            node = (row, col)
            grid.append(node)
            if c == 'S':
                start = node

    nodes = bfs(grid, start, 64)
    #print(nodes)
    result = len(nodes)
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