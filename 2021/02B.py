import sys

def solve(input):
    commands = [(line.split()[0], int(line.split()[1])) for line in input.splitlines()]
    aim = 0
    horizontal = 0
    depth = 0
    for (dir, val) in commands:
        match dir:
            case 'forward':
                horizontal += val
                depth += aim * val
            case 'down':
                aim += val
            case 'up':
                aim -= val
    result = horizontal * depth
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))