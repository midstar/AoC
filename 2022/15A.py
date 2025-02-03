import sys, re

def dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def add_range(ranges, from_x, to_x):
    new_range = None
    for i, (from_x2, to_x2) in enumerate(ranges):
        if (from_x < from_x2 and to_x >= from_x2) or \
           (from_x <= to_x2 and to_x >= from_x2):
            new_range = (min(from_x, from_x2), max(to_x, to_x2))
            ranges.pop(i)
            break
    if new_range == None:
        ranges.append((from_x,to_x))
    else:
        add_range(ranges,*new_range)


def solve(input):
    ranges = []
    beacons = set()
    row = 2000000
    for line in input.splitlines():
        x,y,bx,by = list(map(int,re.findall(r'=(-?\d+)', line)))
        if by == row: beacons.add(bx)
        d = dist(x,y,bx,by)
        remain_d = d - abs(row - y)
        if remain_d >= 0:
            add_range(ranges, x - remain_d, x + remain_d)

    result = 0
    for from_x, to_x in ranges:
        result += to_x - from_x + 1
    result -= len(beacons)

    return result
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))