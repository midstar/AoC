import argparse, time

DIRECTION = {
    'U' : (-1,  0 ),
    'D' : ( 1,  0 ),
    'L' : ( 0, -1 ),
    'R' : ( 0,  1 ) 
}

SIDE = { 'U' : 'D', 'D' : 'U', 'L' : 'R', 'R' : 'L'}

def move(node, dir):
    return tuple(map(lambda i, j: i + j, node, DIRECTION[dir]))

def dist(head, tail):
    return max(abs(head[0] - tail[0]), abs(head[1] - tail[1]))

def follow(head, tail, dir):
    if dist(head, tail) > 1:
        return move(head, SIDE[dir])
    return tail
        


def solve(input):
    head = (0,0)
    tail = (0,0)
    positions = set([tail])
    for line in input.splitlines():
        dir, l = tuple(line.split())
        for i in range(int(l)):
            head = move(head, dir)
            tail = follow(head, tail, dir)
            positions.add(tail)

    return len(positions)
        
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