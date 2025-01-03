import sys

def hash(input):
    h = 0
    for c in input:
        h += ord(c)
        h *= 17
        h = h % 256
    return h

def solve(input):
    #lines = input.splitlines()
    #matrix = [list(line) for line in lines]
    result = 0

    words = input.split(',')
    for word in words:
        result += hash(word)

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))