import sys

def solve(input):
    elf_calories = []
    for elf in input.split('\n\n'):
        tot_calories = 0
        for calories in elf.splitlines():
            tot_calories += int(calories)
        elf_calories.append(tot_calories)
    elf_calories.sort()
    return sum(elf_calories[-3:])
    

if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))