import argparse

def solve(input):
    lines = input.splitlines()
    times = lines[0].split(':')[1].split()
    record_dists = lines[1].split(':')[1].split()

    result = 1
    for i in range(0, len(times)):
        time = int(times[i])
        record_dist = int(record_dists[i])
        nbr_wins = 0
        for hold_time in range(0, time+1):
            speed = hold_time
            distance = (time - hold_time) * speed
            if (distance > record_dist):
                nbr_wins += 1
        result *= nbr_wins
        print('Time: %s Record: %s Nbr wins: %s' % (time, record_dist, nbr_wins))

    print('Result: %s' % str(result))

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    