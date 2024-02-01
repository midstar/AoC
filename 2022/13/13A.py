import argparse, time

def compare(left, right):
    if isinstance(left, int) and isinstance(right,int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    if not isinstance(left, list): left = [left]
    if not isinstance(right, list): right = [right]
    for lv, rv in zip(left, right):
        #print(lv, ' <-> ',  rv)
        res = compare(lv, rv)
        if res != None:
            return res
    if len(left) < len(right): 
        return True
    elif len(left) > len(right):
        return False

    return None
        

def solve(input):
    pairs = [p.splitlines() for p in input.split('\n\n')]
    result = 0
    for i, pair in enumerate(pairs):
        #print('\n\nPair', i + 1)
        #print(pair[0])
        #print(pair[1])
        left = eval(pair[0])
        right = eval(pair[1])
        if compare(left,right) != False:
            result += i + 1
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