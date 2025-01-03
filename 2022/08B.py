import sys

def score(v, trees):
    view = 0
    for tree in trees:
        view += 1
        if v <= tree:
            break
    return view

def solve(input):
    forest = [[int(i) for i in line] for line in input.splitlines()]
    forest_t = [[row[i] for row in forest] for i in range(len(forest))]

    result = 0
    for row in range(1, len(forest) - 1):
        for col in range(1, len(forest) - 1):
            v = forest[row][col]
            view =  1
            view *= score(v, forest[row][col - 1::-1])
            view *= score(v, forest[row][col + 1:])
            view *= score(v, forest_t[col][row -1::-1])
            view *= score(v, forest_t[col][row + 1:])
            if view > result:
                result = view
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))