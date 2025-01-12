import sys

def hash(input):
    h = 0
    for c in input:
        h += ord(c)
        h *= 17
        h = h % 256
    return h

def solve(input):
    return sum([hash(word) for word in input.strip().split(',')])

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))