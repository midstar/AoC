import sys

def val(grid, node):
    if node in grid: return grid[node]
    return ''

def solve(input):
    grid = {(r,c) : v for r, line in enumerate(input.splitlines()) for c, v in enumerate(line)}
    result = 0
    for (r, c), value in grid.items():
        # Check for center points (=A)
        if value == 'A':
            lr = val(grid,(r - 1, c - 1)) + 'A' + val(grid,(r + 1, c + 1))
            rl = val(grid,(r - 1, c + 1)) + 'A' + val(grid,(r + 1, c - 1))
            if (lr == 'MAS' or lr == 'SAM') and (rl == 'MAS' or rl == 'SAM'):
                result += 1 
    
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))