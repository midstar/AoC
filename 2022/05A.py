import sys

def solve(input):
    stack_in, proc_in = tuple([[l for l in s_p.splitlines()] for s_p in input.split('\n\n')])

    stacks = [[] for _ in stack_in[-1].split()]
    for row in stack_in[:-1]:
        for i, s in enumerate(stacks):
            pos = 1 + i * 4
            if row[pos] != ' ': s.insert(0, row[pos])

    for proc in proc_in:
        l, src, dst = tuple([int(v) for v in proc.split() if v.isnumeric()])
        for i in range(l):
            stacks[dst - 1].append(stacks[src - 1].pop())
    
    result = ''
    for s in stacks:
        result = result + s[-1]
    return result
    

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))