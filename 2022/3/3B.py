import argparse, time

def solve(input):
    result = 0
    lines = input.splitlines()
    while lines:
        c1 = lines.pop(0)
        c2 = lines.pop(0)
        c3 = lines.pop(0)
        for c in c1:
            if c in c2 and c in c3:
                if c.islower():
                    result += ord(c) - ord('a') + 1
                else:
                    result += ord(c) - ord('A') + 27
                break
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