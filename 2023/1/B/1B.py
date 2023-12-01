import argparse

def solve(input):
    sum = 0
    for line in input.splitlines():
        first = -1
        last  = -1
        line2 = line
        while len(line2) > 0:
            n = -1
            if (line2[0].isnumeric()):
                n = int(line2[0])
            elif line2.startswith('one'):
                n = 1
            elif line2.startswith('two'):
                n = 2
            elif line2.startswith('three'):
                n = 3
            elif line2.startswith('four'):
                n = 4
            elif line2.startswith('five'):
                n = 5
            elif line2.startswith('six'):
                n = 6
            elif line2.startswith('seven'):
                n = 7
            elif line2.startswith('eight'):
                n = 8
            elif line2.startswith('nine'):
                n = 9

            if n > -1:
                if first == -1:
                    first = n
                last = n
            
            line2 = line2[1:]
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