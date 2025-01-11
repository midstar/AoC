import sys

def match_range(a_s, a_r, b_s, b_r):
    if (a_s + a_r - 1) < b_s:
        return None, {(a_s, a_r)} # a is completely left of b
    if (b_s + b_r - 1) < a_s:
        return None, {(a_s, a_r)} # a is completely right of b
    outside = set()
    if a_s < b_s:
        outside.add((a_s, b_s - a_s)) # Left outside
        a_r -= b_s - a_s
        a_s = b_s
    if (a_s + a_r) > (b_s + b_r):
        outside.add((b_s + b_r, (a_s + a_r) - (b_s + b_r))) # Right outside
        a_r = (b_s + b_r) - a_s
    return (a_s, a_r), outside

def find_lowest(maps,map,seeds):
    lowest = 999999999999999999
    while (len(seeds) > 0):
        s_s, s_r = seeds.pop()
        found = False
        for src, range, dst in maps[map]['map']:
            inside, outside = match_range(s_s, s_r, src, range)
            if inside != None:
                seeds.update(outside)
                found = True
                s, r = inside
                new_s = dst + (s - src)
                if maps[map]['to'] == 'location':
                    lowest = min(lowest, new_s)
                else:
                    lowest = min(lowest, find_lowest(maps,maps[map]['to'],{(new_s,r)}))
                break
        if not found: # No mapping performed
            if maps[map]['to'] == 'location':
                lowest = min(lowest, s_s)
            else:
                lowest = min(lowest, find_lowest(maps,maps[map]['to'],{(s_s,s_r)}))         
    return lowest

def solve(input):
    lines = input.splitlines()
    seedsStr = lines[0].split(':')[1].split()
    seeds = set()
    while len(seedsStr) > 0:
        seeds.add((int(seedsStr.pop(0)),int(seedsStr.pop(0))))
    lines = lines[2:]
    maps = {}
    while len(lines) > 0:
        name = lines.pop(0).split(':')[0]
        from_to = name.split('-')
        fromV = from_to[0]
        toV = from_to[2].split()[0]
        maps[fromV] = {
            'to' : toV,
            'map': []
        }
        entry = lines.pop(0)
        while entry != "":
            items = list(map(int,entry.split()))
            maps[fromV]['map'].append((items[1],items[2], items[0])) # src, range, dst
            if len(lines) == 0:
                break
            entry = lines.pop(0)
    
    return find_lowest(maps,'seed',  seeds)

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))