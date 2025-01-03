import sys
from functools import cmp_to_key

def compare(line1, line2):
    z_min = [0, 0]
    z_max = [0, 0]
    for i, line in enumerate([line1, line2]):
        A_B = line.split('~')
        A_Z = [int(c) for c in A_B[0].split(',')][2]
        B_Z = [int(c) for c in A_B[1].split(',')][2]
        z_min[i] = min(A_Z, B_Z)
        z_max[i] = max(A_Z, B_Z)
    if z_min[0] != z_min[1]:
        return z_min[0] - z_min[1]
    return z_max[0] - z_max[1]

def remove_brick(space, bricks, index):
    for coord in bricks[index]:
        if coord not in space:
            print(f'Error! Brick {index} coord {coord} free')
            exit(1)
        space.remove(coord)

def add_brick(space, bricks, index):
    for coord in bricks[index]:
        if coord in space:
            print(f'Error! Brick {index} coord {coord} not free')
            exit(1)
        space.add(coord)

def free_z_below(space, bricks, index):
    brick = bricks[index]
    z_down = brick[0][2]
    free_z = 10000000
    for (_, _, z) in brick:
        z_down = z if z < z_down else z_down
    for (x, y, z) in brick:
        if z != z_down: continue
        z_offset = 0
        while((z - z_offset) > 1):
            z_offset += 1
            if (x, y, z - z_offset) in space:
                z_offset -= 1
                break
        free_z = min(z_offset, free_z)
        
    return free_z

def remove_all_fallable(space, bricks, removed):
    result = 0
    l1 = len(removed)
    any_removed = True
    while any_removed:
        any_removed = False
        for i in range(len(bricks)):
            if i not in removed:
                if free_z_below(space, bricks, i) != 0:
                    remove_brick(space, bricks, i)
                    removed.append(i)
                    any_removed = True
                    continue
    return len(removed) - l1

def solve(input):
    lines = input.splitlines()

    # Sort based on z
    compare_key = cmp_to_key(compare)
    lines = sorted(lines, key=compare_key)

    # Create bricks
    bricks = []
    for i, line in enumerate(lines):
        A_B = line.split('~')
        A = [int(c) for c in A_B[0].split(',')]
        B = [int(c) for c in A_B[1].split(',')]

        base = A
        size = 1
        axis = 0
        xyz = [0,1,2]
        for i in xyz:
            diff = A[i] - B[i]
            if diff != 0:
                axis = i
                if diff > 0:
                    base = B
                size = abs(diff) + 1
                break

        coords = []
        for v in range(base[axis], base[axis] + size):
            base[axis] = v
            coords.append((base[0], base[1], base[2]))
        if len(coords) == 0:
            print('Error', line, A, B, base, size)
            exit()
        bricks.append(coords)

    # Add bricks to space
    space = set()
    for i in range(len(bricks)):
        add_brick(space, bricks, i)

    # Drop bricks one-by-one
    moved = True
    while(moved):
        moved = False
        for i in range(len(bricks)):
            z_offset = free_z_below(space, bricks, i)
            if z_offset > 0:
                moved = True
                remove_brick(space, bricks, i)
                new_coords = []
                for (x, y, z) in bricks[i]:
                    new_coords.append((x, y, z - z_offset))
                bricks[i] = new_coords
                add_brick(space, bricks, i)    

    # Test remove one-by-one
    result = 0
    for i in range(len(bricks)):
        space2 = space.copy()
        remove_brick(space2, bricks, i)
        result += remove_all_fallable(space2, bricks, [i])

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))