import sys

def solve(input):
    result = 0
    lines = input.splitlines()
    while lines:
        c1 = lines.pop(0)
        c2 = lines.pop(0)
        c3 = lines.pop(0)
        for c in c1:
            if c in c2 and c in c3:
                if c.islower():
                    result += ord(c) - ord('a') + 1
                else:
                    result += ord(c) - ord('A') + 27
                break
    return result
    

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))