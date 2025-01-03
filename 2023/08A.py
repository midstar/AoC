import sys
from functools import cmp_to_key

def solve(input):
    lines = input.splitlines()
    instructions = lines.pop(0)
    lines.pop(0)
    nodes = {}
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
    #print(nodes)

    node = 'AAA'
    steps = 0
    i = 0
    while node != 'ZZZ':
        node = nodes[node][instructions[i]]
        steps += 1
        i += 1
        if i >= len(instructions):
            i = 0
    return steps

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))