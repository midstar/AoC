import sys
from functools import cache

@cache
def is_possible(towels,pattern):
    if pattern == '':
        return 1
    result = 0
    for i, towel in enumerate(towels):
        if pattern.startswith(towel):
            result += is_possible(towels, pattern[len(towel):])
    return result

def solve(input):
    lines = input.splitlines()
    towels = [t.strip() for t in lines[0].split(',')]

    result = 0
    for pattern in lines[2:]:
        result += is_possible(frozenset(towels),pattern)

    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))