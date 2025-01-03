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
        if dir == 'up':
            traverse(matrix, row, col - 1, 'left')
        elif dir == 'down':
            traverse(matrix, row, col + 1, 'right')
        elif dir == 'right':
            traverse(matrix, row + 1, col, 'down')
        elif dir == 'left':
            traverse(matrix, row - 1, col, 'up')

def energized(matrix, do_print = False):
    result = 0
    for row in matrix:
        line = []
        for col in row:
            if col['up'] or col['down'] or col['right'] or col['left']:
                line.append('#')
                result += 1
            else:
                line.append('.')
        if do_print:
            print(''.join(line))
    return result    

def new_matrix(lines):
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
    return matrix

def solve(input):
    lines = input.splitlines()
    matrix = new_matrix(lines)

    sys.setrecursionlimit(100000)

    values = []

    # Upper and bottom edge
    for col in range(0, len(matrix[0])):
        matrix = new_matrix(lines)
        traverse(matrix, 0, col, 'down')
        values.append(energized(matrix, False))
        
        matrix = new_matrix(lines)
        traverse(matrix, len(matrix) - 1, col, 'up')
        values.append(energized(matrix, False))        

    # Left and Right edge:
    for row in range(0, len(matrix)):
        matrix = new_matrix(lines)
        traverse(matrix, row, 0, 'right')
        values.append(energized(matrix, False))
        
        matrix = new_matrix(lines)
        traverse(matrix, row, len(matrix[row]) - 1, 'left')
        values.append(energized(matrix, False))

    return max(values)

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))