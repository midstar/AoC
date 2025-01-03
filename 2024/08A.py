import sys

def get_antinode(pos1, pos2, r_max, c_max):
    r1, c1 = pos1
    r2, c2 = pos2
    ar = (r2 - r1) + r2
    ac = (c2 - c1) + c2
    if ar < 0 or ar > r_max or ac < 0 or ac > c_max: return None
    return (ar, ac)

def get_antinodes(freq_positions, r_max, c_max):
    #print(freq_positions,'-----')
    antinodes = set()
    for i in range(len(freq_positions) - 1):
        pos1 = freq_positions[i]
        for pos2 in freq_positions[i+1:]:
            antinode = get_antinode(pos1, pos2, r_max, c_max)
            if antinode != None: antinodes.add(antinode)
            antinode = get_antinode(pos2, pos1, r_max, c_max)
            if antinode != None: antinodes.add(antinode)
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
            antennas.setdefault(freq, [])
            antennas[freq].append((r,c))
    result = set()
    for _, positions in antennas.items():
        result |= get_antinodes(positions, r_max, c_max)

    return len(result)
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))