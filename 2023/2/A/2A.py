import argparse

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
        print('Game %s: %s' % (game, possible))
        if possible:
            sum += game
    print('Result: %s' % str(sum))



def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    