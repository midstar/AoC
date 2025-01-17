import sys
import random

def bfs(nodes, node1, node2):
    q = [(node1,[node1])]
    visited = set()
    while q:
        node, path = q.pop(0)
        if node == node2:
            return path
        if node in visited:   
            continue
        visited.add(node)
        for neighbour in nodes[node]:
            path2 = path.copy()
            path2.append(neighbour)
            q.append((neighbour, path2))
    return [] # No Path

def bfs_count(nodes, node1):
    q = [(node1)]
    visited = set()
    nbr_nodes = 0
    while q:
        node = q.pop(0)
        if node in visited:   
            continue
        nbr_nodes += 1
        visited.add(node)
        for neighbour in nodes[node]:
            q.append(neighbour)
    return nbr_nodes

def solve(input):
    nodes = {}
    for line in input.splitlines():
        f_t = line.split(':')
        from_node = f_t[0].strip()
        to_nodes = f_t[1].split()
        if from_node not in nodes:
            nodes[from_node] = set()
        for to_node in to_nodes:
            # Below will give PlantULM State Diagram output
            #print(from_node,'--',to_node)
            nodes[from_node].add(to_node)
            if to_node not in nodes:
                nodes[to_node] = set()
            nodes[to_node].add(from_node)

    all_routes_exists = True
    node1_removed = None
    node2_removed = None
    while all_routes_exists:  
        node_list = random.choices(list(nodes.keys()), k=100)
        vertex_cnt = {}
        while node_list:
            node = node_list.pop()
            for node2 in node_list:
                path = bfs(nodes, node, node2)
                if not path:
                    #print('No route ', node, '-', node2)
                    all_routes_exists = False
                    break
                for i in range(0, len(path) - 1):
                    n1 = path[i]
                    n2 = path[i+1]
                    vertex_l = [n1, n2]
                    vertex_l.sort()
                    vertex = tuple(vertex_l)
                    if vertex not in vertex_cnt:
                        vertex_cnt[vertex] = 1
                    else:
                        vertex_cnt[vertex] += 1
            if not all_routes_exists:
                break
        if not all_routes_exists:
            break

        cnt_list = {}
        for vertex, cnt in vertex_cnt.items():
            if cnt not in cnt_list:
                cnt_list[cnt] = []
            cnt_list[cnt].append(vertex)

        cnt_l = list(cnt_list.keys())
        cnt_l.sort(reverse=True)
        for i in range(0, min(len(cnt_l),5)):
            cnt = cnt_l[i]
            #print(cnt, *cnt_list[cnt])
        
        # Remove vertex with highest traffic
        (node1, node2) = cnt_list[cnt_l[0]][0]
        node1_removed = node1
        node2_removed = node2
        #print()
        #print('Removing', node1, '-', node2)
        if node1 in nodes[node2]:
            nodes[node2].remove(node1)
        if node2 in nodes[node1]:
            nodes[node1].remove(node2)

    g1_cnt = bfs_count(nodes, node1_removed)
    g2_cnt = bfs_count(nodes, node2_removed)

    #print('Group 1: ', g1_cnt, '  Group 2: ', g2_cnt)

    result = g1_cnt * g2_cnt
    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))