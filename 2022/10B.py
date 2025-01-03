import sys

width = 40

def next_cycle(pixels, x, cycle):
    cycle += 1
    row = int((cycle - 1) / width)
    crt_index = (cycle - 1) % width
    #print(x, cycle, row, crt_index)
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
        
    #for i, c in enumerate(pixels):
    #    print(c, end='')
    #    if i > 0 and (i + 1) % width == 0:
    #        print()
    #print()
            
    return 0
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))