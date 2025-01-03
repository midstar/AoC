import sys

OP = {
    'AND' : 'and',
    'OR'  : 'or',
    'XOR' : '^'
}

def solve(input):
    parts = input.split('\n\n')

    wires = {}
    for l in parts[0].splitlines():
        name, val = l.split(': ')
        wires[name] = int(val)

    gates = {}
    for line in parts[1].splitlines():
        i1, op, i2, _, o = line.split()
        gates[line] = {'i1':i1,'i2':i2,'op':OP[op],'o':o}
        for w in [i1,i2,o]:
            if w not in wires: wires[w] = None
        
    saturated = False
    while not saturated:
        saturated = True
        for g in gates.values():
            if wires[g['i1']] == None or wires[g['i2']] == None:
                saturated = False
            else:
                o2 = eval(f'{wires[g["i1"]]} {g["op"]} {wires[g["i2"]]}')
                if o2 != wires[g['o']]:
                    wires[g['o']] = o2
                    saturated = False

    wires_out = sorted([w for w in wires.keys() if w.startswith('z')])
    result = 0
    for i, w in enumerate(wires_out):
        result += wires[w] * 2**i
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))