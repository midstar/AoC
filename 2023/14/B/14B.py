import argparse

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

def score(pattern):
    score = 0
    for row in range(0, len(pattern)):
        score_base = len(pattern) - row
        score += pattern[row].count('O') * score_base
    return score

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


def solve(input):
    lines = input.splitlines()
    pattern = []
    for line in lines:
        pattern.append([*line])

    print_pattern(pattern)
    print()

    scores = []
    for i in range(0, 2000): #1000000000):
        for i in range(0, 4):
            pattern = transpose(pattern)
            pattern = tilt(pattern)
        scores.append(score(pattern))

    # Find repeating pattern
    start_index = 100
    repeating = scores[start_index:200] # Try some
    repeating_indexes = []
    for i in range(1, len(scores) - len(repeating)):
        repeating_index = i
        for j in range(0, len(repeating)):
            if scores[i+j] != repeating[j]:
                repeating_index = -1
                break
        if repeating_index != -1:
            repeating_indexes.append(repeating_index)

    # Validate repeating pattern
    offset = repeating_indexes[1] - repeating_indexes[0]
    for i in range(0, len(repeating_indexes) - 1):
        if repeating_indexes[i+1] - repeating_indexes[i] != offset:
            print("No pattern found!")
            exit(1)
    
    repeating[:offset]
    print('Offset', offset)
    print('Sequence', repeating)

    s = 0
    for i in range(start_index, 1000000000): 
        result = repeating[s]
        s += 1
        if s >= offset:
            s = 0

    print('Result: %s' % result)

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    