import sys
import sys

def next_sec_num(sec_num):
    sec_num = (sec_num ^ (sec_num * 64)) % 16777216
    sec_num = (sec_num ^ int(sec_num / 32)) % 16777216
    sec_num = (sec_num ^ (sec_num * 2048)) % 16777216
    return sec_num

def next_sec_num_req(seq_out, sec_num, times, p1 = None, p2 = None, p3 = None, p4 = None):
    sec_num = next_sec_num(sec_num)
    p = sec_num % 10
    if p1 != None:
        seq = (p2 - p1, p3 - p2, p4 - p3, p - p4)
        if seq not in seq_out:
            seq_out[seq] = p 

    if times == 1: return sec_num
    return next_sec_num_req(seq_out, sec_num, times - 1, p2, p3, p4, p)

def solve(input):
    sys.setrecursionlimit(10**6)
    sec_nums = [int(line) for line in input.splitlines()]

    seq_all = {}
    for sec_num in sec_nums:
        seq = {}
        sec_num2 = next_sec_num_req(seq, sec_num,2000)
        #print(f'{sec_num}:',sec_num2)
        for key, val in seq.items():
            seq_all.setdefault(key,0)
            seq_all[key] += val

    return max([v for v in seq_all.values()])
        
if __name__ == '__main__':
        print(solve(open(sys.argv[1]).read()))