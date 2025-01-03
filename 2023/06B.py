import sys

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

    return nbr_wins

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))