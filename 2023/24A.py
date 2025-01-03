import sys
import matplotlib.pyplot as plt

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(line1, line2):
    A, B = line1
    C, D = line2
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def get_coords(xy, speed): # z ignored
    xy_min = 200000000000000
    xy_max = 400000000000000
    # c = c0 + s * t => t * s = c - c0 => t = (c - c0) / s
    tx = []
    ty = []
    for v in [xy_min, xy_max]:
        tx.append((v - xy[0]) / speed[0])
        ty.append((v - xy[1]) / speed[1])
    tx.sort()
    ty.sort()
    t = []
    if tx[0] > ty[0] and tx[0] < ty[1]:
        t.append(tx[0])
    elif ty[0] > tx[0] and ty[0] < tx[1]:
        t.append(ty[0])
    else:
        print('Impossible coord pos 1: ', tx, ty, xy)
        return None, None
    t[0] = max(0, t[0])

    if tx[1] < ty[1] and tx[1] > ty[0]:
        t.append(tx[1])
    elif ty[1] < tx[1] and ty[1] > tx[0]:
        t.append(ty[1])

    if len(t) != 2 or t[1] < 0: 
        print('Impossible coord pos 2: ', tx, ty, xy)
        return None, None
    return ((xy[0] + speed[0] * t[0], xy[1] + speed[1] * t[0]), \
            (xy[0] + speed[0] * t[1], xy[1] + speed[1] * t[1]))
    

def solve(input):

    graph = []

    for line in input.replace(' ','').splitlines():
        c_s = line.split('@')
        c = tuple([int(i) for i in c_s[0].split(',')])
        s = tuple([int(i) for i in c_s[1].split(',')])
        c1, c2 = get_coords(c, s)
        if c1 and c2:
            graph.append((c1, c2))
        #print('  ',c, s, c1, c2)

    result = 0
    for i, line1 in enumerate(graph):
        for j, line2 in enumerate(graph):
            if j > i:
                #print(line1, line2)
                #plt.plot([line1[0][0],line1[1][0]],[line1[0][1],line1[1][1]])
                #plt.plot([line2[0][0],line2[1][0]],[line2[0][1],line2[1][1]])
                #plt.show()
                if(intersect(line1, line2)):
                    result += 1
                    #print('   EQUAL')
                


    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))