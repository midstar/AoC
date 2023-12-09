import argparse

def calc(values):
    result = values[0]
    sign = -1
    while (any(values)):
        print(values[0])
        diff = []
        for i in range (0, len(values) - 1):
            diff.append(values[i+1] - values[i])
        values = diff
        result += sign * values[0]
        sign *= -1
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