import sys

def get_neighbours(lines, pos, pos_prev):
    p = []
    row, col = pos
    if row > 0:
        o = lines[row-1][col]
        if o != '#':
            pos_next = (row - 1,col)
            if pos_next != pos_prev:
                p.append((pos_next))
    if row < (len(lines) - 1):
        o = lines[row+1][col]
        if o != '#':
            pos_next = (row + 1,col)
            if pos_next != pos_prev:
                p.append((pos_next))
    if col > 0:
        o = lines[row][col-1]
        if o != '#':
            pos_next = (row,col - 1)
            if pos_next != pos_prev:
                p.append((pos_next))
    if col < (len(lines[0]) - 1):
        o = lines[row][col+1]
        if o != '#':
            pos_next = (row,col + 1)
            if pos_next != pos_prev:
                p.append((pos_next))
    return p


def bfs(lines, start, stop):
    # (steps, pos, path)
    q = [(0, start,[start])]
    max_steps = 0
    max_path = []
    teleport = {}
    while q:
        (steps, pos, path) = q.pop()
        pos_prev = None
        if (len(path) > 1):
            pos_prev = path[-2]
        neighbours = get_neighbours(lines, pos, pos_prev)

        if len(neighbours) == 1:
            # We are in a small passage
            first_pos = neighbours[0]
            if first_pos in teleport:
                (steps_offset, pos2, pos2_prev) = teleport[first_pos]
                path2 = path.copy()
                path2.append(pos2_prev)
                path2.append(pos2) 
                if pos2 not in path:
                    q.append((steps + steps_offset, pos2, path2))
            else:
                first_pos = neighbours[0]
                steps2 = steps
                pos2 = pos
                path2 = path.copy()
                while len(neighbours) == 1:
                    pos2_prev = pos2
                    pos2 = neighbours[0]
                    path2.append(pos2)
                    steps2 += 1
                    if pos2 == stop:
                        if steps2 > max_steps:
                            max_steps = steps2
                            max_path = path2
                        break
                    neighbours = get_neighbours(lines, pos2, pos2_prev)
                if pos2 != stop and len(neighbours) > 1:
                    teleport[first_pos] = (steps2 - steps, pos2, pos2_prev) 
                    if pos2 not in path:
                        q.append((steps2, pos2, path2))
        else:
            for pos2 in neighbours:
                if pos2 not in path:
                    path2 = path.copy()
                    path2.append(pos2)
                    steps2 = steps + 1
                    if pos2 == stop:
                        if steps2 > max_steps:
                            max_steps = steps2
                            max_path = path2
                    else:
                        q.append((steps2, pos2, path2))
    return max_steps, max_path




def solve(input):
    lines = input.splitlines()

    start = (0, lines[0].index('.'))
    last_row = len(lines) - 1
    stop = (last_row, lines[last_row].index('.'))

    max_steps, max_path = bfs(lines, start, stop)
    #print(max_path)
    result = max_steps

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))