import sys

def solve(input):
    commands = [(line.split()[0], int(line.split()[1])) for line in input.splitlines()]
    horizontal = 0
    depth = 0
    for (dir, val) in commands:
        match dir:
            case 'forward':
                horizontal += val
            case 'down':
                depth += val
            case 'up':
                depth -= val
    result = horizontal * depth
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))