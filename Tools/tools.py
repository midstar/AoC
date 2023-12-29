# Print matrix with (row, col) entries
def print_matrix(matrix, r_min = None, r_max = None, c_min = None, c_max = None):
    if r_min == None : r_min = min([r for (r, _) in matrix])
    if r_max == None : r_max = max([r for (r, _) in matrix])
    if c_min == None : c_min = min([c for (_, c) in matrix])
    if c_max == None : c_max = max([c for (_, c) in matrix])
    for r in range(r_min, r_max + 1):
        chars = []
        for c in range(c_min, c_max + 1):
            if (r, c) in matrix:
                chars.append('x')
            else:
                chars.append('.')
        print(''.join(chars))