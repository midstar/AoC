import sys
import re

A_TOKENS = 3
B_TOKENS = 1

def price(a_x, a_y, b_x, b_y, x, y):
    max_a = min(x // a_x, y // a_y)
    for a in reversed(range(max_a + 1)):
        cx = x - a * a_x
        cy = y - a * a_y
        if (cx % b_x == 0 and cy % b_y == 0 and (cx // b_x) == (cy // b_y)):
            b = cx // b_x
            return A_TOKENS * a + B_TOKENS * b
    return 0

def solve(input):
    result = 0
    for part in input.split('\n\n'):
        a_x, a_y, b_x, b_y, x, y = re.findall(r'(\d+)', part)
        result += price(int(a_x), int(a_y), int(b_x), int(b_y), int(x), int(y))
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))