import sys

DIR = {
    '^' : (-1, 0),
    'v' : (1, 0),
    '<' : (0, -1),
    '>' : (0, 1)
}

def get_new_pos(pos, dir):
    return (pos[0] + DIR[dir][0], pos[1] + DIR[dir][1])

def print_grid(grid, width, height, current = None):
    text = []
    for r in range(height):
        row = []
        for c in range(width):
            if (r,c) == current:
                row.append('@')
            else:
                row.append(grid[(r,c)])
        text.append(''.join(row))
    print('\n'.join(text))

def move_box(grid, pos_l, pos_r, dir,test = False):
    pos_l2 = get_new_pos(pos_l, dir)
    pos_r2 = get_new_pos(pos_r, dir)
    if dir in '^v':
        if grid[pos_l2] == '#' or grid[pos_r2] == '#':
            return False
        if grid[pos_l2] == '[' and grid[pos_r2] == ']':
            if not move_box(grid, pos_l2, pos_r2, dir, test):
                return False
        if grid[pos_l2] == ']' and grid[pos_r2] == '[':
            box_l_l = get_new_pos(pos_l2, '<')
            box_l_r = pos_l2
            box_r_l = pos_r2
            box_r_r = get_new_pos(pos_r2, '>')
            if move_box(grid, box_l_l, box_l_r, dir, True) and move_box(grid, box_r_l, box_r_r, dir, True):
                move_box(grid, box_l_l, box_l_r, dir, test)  
                move_box(grid, box_r_l, box_r_r, dir, test)          
            else:
                return False
        if grid[pos_l2] == ']' and grid[pos_r2] == '.':
            box_l_l = get_new_pos(pos_l2, '<')
            box_l_r = pos_l2
            if not move_box(grid, box_l_l, box_l_r, dir, test):         
                return False
        if grid[pos_l2] == '.' and grid[pos_r2] == '[':
            box_r_l = pos_r2
            box_r_r = get_new_pos(pos_r2, '>')
            if not move_box(grid, box_r_l, box_r_r, dir, test):
                return False            
        
    if dir in '<':
        if grid[pos_l2] == '#':
            return False
        if grid[pos_l2] == ']':
            box_l = get_new_pos(pos_l2, '<')
            box_r = pos_l2
            if not move_box(grid, box_l, box_r, dir, test):
                return False

    if dir in '>':
        if grid[pos_r2] == '#':
            return False
        if grid[pos_r2] == '[':
            box_l = pos_r2
            box_r = get_new_pos(pos_r2, '>')
            if not move_box(grid, box_l, box_r, dir, test):
                return False

    if not test:
        grid[pos_l] = '.'
        grid[pos_r] = '.'
        grid[pos_l2] = '['
        grid[pos_r2] = ']' 

    return True

def solve(input):
    parts = input.split('\n\n')

    grid = {}
    width = 0
    height = 0
    current = None
    for r, line in enumerate(parts[0].splitlines()):
        for c, val in enumerate(line):
            c2 = c*2
            if val == '@':
                 current = (r,c2)
                 val = '.'       
            grid[(r,c2    )] = val
            grid[(r,c2 + 1)] = val
            if val == 'O':
                grid[(r,c2    )] = '['
                grid[(r,c2 + 1)] = ']'               
            width  = max(width,  c2 + 1)
            height = max(height, r + 1)


    sequence = parts[1].replace('\n', '')

    #print_grid(grid,width,height,current)

    for dir in sequence:
        pos2 = get_new_pos(current, dir)
        if pos2 not in grid or grid[pos2] == '#':
            continue
        if grid[pos2] in '[]':
            if grid[pos2] in '[':
                pos_l = pos2
                pos_r = get_new_pos(pos_l, '>')
            else:
                pos_r = pos2
                pos_l = get_new_pos(pos_r, '<')
            if not move_box(grid, pos_l, pos_r, dir):
                continue  
        current = pos2
    
    #print()
    #print_grid(grid,width,height,current)

    # Calculate score
    result = 0
    for (r, c), val in grid.items():
        if val == '[':
            result += 100 * r + c

    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))