import sys

DIRECTION = {
    'U' : (-1,  0 ),
    'D' : ( 1,  0 ),
    'L' : ( 0, -1 ),
    'R' : ( 0,  1 ) 
}

def get_node(node, dir, steps):
    dr, dc = DIRECTION[dir]
    return (node[0] + dr * steps, node[1] + dc * steps)

def solve(input):
    node = (0,0)
    nodes = [node]
    steps_tot = 0
    for line in input.splitlines():
        dir = line.split()[0]
        steps = int(line.split()[1])
        node = get_node(node, dir, steps)
        nodes.append(node)
        steps_tot += steps

    # Calculate polygon area using Shoelace Formula (Triangle formula)
    area = 0
    for i in range(0, len(nodes) - 1):
        node_a = nodes[i]
        node_b = nodes[i+1]
        area += 0.5 * (node_a[0] * node_b[1] - node_b[0] * node_a[1])
    area = abs(area)

    # The problem with the area above is that includes only half of
    # the border. Draw a rectancle with corners 0,0 0,3 3,3 and 3,0
    # on a checkered paper you will se that the left and bottom 
    # border are within the area and top and right border are outside 
    # the area. Shoelace Formula will give area 9 but with the border
    # (count squares on paper) the area is 9 + 7 = 16. 
    #
    # You kan use Pick's Theorem to calculate the inner are as:
    #
    # A = i + b/2 - 1  => i = A - b/2 + 1
    #
    # A is the area we calculated above (area variable)
    #
    # The area with border (AB) is AB = i + b
    #
    # Replace i and get AB = (A - b/2 + 1) + b = A + b/2 + 1
    return int(area + steps_tot / 2 + 1)

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))