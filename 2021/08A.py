import sys

def solve(input):
    result = 0
    for line in input.splitlines():
        for segment in line.split('|')[1].split():
            if len(segment) in [2,3,4,7]: result += 1
    return result
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))