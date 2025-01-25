import sys
from functools import cache

@cache
def nbr_lanternfish(timer, days):
    result = 1
    while days > 0:
        days -= 1
        if timer > 0:
            timer -= 1
        else:
            timer = 6
            result += nbr_lanternfish(8, days)
    return result


def solve(input):
    return sum(nbr_lanternfish(int(timer),256) for timer in input.strip().split(','))
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))