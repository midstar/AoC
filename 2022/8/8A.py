import argparse, time


def solve(input):
    forest = [[int(i) for i in line] for line in input.splitlines()]
    forest_t = [[row[i] for row in forest] for i in range(len(forest))]

    result = len(forest) * 4 - 4
    for row in range(1, len(forest) - 1):
        for col in range(1, len(forest) - 1):
            v = forest[row][col]
            if v > max(forest[row][:col]) or v > max(forest[row][col + 1:]) or \
               v > max(forest_t[col][:row]) or v > max(forest_t[col][row + 1:]):
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