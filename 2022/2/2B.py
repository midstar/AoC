import argparse, time

def solve(input):
    points = { 'A' : 1, 'B' : 2, 'C' : 3}
    win = { 'A' : 'C', 'B' : 'A', 'C' : 'B'}
    loose = {v : k for k,v in win.items()}
    result = 0
    for line in input.splitlines():
        tactics = line.split()[1]
        you = line.split()[0]
        if tactics == 'X': # Loose
            me = win[you]
        elif tactics == 'Y': # Draw
            me = you
            result += 3
        elif tactics == 'Z': # Win
            me = loose[you]
            result += 6
        result += points[me]
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