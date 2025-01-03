import sys
import re

def count(robots, min_x, max_x, min_y, max_y):
    result = 0
    for robot in robots:
        x, y = robot['p']
        if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
            result += 1
    return result

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
    TIME = 100
    for robot in robots:
        new_x = (robot['p'][0] + robot['v'][0] * TIME) % width
        new_y = (robot['p'][1] + robot['v'][1] * TIME) % height
        robot['p'] = (new_x, new_y)

    # Count
    mid_x = (width  - 1) // 2
    mid_y = (height - 1) // 2

    q1 = count(robots, 0,         mid_x - 1, 0,         mid_y - 1)
    q2 = count(robots, mid_x + 1, width - 1, 0,         mid_y - 1)
    q3 = count(robots, 0,         mid_x - 1, mid_y + 1, height - 1)
    q4 = count(robots, mid_x + 1, width - 1, mid_y + 1, height - 1)

    return q1 * q2 * q3 * q4
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))