import sys

def solve(input):
    sum = 0
    for line in input.splitlines():
        first = -1
        last  = -1
        line2 = line
        while len(line2) > 0:
            n = -1
            if (line2[0].isnumeric()):
                n = int(line2[0])
            elif line2.startswith('one'):
                n = 1
            elif line2.startswith('two'):
                n = 2
            elif line2.startswith('three'):
                n = 3
            elif line2.startswith('four'):
                n = 4
            elif line2.startswith('five'):
                n = 5
            elif line2.startswith('six'):
                n = 6
            elif line2.startswith('seven'):
                n = 7
            elif line2.startswith('eight'):
                n = 8
            elif line2.startswith('nine'):
                n = 9

            if n > -1:
                if first == -1:
                    first = n
                last = n
            
            line2 = line2[1:]
        if first == -1 or last == -1:
            print('Error line: %s' % line)
            exit(1)
        num = first * 10 + last
        #print(str(num))
        sum += num
    return sum

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))