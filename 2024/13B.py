import sys
import re

A_TOKENS = 3
B_TOKENS = 1


'''
Can be treated as two equations:
a * a_x + b * b_x = x
a * a_y + b * b_y = y

Where a is =>
a = (x - b * b_x) / a_x

Insert a in equation 2 to figure out b =>
a_y * (x - b * b_x) / a_x + b * b_y = y
=>
a_y * (x - b * b_x) + b * b_y * a_x = y * a_x
=>
a_y * x - a_y * b * b_x + b * b_y * a_x = y * a_x
=>
b * b_y * a_x - a_y * b * b_x = y * a_x - a_y * x
=>
b * (b_y * a_x - a_y * b_x) = y * a_x - a_y * x

Thus, b will be =>
b = (y * a_x - a_y * x) / (b_y * a_x - a_y * b_x)

'''
def price(a_x, a_y, b_x, b_y, x, y):
    b = (y * a_x - a_y * x) / (b_y * a_x - a_y * b_x)
    a = (x - b * b_x) / a_x
    if b.is_integer() and a.is_integer():
        return int(A_TOKENS * a + B_TOKENS * b)
    return 0

'''
Alternative solutions is to use numpy

import numpy as np
def price(a_x, a_y, b_x, b_y, x, y):
    a = np.array([[a_x, b_x], [a_y, b_y]])
    b = np.array([x, y])
    a, b = np.linalg.solve(a, b)
    a = round(a)
    b = round(b)
    if (a*a_x+b*b_x)==x and (a*a_y+b*b_y)==y:
        return A_TOKENS * a + B_TOKENS * b
    return 0

'''

def solve(input):
    result = 0
    for part in input.split('\n\n'):
        a_x, a_y, b_x, b_y, x, y = re.findall(r'(\d+)', part)
        result += price(int(a_x), int(a_y), int(b_x), int(b_y), 10000000000000 + int(x), 10000000000000 + int(y))
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))