import sys

def get_antinodesPP(pos1, pos2, r_max, c_max):
    result = {pos1, pos2}
    r1, c1 = pos1
    r2, c2 = pos2
    ard = (r2 - r1)
    acd = (c2 - c1)
    ar = ard + r2
    ac = acd + c2
    while ar >= 0 and ar <= r_max and ac >= 0 and ac <= c_max:
        result.add((ar, ac))
        ar += ard
        ac += acd
    return result

def get_antinodes(freq_positions, r_max, c_max):
    #print(freq_positions,'-----')
    antinodes = set()
    for i in range(len(freq_positions) - 1):
        pos1 = freq_positions[i]
        for pos2 in freq_positions[i+1:]:
            antinodes |= get_antinodesPP(pos1, pos2, r_max, c_max) | get_antinodesPP(pos2, pos1, r_max, c_max)
    #print(antinodes)
    return antinodes

def solve(input):
    antennas = {}
    r_max = 0
    c_max = 0
    for r, line in enumerate(input.splitlines()):
        r_max = max(r_max, r)
        for c, freq in enumerate(line):
            c_max = max(c_max, c)
            if freq == '.': continue
            antennas.setdefault(freq,[])
            antennas[freq].append((r,c))
    result = set()
    for _, positions in antennas.items():
        result |= get_antinodes(positions, r_max, c_max)

    return len(result)
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))