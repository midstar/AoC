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
            grid[pos]['sides'] += 1
    return True

def get_price(grid, id):
    area = 0
    perimeter = 0
    for pos, data in grid.items():
        if data['group'] == id:
            #print(pos,data,id)
            area += 1
            perimeter += data['sides']
    #print('  Price', area * perimeter)
    return area * perimeter

def solve(input):
    grid = {}
    for r, line in enumerate(input.splitlines()):
        for c, val in enumerate(line):
            grid[(r,c)] = {'val' : val, 'group' : -1, 'sides' : 0}
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