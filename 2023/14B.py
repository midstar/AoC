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

    #print_pattern(pattern)
    #print()

    scores = []
    for i in range(0, 500): #1000000000):
        for i in range(0, 4):
            pattern = transpose(pattern)
            pattern = tilt(pattern)
        scores.append(score(pattern))

    # Find repeating pattern
    start_index = 100
    repeating = scores[start_index:start_index + 100] # Try some
    repeating_indexes = []
    for i in range(1, len(scores) - len(repeating)):
        repeating_index = i
        for j in range(0, len(repeating)):
            if scores[i+j] != repeating[j]:
                repeating_index = -1
                break
        if repeating_index != -1:
            repeating_indexes.append(repeating_index)

    #print(repeating_indexes)

    # Validate repeating pattern
    offset = repeating_indexes[1] - repeating_indexes[0]
    for i in range(0, len(repeating_indexes) - 1):
        if repeating_indexes[i+1] - repeating_indexes[i] != offset:
            print("No pattern found!")
            exit(1)
    
    repeating = repeating[:offset]
    #print('Offset', offset)
    #print('Sequence', repeating)

    pattern_offset = (1000000000 - start_index) % offset
    result = repeating[pattern_offset - 1]

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))