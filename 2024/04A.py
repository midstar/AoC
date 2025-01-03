import sys

key = "XMAS"

# Count for key in one direction
def cnt(s):
    result = 0
    for i in range(len(s)):
        if s[i:].startswith(key): result += 1
    return result

# Count for key in two directions
def cnt_2dir(row):
    s = ''.join(row)
    return cnt(s) + cnt(s[::-1])

def transpose(matrix):
    tmatrix = []
    for col in range(len(matrix[0])):
        tmatrix.append([row[col] for row in matrix])
    return tmatrix

def diagrow(matrix, sr, sc, to_right):
    result = []
    while(sr >= 0 and sr < len(matrix) and sc >= 0 and sc < (len(matrix[0]))):
        result.append(matrix[sr][sc])
        sr += 1
        sc = sc + 1 if to_right else sc - 1
    return result

def diagr(matrix):
    result = []
    for c in range(len(matrix[0])):
        result.append(diagrow(matrix,0,c,True))
    for r in range(1, len(matrix)):
        result.append(diagrow(matrix,r,0,True))
    return result

def diagl(matrix):
    result = []
    for c in range(len(matrix[0])):
        result.append(diagrow(matrix,0,c,False))
    for r in range(1, len(matrix)):
        result.append(diagrow(matrix,r,len(matrix[r]) - 1,False))
    return result


def solve(input):
    matrix = [[c for c in line] for line in input.splitlines()]
    result = 0

    # Horizontal
    result += sum([cnt_2dir(row) for row in matrix])

    # Vertical
    result += sum([cnt_2dir(row) for row in transpose(matrix)])

    # Diagonal right
    result += sum([cnt_2dir(row) for row in diagr(matrix)])

    # Diagonal left
    result += sum([cnt_2dir(row) for row in diagl(matrix)])

    return result
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))