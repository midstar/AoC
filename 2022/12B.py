import argparse

def climbeable(type_from, type_to):
    if ord(type_to) <= (ord(type_from) + 1):
        return True
    return False

def get_neighbours(graph, node):
    row = node[0]
    col = node[1]
    result = []
    type_from = graph[row][col]
    if row > 0 and climbeable(type_from, graph[row - 1][col]):
        result.append((row - 1, col))
    if row < (len(graph) - 1) and climbeable(type_from, graph[row + 1][col]):
        result.append((row + 1, col))
    if col > 0 and climbeable(type_from, graph[row][col - 1]):
        result.append((row, col - 1))
    if col < (len(graph[row]) - 1) and climbeable(type_from, graph[row][col + 1]):
        result.append((row, col + 1))
        
    return result

# BFS Shortest Path Algorithm
def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the 
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is 
    # reached
    if start == goal:
        #print("Same Node")
        return
     
    # Loop to traverse the graph 
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = get_neighbours(graph, node)
             
            # Loop to iterate over the 
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the 
                # neighbour node is the goal
                if neighbour == goal:
                    return new_path
            explored.append(node)
 
    # Condition when the nodes 
    # are not connected
    return []

def solve(input):
    lines = input.splitlines()

    # Find start and goal
    starts = []
    goal = (0, 0)
    for row in range(0, len(lines)):
        if 'S' in lines[row]:
            lines[row] = lines[row].replace('S', 'a')
        if 'E' in lines[row]:
            goal = (row, lines[row].index('E'))
            lines[row] = lines[row].replace('E', 'z')
        for col in range(0, len(lines[row])):
            if lines[row][col] == 'a':
                starts.append((row,col))

    result = 0
    for start in starts:
        path = BFS_SP(lines, start, goal)
        length = len(path) - 1
        if length < 0:
            continue # No path exists
        if result == 0 or length < result:
            result = length

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))