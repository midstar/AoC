import sys

def solve(input):
    points = { 'A' : 1, 'B' : 2, 'C' : 3}
    win = { 'A' : 'C', 'B' : 'A', 'C' : 'B'}
    loose = {v : k for k,v in win.items()}
    result = 0
    for line in input.splitlines():
        tactics = line.split()[1]
        you = line.split()[0]
        if tactics == 'X': # Loose
            me = win[you]
        elif tactics == 'Y': # Draw
            me = you
            result += 3
        elif tactics == 'Z': # Win
            me = loose[you]
            result += 6
        result += points[me]
    return result
    

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))