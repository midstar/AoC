import sys

def check_type(row, col, lines):
    c = lines[row][col]
    if c.isnumeric():
        return 'number'
    if c == '.':
        return 'space'
    else:
        return 'symbol'

def next_to_symbol(row, col, lines):
    row_start = max(0, row - 1)
    row_end = min(len(lines) - 1, row + 1)
    col_start = max(0, col - 1)
    col_end = min(len(lines[row]) - 1, col + 1)

    for r in range(row_start, row_end + 1):
        for c in range(col_start, col_end + 1):
            if r == row and c == col:
                continue
            if check_type(r,c,lines) == 'symbol':
                return True
    return False

def solve(input):
    sum = 0
    lines = input.splitlines()
    for r in range(0, len(lines)):
        numStr = ""
        nextToSymbol = False
        for c in range (0, len(lines[r])):
            if check_type(r, c, lines) == 'number':
                numStr = numStr + lines[r][c]
                if next_to_symbol(r, c, lines):
                    nextToSymbol = True
            if check_type(r, c, lines) != 'number' or c == (len(lines[r]) - 1):
                if numStr != "" and nextToSymbol:
                    #print(numStr)
                    sum += int(numStr)
                numStr = ""
                nextToSymbol = False
            
    return sum



if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))