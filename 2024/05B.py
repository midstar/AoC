import sys

def is_valid(before, update):
    for i, val in enumerate(update):
        for after in update[i:]:
            if (after, val) in before:
                return False
    return True

def fix(before, update):
    while not is_valid(before, update):
        for i, val in enumerate(update):
            fix = False
            for j, after in enumerate(update[i:]):
                if (after, val) in before:
                    update.pop(i + j)
                    update.insert(i, after)
                    fix = True
                    break
            if fix: break


def solve(input):
    part = input.split('\n\n')
    before = [(int(line.split("|")[0]),int(line.split("|")[1])) for line in part[0].splitlines()]
    updates = [[int(a) for a in line.split(',')] for line in part[1].splitlines()]
    result = 0
    for update in updates:
        if not is_valid(before,update):
            fix(before, update)
            result += update[len(update) // 2]
    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))