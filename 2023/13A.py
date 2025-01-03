import sys

def horizontal_match(pattern):
    for center in range(0, len(pattern) - 1):
        offset = 1
        valid_center = True
        while (center - (offset - 1)) >= 0 and (center + offset) < len(pattern):
            if pattern[center - (offset - 1)] != pattern[center + offset]:
                valid_center = False
                break
            offset += 1
        if valid_center:
            return center + 1
    return 0

def transpose(pattern):
    new = []
    for col in range(0, len(pattern[0])):
        l = []
        for row in range(0, len(pattern)):
            l.append(pattern[row][col])
        new.append(''.join(l))
    return new

def score(pattern):
    # Horizontal
    score = horizontal_match(pattern) * 100

    # Vertical
    score += horizontal_match(transpose(pattern))

    return score

def print_pattern(pattern):
    for line in pattern:
        print(line)

def solve(input):
    lines = input.splitlines()
    patterns = [[]]
    for line in lines:
        if line == '':
            patterns.append([])
        else:
            patterns[-1].append(line)
        
    result = 0
    for pattern in patterns:
        s = score(pattern)
        result += s

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))