import argparse
from functools import cmp_to_key

def solve(input):
    lines = input.splitlines()
    instructions = lines.pop(0)
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
    #print(nodes)

    steps = 0
    i = 0
    while True:
        j = 0
        nbrZ = 0
        steps += 1
        for node in current_nodes:
            node = nodes[node][instructions[i]]
            current_nodes[j] = node
            j += 1
            if node[2] == 'Z':
                nbrZ += 1
        if nbrZ == len(current_nodes):
            break
        i += 1
        if i >= len(instructions):
            i = 0
    print('Result: %s' % str(steps))

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    