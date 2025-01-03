import sys

def solve(input):
    result = 0
    for line in input.splitlines():
        you = line.split()[0]
        me = line.split()[1]
        if me == 'X' and you == 'C' or me == 'Y' and you == 'A' or me == 'Z' and you == 'B':
            result += 6
        elif me == 'X' and you == 'A' or me == 'Y' and you == 'B' or me == 'Z' and you == 'C':
            result +=3
        if me == 'X':
            result += 1
        elif me == 'Y':
            result += 2
        elif me == 'Z':
            result += 3
    return result
    

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))