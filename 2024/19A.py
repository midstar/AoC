import sys
from functools import cache

@cache
def is_possible(towels,pattern):
    if pattern == '':
        return True
    for i, towel in enumerate(towels):
        if pattern.startswith(towel):
            if is_possible(towels, pattern[len(towel):]): return True
    return False

def solve(input):
    lines = input.splitlines()
    towels = [t.strip() for t in lines[0].split(',')]

    result = 0
    for pattern in lines[2:]:
        if is_possible(frozenset(towels),pattern):
            result += 1

    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))