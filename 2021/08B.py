import sys

def solve(input):
    result = 0
    for line in input.splitlines():

        patterns = {}
        for pattern in line.split('|')[0].split():
            patterns.setdefault(len(pattern),[])
            patterns[len(pattern)].append(set(pattern))
        
        digits = {}

        # Unique
        digits[1] = patterns[2][0]
        digits[4] = patterns[4][0]
        digits[7] = patterns[3][0]
        digits[8] = patterns[7][0]

        # Figure out based on previous
        dig_i = 0
        for i, p in enumerate(patterns[5]):
            if len(p - digits[7]) == 2:
                dig_i = i
                break
        digits[3] = patterns[5].pop(dig_i)
        digits[9] = digits[3] | digits[4]
        e_seg = digits[8] - digits[9]
        for i, p in enumerate(patterns[5]):
            if len(p - e_seg) == 4:
                dig_i = i
                break
        digits[2] = patterns[5].pop(dig_i)
        digits[5] = patterns[5].pop()
        digits[6] = digits[5] | e_seg
        for i, p in enumerate(patterns[6]):
            if p != digits[6] and p != digits[9]:
                dig_i = i
                break
        digits[0] = patterns[6].pop(dig_i)

        mul = 1000
        part_result = 0
        for pattern in line.split('|')[1].split():
            for num, digit in digits.items():
                if set(pattern) == digit:
                    part_result += int(num * mul)
                    break
            mul /= 10
        result += part_result

    return result
        
if __name__ == '__main__':
    print(solve(open(sys.argv[1]).read()))