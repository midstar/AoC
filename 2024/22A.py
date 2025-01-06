import sys
import sys

def next_sec_num(sec_num):
    sec_num = (sec_num ^ (sec_num * 64)) % 16777216
    sec_num = (sec_num ^ int(sec_num / 32)) % 16777216
    sec_num = (sec_num ^ (sec_num * 2048)) % 16777216
    return sec_num

def next_sec_num_req(sec_num, times):
    if times == 0: return sec_num
    return next_sec_num_req(next_sec_num(sec_num), times - 1)

def solve(input):
    sys.setrecursionlimit(10**6)
    sec_nums = [int(line) for line in input.splitlines()]

    result = 0
    for sec_num in sec_nums:
        sec_num2 = next_sec_num_req(sec_num,2000)
        result += sec_num2
        #print(f'{sec_num}:',sec_num2)

    return result
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))