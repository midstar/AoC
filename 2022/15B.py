import sys, re

# See https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
# Wiki is invalid got some help from ChatGPT
def intersection(line1,line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    den = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if den == 0: return None
    t = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / den
    u = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / den
    if 0 <= t <= 1 and 0 <= u <= 1:
        return x1+t*(x2-x1), y1+t*(y2-y1)
    return None

def dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def sides(sensor):
    x, y, d = sensor
    top     = y - d
    bottom  = y + d
    right   = x + d
    left    = x - d
    return [((x,top),(right,y)),((x,top),(left,y)),((x,bottom),(right,y)),((x,bottom),(left,y))]

#MAX = 20      # Example
MAX = 4000000 
def is_possible_around_point(sensors, px,py):
    for dx, dy in [(-1,-1),(0,-1),(1,-1), \
                   (-1, 0),(0, 0),(1, 0), \
                   (-1, 1),(0, 1),(1, 1)]:
        x = px + dx
        y = py + dy 
        if x < 0 or x > MAX or y < 0 or y > MAX: continue
        if beacon_possible(sensors,x,y):
            return int(x * 4000000 + y)  
    return None 

def beacon_possible(sensors,x,y):
    for sx,sy,d in sensors:
        if dist(x,y,sx,sy) <= d:
            return False
    return True

def solve(input):
    sensors = []
    for line in input.splitlines():
        x,y,bx,by = list(map(int,re.findall(r'=(-?\d+)', line)))
        sensors.append((x,y,dist(x,y,bx,by)))

    for i, sensor in enumerate(sensors[:-1]):
        for side in sides(sensor):
            for sensor2 in sensors[i+1:]:
                for side2 in sides(sensor2):
                    inters = intersection(side,side2)
                    if not inters: continue
                    v = is_possible_around_point(sensors,*inters)
                    if v: return v
    return None
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))