import sys
import re

def solve(input):
    return sum([int(a) * int(b) for (a,b) in re.findall(r'mul\((\d+),(\d+)\)', input)])      
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read())) 