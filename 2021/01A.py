import sys

def solve(input):
    nums = [int(line) for line in input.splitlines()]
    prev_num = nums.pop(0)
    result = 0
    for num in nums:
        if num > prev_num: result += 1
        prev_num = num
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))