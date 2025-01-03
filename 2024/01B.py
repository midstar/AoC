import sys

def solve(input):
    nums1 = [int(line.split()[0]) for line in input.splitlines()]
    nums2 = [int(line.split()[1]) for line in input.splitlines()]

    result = 0
    for num1 in nums1:
        result += num1 * nums2.count(num1)

    return result
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))  