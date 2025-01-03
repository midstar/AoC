import sys
import re

def solve(input):
    result = 0
    
    parts = input.split('do()')
    for part in parts:
        part = part.split("don't()")[0]
        result += sum([int(a) * int(b) for (a,b) in re.findall(r'mul\((\d+),(\d+)\)', part)])

    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))