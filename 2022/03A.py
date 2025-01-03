import sys

def solve(input):
    result = 0
    for line in input.splitlines():
        l = int(len(line) / 2)
        c1 = line[:l]
        c2 = line[l:]
        for c in c1:
            if c in c2:
                if c.islower():
                    result += ord(c) - ord('a') + 1
                else:
                    result += ord(c) - ord('A') + 27
                break
    return result
    

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))