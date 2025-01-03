import sys

def check_type(row, col, lines):
    c = lines[row][col]
    if c.isnumeric():
        return 'number'
    if c == '*':
        return 'symbol'
    else:
        return 'space'

def next_to_symbol(row, col, lines):
    ''' Returns a list of symbols '''
    row_start = max(0, row - 1)
    row_end = min(len(lines) - 1, row + 1)
    col_start = max(0, col - 1)
    col_end = min(len(lines[row]) - 1, col + 1)

    symbols = []
    for r in range(row_start, row_end + 1):
        for c in range(col_start, col_end + 1):
            if r == row and c == col:
                continue
            if check_type(r,c,lines) == 'symbol':
                symbols.append("%s_%s" % (r, c))
    return symbols

def solve(input):
    lines = input.splitlines()
    symbolMap = {}
    for r in range(0, len(lines)):
        numStr = ""
        symbols = []
        for c in range (0, len(lines[r])):
            if check_type(r, c, lines) == 'number':
                numStr = numStr + lines[r][c]
                symbols = list(set(symbols + next_to_symbol(r, c, lines)))
            if check_type(r, c, lines) != 'number' or c == (len(lines[r]) - 1):
                if numStr != "" and len(symbols) > 0:
                    for symbol in symbols:
                        if symbol not in symbolMap:
                            symbolMap[symbol] = []
                        symbolMap[symbol].append(int(numStr))
                numStr = ""
                symbols = []

    sum = 0        
    for key, values in symbolMap.items():
        if len(values) == 2:
            v1 = values[0]  
            v2 = values[1]
            product = v1 * v2
            #print("%s * %s = %s" % (v1, v2, product))
            sum += product       

    return sum



if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))