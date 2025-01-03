import sys

def solve(input):
    result = 0
    lines = input.splitlines()

    # Find empty colums
    empty_cols = set()
    first_line = True
    for line in lines:
        for col in range(0, len(line)):
            if line[col] == '.':
                if first_line:
                    empty_cols.add(col)
            else:
                empty_cols.discard(col)
        first_line = False

    #print(empty_cols)   

    # New expanded galaxy
    galaxy = []
    galaxy_index = 1
    for line in lines:
        galaxy_row = []
        empty_row = True
        for col in range(0, len(line)):
            val = line[col]
            if val != '.':
                val = str(galaxy_index)
                galaxy_index += 1
                empty_row = False
            galaxy_row.append(val)
            if col in empty_cols:
               galaxy_row.append('.') 
        galaxy.append(galaxy_row)
        if empty_row:
            galaxy.append(['.'] * len(galaxy_row))

    #for row in galaxy:
    #    print(''.join(row))

    # Find positions
    positions = {}
    for row in range(0, len(galaxy)):
        for col in range(0, len(galaxy[row])):
            val = galaxy[row][col]
            if val != '.':
                positions[val] = (row, col)


    #print(positions)

    # Calculate shortest path
    result = 0
    while positions:
        name1 = list(positions.keys())[0]
        pos1 = positions.pop(name1)
        for name2, pos2 in positions.items():
            dist = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
            result += dist
            #print('%s - %s : %s' % (name1, name2, dist))

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))