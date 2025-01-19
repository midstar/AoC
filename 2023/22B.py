import sys

from functools import cmp_to_key

def compare_bricks(brick1, brick2):
    z_min = min(b[2] for b in brick1) -  min(b[2] for b in brick2)
    if z_min != 0: return z_min
    return max(b[2] for b in brick1) -  max(b[2] for b in brick2)

def place(blocks,brick):
    rests_on = set()
    min_z = min(b[2] for b in brick)
    while min_z > 1:
        brick2 = {(b[0], b[1], b[2] - 1) for b in brick}
        rests_on = blocks & brick2
        if len(rests_on) != 0:
             break
        brick = brick2
        min_z -= 1
    return brick, rests_on

def will_fall(bricks_depends, i):
    fallen = {i}
    for j in range(i+1,len(bricks_depends)):
        dep = bricks_depends[j]
        if dep and dep.issubset(fallen):
            fallen.add(j)
    return len(fallen) - 1

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
    bricks_depends = []
    blocks = set()
    for brick in sorted(unsorted_bricks,key=cmp_to_key(compare_bricks)):
        placed_brick, rests_on = place(blocks,brick)
        depends = set()
        bricks_depends.append(depends)
        i = 0
        while rests_on and i < len(bricks):
            match_block = rests_on & bricks[i]
            if match_block:
                depends.add(i)
                rests_on -= match_block
            i += 1
        bricks.append(placed_brick)
        blocks |= bricks[-1]

    return sum(will_fall(bricks_depends,i) for i in range(len(bricks)))

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))