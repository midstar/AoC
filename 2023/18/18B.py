import argparse, time
import sys

DIRECTION = {
    '0' : ( 0,  1 ), # R
    '1' : ( 1,  0 ), # D
    '2' : ( 0, -1 ), # L
    '3' : (-1,  0 )  # U
}

def get_node(node, dir, steps):
    dr, dc = DIRECTION[dir]
    return (node[0] + dr * steps, node[1] + dc * steps)

def solve(input):
    node = (0,0)
    nodes = [node]
    steps_tot = 0
    for line in input.splitlines():
        steps = int(line[-7:-2],16)
        dir = line[-2:-1]
        node = get_node(node, dir, steps)
        nodes.append(node)
        steps_tot += steps

    # Calculate polygon area using Shoelace Formula (Triangle formula)
    area = 0
    for i in range(0, len(nodes) - 1):
        node_a = nodes[i]
        node_b = nodes[i+1]
        area += 0.5 * (node_a[0] * node_b[1] - node_b[0] * node_a[1])
    area = abs(area)

    # Area including border - sort of Pick's Theorem but +1 instead of -1 
    result = int(area + steps_tot / 2 + 1)

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