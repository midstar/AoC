import argparse, time
from functools import cmp_to_key

def high_z(x, y, coordinates):
    high_z = 0
    for (a,b,c) in coordinates:
        if a == x and b == y and high_z < c:
            high_z = c
    return high_z

def place_brick(field, brick):
    # Find z level for brick
    z_level = 1
    for (x,y,z) in brick:
        z_high = high_z(x, y, field)
        if z_high >= z_level:
            z_level = z_high + 1

    # Place brick on field on z_evel
    for (x,y,z) in brick:
        field.append((x,y,z + z_level))

    return z_level

def create_field(bricks, skip = -1):
    field = []
    bricks_z = [0 for _ in range(0, len(bricks))]
    for index, brick in enumerate(bricks):
        if skip != index:
            bricks_z[index] = place_brick(field, brick)
    return field, bricks_z

def compare(line1, line2):
    z = [0, 0]
    for i, line in enumerate([line1, line2]):
        A_B = line.split('~')
        A_Z = [int(c) for c in A_B[0].split(',')][2]
        B_Z = [int(c) for c in A_B[1].split(',')][2]
        z[i] = min(A_Z, B_Z)
    return z[0] - z[1]


def solve(input):
    lines = input.splitlines()
    # Sort based on z
    compare_key = cmp_to_key(compare)
    lines = sorted(lines, key=compare_key)

    bricks = []
    for line in lines:
        A_B = line.split('~')
        A = [int(c) for c in A_B[0].split(',')]
        B = [int(c) for c in A_B[1].split(',')]

        base = A
        size = 1
        axis = 0
        xyz = [0,1,2]
        for i in xyz:
            size = A[i] - B[i]
            if size != 0:
                axis = i
                if size > 0:
                    base = B
                size = abs(size) + 1
                break
        nodes = []
        nl = [0,0,0]
        z_offset = 100000000
        for i in xyz:
            nl[i] = base[i]
            if z_offset > base[2]:
                z_offset = base[2] 
        for v in range(base[axis], base[axis] + size):
            nl[axis] = v
            nodes.append((nl[0], nl[1], nl[2] - z_offset))
        bricks.append(nodes)

    _, bricks_z = create_field(bricks)
    #print(bricks_z)

    result = 0
    percent = max(int(len(bricks)/100),1)
    for skip_i in range(0, len(bricks)):
        if skip_i % percent == 0:
            print(skip_i / percent, '%')
        _, bricks_z2 = create_field(bricks, skip_i)
        falling = False
        for i in range(0, len(bricks_z)):
            if i != skip_i:
                if bricks_z[i] != bricks_z2[i]:
                    falling = True
                    break
        if not falling:
            result += 1
        #print(skip_i, bricks_z2, falling)

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