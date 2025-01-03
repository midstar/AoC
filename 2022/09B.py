import sys

DIRECTION = {
    'U' : (-1,  0 ),
    'D' : ( 1,  0 ),
    'L' : ( 0, -1 ),
    'R' : ( 0,  1 ) 
}

def move(node, dir):
    return tuple(map(lambda i, j: i + j, node, DIRECTION[dir]))

def follow(head, tail):
    dr = head[0] - tail[0]
    dc = head[1] - tail[1]
    if abs(dr) <= 1 and abs(dc) <= 1:
        return tail # No move
    dc_n = 1 if dc > 0 else -1 if dc < 0 else 0
    dr_n = 1 if dr > 0 else -1 if dr < 0 else 0

    return (tail[0] + dr_n, tail[1] + dc_n)

def solve(input):
    rope = [(0,0)] * 10
    positions = set([(0,0)])
    for line in input.splitlines():
        dir, l = tuple(line.split())
        for i in range(int(l)):
            rope[0] = move(rope[0], dir) 
            for i in range(1, len(rope)):
                rope[i] = follow(rope[i - 1], rope[i])
            positions.add(rope[-1]) 

    return len(positions)
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))