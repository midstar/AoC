import argparse, time

def solve(input):
    result = 0
    for line in input.splitlines():
        a_min, a_max, b_min, b_max = tuple([int(v) for r in line.split(',') for v in r.split('-')])
        if a_min >= b_min and a_min <= b_max or a_max >= b_min and a_max <= b_max or \
           b_min >= a_min and b_min <= a_max or b_max >= a_min and b_max <= a_max :
            result += 1
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