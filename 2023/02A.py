import sys

def solve(input):
    MAX_RED   = 12
    MAX_GREEN = 13
    MAX_BLUE  = 14
    sum = 0
    game = 0
    for line in input.splitlines():
        game +=1 
        sets = line.split(':')[1]
        possible = True
        for s in sets.split(';'):
            for v_c in s.split(','):
                value = int(v_c.split()[0])
                color = v_c.split()[1]
                if color == 'red' and value > MAX_RED:
                    possible = False
                if color == 'green' and value > MAX_GREEN:
                    possible = False
                if color == 'blue' and value > MAX_BLUE:
                    possible = False
        #print('Game %s: %s' % (game, possible))
        if possible:
            sum += game
    return sum



if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))