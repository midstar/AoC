import sys

DIR = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}

def get_new_pos(pos, dir):
    return (pos[0] + DIR[dir][0], pos[1] + DIR[dir][1])

def build_group(grid, pos, id):
    if grid[pos]['group'] != -1:
        return False # Already within a group
    grid[pos]['group'] = id
    for dir in DIR.keys():
        pos2 = get_new_pos(pos, dir)
        if pos2 in grid and grid[pos2]['val'] == grid[pos]['val']: 
            build_group(grid,pos2,id)
        else:
            grid[pos]['sides'].append(dir)
    return True

def get_group(grid, id):
    group = {}
    for pos, data in grid.items():
        if data['group'] == id:
            group[pos] = data
    return group

def get_side(group, side, check):
    done = set()
    result = 0
    for pos, data in group.items():
        if pos in done or side not in data['sides']:
            continue
        result += 1
        done.add(pos)
        for dir in check:
            pos2 = get_new_pos(pos, dir)
            while pos2 in group and side in group[pos2]['sides']:
                done.add(pos2)
                pos2 = get_new_pos(pos2, dir)
    return result
        
def get_price(grid, id):
    group = get_group(grid,id)
    sideU = get_side(group, 'U', ['L', 'R'])
    sideD = get_side(group, 'D', ['L', 'R'])
    sideR = get_side(group, 'R', ['U', 'D'])
    sideL = get_side(group, 'L', ['U', 'D'])
    #print(group)
    #print(id, sideU, sideD, sideR, sideL)
    return len(group) * (sideU + sideD + sideR + sideL)

def solve(input):
    grid = {}
    for r, line in enumerate(input.splitlines()):
        for c, val in enumerate(line):
            grid[(r,c)] = {'val' : val, 'group' : -1, 'sides' : []}
    id = 0
    for pos in grid.keys():
        if build_group(grid,pos,id):
            id += 1

    result = 0
    for i in range(id):
        result += get_price(grid, i)

    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))