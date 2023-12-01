import argparse

def solve(input):
    sum = 0
    for line in input.splitlines():
        first = -1
        last  = -1
        for c in list(line):
            if c.isnumeric():
                if first == -1:
                    first = int(c)
                last = int(c)
        if first == -1 or last == -1:
            print('Error line: %s' % line)
            exit(1)
        num = first * 10 + last
        print(str(num))
        sum += num
    print('Result: %s' % str(sum))

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    