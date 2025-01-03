import sys

def solve(input):
    result = 0
    lines = input.splitlines()

    # Find empty colums and columns
    empty_rows = set()
    empty_cols = set()
    first_line = True
    for r in range(0, len(lines)):
        if lines[r].count('.') == len(lines[r]):
            empty_rows.add(r)
        for c in range(0, len(lines[r])):
            if lines[r][c] == '.':
                if first_line:
                    empty_cols.add(c)
            else:
                empty_cols.discard(c)
        first_line = False

    #print(empty_rows) 
    #print(empty_cols)   

    # Find positions
    positions = {}
    name_index = 1
    for row in range(0, len(lines)):
        for col in range(0, len(lines[row])):
            val = lines[row][col]
            if val != '.':
                positions[str(name_index)] = (row, col)
                name_index += 1


    #print(positions)

    # Calculate shortest path
    result = 0
    while positions:
        name1 = list(positions.keys())[0]
        pos1 = positions.pop(name1)
        for name2, pos2 in positions.items():
            row_dist = abs(pos1[0] - pos2[0])
            row_i = [pos1[0], pos2[0]]
            row_i.sort()
            for expand in empty_rows:
                if expand > row_i[0] and expand < row_i[1]:
                    row_dist += 1000000 - 1

            col_dist = abs(pos1[1] - pos2[1])
            col_i = [pos1[1], pos2[1]]
            col_i.sort()
            for expand in empty_cols:
                if expand > col_i[0] and expand < col_i[1]:
                    col_dist += 1000000 - 1

            dist = row_dist + col_dist
            result += dist
            #print('%s - %s : %s' % (name1, name2, dist))

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))