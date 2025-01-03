import sys

# '0', '1' ('1' if equal)
def get_most_common(vals, bitno):
    l = len(vals)
    num_ones = 0
    for val in vals:
        if val[bitno] == '1':
            num_ones += 1
    num_zeros = l - num_ones
    if num_ones >= num_zeros: return '1'
    return '0'


def filter(vals, bitno, most_common):
    bitval = get_most_common(vals, bitno)
    if most_common == False:
        bitval = '0' if bitval == '1' else '1'
    new_vals = []
    for val in vals:
        if val[bitno] == bitval:
            new_vals.append(val)
    return new_vals

def value(vals, most_common):
    for bitno in range(0, len(vals[0])):
        vals = filter(vals, bitno, most_common)
        #print(vals)
        if len(vals) == 1:
            break
    if len(vals) != 1:
        print("Error! Only one value expected!", vals)
    return int(vals[0], 2)

def solve(input):
    vals = input.splitlines()
    oxygen = value(vals, True)
    co2 = value(vals, False)
    #print(oxygen)
    #print(co2)
    return oxygen * co2
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))