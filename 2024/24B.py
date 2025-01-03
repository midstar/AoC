import sys

# Circuit is a binary adder cirquit based on full adder blocks:
# https://www.geeksforgeeks.org/binary-adder-with-logic-gates/
#
# Assumptions:
#  1. Two wires are only switched within same full adder block
#  2. No more than two wires switched within each full adder block
#  3. Only logic gate output connections are switched
#  4. No error in "block" 0. block 0 is a special block not following
#     the same pattern as a full adder (nor half adder) scheme.

def match(wires, gates, wire,expected_gates):
    result = [None] * len(expected_gates)
    if (len(wires[wire]['to']) == len(result)):
        for gate_key in wires[wire]['to']:
            if gates[gate_key]['op'] in expected_gates: 
                i = expected_gates.index(gates[gate_key]['op'])
                result[i] = gates[gate_key]
    if len(result) == 1:
        return result[0]
    return result

# Comments based on wire names in following image:
# https://media.geeksforgeeks.org/wp-content/uploads/20240404130934/Binary-Adder-with-Logic-Gates.png
def check_full_adder(wires,gates,no):
    invalid_wires = set()
    AB_XOR, AB_AND = match(wires, gates, f'x{no:02}',['XOR','AND'])

    AxB_XOR, AxB_AND = match(wires, gates, AB_XOR['out'],['XOR','AND'])
    if AxB_XOR == None or AxB_AND == None:
        invalid_wires.add(AB_XOR['out'])
    else:
        if AxB_XOR['out'] != f'z{no:02}':
            invalid_wires.add(AxB_XOR['out'])
        Cin_AdB_OR = match(wires, gates, AxB_AND['out'],['OR'])
        if Cin_AdB_OR == None:
            invalid_wires.add(AxB_AND['out'])
        elif no < 44:
            Cout_XOR, Cout_AND = match(wires, gates, Cin_AdB_OR['out'],['XOR','AND'])
            if Cout_XOR == None or Cout_AND == None:
                invalid_wires.add(Cin_AdB_OR['out'])
    Cin_AdB_OR = match(wires, gates, AB_AND['out'],['OR'])
    if Cin_AdB_OR == None:
        invalid_wires.add(AB_AND['out'])
    elif no < 44:
        Cout_XOR, Cout_AND = match(wires, gates, Cin_AdB_OR['out'],['XOR','AND'])
        if Cout_XOR == None or Cout_AND == None:
            invalid_wires.add(Cin_AdB_OR['out'])

    if len(invalid_wires) % 2 != 0:
        print(f'Adder {no} Warning! 0 or 2 invalid wires expected: {invalid_wires}')
    return invalid_wires


def solve(input):
    wires = {}
    gates = {}
    for line in input.split('\n\n')[1].splitlines():
        i1, op, i2, _, o = line.split()
        gates[line] = {'in':[i1,i2],'op':op,'out':o}
        for w in [i1,i2,o]:
            if w not in wires: wires[w] = {'to':[]}
        wires[o]['from'] = line
        wires[i1]['to'].append(line)
        wires[i2]['to'].append(line)

    invalid_wires = set()
    for i in range(1,45):
        invalid_wires |= check_full_adder(wires,gates,i)
    
    if len(invalid_wires) != 8:
        print(f'Warning! Not all wires were found.')

    return ','.join(sorted(list(invalid_wires)))
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))