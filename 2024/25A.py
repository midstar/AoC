import sys

def match(l,k):
    return not any([(l[i][j] == '#' and k[i][j] == '#') \
                    for i in range(len(l)) for j in range(len(l[0]))])

def solve(input):
    locks = [p.splitlines() for p in input.split('\n\n') if p[0] == '#']
    keys =  [p.splitlines() for p in input.split('\n\n') if p[0] == '.']
    return sum([match(l,k) for l in locks for k in keys])
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))