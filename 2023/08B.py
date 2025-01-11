import sys, math 

def steps_to_z(instructions, nodes, node, xxZ_nodes):
    steps = 0
    i = 0
    while True:
        node = nodes[node][instructions[i]]
        steps += 1
        i += 1
        if i >= len(instructions):
            i = 0
        if node in xxZ_nodes:
            break
    return steps

def solve(input):
    lines = input.splitlines()
    instructions = lines.pop(0)
    lines.pop(0)
    nodes = {}
    xxA_nodes = set()
    xxZ_nodes = set()
    for line in lines:
        name_conn = line.split('=')
        name = name_conn[0].strip()
        conn = name_conn[1].split(',')
        name_left = conn[0].replace('(', '').strip()
        name_right = conn[1].strip(')').strip()
        nodes[name] = {
            'L' : name_left,
            'R' : name_right
        }
        if name[2] == 'A':
            xxA_nodes.add(name)
        if name[2] == 'Z':
            xxZ_nodes.add(name)

    steps = [steps_to_z(instructions, nodes, node, xxZ_nodes) for node in xxA_nodes]
    return math.lcm(*steps)

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))