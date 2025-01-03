import sys

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

    #print('Start: %s' % str(s))

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
        pipe_map.append(['.'] * len(rows[0]) * 3)
    for r in range(0, len(rows)):
        rl = r * 3
        for c in range (0, len(rows[r])):
            cl = c * 3
            if not pipe_positions[r][c]:
                continue
            pipe_map[rl+1][cl+1] = 'x'
            nt = NODE_TYPE[rows[r][c]]
            if nt['n']:
                pipe_map[rl][cl+1] = 'x'
            if nt['s']:
                pipe_map[rl+2][cl+1] = 'x'
            if nt['w']:
                pipe_map[rl+1][cl] = 'x'
            if nt['e']:
                pipe_map[rl+1][cl+2] = 'x'

    
    #for row in pipe_map:
    #    print(''.join(row))

    row_found = True
    while row_found:
        row_found = False
        for r in range(0, len(pipe_map)):
            col_found = True
            while col_found:
                col_found = False
                for c in range (0, len(pipe_map[r])):
                    if pipe_map[r][c] != 'x' and pipe_map[r][c] != 'O':
                        if r == 0 or r == (len(pipe_map) - 1) or c == 0 or (c == len(pipe_map[r]) - 1):
                            pipe_map[r][c] = 'O' # Edge
                            col_found = True
                        elif pipe_map[r - 1][c] == 'O' or pipe_map[r + 1][c] == 'O' or pipe_map[r][c - 1] == 'O' or pipe_map[r][c + 1] == 'O':
                            pipe_map[r][c] = 'O' # Next to another O
                            col_found = True  
                if col_found:
                    row_found = True                     

    #print('--------------------')
    #for row in pipe_map:
    #    print(''.join(row))

    result = 0
    # Check smaller map
    for r in range(0, len(rows)):
        for c in range (0, len(rows[r])):
            if not pipe_positions[r][c]:
                if pipe_map[r*3][c*3] == '.':
                    result += 1

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))