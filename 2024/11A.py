import sys

def blink(stones):
    new = []
    for stone in stones:
        if stone == 0: 
            new.append(1)
            continue

        stoneS = str(stone)
        l = len(stoneS)
        if l % 2 == 0:
            new.append(int(stoneS[:int(l/2)]))
            new.append(int(stoneS[int(l/2):]))
            continue
        
        new.append(stone * 2024)
    return new

def solve(input):
    stones = [int(val) for val in input.split()]
    for i in range(25): stones = blink(stones)
    return len(stones)
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))