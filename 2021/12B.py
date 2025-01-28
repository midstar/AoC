import sys
from collections import defaultdict

def BFS(nodes):
    q = [('start',{'start'},False)]
    result = []
    while q:
        node, path, twiceUsed = q.pop()
        if node == 'end':
            result.append(path)
            continue
        for node2 in nodes[node]:
            twiceUsed2 = twiceUsed
            if node2.lower() == node2 and node2 in path:
                if twiceUsed:
                    continue # Small cave already visited
                twiceUsed2 = True
            q.append((node2, path | {node2}, twiceUsed2))
    return result


def solve(input):
    nodes = defaultdict(set)
    for line in input.splitlines():
        n1, n2 = line.split('-')
        nodes[n1].add(n2)
        if n1 != 'start' and n2 != 'end':
            nodes[n2].add(n1)
    return len(BFS(nodes))
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))