import sys

# Print grid, i.e. a dict with tuple key (row,col) and value max 1 char long
def print_dots(dots):
    max_x = max(x for x,_ in dots)
    max_y = max(y for _,y in dots)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in dots:
                print('#',end='')
            else:
                print('.',end='')
        print()

def fold_y(dots,y_fold):
    dots2 = set()
    for x,y in dots:
        if y > y_fold:
            y = y_fold - (y - y_fold)
        dots2.add((x,y))
    return dots2

def fold_x(dots,x_fold):
    dots2 = set()
    for x,y in dots:
        if x > x_fold:
            x = x_fold - (x - x_fold)
        dots2.add((x,y))
    return dots2

def solve(input):
    coordinates, foldinstr = input.split('\n\n')
    dots = {tuple(map(int,c.split(','))) for c in coordinates.splitlines()}
    for fold in foldinstr.splitlines():
        if 'y' in fold:
            dots = fold_y(dots,int(fold.split('=')[1]))
        if 'x' in fold:
            dots = fold_x(dots,int(fold.split('=')[1]))
    print_dots(dots)
    return 'Se output'
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))