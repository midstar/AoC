import sys

def solve(input):
    nums1 = sorted([int(line.split()[0]) for line in input.splitlines()])
    nums2 = sorted([int(line.split()[1]) for line in input.splitlines()])

    result = 0
    for (num1, num2) in zip(nums1, nums2):
        result += abs(num1 - num2)

    return result

if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))   