import sys



def traverse(matrix, row, col, dir):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]):
        return
    p = matrix[row][col]
    if p[dir]:
        return # Already been here from this direction
    p[dir] = True
    if p['obj'] == '.':
        if dir == 'up':
            traverse(matrix, row - 1, col, 'up')
        elif dir == 'down':
            traverse(matrix, row + 1, col, 'down')
        elif dir == 'right':
            traverse(matrix, row, col + 1, 'right')
        elif dir == 'left':
            traverse(matrix, row, col - 1, 'left')
    elif p['obj'] == '-':
        if dir == 'up' or  dir == 'down':
            traverse(matrix, row, col + 1, 'right')
            traverse(matrix, row, col - 1, 'left')
        elif dir == 'right':
            traverse(matrix, row, col + 1, 'right')
        elif dir == 'left':
            traverse(matrix, row, col - 1, 'left')
    elif p['obj'] == '|':
        if dir == 'up':
            traverse(matrix, row - 1, col, 'up')
        elif dir == 'down':
            traverse(matrix, row + 1, col, 'down')
        if dir == 'right' or  dir == 'left':
            traverse(matrix, row - 1, col, 'up')
            traverse(matrix, row + 1, col, 'down')
    elif p['obj'] == '/':
        if dir == 'up':
            traverse(matrix, row, col + 1, 'right')
        elif dir == 'down':
            traverse(matrix, row, col - 1, 'left')
        elif dir == 'right':
            traverse(matrix, row - 1, col, 'up')
        elif dir == 'left':
            traverse(matrix, row + 1, col, 'down')
    elif p['obj'] == '\\':
        #print(row, col, 'match', dir)
        if dir == 'up':
            traverse(matrix, row, col - 1, 'left')
        elif dir == 'down':
            traverse(matrix, row, col + 1, 'right')
        elif dir == 'right':
            traverse(matrix, row + 1, col, 'down')
        elif dir == 'left':
            traverse(matrix, row - 1, col, 'up')



def solve(input):
    lines = input.splitlines()
    matrix = []
    for row in lines:
        mrow = []
        for col in row:
            mrow.append({
                'obj' : col,
                'up' : False, 
                'down' : False, 
                'right' : False, 
                'left' : False
            })
        matrix.append(mrow)

    sys.setrecursionlimit(100000)
    traverse(matrix, 0, 0, 'right')

    result = 0
    for row in matrix:
        line = []
        for col in row:
            if col['up'] or col['down'] or col['right'] or col['left']:
                line.append('#')
                result += 1
            else:
                line.append('.')
        #print(''.join(line))

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))