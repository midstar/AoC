import sys

def solve(input):
    cubes = {tuple(map(int,line.split(','))) for line in input.splitlines()}
    sides = 0
    for x, y, z in cubes:
        for dx,dy,dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            if (x + dx,y + dy,z + dz) not in cubes:
                sides += 1
    return sides
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))