import sys,math

'''
d = distance
t = total time
h = hold time

d = (t - h) * h
=>
d = h * t - h^2
=>
h^2 - t * h + d = 0

PQ formula:
h = t / 2 +/- root((-1 * t/2)^2 - d)
'''
# PQ Formula
def hold_time(time, distance):
    p1 = time / 2
    p2 = math.sqrt((-1 * time/2)**2 - distance)
    return sorted([p1 + p2, p1 - p2])

def solve(input):
    lines = input.splitlines()
    time = int(lines[0].split(':')[1].replace(" ", ""))
    record_dist = int(lines[1].split(':')[1].replace(" ", ""))
    
    ht_low, ht_high = hold_time(time,record_dist)
    return math.floor(ht_high) - math.ceil(ht_low) + 1

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))

