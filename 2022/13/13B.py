import argparse, time
from functools import cmp_to_key

def compare(left, right):
    if isinstance(left, int) and isinstance(right,int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    if not isinstance(left, list): left = [left]
    if not isinstance(right, list): right = [right]
    for lv, rv in zip(left, right):
        #print(lv, ' <-> ',  rv)
        res = compare(lv, rv)
        if res != 0:
            return res
    if len(left) < len(right): 
        return -1
    elif len(left) > len(right):
        return 1

    return 0

def str_compare(left_str, right_str):
    return compare(eval(left_str), eval(right_str))

def solve(input):
    packets = [s for s in input.splitlines() if s]
    packets.append('[[2]]')
    packets.append('[[6]]')
    packets = sorted(packets, key=cmp_to_key(str_compare))
    #print('\n'.join(packets))
    div_1_idx = packets.index('[[2]]') + 1
    div_2_idx = packets.index('[[6]]') + 1
    result = div_1_idx * div_2_idx
    return result
        
def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        start_time = time.time()
        result = solve(f.read())
        print('Result: %s  (excution time %0.4f s)' % (result, time.time() - start_time))

if __name__ == '__main__':
    main()    