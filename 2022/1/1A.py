import argparse, time

def solve(input):
    result = 0
    for elf in input.split('\n\n'):
        tot_calories = 0
        for calories in elf.splitlines():
            tot_calories += int(calories)
        result = max(result, tot_calories)
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