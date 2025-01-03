import sys

def solve(input):
    sum = 0
    game = 0
    for line in input.splitlines():
        game += 1
        game_str = line.split(':')[1].split('|')
        win_numbers = game_str[0].split()
        numbers = game_str[1].split()
        points = 0
        for win_number in win_numbers:
            if win_number in numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        #print('Game %s : %s points' % (game, points))
        sum += points
    return sum

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))