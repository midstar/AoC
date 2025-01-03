import sys


def solve(input):
    forest = [[int(i) for i in line] for line in input.splitlines()]
    forest_t = [[row[i] for row in forest] for i in range(len(forest))]

    result = len(forest) * 4 - 4
    for row in range(1, len(forest) - 1):
        for col in range(1, len(forest) - 1):
            v = forest[row][col]
            if v > max(forest[row][:col]) or v > max(forest[row][col + 1:]) or \
               v > max(forest_t[col][:row]) or v > max(forest_t[col][row + 1:]):
                result += 1
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))