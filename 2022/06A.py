import sys

def solve(input):
    m = 4
    for i in range(0, len(input) - m):
        if len(set(input[i:i + m])) == m: return i + m
    

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))