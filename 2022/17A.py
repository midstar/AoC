import sys

class Shape():
    def __init__(self, shape_c):
        self.s = {(r,c) for r, l in enumerate(shape_c.splitlines()) for c,v in enumerate(l) if v == '#'}

    def borders(self):
        rows = {r for r,_ in self.s}
        cols = {c for _,c in self.s}
        return min(rows),min(cols),max(rows),max(cols)
    
    def move(self,grid,dr,dc):
        s2 = set()
        for r,c in self.s:
            r += dr
            if r > 0: return False
            c += dc
            if c < 0 or c > 6: return False
            if (r,c) in grid: return False
            s2.add((r,c))
        self.s = s2
        return True 

def solve(input):
    winds = input.strip()
    shapes_c = '''####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##'''
    shapes = [Shape(s) for s in shapes_c.split('\n\n')]
    grid = set()
    top_r = 1
    wi = 0
    for i in range(2022):
        shape = shapes[i % len(shapes)]
        _, min_c, max_r, _ = shape.borders()
         # Start pos
        shape.move(grid, top_r - max_r - 4, 2 - min_c)
        while True:
            wind = winds[wi % len(winds)]
            wi += 1

            # Wind
            dc = -1 if wind == '<' else 1
            shape.move(grid, 0, dc)

            # Down
            if not shape.move(grid, 1, 0):
                break
        
        grid |= shape.s # Add stone to grid
        min_r, _, _, _ = shape.borders()
        top_r = min(top_r, min_r)

    return abs(top_r) + 1
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))