import sys

from functools import cmp_to_key

def compare_bricks(brick1, brick2):
    z_min = min(b[2] for b in brick1) -  min(b[2] for b in brick2)
    if z_min != 0: return z_min
    return max(b[2] for b in brick1) -  max(b[2] for b in brick2)

def place(blocks,brick):
    min_z = min(b[2] for b in brick)
    while min_z > 1:
        brick2 = {(b[0], b[1], b[2] - 1) for b in brick}
        if len(blocks & brick2) != 0:
             break
        brick = brick2
        min_z -= 1
    return brick

def brick_steady(blocks,brick):
    blocks -= brick 
    result = True
    if min(b[2] for b in brick) > 1:
        brick2 = {(b[0], b[1], b[2] - 1) for b in brick}
        result = len(brick2 & blocks) > 0
    blocks |= brick
    return result   

def safe_to_remove(blocks, bricks, i):
    brick = bricks[i]
    result = True
    blocks -= brick

    support_blocks = {(b[0], b[1], b[2] + 1) for b in brick}
    support_blocks &= blocks
    while len(support_blocks) > 0 and i < (len(bricks) - 1):
        i += 1
        brick2 = bricks[i]
        match_blocks = support_blocks & brick2
        if len(match_blocks) > 0:
            if not brick_steady(blocks,brick2):
                result = False
                break
            support_blocks -= match_blocks

    blocks |= brick
    return result

def solve(input):
    unsorted_bricks = []
    for line in input.splitlines():
        x, y, z, x2, y2, z2 = map(int,line.replace('~',',').split(','))
        brick = {(x,y,z)}
        while x != x2 or y != y2 or z != z2:
            if x < x2: x += 1
            if y < y2: y += 1
            if z < z2: z += 1
            brick.add((x,y,z))
        unsorted_bricks.append(brick) 

    bricks = []
    blocks = set()
    for brick in sorted(unsorted_bricks,key=cmp_to_key(compare_bricks)):
        bricks.append(place(blocks,brick))
        blocks |= bricks[-1]

    return sum(safe_to_remove(blocks,bricks,i) for i in range(len(bricks)))

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))