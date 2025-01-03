import sys
from collections import defaultdict
import re

def fill(filled, x1, y1, x2, y2):
    xd = 1 if x1 < x2 else -1 if x1 > x2 else 0
    yd = 1 if y1 < y2 else -1 if y1 > y2 else 0
    while(x1 != x2 or y1 != y2):
        filled[(x1,y1)] += 1
        x1 += xd
        y1 += yd
    filled[(x1,y1)] += 1  

def solve(input):
    filled = defaultdict(lambda: 0)
    for line in input.splitlines():
        x1, y1, x2, y2 = map(int,re.findall('(\d+)',line))
        if x1 != x2 and y1 != y2:
            continue
        fill(filled, x1, y1, x2, y2)
    
    return len([v for v in filled.values() if v > 1])
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))