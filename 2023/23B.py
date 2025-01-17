import sys

def w_graph(grid,graph,steps,g_node,node,node_prev = None):
    if node in graph and steps > 0:
        graph[node][g_node] = steps
    else:
        r, c = node
        paths = set()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            node2 = (r + dr, c + dc)
            if node2 != node_prev and node2 in grid:
                 paths.add(node2)
        if len(paths) == 0:
            if node != max(grid):
                # Dead end
                pass
            else:
                # Exit node
                graph[node] = {g_node:steps}
        else:
            if len(paths) > 1:
                graph[node] = {g_node:steps}
                g_node = node
                steps = 0
            for n in paths:
                w_graph(grid, graph,steps + 1, g_node, n, node)

# Secure that all connections goes both ways
def w_graph_dual(graph):
    for key, value in graph.items():
        for key2, l in value.items():
            graph[key2][key] = l

def s(name):
    r,c = name
    return f'{r}_{c}'

def to_plantuml(graph):
    for key, value in graph.items():
        for key2, l in value.items():
            print(f'{s(key)} --> {s(key2)}: {l}')

def longest_path(graph,current,visited,length,last):
    if current == last: return length
    result = 0
    for node, l in graph[current].items():
        if node not in visited:
            result = max(result, longest_path(graph,node,visited | {node},length + l, last))
    return result

def solve(input):
    sys.setrecursionlimit(100000)

    lines = input.splitlines()
    grid = {(r,c) for r, line in enumerate(input.splitlines()) \
                  for c, val in enumerate(line) if val != '#'}
    
    graph = {(0,1):{}}
    w_graph(grid,graph,0,(0,1),(0,1))
    w_graph_dual(graph)
    #to_plantuml(graph)
    return longest_path(graph,(0,1),set(),0,max(grid))


if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))