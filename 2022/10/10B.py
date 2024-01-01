import argparse, time

width = 40

def next_cycle(pixels, x, cycle):
    cycle += 1
    row = int((cycle - 1) / width)
    crt_index = (cycle - 1) % width
    print(x, cycle, row, crt_index)
    if x in [max(crt_index - 1, 0), crt_index, min(crt_index + 1, width)]:
        pixels[cycle - 1] = '#'
    return cycle


def solve(input):
    cycle = 0
    x = 1
    pixels = ['.'] * 6 * width
    for line in input.splitlines():
        if line.startswith('a'):
            cycle = next_cycle(pixels, x, cycle)
            cycle = next_cycle(pixels, x, cycle)
            x += int(line.split()[1])
        else:
            cycle = next_cycle(pixels, x, cycle)
        
    for i, c in enumerate(pixels):
        print(c, end='')
        if i > 0 and (i + 1) % width == 0:
            print()
    print()
            
    return 0
        
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