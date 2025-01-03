import sys

SIDE = 5

def bingo(board, pos, number):
    row, col = pos
    if all([board[r, col][1] for r in range(SIDE)]) or all([board[row, c][1] for c in range(SIDE)]):
        return sum([val for (val, mark) in board.values() if not mark]) * number
    return 0

def mark(board, number):
    for pos, (val, _) in board.items(): 
        if number == val: 
            board[pos] = (val, True)
            return bingo(board, pos, number)
    return 0

def solve(input):
    parts = input.split('\n\n')
    numbers = [int(n) for n in parts[0].split(',')]
    boards = [{(r,c):(int(v),False) for r, line in enumerate(bs.splitlines()) for c, v in enumerate(line.split())} for bs in parts[1:]]
    for number in numbers:
        for board in boards:
            v = mark(board, number)
            if v > 0: return v
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))