import argparse, time, sys

class Graph(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width  = len(matrix[0])

    def get_nodes(self):
        nodes = []
        for row in range(0, len(self.matrix)):
            for col in range(0, len(self.matrix[row])):
                nodes.append((row, col))
        return nodes
    
    def get_outgoing_edges(self, node, previous_nodes):
        horizontal_allowed = True
        vertical_allowed = True
        if node in previous_nodes:
            prev1 = previous_nodes[node]
            if prev1 in previous_nodes:
                prev2 = previous_nodes[prev1]
                if prev2 in previous_nodes:
                    prev3 = previous_nodes[prev2]
                    if node[0] == prev1[0] == prev2[0] == prev3[0]:
                        vertical_allowed = False
                    if node[1] == prev1[1] == prev2[1] == prev3[1]:
                        horizontal_allowed = False

        row = node[0]
        col = node[1]
        nodes = []
        if horizontal_allowed and row > 0:
            nodes.append((row - 1, col))
        if horizontal_allowed and row < (self.height - 1):
            nodes.append((row + 1, col))
        if vertical_allowed and col > 0:
            nodes.append((row, col - 1))
        if vertical_allowed and col < (self.width - 1):
            nodes.append((row, col + 1))
        return nodes
    
    def value(self, from_node, to_node):
        return int(self.matrix[to_node[0]][to_node[1]])


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = graph.get_nodes()
 
    # We'll use this dict to save the cost of visiting each node and update it as
    # we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited 
    # nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates
        # their distances
        neighbors = graph.get_outgoing_edges(current_min_node, previous_nodes)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def get_path(start_node, end_node, previous_nodes):
    path = []
    node = end_node
    while (node != start_node):
        path.append(node)
        node = previous_nodes[node]
    path.append(start_node)
    path.reverse()
    return path


def solve(input):
    matrix = [list(line) for line in input.splitlines()]
    graph = Graph(matrix)
    start_node = (0,0)
    end_node = (len(matrix) - 1, len(matrix[0]) - 1)
    previous_nodes, shortest_path = dijkstra_algorithm(graph, start_node)

    
    path = get_path(start_node, end_node, previous_nodes)

    print(path)
    print()
    for row in range(0, len(matrix)):
        line = []
        for col in range(0, len(matrix[row])):
            if (row, col) in path:
                line.append('#')
            else:
                line.append(matrix[row][col])
        print(''.join(line))

    return shortest_path[end_node]
    

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        start_time = time.time()
        result = solve(f.read())
        print('Result: %s  (excution time %0.4f s)' % (result, time.time() - start_time))

if __name__ == '__main__':
    main()    