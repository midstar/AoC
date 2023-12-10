import argparse, sys

NODE_TYPE = {
    'S' : {
        'n' : True,
        'e' : True,
        's' : True,
        'w' : True
    },
    '|' : {
        'n' : True,
        'e' : False,
        's' : True,
        'w' : False
    },
    '-' : {
        'n' : False,
        'e' : True,
        's' : False,
        'w' : True
    },
    'L' : {
        'n' : True,
        'e' : True,
        's' : False,
        'w' : False
    },
    'J' : {
        'n' : True,
        'e' : False,
        's' : False,
        'w' : True
    },
    '7' : {
        'n' : False,
        'e' : False,
        's' : True,
        'w' : True
    },
    'F' : {
        'n' : False,
        'e' : True,
        's' : True,
        'w' : False
    },
    '.' : {
        'n' : False,
        'e' : False,
        's' : False,
        'w' : False
    }
}

# Range set i solve below
pipe_positions = []
escapable_positions = []

# Returns longest path to S
def navigate(r, c, rows, from_direction):
    result = [0]
    if (from_direction != '' and rows[r][c] == 'S'):
        return 0 # We are done
    pipe_positions[r][c] = True
    direction = NODE_TYPE[rows[r][c]]
    #print('%s (%s, %s) - from: %s' % (rows[r][c], r, c, from_direction))
    if direction['n'] and from_direction != 'n' and r > 0 and NODE_TYPE[rows[r - 1][c]]['s']:
        result.append(1 + navigate(r-1, c, rows, 's'))
    if direction['s'] and from_direction != 's'and r < (len(rows) - 1) and NODE_TYPE[rows[r + 1][c]]['n']:
        result.append(1 + navigate(r+1, c, rows, 'n'))
    if direction['e'] and from_direction != 'e' and c < (len(rows[r]) - 1) and NODE_TYPE[rows[r][c + 1]]['w']:
        result.append(1 + navigate(r, c + 1, rows, 'w'))
    if direction['w'] and from_direction != 'w' and c > 0 and NODE_TYPE[rows[r][c - 1]]['e']:
        result.append(1 + navigate(r, c - 1, rows, 'e'))

    return max(result)

def is_escapable(r, c, pipe_map):
    if escapable_positions[r][c] == 'x':
        return True
    if escapable_positions[r][c] == '-':
        return False # Not escapable
    if escapable_positions[r][c] == '?':
        return None # Unknown

    if r == 0 or r == (len(pipe_map) - 1) or c == 0 or c == (len(pipe_map[r]) - 1):
        escapable_positions[r][c] = 'x'
        return True
    
    escapable_positions[r][c] = '?' # Mark as under test
    result = []
    # Check north
    if not pipe_map[r - 1][c]:
        result.append(is_escapable(r - 1, c, pipe_map))
    # Check south
    if not pipe_map[r + 1][c]:
        result.append(is_escapable(r + 1, c, pipe_map)) 
    # Check east
    if not pipe_map[r][c + 1]:
        result.append(is_escapable(r, c + 1, pipe_map))         
    # Check west
    if not pipe_map[r][c - 1]:
        result.append(is_escapable(r, c - 1, pipe_map))

    if True in result:
        escapable_positions[r][c] = 'x'
        return True
    if None in result:
        return None

    escapable_positions[r][c] = '-' # Not escapable
    return False
    


def solve(input):
    rows = input.splitlines()

    sys.setrecursionlimit(100000)

    # Setup pipe_positions
    for cols in rows:
        l = []
        for col in cols:
            l.append(False)
        pipe_positions.append(l)

    # Find start (S)
    s = (0,0)
    for r in range(0, len(rows)):
        for c in range (0, len(rows[r])):
            if rows[r][c] == 'S':
                s = (r,c)

    print('Start: %s' % str(s))

    # Find pipe
    navigate(s[0], s[1], rows, '')

    # Replace S with a pipe
    north = False
    east = False
    south = False
    west = False
    if pipe_positions[s[0]-1][s[1]] and NODE_TYPE[rows[s[0]-1][s[1]]]['s']:
        north = True
    if pipe_positions[s[0]+1][s[1]] and NODE_TYPE[rows[s[0]+1][s[1]]]['n']:
        south = True
    if pipe_positions[s[0]][s[1]+1] and NODE_TYPE[rows[s[0]][s[1]+1]]['w']:
        east = True
    if pipe_positions[s[0]][s[1]-1] and NODE_TYPE[rows[s[0]][s[1]-1]]['e']:
        west = True
    if north and south:
        rows[s[0]] = rows[s[0]].replace('S','|')
    elif east and west:
        rows[s[0]] = rows[s[0]].replace('S','-')
    elif north and east:
        rows[s[0]] = rows[s[0]].replace('S','L')
    elif south and west:
        rows[s[0]] = rows[s[0]].replace('S','7')
    elif south and east:
        rows[s[0]] = rows[s[0]].replace('S','F')
    else:
        print("Impossible start position")
        exit(1)

    # Expand field in pipe_map
    pipe_map = []
    for i in range(0, len(rows) * 3):
        pipe_map.append([False] * len(rows[0]) * 3)
    for r in range(0, len(rows)):
        rl = r * 3
        for c in range (0, len(rows[r])):
            cl = c * 3
            if not pipe_positions[r][c]:
                continue
            pipe_map[rl+1][cl+1] = True
            nt = NODE_TYPE[rows[r][c]]
            if nt['n']:
                pipe_map[rl][cl+1] = True
            if nt['s']:
                pipe_map[rl+2][cl+1] = True
            if nt['w']:
                pipe_map[rl+1][cl] = True
            if nt['e']:
                pipe_map[rl+1][cl+2] = True

    
    for row in pipe_map:
        line = ['x' if i==True else '.' for i in row]
        print(''.join(line))

    # Setup escapable_positions
    for cols in pipe_map:
        l = []
        for col in cols:
            l.append('')
        escapable_positions.append(l)

    # Start with large map
    for r in range(0, len(pipe_map)):
        for c in range (0, len(pipe_map[r])):
            if not pipe_map[r][c]:
                #print('(%s, %s)' % (r,c))
                esc_value = 'x'
                if not is_escapable(r, c, pipe_map):
                    esc_value = '-'
                # Fill in all the unkown positions
                for i in range(0, len(escapable_positions)):
                    for j in range (0, len(escapable_positions[i])):
                        if escapable_positions[i][j] == '?':
                            escapable_positions[i][j] = esc_value


    result = 0
    # Check smaller map
    for r in range(0, len(rows)):
        for c in range (0, len(rows[r])):
            if not pipe_positions[r][c]:
                if escapable_positions[r*3][c*3] == '-':
                    result += 1

    print('Result: %s' % result)

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    