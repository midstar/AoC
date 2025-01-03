import sys

def get_window(l, i):
    return l[i] + l[i+1] + l[i+2]

def solve(input):
    nums = [int(line) for line in input.splitlines()]
    prev_window = get_window(nums,0)
    result = 0
    for i in range(1, len(nums) - 2):
        window = get_window(nums,i)
        if window > prev_window: result += 1
        prev_window = window
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))