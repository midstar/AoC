import sys

def solve(input):
    sum = 0
    for line in input.splitlines():
        first = -1
        last  = -1
        for c in list(line):
            if c.isnumeric():
                if first == -1:
                    first = int(c)
                last = int(c)
        if first == -1 or last == -1:
            print('Error line: %s' % line)
            exit(1)
        num = first * 10 + last
        #print(str(num))
        sum += num
    return sum

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))