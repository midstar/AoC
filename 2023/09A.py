import sys

def calc(values):
    result = 0
    while (any(values)):
        #print(values[-1])
        result += values[-1]
        diff = []
        for i in range (0, len(values) - 1):
            diff.append(values[i+1] - values[i])
        values = diff
    #print(result)
    return result

def solve(input):
    result = 0
    lines = input.splitlines()
    for line in lines:
        #print(line)
        values = [eval(i) for i in line.split()]
        result += calc(values)

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))