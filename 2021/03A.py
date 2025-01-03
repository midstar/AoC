import sys

def rate(vals, bitno, gamma):
    l = len(vals)
    num_ones = 0
    for val in vals:
        if val[bitno] == '1':
            num_ones += 1
    num_zeros = l - num_ones
    if gamma:
        if num_ones > num_zeros: 
            return '1'
        else:
            return '0'
    else: # epsilon
        if num_ones > num_zeros: 
            return '0'
        else:
            return '1'       

def value(vals, gamma):
    bits = ''
    for bitno in range(0, len(vals[0])):
        bits += rate(vals, bitno, gamma = gamma)
    return int(bits, 2)      

def solve(input):
    vals = input.splitlines()
    gamma = value(vals,gamma=True)
    epsilon = value(vals,gamma=False)
    return gamma*epsilon
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))