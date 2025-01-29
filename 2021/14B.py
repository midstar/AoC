import sys
from functools import cache

rules = None
chars = None

@cache
def count_pair(pair, steps):
    result = [0] * len(chars)
    if steps == 0:
        for c in pair:
            result[chars.index(c)] += 1
    else:
        n = rules[pair]
        r1 = count_pair(pair[0] + n, steps - 1)
        r2 = count_pair(n + pair[1], steps - 1)
        for i in range(len(result)):
            result[i] = r1[i] + r2[i]
        result[chars.index(n)] -= 1
    return tuple(result)

def solve(input):
    global rules
    global chars
    polymer, rules = input.split('\n\n')
    polymer = [polymer[i]+polymer[i+1] for i in range(len(polymer) - 1)]
    rules = {rule.split(' -> ')[0]:rule.split(' -> ')[1] for rule in rules.splitlines()}
    chars = sorted(list({k[0] for k in rules}))

    STEPS = 40
    c_count = [0] * len(chars)
    for i,pair in enumerate(polymer):
        r = count_pair(pair, STEPS)
        for j in range(len(c_count)):
            c_count[j] += r[j]
        if i > 0:
            c_count[chars.index(pair[0])] -= 1

    #print(chars)
    #print(c_count)
    c_count.sort()
    return c_count[-1] - c_count[0]
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))