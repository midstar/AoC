import sys

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
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))