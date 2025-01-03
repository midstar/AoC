import sys
import z3

def solve(input):

    hailstones = []

    for line in input.replace(' ','').splitlines():
        c_s = line.split('@')
        c = tuple([int(i) for i in c_s[0].split(',')])
        s = tuple([int(i) for i in c_s[1].split(',')])
        hailstones.append((c,s))

    # Need to figure out this for every hailstone:
    #
    # H1x + H1dx * H1t = Sx + Sdx * H1t
    # H1y + H1dy * H1t = Sy + Sdy * H1t
    # H1z + H1dz * H1t = Sz + Sdz * H1t
    #
    # H2x + H2dx * H2t = Sx + Sdx * H2t
    # H2y + H2dy * H2t = Sy + Sdy * H2t
    # H2z + H2dz * H2t = Sz + Sdz * H2t
    #
    # ...
    #
    # Where:
    #   - H = Hailstone (H1 hailstone 1, H2 hailstone 2 etc.)
    #         Ht is time of impact of specific hailstone
    #   - S = Throwing stone. x, y, z, dx, dy and dz will be
    #         fixed for all collisions
    #
    # For every hailstone collision we have three equations
    # and 7 unknown varialbes, thus impossible to solve.
    #
    # If we use three different hailstone collisions we get
    # 3 * 3 = 9 equations and 9 unknowns and is thus solvable
    sx, sy, sz, sdx, sdy, sdz = z3.Ints('sx sy sz sdx sdy sdz')
    hts = z3.Ints('h1t h2t h3t')
    s = z3.Solver()
    for i in range(0, 3):
        hx, hy, hz = hailstones[i][0]
        hdx, hdy, hdz = hailstones[i][1]
        ht = hts[i]
        s.add(hx + hdx * ht == sx + sdx * ht)
        s.add(hy + hdy * ht == sy + sdy * ht)
        s.add(hz + hdz * ht == sz + sdz * ht)

    s.check()
    model = s.model()

    result = model[sx].as_long() + model[sy].as_long() + model[sz].as_long()

    return result

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))