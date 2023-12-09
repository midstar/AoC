import argparse

def calc(values):
    result = 0
    while (any(values)):
        print(values[-1])
        result += values[-1]
        diff = []
        for i in range (0, len(values) - 1):
            diff.append(values[i+1] - values[i])
        values = diff
    print(result)
    return result

def solve(input):
    result = 0
    lines = input.splitlines()
    for line in lines:
        print(line)
        values = [eval(i) for i in line.split()]
        result += calc(values)

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