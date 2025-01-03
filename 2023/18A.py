import sys

DIRECTION = {
    'U' : (-1,  0 ),
    'D' : ( 1,  0 ),
    'L' : ( 0, -1 ),
    'R' : ( 0,  1 ) 
}

def get_node(node, dir):
    return tuple(map(lambda i, j: i + j, node, DIRECTION[dir]))

def solve(input):
    row_min = 0
    row_max = 0
    col_min = 0
    col_max = 0
    last_node = (0, 0)
    dig_nodes = [last_node]
    for line in input.splitlines():
        dir = line.split()[0]
        len = int(line.split()[1])
        for i in range(0, len):
            next = get_node(last_node, dir)
            dig_nodes.append(next)
            last_node = next
            row, col = last_node
            row_min = min(row_min, row)
            row_max = max(row_max, row)
            col_min = min(col_min, col)
            col_max = max(col_max, col)

    height = 1 + row_max - row_min
    width = 1 + col_max - col_min
    
    grid = {}
    for row, col in dig_nodes:
        grid[(row - row_min, col - col_min)] = '#'

    for row in range(0, height):
        for col in range(0, width):
            node = (row, col)
            if node not in grid:
                grid[node] = ''

    found_row = True
    while(found_row):
        found_row = False
        for row in range(0, height):
            found_col = True
            while(found_col):
                found_col = False
                for col in range(0, width):
                    node = (row, col)
                    if grid[node] == '':
                        if row == 0 or (row == height - 1) or col == 0 or (col == width - 1):
                            grid[node] = '.'
                            found_col = True
                        else:
                            if grid[(row - 1, col)] == '.' or grid[(row + 1, col)] == '.' or \
                            grid[(row, col - 1)] == '.' or grid[(row, col + 1)] == '.' :
                                grid[node] = '.'
                                found_col = True
                if found_col:
                    found_row = True

    result = 0
    for node, val in grid.items():
        if val == '' or val == '#':
            result += 1

    #print(grid)
    #print()
    #print(height, width)




    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))