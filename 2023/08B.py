import sys
from functools import cmp_to_key

def solve(input):
    lines = input.splitlines()
    instr = lines.pop(0)
    instructions = ""
    for i in range (0, 1000):
        instructions += instr
    lines.pop(0)
    nodes = {}
    current_nodes = []
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
            current_nodes.append(name)

    # Preprocess
    for name, node in nodes.items():
        node['endNodes'] = []
        name2 = name
        for i in range(0, len(instructions)):
            name2 = nodes[name2][instructions[i]]
            if name2[2] == 'Z':
                node['endNodes'].append(i + 1)
        node['nextNode'] = name2
    
    #print(current_nodes)

    # Check
    step_big = len(instructions)
    steps = 0
    while True:
        endNodes = nodes[current_nodes[0]]['endNodes']
        found = -1
        maxMatches = 0
        for endNode in endNodes:
            found = endNode
            for i in range(1, len(current_nodes)):
                if found not in nodes[current_nodes[i]]['endNodes']:
                    found = -1
                    break
                if maxMatches < i:
                    maxMatches = i
            if found != -1:
                break
        if found != -1:
            steps += found
            break # We are done
        
        for i in range(0, len(current_nodes)):
            current_nodes[i] = nodes[current_nodes[i]]['nextNode']

        steps += step_big

        #if (maxMatches > 4):
        #    print('%s %s' % (current_nodes, steps))

    return steps

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))