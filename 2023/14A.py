import sys

def tilt(pattern):
    for row in range(len(pattern)):
        for col in reversed(range(len(pattern[row]))):
            if pattern[row][col] == '.':
                col2 = col - 1
                while col2 >= 0 and pattern[row][col2] != '#':
                    if pattern[row][col2] == 'O':
                        pattern[row][col]  = 'O' 
                        pattern[row][col2] = '.'
                        break
                    col2 -= 1
    return pattern

def transpose(pattern):
    new = []
    for col in range(0, len(pattern[0])):
        l = []
        for row in reversed(range(0, len(pattern))):
            l.append(pattern[row][col])
        new.append(l)
    return new

def print_pattern(pattern):
    for line in pattern:
        print(''.join(line))

def score(pattern):
    score = 0
    for row in range(0, len(pattern)):
        score_base = len(pattern) - row
        score += pattern[row].count('O') * score_base
    return score


def solve(input):
    lines = input.splitlines()
    pattern = []
    for line in lines:
        pattern.append([*line])

    #print_pattern(pattern)
    #print()
    pattern = transpose(pattern)
    #print_pattern(pattern)
    #print()
    pattern = tilt(pattern)
    #print_pattern(pattern)
    #print()
    pattern = transpose(pattern)
    pattern = transpose(pattern)
    pattern = transpose(pattern)
    #print_pattern(pattern)
    #print()

    return score(pattern)

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))