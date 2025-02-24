import sys

def neighbours(grid,pos):
    n = set()
    for dx,dy,dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
        p = (pos[0] + dx,pos[1] + dy,pos[2] + dz)
        if p not in grid:
            n.add(p)
    return n

def is_inside(pos, cubes, inside, outside, min_x, max_x, min_y, max_y, min_z, max_z, visited, top=True):
    if pos in inside: return True
    if pos in outside: return False
    if pos in visited: return None
    visited.add(pos)
    x, y, z = pos
    if x <= min_x or x >= max_x: return False
    if y <= min_y or y >= max_y: return False
    if z <= min_z or z >= max_z: return False
    for pos2 in neighbours(cubes,pos):
        if is_inside(pos2, cubes, inside, outside, min_x, max_x, min_y, max_y, min_z, max_z, visited , False) == False:
            outside.update(visited)
            return False
    if top:
        inside.update(visited)
        return True
    return None    

def solve(input):
    cubes = {tuple(map(int,line.split(','))) for line in input.splitlines()}
    all_x = {p[0] for p in cubes}
    all_y = {p[1] for p in cubes}
    all_z = {p[2] for p in cubes}
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    min_z, max_z = min(all_z), max(all_z)

    inside = set()
    outside = set()
    sides = 0
    for cube in cubes: 
        for n in neighbours(cubes,cube):  
            if not is_inside(n, cubes, inside, outside, min_x, max_x, min_y, max_y, min_z, max_z, set()):
                sides += 1

    return sides
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))