import argparse

def hash(input):
    h = 0
    for c in input:
        h += ord(c)
        h *= 17
        h = h % 256
    return h

def solve(input):
    #lines = input.splitlines()
    #matrix = [list(line) for line in lines]
    result = 0

    words = input.split(',')
    for word in words:
        result += hash(word)


    print('Result: %s' % result)

def main():
    parser = argparse.ArgumentParser(description='Advent Of Code Solver %s' % __file__)
    parser.add_argument('input_filename', help='Input', 
                        nargs='?', default='input.txt')
    args = vars(parser.parse_args())

    with open(args['input_filename'],'r') as f:
        solve(f.read())

if __name__ == '__main__':
    main()    