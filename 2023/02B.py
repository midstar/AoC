import sys

def solve(input):
    sum = 0
    game = 0
    for line in input.splitlines():
        game +=1 
        max_red = 0
        max_green = 0
        max_blue = 0
        sets = line.split(':')[1]
        for s in sets.split(';'):
            for v_c in s.split(','):
                value = int(v_c.split()[0])
                color = v_c.split()[1]
                if color == 'red' and value > max_red:
                    max_red = value
                if color == 'green' and value > max_green:
                    max_green = value
                if color == 'blue' and value > max_blue:
                    max_blue = value
        power = max_red * max_green * max_blue
        #print('Game %s: r %s  g %s  b %s  pow %s' % (game, max_red, max_green, max_blue, power))
        sum += power
    return sum


if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))