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

def solve(input):
    parts = input.split('\n\n')

    grid = {}
    width = 0
    height = 0
    current = None
    for r, line in enumerate(parts[0].splitlines()):
        for c, val in enumerate(line):
            grid[(r,c)] = val
            if val == '@':
                grid[(r,c)] = '.'
                current = (r,c)
            width  = max(width,  c + 1)
            height = max(height, r + 1)

    sequence = parts[1].replace('\n', '')

    #print_grid(grid,width,height,current)

    for dir in sequence:
        pos2 = get_new_pos(current, dir)
        if pos2 not in grid or grid[pos2] == '#':
            continue
        if grid[pos2] == 'O':
            pos3 = pos2
            while pos3 in grid and grid[pos3] not in ['#', '.']:
                pos3 = get_new_pos(pos3, dir)
            if grid[pos3] == '.':
                # Move box
                grid[pos2] = '.'
                grid[pos3] = 'O'
            else: 
                continue
        current = pos2

    #print()
    #print_grid(grid,width,height,current)

    # Calculate score
    result = 0
    for (r, c), val in grid.items():
        if val == 'O':
            result += 100 * r + c

    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))