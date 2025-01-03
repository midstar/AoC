import sys

def tilt(pattern):
    for row in range(0, len(pattern)):
        changed = True
        while changed:
            changed = False
            rock_col = -1
            for col in range (0, len(pattern[row])):
                if pattern[row][col] == 'O':
                    rock_col = col
                elif pattern[row][col] == '#':
                    rock_col = -1
                elif pattern[row][col] == '.' and rock_col != -1:
                    pattern[row][col] = 'O'
                    pattern[row][rock_col] = '.'
                    rock_col = col
                    changed = True
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