import sys
import matplotlib.pyplot as plt

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
    heights = []
    for i in range(20000):
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

        #if i % len(shapes) == 0: heights.append(abs(top_r) + 1)
        heights.append(abs(top_r) + 1)

    # Check if to lists of values are equal
    def values_equal(values1, values2):
        return all(v1 == v2 for v1, v2 in zip(values1, values2))

    # Find repeating pattern in list, returns index just before pattern and pattern
    def pattern(values, min_length):
        values_rev = list(reversed(values))
        pattern = values_rev[:min_length]
        values_rev = values_rev[min_length:]
        while not values_equal(pattern,values_rev[:len(pattern)]):
            if len(values_rev) == 0: return None # No pattern found
            pattern.append(values_rev.pop(0))
        pattern.reverse()
        for i in range(len(values)):
            if values_equal(pattern, values[i:i+len(pattern)]):
                return i, pattern
    
    # Figures out value at index (index may be larger than len(values)). The values
    # list needs to increase in a repeating pattern for this function to work
    def value_at(values,index,min_pattern_length=5):
        steps = []
        for i, v in enumerate(values[:-1]):
            steps.append(values[i+1]-v)
        start_i, p = pattern(steps,min_pattern_length)
        print(len(p),p)
        l = index - start_i
        return values[start_i] + sum(p) * (l // len(p)) + sum(p[:l % len(p)])

    #ys = heights
    #for i, v in enumerate(heights[:100]):
    #    print(f'{i}: {v}')
    ind = 1000000000000-1
    print(ind,len(heights))
    print(value_at(heights,ind))
    '''
    ys = []
    for i, v in enumerate(heights[:-1]):
        ys.append(heights[i+1]-v)
    print(ys[:40])
    print(pattern(ys,4))
    '''
    #xs = [x for x in range(len(ys))]
    #plt.plot(xs, ys)
    #plt.show()


    return abs(top_r) + 1
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))