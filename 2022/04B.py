import sys

def solve(input):
    result = 0
    for line in input.splitlines():
        a_min, a_max, b_min, b_max = tuple([int(v) for r in line.split(',') for v in r.split('-')])
        if a_min >= b_min and a_min <= b_max or a_max >= b_min and a_max <= b_max or \
           b_min >= a_min and b_min <= a_max or b_max >= a_min and b_max <= a_max :
            result += 1
    return result
    

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))