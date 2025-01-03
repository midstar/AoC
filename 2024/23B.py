import sys
from functools import cache

connections = {}

def set2tuple(a_set):
    return tuple(sorted(list(a_set)))

@cache
def get_cluster(head, tail):
    global connections
    if len(tail) <= 1:
        return {set2tuple(head | tail)}
    clusters = set()
    for computer in tail:
        cluster_set = connections[computer].intersection(tail)
        clusters |= get_cluster(frozenset(head | {computer}), frozenset(cluster_set))
    return clusters

def solve(input):
    global connections
    for line in input.splitlines():
        c1, c2 = line.split('-')
        connections.setdefault(c1,set())
        connections.setdefault(c2,set())
        connections[c1].add(c2)
        connections[c2].add(c1)

    clusters = set()
    for computer, remotes in connections.items():
        clusters |= get_cluster(frozenset({computer}),frozenset(remotes))

    return ','.join(max(clusters,key=len))
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))