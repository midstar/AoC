import argparse, time

def next_cycle(storage, x, cycle):
    cycle += 1
    if cycle > 0:
        if cycle == 20 or cycle <= 220 and (cycle - 20) % 40 == 0:
            print(cycle,'*', x,'=',cycle * x)
            storage.append(cycle * x)
    return cycle


def solve(input):
    storage = []
    cycle = 0
    x = 1
    for line in input.splitlines():
        if line.startswith('a'):
            cycle = next_cycle(storage, x, cycle)
            cycle = next_cycle(storage, x, cycle)
            x += int(line.split()[1])
        else:
            cycle = next_cycle(storage, x, cycle)
    print(storage)
    return sum(storage)
        
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