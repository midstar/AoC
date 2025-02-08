import sys, re

def dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def sides(sensor):
    x, y, d = sensor
    top     = y - d
    bottom  = y + d
    right   = x + d
    left    = x - d
    return [((x,top),(right,y)),((x,top),(left,y)),((x,bottom),(right,y)),((x,bottom),(left,y))]

# See https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def intersection(line1,line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if den == 0: return None
    t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)) / den
    u = ((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)) / den
    if t < 0 or t > 1 or u < 0 or u > 1: return None
    Px = x1+t*(x2-x1)
    Py = y1+t*(y2-y1)
    return round(Px),round(Py)

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

    MAX = 4000000 # For example use 20
    for i, sensor in enumerate(sensors[:-1]):
        for side in sides(sensor):
            for sensor2 in sensors[i+1:]:
                for side2 in sides(sensor2):
                    inters = intersection(side,side2)
                    if not inters: continue
                    ix, iy = inters
                    for dx, dy in [(0,0),(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
                        x = ix + dx
                        y = iy + dy
                        if x < 0 or x > MAX or y < 0 or y > MAX: continue
                        if beacon_possible(sensors,x,y):
                            return x * 4000000 + y

    return None
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))