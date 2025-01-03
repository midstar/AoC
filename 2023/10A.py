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

# Returns longest path to S
def navigate(r, c, rows, from_direction):
    result = [0]
    if (from_direction != '' and rows[r][c] == 'S'):
        return 0 # We are done
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

    # Find start (S)
    s = (0,0)
    for r in range(0, len(rows)):
        for c in range (0, len(rows[r])):
            if rows[r][c] == 'S':
                s = (r,c)

    #print('Start: %s' % str(s))

    longest_path = navigate(s[0], s[1], rows, '')
    result = int(longest_path / 2)
    #print('Longest: %s  (%s)' % (longest_path, result))

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))