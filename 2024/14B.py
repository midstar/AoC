import sys
import re

def print_grid(grid, width, height):
    text = []
    for r in range(height):
        row = []
        for c in range(width):
            if (c,r) in grid:
                row.append('x')
            else:
                row.append(' ')
        text.append(''.join(row))
    print('\n'.join(text))

def solve(input):
    robots = []
    width = 0
    height = 0
    for line in input.splitlines():
        x, y, vx, vy = map(int,re.findall('-?\d+', line))
        robots.append({'p':(x,y),'v':(vx,vy)})
        width  = max(width,  x + 1)
        height = max(height, y + 1)

    # Simulate
    TIME = 100000
    for s in range(TIME):
        grid = set()
        for robot in robots:
            new_x = (robot['p'][0] + robot['v'][0]) % width
            new_y = (robot['p'][1] + robot['v'][1]) % height
            robot['p'] = (new_x, new_y)
            grid.add(robot['p'])
        if len(grid) == len(robots):
            #print(s + 1)
            #print_grid(grid,width,height)
            # Note the easter egg (christmas tree) appears as soon as no robot
            # is covered with another robot (in my input at least)
            return s + 1

    return 0      
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))