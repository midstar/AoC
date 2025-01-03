import sys

def is_possible(tv, ns):
    *ns, last = ns
    if not ns: return last == tv
    if (tv % last == 0) and is_possible(tv // last, ns): return True
    if tv != last and str(tv).endswith(str(last)):
        if is_possible(int(str(tv)[:-1 * len(str(last))]), ns): return True
    if tv > last and is_possible(tv - last, ns): return True
    return False

def solve(input):
    equations = [(int(line.split(':')[0]), [int(n) for n in line.split(':')[1].split()]) for line in input.splitlines()]
    return sum([tv for (tv, ns) in equations if is_possible(tv,ns)])
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))