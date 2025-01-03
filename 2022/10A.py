import sys

def next_cycle(storage, x, cycle):
    cycle += 1
    if cycle > 0:
        if cycle == 20 or cycle <= 220 and (cycle - 20) % 40 == 0:
            #print(cycle,'*', x,'=',cycle * x)
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
    #print(storage)
    return sum(storage)
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))