import sys

def sand_fall(grid, pos, path, max_y):
    path.append(pos)
    x, y = pos
    if y >= max_y:
        return None, path
    elif (x, y + 1) not in grid:
        return sand_fall(grid, (x, y + 1), path, max_y)
    elif (x - 1, y + 1) not in grid:
        return sand_fall(grid, (x - 1, y + 1), path, max_y)
    elif (x + 1, y + 1) not in grid:
        return sand_fall(grid, (x + 1, y + 1), path, max_y)
    return pos, path


def solve(input):
    grid = set()
    for line in input.splitlines():
        x0, y0 = 0, 0
        for i, pos in enumerate(line.split(' -> ')):
            x, y = map(int,pos.split(','))
            if i == 0:
                x0, y0 = x, y
                grid.add((x0,y0))
            else:
                while (x0, y0) != (x, y):
                    x0 = x0 - 1 if x < x0 else x0 + 1 if x > x0 else x0
                    y0 = y0 - 1 if y < y0 else y0 + 1 if y > y0 else y0
                    grid.add((x0,y0))
    max_y = max(y for _, y in grid)
    result = 0
    while True:
        pos, path = sand_fall(grid, (500, 0), [], max_y)
        if pos != None:
            grid.add(pos)
            result += 1
        else:
            break
    return result
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))