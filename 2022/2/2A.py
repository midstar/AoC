import argparse, time

def solve(input):
    result = 0
    for line in input.splitlines():
        you = line.split()[0]
        me = line.split()[1]
        if me == 'X' and you == 'C' or me == 'Y' and you == 'A' or me == 'Z' and you == 'B':
            result += 6
        elif me == 'X' and you == 'A' or me == 'Y' and you == 'B' or me == 'Z' and you == 'C':
            result +=3
        if me == 'X':
            result += 1
        elif me == 'Y':
            result += 2
        elif me == 'Z':
            result += 3
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