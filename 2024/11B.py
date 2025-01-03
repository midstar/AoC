import sys
import matplotlib.pyplot as plt 
import math

cache = {}
def blink(stone, times):
    if times == 0: 
        return 1
    elif (stone, times) in cache:
        return cache[(stone, times)]

    l = len(str(stone))
    if stone == 0:
        new_stones = [1]
    elif l % 2 == 0:
        new_stones = [int(str(stone)[:l // 2]), int(str(stone)[l // 2:])]
    else:
        new_stones = [stone * 2024]

    cache[(stone, times)] = sum([blink(s, times - 1) for s in new_stones])
    return cache[(stone, times)]

def solve(input):
    return sum([blink(int(val), 75) for val in input.split()])
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))