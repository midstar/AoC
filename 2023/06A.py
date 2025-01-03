import sys

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
        #print('Time: %s Record: %s Nbr wins: %s' % (time, record_dist, nbr_wins))

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))