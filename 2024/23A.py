import sys

def solve(input):
    connections = {}
    for line in input.splitlines():
        c1, c2 = line.split('-')
        connections.setdefault(c1,set())
        connections.setdefault(c2,set())
        connections[c1].add(c2)
        connections[c2].add(c1)

    connect3 = set()
    for c1, remotes in connections.items():
        for c2 in remotes:
            for c3 in connections[c2]:
                if c1 in connections[c3]:
                    connect3.add(tuple(sorted([c1,c2,c3])))

    return sum([any(c.startswith('t') for c in con) for con in connect3])
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))