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
    
# Debug remove
def print_matrix(matrix, filled='#', empty='.',min_row=None,min_col=None,max_row=None,max_col=None):
    rows = {r for r,_ in matrix}
    cols = {c for _,c in matrix}
    min_r,min_c,max_r,max_c = min(rows),min(cols),max(rows),max(cols)
    if min_row != None: min_r = min(min_r,min_row)
    if min_col != None: min_c = min(min_c,min_col)
    if max_row != None: max_r = max(max_r,max_row)
    if max_col != None: max_c = max(max_c,max_col)
    for r in range(min_r,max_r + 1):
        for c in range(min_c,max_c + 1):
            val = empty
            if((r,c) in matrix): val = filled
            print(val,end='')
        print()

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
        #print('\n------------------\n','top_r',top_r,'max_r',max_r)
        #print_matrix(grid | shape.s,'#','.',-5,0,0,6)
        while True:
            wind = winds[wi % len(winds)]
            wi += 1

            # Wind
            dc = -1 if wind == '<' else 1
            shape.move(grid, 0, dc)

            # Down
            if not shape.move(grid, 1, 0):
                break
            #print()
            #print_matrix(grid | shape.s,'#','.',-5,0,0,6)
        
        grid |= shape.s # Add stone to grid
        min_r, _, _, _ = shape.borders()
        top_r = min(top_r, min_r)
        #print()
        #print_matrix(grid,'#','.',-10,0,0,6)

    return abs(top_r) + 1
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))