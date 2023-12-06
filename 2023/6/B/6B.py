import argparse

def solve(input):
    lines = input.splitlines()
    time = int(lines[0].split(':')[1].replace(" ", ""))
    record_dist = int(lines[1].split(':')[1].replace(" ", ""))

    nbr_wins = 0
    for hold_time in range(0, time+1):
        speed = hold_time
        distance = (time - hold_time) * speed
        if (distance > record_dist):
            nbr_wins += 1
    print('Time: %s Record: %s Nbr wins: %s' % (time, record_dist, nbr_wins))

    print('Result: %s' % str(nbr_wins))

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    