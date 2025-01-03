import sys

def solve(input):
    result = 0
    for elf in input.split('\n\n'):
        tot_calories = 0
        for calories in elf.splitlines():
            tot_calories += int(calories)
        result = max(result, tot_calories)
    return result
    

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))