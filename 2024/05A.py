import sys

def is_valid(before, update):
    for i, val in enumerate(update):
        for after in update[i:]:
            if (after, val) in before:
                return False
    return True

def solve(input):
    part = input.split('\n\n')
    before = [(int(line.split("|")[0]),int(line.split("|")[1])) for line in part[0].splitlines()]
    updates = [[int(a) for a in line.split(',')] for line in part[1].splitlines()]
    return sum([update[len(update) // 2] for update in updates if is_valid(before, update)])
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))