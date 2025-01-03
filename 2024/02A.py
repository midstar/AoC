import sys

def is_safe(report):
    diffs = set([report[i] - report[i - 1] for i in range(1,len(report))])
    if diffs.issubset({1,2,3}) or diffs.issubset({-1,-2,-3}):
        return True
    return False

def solve(input):
    reports = [[int(word) for word in line.split()] for line in input.splitlines()]   
    return sum(is_safe(report) for report in reports)
     
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read())) 