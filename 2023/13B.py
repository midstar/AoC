import sys

def smudge_comp(s1, s2, smudges_allowed):
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            if smudges_allowed > 0:
                smudges_allowed -= 1
            else:
                return (False, 0)
    return (True, smudges_allowed)


def horizontal_match(pattern):
    for center in range(0, len(pattern) - 1):
        offset = 1
        valid_center = True
        smudges_allowed = 1
        while (center - (offset - 1)) >= 0 and (center + offset) < len(pattern):
            result, smudges_allowed = smudge_comp(pattern[center - (offset - 1)], pattern[center + offset], smudges_allowed)
            if not result:
                valid_center = False
                break
            offset += 1
        if valid_center and smudges_allowed == 0:
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
        #print(s)
        #if s == 0:
        #    print_pattern(pattern)
        #    print()
        #    print()
        result += s

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))