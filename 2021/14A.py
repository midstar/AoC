import sys
from collections import defaultdict

def run(polymer, rules):
    polymer2 = []
    for i in range(len(polymer) - 1):
        ins = rules[polymer[i:i+2]]
        polymer2.append(polymer[i])
        polymer2.append(ins)
    polymer2.append(polymer[-1])
    return ''.join(polymer2)

def solve(input):
    polymer, rules = input.split('\n\n')
    rules = {rule.split(' -> ')[0]:rule.split(' -> ')[1] for rule in rules.splitlines()}
    for _ in range(10):
        polymer = run(polymer, rules)
    cnt = defaultdict(lambda:0)
    for c in polymer:
        cnt[c] += 1
    return max(cnt.values()) - min(cnt.values())
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))